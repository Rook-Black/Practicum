FROM python:3.10.4

COPY /app /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm


CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]