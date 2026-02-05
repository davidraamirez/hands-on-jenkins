from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26383-1381845104-25.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26358-1381845043-13.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-25329-1381845415-0.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-23859-1381845509-0.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-19708-1381845008-7.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-19667-1381844937-10.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-3409-1381844582-13.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-3391-1381844336-26.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-1376-1381846217-0.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26390-1381844163-18.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26388-1381844103-11.gif",
    "https://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-27162-1381845360-0.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
