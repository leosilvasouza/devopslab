# Use uma imagem oficial do Python
FROM python:3

# Instalar o Nginx e o supervisord
RUN apt-get update && \
    apt-get install -y nginx supervisor

# Instalar dependências Python
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copiar o arquivo de configuração do Nginx
COPY ./nginx/default.conf /etc/nginx/sites-available/default

# Copiar o arquivo de configuração do supervisor
COPY ./nginx/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expor as portas necessárias
EXPOSE 8080
EXPOSE 5000

# Iniciar o supervisord que gerenciará o Nginx e o Gunicorn
CMD ["/usr/bin/supervisord"]
