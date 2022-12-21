FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7 as base

ADD requirements.txt .
RUN pip3 install -r requirements.txt

ENV PYTHONPATH=$PYTHONPATH:/src/

ADD ./ /src/

WORKDIR /src

EXPOSE 800

FROM base as build
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "800","--reload"]

