from flask import Flask
from flask_talisman import Talisman

# Inicializa o app Flask
app = Flask(__name__)

# Configurações de segurança com Flask-Talisman
csp = {
    'default-src': '\'self\'',
    'script-src': '\'self\'',
    'style-src': '\'self\''
}
Talisman(app, content_security_policy=csp)

@app.route('/')
def home():
    return 'Hello, Secure World!'

# Inicializa a aplicação
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
