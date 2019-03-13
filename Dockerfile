FROM python:2.7

COPY . ./

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8080", "-w", "4", "app:app"]
