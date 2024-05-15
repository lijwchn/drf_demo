FROM python:3.10-alpine
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -i https://mirror.baidu.com/pypi/simple -r requirements.txt
CMD ["gunicorn", "drf_demo.wsgi", "-b", "0.0.0.0:8000", "--workers", "4"]