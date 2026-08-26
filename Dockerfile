FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock README.md ./
COPY src/ ./src/

RUN pip install --no-cache-dir uv && uv sync --frozen

CMD ["uv", "run", "ai-use-philosophy"]