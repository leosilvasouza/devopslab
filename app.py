from flask import Flask
from flask_talisman import Talisman

# Inicializa o app Flask
app = Flask(__name__)

# Definindo a política de segurança de conteúdo
csp = {
    'default-src': '\'self\'',
    'script-src': '\'self\'',
    'style-src': '\'self\''
}

# Configurações de segurança com Flask-Talisman
Talisman(app, content_security_policy=csp, force_https=False)

@app.route("/")
def pagina_inicial():
    return "App do Leonardo Silva Souza github: leosilvasouza"
    
# Inicializa a aplicação
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
