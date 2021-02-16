FROM python:3.8-slim-buster

LABEL author="Johan Schreurs" version="1.0"

WORKDIR /app

ENV FLASK_APP=/app/helloworld/app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000

#
# I switched to using a volume linked to my local code, for easier development and demonstration.
# For production we would need to copy the following:
#
# COPY example-config/example_config.py /app/instance/config.py
# COPY helloworld /app/helloworld

CMD ["flask", "run"]