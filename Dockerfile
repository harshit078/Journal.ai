FROM python:3.8

WORKDIR /Journal.ai

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8080

COPY . /Journal.ai

CMD streamlit run --server.port 8080 --server.enableCORS false app.py

