
FROM python:3.11

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt



COPY . /app/

RUN chmod +x /app/entrypoint.sh
CMD ["/bin/bash", "/app/entrypoint.sh"]

