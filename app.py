from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('wish.html', brother_name='Sri Hari')

if __name__ == '__main__':
    app.run(debug=True)