FROM python:3.12-slim-bookworm
ARG BUILD_VERSION
ARG BUILD_ARCH
LABEL io.hass.version="${BUILD_VERSION}" io.hass.type="addon" io.hass.arch="${BUILD_ARCH}"
RUN pip install --no-cache-dir paho-mqtt==2.1.0 pyserial==3.5
WORKDIR /app
COPY ca350.py config.ini.dist LICENSE run.py ./
ENV PYTHONUNBUFFERED=1
CMD ["python", "/app/run.py"]
