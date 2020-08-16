FROM python:3.7.0

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8501

COPY ./ /app

ENTRYPOINT ["streamlit", "run"]

CMD ["app_senior.py"]
