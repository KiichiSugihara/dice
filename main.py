import random
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    dice = 0
    if request.args.get('dice',''):
        dice = random.randint(1,6)

    return render_template('index.html',dice=dice)



if __name__ == '__main__':
    # IPアドレス0.0.0.0の8000番ポートでアプリケーションを実行します
    app.run('0.0.0.0', 8000, debug=True)
