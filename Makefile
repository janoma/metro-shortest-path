init:
	pip3 install --user --quiet --requirement requirements.txt

test:
	py.test tests

.PHONY: init test
