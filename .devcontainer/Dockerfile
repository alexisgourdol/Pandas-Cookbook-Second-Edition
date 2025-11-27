ARG PLATFORM=amd64
FROM --platform=linux/${PLATFORM} python:3.11 AS base

WORKDIR /workspace

RUN apt-get update \
    && apt-get install -y --no-install-recommends less curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

# =============================================================================
# Development stage - includes dev tools and dependencies
# =============================================================================
FROM base AS dev

# Suppress uv hardlink warning for bind-mounted volumes
ENV UV_LINK_MODE=copy

# Copy project files for initial setup
COPY pyproject.toml uv.lock* ./

# Add venv to PATH
ENV PATH=/workspace/.venv/bin:${PATH}

# =============================================================================
# Production stage - minimal, production-ready image
# =============================================================================
FROM base AS prod

# Copy project metadata
COPY pyproject.toml uv.lock* ./

# Copy full project
COPY . .

# Create venv and install production dependencies
RUN uv venv /workspace/.venv \
    && . /workspace/.venv/bin/activate \
    && uv pip install --no-cache-dir -e .

# Add venv to PATH
ENV PATH=/workspace/.venv/bin:${PATH}
