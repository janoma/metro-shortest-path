init:
	pip install --quiet --requirement requirements.txt

test:
	py.test tests
