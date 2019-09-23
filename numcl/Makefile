

all: $(patsubst %.ros,logs/%.log,$(wildcard *.ros))

logs:
	-mkdir $@

# %.bin: %.ros
# 	ros dump executable $< -o $@

logs/%.log: %.ros timer.lisp
	./$< > $@

clean:
	-rm logs/*.log
