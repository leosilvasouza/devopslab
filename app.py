from flask import Flask, render_template
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect

# Inicializa o app Flask
app = Flask(__name__)
csrf = CSRFProtect(app)

# Definindo constantes para repetição de strings
SELF = "'self'"

# Definindo a política de segurança de conteúdo
csp = {
    'default-src': SELF,
    'script-src': SELF,
    'style-src': SELF
}

# Configurações de segurança com Flask-Talisman
Talisman(app, content_security_policy=csp, force_https=False)

@app.route("/")
def pagina_inicial():
    return render_template('index.html')  # Renderiza o template HTML para a página inicial

@app.route("/products")
def products():
    return render_template('products/index.html')  # Rendeiza a página de produtos

@app.route("/terms")
def terms():
    return render_template('terms/index.html')  # Rendeiza a página de termos

@app.route("/contact")
def contact():
    return render_template('contact/index.html')  # Rendeiza a página de contato

# Inicializa a aplicação
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
