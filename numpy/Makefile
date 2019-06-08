

all: $(patsubst %.py,%.log,$(wildcard *.py))


%.log: %.py
	python3 $< > $@

