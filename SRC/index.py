from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #pagina principal
def home():
    return render_template('home.html')

@app.route('/quienessomos') #quienes somos
def quienessomos():
    return render_template('quienessomos.html')

if __name__ == '__main__':
    app.run(debug = True)
