FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --force-reinstall httpcore==0.15
COPY . .

EXPOSE 80

CMD [ "python", "__main__.py"]
