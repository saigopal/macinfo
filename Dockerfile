FROM python:3.7.2-alpine3.8 as base
COPY requirements* ./
COPY src app/

FROM base as test
COPY tests /app/tests
RUN pip install --no-cache-dir -r requirements_test.txt
WORKDIR /app
ENTRYPOINT ["python", "-m", "pytest", "-sv" ,".", "/app/tests"]

FROM base as release
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app
ENTRYPOINT ["python", "macinfo.py"]
