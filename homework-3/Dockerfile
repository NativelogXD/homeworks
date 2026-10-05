FROM python:3.11-slim

WORKDIR /app

# Install uv for fast, reliable dependency resolution
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy dependency files first for Docker caching
COPY pyproject.toml uv.lock ./

# Install dependencies (production only, no dev)
RUN uv sync --frozen --no-dev

# Copy application files
COPY . .

# Documentation: Port 8000
EXPOSE 8000

# Run uvicorn on 0.0.0.0 so Docker port mapping (-p) works
CMD ["/bin/uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
