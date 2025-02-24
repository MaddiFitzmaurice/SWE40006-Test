FROM python:3.12.3

WORKDIR /app

COPY . .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python", "web_calculator.py"]
