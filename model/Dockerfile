FROM python:3.10.6 as base

ADD requirements.txt .
RUN pip3 install -r requirements.txt

ENV PYTHONPATH=$PYTHONPATH:/src/

ADD ./ /src/

WORKDIR /src

FROM base as build
ENTRYPOINT ["python3", "/src/ml_service.py"]

