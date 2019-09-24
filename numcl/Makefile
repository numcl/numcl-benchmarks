

all: $(patsubst %.ros,logs/%.log,$(wildcard *.ros))

logs/%.log: %.ros timer.lisp
	mkdir -p logs
	./$< > $@

clean:
	-rm logs/*.log
