

all: $(patsubst %.ros,logs/%.log,$(wildcard *.ros))

logs/0template.log: 0template.ros timer.lisp
	mkdir -p logs
	./$< > $@

logs/%.log: %.ros timer.lisp logs/0template.log
	mkdir -p logs
	./$< > $@

clean:
	-rm logs/*.log
