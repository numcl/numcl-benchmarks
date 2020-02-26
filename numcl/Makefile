
version = $(shell ros -s numcl -e "(write-sequence (numcl:numcl-version) *standard-output*)")

all: $(patsubst %.ros,logs-$(version)/%.log,$(wildcard *.ros))

logs-$(version)/0template.log: 0template.ros timer.lisp
	mkdir -p logs-$(version)
	./$< > $@

logs-$(version)/%.log: %.ros timer.lisp logs-$(version)/0template.log
	mkdir -p logs-$(version)
	./$< > $@

clean:
	-rm logs-$(version)/*.log
