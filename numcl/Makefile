

all: $(patsubst %.ros,%.log,$(wildcard *.ros))


%.log: %.lisp
	ros -L sbcl $< > $@

