

all: $(patsubst %.py,logs/%.json,$(wildcard *.py))

logs:
	-mkdir $@

logs/%.json: %.py logs
	python3 $< -f 'tag!=slow' -o $@

clean:
	-rm logs/*.json
