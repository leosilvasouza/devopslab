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
        # Cria um cliente de teste
        with app.test_client() as client:
            # Faz a requisição GET para a página inicial
            response = client.get('/')
            
            # Verifica se a resposta contém partes do conteúdo esperado
            self.assertIn('Bem-vindo ao App de Leonardo Silva Souza', response.data.decode('utf-8'))
            self.assertIn('Produtos', response.data.decode('utf-8'))
            self.assertIn('Termos de Uso', response.data.decode('utf-8'))
            self.assertIn('Contato', response.data.decode('utf-8'))
        # Verifica o conteúdo retornado pela página
        result = self.client.get('/')
        print(result.data.decode('utf-8'))  # Adiciona um print para depuração

if __name__ == '__main__':
    unittest.main()
