FROM python:3.12-slim
WORKDIR /app
ADD templates /app/templates
COPY app.py requirements.txt .
RUN pip install -r requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]