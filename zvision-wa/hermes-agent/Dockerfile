FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg curl && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

RUN useradd -m -u 10000 hermes

WORKDIR /opt/hermes

COPY requirements.txt ./
RUN uv venv /opt/hermes/.venv && \
    . /opt/hermes/.venv/bin/activate && \
    uv pip install -r requirements.txt

COPY --chown=hermes:hermes . .

RUN mkdir -p /opt/data/leads /opt/data/knowledge /opt/data/sessions && \
    chown -R hermes:hermes /opt/data

ENV VIRTUAL_ENV=/opt/hermes/.venv
ENV PATH="/opt/hermes/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1
ENV HERMES_HOME=/opt/data

USER hermes

EXPOSE 3400

CMD ["python", "main.py"]
