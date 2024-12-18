# -*- coding: utf-8 -*-
from app import app  # Não é necessário importar o Talisman aqui
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        # Usa o contexto do Flask sem precisar do test_client
        app.config['TESTING'] = True
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False  # Evita redirecionamentos indesejados
        self.client = app.test_client()  # Inicializa o client aqui

    def test_requisicao(self):
        # Envia uma requisição GET para a URL e verifica o status
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)

    def test_conteudo(self):
        # Verifica o conteúdo retornado pela página
        result = self.client.get('/')
        print(result.data.decode('utf-8'))  # Adiciona um print para depuração
        self.assertEqual(result.data.decode('utf-8'), "App do Leonardo Silva Souza github: leosilvasouza")

if __name__ == '__main__':
    unittest.main()
