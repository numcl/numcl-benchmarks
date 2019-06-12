
all:
	$(MAKE) -C numcl
	$(MAKE) -C numpy
clean:
	$(MAKE) -C numcl clean
	$(MAKE) -C numpy clean

