FROM python:3.11-alpine AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    python -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

FROM python:3.11-alpine
WORKDIR /app
COPY --from=builder /app/venv /app/venv
COPY . .

# Activate the virtual environment
ENV PATH="/app/venv/bin:$PATH"

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
