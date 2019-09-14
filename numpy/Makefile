

all: $(patsubst %.py,logs/%.json,$(wildcard *.py))

logs:
	-mkdir $@

logs/%.json: %.py logs
	python3 $< -o $@

clean:
	-rm logs/*.json
