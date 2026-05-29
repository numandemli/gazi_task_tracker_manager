FROM python:3.12-slim

# Python çalışma ortamı değişkenleri
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP run.py

# Çalışma dizini oluştur
WORKDIR /app

# PostgreSQL ve c derleyicisi gereksinimlerini kur (psycopg2 derlemesi için)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Bağımlılıkları kopyala ve yükle
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Proje kaynak kodlarını kopyala
COPY . /app/

# Gunicorn servis portunu dışarı aç
EXPOSE 5000

# Uygulamayı Gunicorn WSGI sunucusuyla başlat
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
