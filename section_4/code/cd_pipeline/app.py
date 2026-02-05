from flask import Flask, render_template, url_for
import random
import os
import requests

app = Flask(__name__)

# URLs de los GIFs
gif_urls = [
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26383-1381845104-25.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26358-1381845043-13.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-25329-1381845415-0.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-23859-1381845509-0.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-19708-1381845008-7.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-19667-1381844937-10.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-3409-1381844582-13.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-3391-1381844336-26.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-1376-1381846217-0.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26390-1381844163-18.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26388-1381844103-11.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-27162-1381845360-0.gif"
]

# Carpeta local para guardar los GIFs
LOCAL_GIF_DIR = "static/gifs"

os.makedirs(LOCAL_GIF_DIR, exist_ok=True)

# Descargar los GIFs si no existen
for url in gif_urls:
    filename = url.split("/")[-1]
    local_path = os.path.join(LOCAL_GIF_DIR, filename)
    if not os.path.exists(local_path):
        print(f"Descargando {filename}...")
        r = requests.get(url)
        with open(local_path, "wb") as f:
            f.write(r.content)

# Lista de GIFs locales
gifs = os.listdir(LOCAL_GIF_DIR)

@app.route('/')
def index():
    gif_file = random.choice(gifs)
    gif_url = url_for('static', filename=f"gifs/{gif_file}")
    return render_template('index.html', url=gif_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

