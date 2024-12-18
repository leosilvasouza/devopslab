# -*- coding: utf-8 -*-
from app import app
from flask_talisman import Talisman
import unittest

# Criando variáveis
# Definindo a política de segurança de conteúdo (csp)
csp = {
    'default-src': '\'self\'',
    'script-src': '\'self\'',
    'style-src': '\'self\''
}

class Test(unittest.TestCase):
    def setUp(self):
        # Usa o contexto do Flask sem precisar do test_client
        app.config['TESTING'] = True
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False  # Evita redirecionamentos indesejados
        app.config['PREFERRED_URL_SCHEME'] = 'http' # Força uso de HTTP no teste
        Talisman(app, content_security_policy=csp, force_https=False) # Configura Talisman
        self.client = app.test_client()

    def test_requisicao(self):
        # Envia uma requisição GET para a URL e verifica o status
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)

    def test_conteudo(self):
        # Verifica o conteúdo retornado pela página
        result = self.client.get('/')
        print(result.status_code)  # Imprime o código de status para depuração
        print(result.data.decode('utf-8'))  # Adiciona um print para depuração
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode('utf-8'), "App do Leonardo Silva Souza github: leosilvasouza")

if __name__ == '__main__':
    unittest.main()

