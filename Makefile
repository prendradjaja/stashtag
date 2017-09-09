.PHONY: test
test:
	. env/bin/activate
	env/bin/py.test
