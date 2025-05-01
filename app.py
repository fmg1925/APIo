from flask import Flask, render_template

app = Flask(__name__)

apio = 'apio'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apio', methods=['GET'])
def get_users():
    return apio
    
if __name__ == '__main__':
    app.run(debug=True)
