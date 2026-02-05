from flask import Flask, render_template, url_for
import random
import os
import requests

app = Flask(__name__)

# Carpeta local para guardar los GIFs
LOCAL_GIF_DIR = "static/gifs"

# Lista de GIFs locales
gifs = os.listdir(LOCAL_GIF_DIR)

@app.route('/')
def index():
    gif_file = random.choice(gifs)
    gif_url = url_for('static', filename=f"gifs/{gif_file}")
    return render_template('index.html', url=gif_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

