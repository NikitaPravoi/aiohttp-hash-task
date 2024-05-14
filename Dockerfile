FROM python:3.12-slim
LABEL maintainer="nikitapravoi@yandex.ru"

WORKDIR /app/src
COPY . /app

RUN pip install --no-cache-dir aiohttp click pytest pytest-aiohttp

EXPOSE 8080

# Mentioned default parameters just to avoid inconveniences
CMD ["python", "main.py", "--host", "0.0.0.0", "--port", "8080"]

HEALTHCHECK --interval=1m --timeout=3s \
  CMD curl -f http://0.0.0.0/ || exit 1
