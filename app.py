from flask import Flask, render_template
import os

app = Flask(__name__)

apio = 'apio'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apio', methods=['GET'])
def get_users():
    return apio
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
