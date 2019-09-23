

all: $(patsubst %.py,logs/%.log,$(wildcard *.py))

logs:
	-mkdir $@

logs/%.log: %.py logs
	python3 $< -f 'tag!=slow' > $@

clean:
	-rm logs/*.log
