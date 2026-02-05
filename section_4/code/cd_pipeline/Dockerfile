FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./
COPY templates/ templates/

# Crear la carpeta de GIFs vacía (los GIFs se descargan al iniciar)
RUN mkdir -p static/gifs
COPY static/ static/

EXPOSE 5000

CMD ["python", "app.py"]
