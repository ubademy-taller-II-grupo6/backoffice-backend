FROM python
WORKDIR /app
COPY ./src/api/*.py ./
COPY ./src/api/requirements.txt ./
RUN pip3 install -r requirements.txt
ENV PORT=$PORT DB_URL=$DB_URL
CMD [ "python3", "main.py" ]