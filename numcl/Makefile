

all: $(patsubst %.ros,logs/%.log,$(wildcard *.ros))

logs:
	mkdir $@

logs/%.log: %.lisp logs
	ros -L sbcl $< > $@

clean:
	-rm logs/*.log
