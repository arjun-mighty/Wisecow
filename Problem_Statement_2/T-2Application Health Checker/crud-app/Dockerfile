FROM ghcr.io/astral-sh/uv:alpine
ADD . /app
WORKDIR /app
RUN uv sync --frozen
EXPOSE 8000
CMD ["uv", "run", "fastapi", "run"]
