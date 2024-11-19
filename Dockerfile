FROM python:3.11

RUN apt-get clean
RUN apt-get update

WORKDIR /app

RUN apt-get update && apt-get install -y \
    xvfb \
    chromium \
    chromium-driver

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PATH="/usr/local/bin/pytest:$PATH"

COPY pages/ ./pages/
COPY tests/ ./tests/
COPY config.py ./
COPY conftest.py ./

CMD ["xvfb-run", "-a", "-s", "'-screen 0 1920x1080x24'", "python3", "-m", "pytest", "tests"]
