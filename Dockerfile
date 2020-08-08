FROM python:3.7-stretch
ARG UPDATE_PYTHON_DEPENDENCIES=""

COPY requirements.txt requirements.lock ./
RUN pip install -U pip
RUN if [ -z "${UPDATE_PYTHON_DEPENDENCIES}" ]; then \
       pip install -r requirements.txt; \
     else \
       pip install -r requirements.lock;fi

WORKDIR /usr/app
COPY src /usr/app/src

ENTRYPOINT ["python3"]
CMD ["src/crawl.py"]
