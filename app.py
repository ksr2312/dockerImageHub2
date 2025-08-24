from flask import Flask

app=Flask(__name__) ## creating basic flask

@app.route("/") ## for home page
def home():
    return "Hello World!"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)