FROM python:latest

WORKDIR /app/auth

copy . /app/auth

RUN pip install --trusted-host mirrors.aliyun.com --index-url https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt

EXPOSE 5001

CMD ["python", "/app/auth/run.py"]
