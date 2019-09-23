

all: $(patsubst %.ros,logs/%.log,$(wildcard *.ros))

logs:
	-mkdir $@

# %.bin: %.ros
# 	ros dump executable $< -o $@

logs/%.log: %.ros logs
	./$< > $@

clean:
	-rm logs/*.log
