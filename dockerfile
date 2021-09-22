FROM python:3.8
WORKDIR /usr/src/app
COPY ./src/*.py ./
COPY ./src/requirements.txt ./
RUN pip install -r requirements.txt
CMD [ "uvicorn", "main:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "8000" ]