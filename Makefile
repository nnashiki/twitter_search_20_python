build:
	docker build . -t twipy

update-dependencies:
	docker build . --build-arg UPDATE_PYTHON_DEPENDENCIES="TRUE" -t twipy
	docker run -it --rm --entrypoint '/usr/local/bin/pip' twipy freeze > requirements.lock

sh:
	docker run -it --rm --entrypoint 'sh' twipy

run:
	docker run -it --rm -v ${PWD}:/usr/app -w /usr/app twipy
