#!/bin/bash

# Usage : ./report.sh [regexp]

regexp=$1

if [ -z $regexp ]
then
    regexp=".*"
else
    ls numcl/logs*/*.log | grep "$regexp" | xargs -n 1 rm -v
fi

make -j $(($(grep -c "^processor" /proc/cpuinfo)/2))

export tmpdir=$(mktemp -d)
trap "rm -rfv $tmpdir" EXIT

memo (){
    tmp=$tmpdir/$(echo "$*" | md5sum | awk '{print $1}')
    if [ -f $tmp ]
    then
        flock -s $tmp cat $tmp
    else
        flock $tmp bash -c "$* | tee $tmp"
    fi
}

memofile (){
    memo $@ > /dev/null
    echo $tmpdir/$(echo "$*" | md5sum | awk '{print $1}')
}

titles (){
    echo title
    cat numcl/logs*/*.log numpy/logs*/*.log | awk -f report.awk | cut -f1 | sort | uniq
}

process-header (){
    echo $1 | sed 's/logs-\?//g;s_/$__g;s_/_@_g' | cut -c-12
}

collect (){
    process-header $1
    memo titles | while read title
    do
        cat $1/*.log | awk -f report.awk | (grep -m 1 $title || echo "N/A" ) | cut -f2
    done
}

ratio (){
    echo "$(process-header $1)/$(process-header $2)"
    paste <(memo collect $1) <(memo collect $2) | while read first second
    do
        python -c "print('{:6.4g}'.format($first / $second))" 2>/dev/null || echo "N/A"
    done
}

export -f memo titles collect ratio process-header

# time memo titles
# time memo titles
# time memo titles

columns=
{
    columns="$columns $(memofile titles)"
    for d in numcl/logs* numpy/logs
    do
        columns="$columns $(memofile collect $d)"
        if ! [ -z $d2 ]
        then
               columns="$columns $(memofile ratio $d2 $d)"
        fi
        d2=$d
    done
    
} > /dev/null

paste $columns | grep "$regexp" | column -t | tee $(date +%Y%m%d%H%M).log
