FROM python:3.12-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

RUN pip install --no-cache-dir sympy==1.12

COPY dockerapp/SPH_DLP_docker.py .

RUN adduser --disabled-password \
            --no-create-home \
            --uid 1000 \
            --gecos "" \
            appuser \
    && chown appuser:appuser /app

USER appuser

CMD ["python", "-u", "SPH_DLP_docker.py"]