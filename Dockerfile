FROM python:3.11-slim

WORKDIR /code
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

# run UI tests against the remote Chrome in the selenium container
CMD pytest tests/ui -q \
    --driver Remote \
    --capability browserName chrome \
    --selenium-host chrome --selenium-port 4444
