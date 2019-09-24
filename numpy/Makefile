

all: $(patsubst %.py,logs/%.log,$(wildcard *.py))

logs/%.log: %.py
	mkdir -p logs
	python3 $< -f 'tag!=slow' > $@

clean:
	-rm logs/*.log
