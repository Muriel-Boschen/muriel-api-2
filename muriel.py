from flask import Flask

app = Flask(__name__)

@app.route('/muriel', methods=['GET'])
def muriel():
    return "oi eu sou a muriel"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
