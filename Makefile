build:
	docker build . -t twipy

update-dependencies:
	docker build . --build-arg UPDATE_PYTHON_DEPENDENCIES="TRUE" -t twipy
	docker run -it --rm --entrypoint '/usr/local/bin/pip' twipy freeze > requirements.lock

sh:
	docker run -it --rm --entrypoint 'sh' twipy

format:
	isort src/*.py
	black -l 100 src/*.py
	mypy src/*.py

init:
	python3 -m venv venv
	(. venv/bin/activate && pip -U pip && pip install -r requirements.txt)

run:
	docker run -it --rm -v ${PWD}:/usr/app -w /usr/app twipy

