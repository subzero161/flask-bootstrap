from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index-2')
def bootstrap():
    return render_template('index-2.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
