ARG PYTHON_VERSION=3.12.8

# Run the build stage
FROM python:${PYTHON_VERSION}-slim AS build

# install poetry
ARG POETRY_VERSION=2.0.1
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=0
RUN pip install poetry==$POETRY_VERSION

# install dependencies
COPY pyproject.toml poetry.lock README.md ./
RUN poetry install --no-root --only main

# Create the production image
FROM python:${PYTHON_VERSION}-slim-bullseye AS production
COPY --from=build /usr/local/lib/python${PYTHON_VERSION%.*}/site-packages /usr/local/lib/python${PYTHON_VERSION%.*}/site-packages
COPY pyproject.toml README.md ./
COPY app/ /app
RUN pip install . --no-deps

# Run the application
CMD ["python", "app/main.py"]
