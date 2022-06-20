FROM python:3.9.13-slim

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install --no-cache-dir 'mlflow==1.26.1'

CMD mlflow server \
    --backend-store-uri sqlite:////app/mlruns.db \
    --default-artifact-root $ARTIFACT_ROOT \
    --host 0.0.0.0
