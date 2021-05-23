from flask import flask
app = Flask("__name__)

@app.route("/exemplo/<int:id>")
def hello1(id):
    return "Hello Wold, %s" %(id)

@app.route("/exemplo/)
def hello():
    return "Teste sua nova rota"

if __name__ =  "__main__":
    app.run(debug=True)