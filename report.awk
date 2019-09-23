
/#/ {
    next
}

/^\s*$/ {
    next
}  

{
    print $1"\t"$2
}

