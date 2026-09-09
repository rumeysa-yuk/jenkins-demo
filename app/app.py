from flask import Flask

app = Flask(__name__)

def topla(a, b):
    return a + b

@app.route("/")
def home():
    return "Merhaba Jenkins! 2 + 3 = " + str(topla(2, 3))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)