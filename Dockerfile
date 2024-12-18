# Use uma imagem oficial do Python
FROM python:3

# Adicionando um usuário de sistema
RUN adduser --system --home /home/myapp  myapp
USER myapp

# Definindo o diretório onde a aplicação será armazenada
WORKDIR /home/myapp

# Definindo o local onde o binário do gunicorn é instalado
ENV PATH="/home/myapp/.local/bin:${PATH}"

# Copiar os arquivos da pasta local para dentro do container
COPY --chown=root:root --chmod=644 app.py requirements.txt /home/myapp/

# Instalar dependências Python
COPY . /home/myapp
# Instalar as dependências de Python de acordo com o que foi desenvolvido na aplicação e que está declarado no arquivo requirements.txt.
RUN pip install --user --trusted-host pypi.python.org -r requirements.txt

# Instalando agente New Relic
WORKDIR /home/myapp
ARG NEW_RELIC_LICENSE_KEY

# Declarando variável que está consumindo o argumento sendo passado na pipeline no --build-arg
ENV NEWRELIC_LICENSE_KEY=${NEW_RELIC_LICENSE_KEY}

# Baixando e instalando o New Relic CLI
RUN curl -Ls https://download.newrelic.com/install/newrelic-cli/scripts/install.sh | bash -s -- -n

# Configurando o agente New Relic com a chave de licença
RUN sudo NEW_RELIC_API_KEY=$NEWRELIC_LICENSE_KEY NEW_RELIC_ACCOUNT_ID=6276743 /usr/local/bin/newrelic install --skip-prompt --tag project:devopslab-impacta

# Gerando arquivo newrelic.ini
RUN newrelic-admin generate-config $NEWRELIC_LICENSE_KEY /home/myapp/newrelic.ini

# Instalar o Nginx e o supervisord
RUN apt-get update && \
    apt-get install -y nginx supervisor


# Copiar o arquivo de configuração do Nginx
COPY ./nginx/default.conf /etc/nginx/sites-available/default

# Copiar o arquivo de configuração do supervisor
COPY ./nginx/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expor as portas necessárias
EXPOSE 8080
EXPOSE 5000

# Iniciar o supervisord que gerenciará o Nginx e o Gunicorn
CMD ["newrelic-admin", "run-program", "/usr/bin/supervisord"]