from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "App do Leonardo Silva Souza github: leosilvasouza"
