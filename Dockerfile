FROM python

WORKDIR /chatbot

ARG secret_key
ENV secret_key=$secret_key
COPY firebase-key.json.gpg ./
CMD ["sh","decrypt_secret.sh","$secret_key"]

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY main.py ./

ENTRYPOINT ["python", "main.py"]

