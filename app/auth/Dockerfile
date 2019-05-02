FROM python:latest
WORKDIR /app/auth
COPY . /app/auth
EXPOSE 5001
RUN pip install --trusted-host mirrors.aliyun.com --index-url https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
CMD ["python", "/app/auth/run.py"]
