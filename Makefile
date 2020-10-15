install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	pylint --disable=R,C hello.py

#format:
#	black *.py

test:
	python -m pytest -vv --cov=hello test_hello.py
