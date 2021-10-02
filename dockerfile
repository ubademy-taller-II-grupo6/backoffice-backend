FROM python
WORKDIR /usr/src/app
COPY ./src/*.py ./
COPY ./src/requirements.txt ./
RUN pip3 install -r requirements.txt
ENV PORT=$PORT DB_URL=$DB_URL
CMD [ "python3", "main.py" ]