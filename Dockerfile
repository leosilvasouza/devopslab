# Use uma Imagem Official do Python
FROM python:3

# Instalar o Nginx
RUN apt-get update && apt-get install -y nginx

# Definindo o diretório onde a aplicação será armazenada
WORKDIR /app

# Copiar os arquivos da pasta local para dentro do container
COPY . /app

# Instalar as dependências de Python de acordo com o que foi desenvolvido na aplicação e que está declarado no arquivo requirements.txt.
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Instalar o Flask-Talisman (se necessário)
RUN pip install flask-talisman

# Copiar a configuração do Nginx
COPY ./nginx/default.conf /etc/nginx/sites-available/default

# Expor a porta 80 para o Nginx
EXPOSE 80

# Expor a porta 5000 para o Gunicorn
EXPOSE 5000

# Executar a inicialização do nginx
service nginx start 

# Execução do gunicorn na porta 5000 exposta
gunicorn -b 0.0.0.0:5000

# Rodar a aplicação em python
CMD ["app:app"]
