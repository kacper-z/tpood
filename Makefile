
IMAGE_NAME = "tpood"
IMAGE_NAME_DEBUG = "tpood_debug"

# creating virtual environment
%.txt: %.in
	pip-compile --generate-hashes $<

.PHONY:
venv: requirements.txt
	python3.9 -m venv .venv
	. .venv/bin/activate; \
	pip install --upgrade virtualenv; \
	pip install --upgrade pip pip-tools setuptools wheel; \
	pip install -r requirements.txt

.PHONY:
venv-dev: requirements-dev.txt
	pip-sync requirements-dev.txt requirements.txt

# building docker image
.PHONY:
docker-build:
	docker build -t $(IMAGE_NAME) .

# running app in docker
.PHONY:
docker-run: docker-build
	docker run --rm -p 8000:8000 $(IMAGE_NAME)

.PHONY:
docker-compose-run: docker-build
	docker-compose build
	docker-compose up


# running tests
.PHONY: docker-build
test: 
	docker run --rm $(IMAGE_NAME) python -m pytest 

.PHONY: venv
black:
	black src/

.PHONY: venv
pylint:
	pylint src/

.PHONY: venv
mypy:
	mypy src/

# cleanup
.PHONY:
venv-clean:
	rm -rf .venv
