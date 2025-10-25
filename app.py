
from flask import Flask, render_template
from memories import SECTIONS, HERO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', hero=HERO, sections=SECTIONS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
