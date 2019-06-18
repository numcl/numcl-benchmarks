

all: $(patsubst %.ros,logs/%.log,$(wildcard *.ros))

logs:
	-mkdir $@

%.bin: %.ros
	ros dump executable $< -o $@

logs/%.log: %.bin logs
	exec ./$< > $@

clean:
	-rm logs/*.log
