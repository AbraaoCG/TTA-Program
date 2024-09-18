# Descrição do Projeto

O TTA-Program é uma aplicação web desenvolvida com Django para monitoramento de ações e envio de alertas baseados em parâmetros predefinidos. O sistema permite que os usuários criem monitores de ações, ao definir limites de alerta, e recebam notificações por e-mail quando os valores das ações atingem limites inferiores e superiories desejados. Assim, o sistema verifica os valores das ações em intervalos regulares para facilitar a vida do usuário entusiasta em trading.

# Estrutura do Projeto

O projeto é estruturado da seguinte forma ( principais estruturas ):

    tta_program/: Diretório principal do projeto Django.
        manage.py: Script para gerenciar o projeto Django.
        tta_app/: Diretório que contém as configurações principais do projeto.
            __init__.py: Inicializa o módulo.
            settings.py: Arquivo de configuração do Django.
            celery.py: Configurações do Celery.
        users/: Aplicação para gerenciamento de usuários e perfis.
            models.py: Modelos do Django para usuários e perfis.
            signals.py: Manipuladores de sinais para criar e remover tarefas periódicas.
            tasks.py: Tarefas assíncronas definidas para monitoramento de ações.
        my_dashboard/: Aplicação para a interface do dashboard.
            models.py: Modelos do Django para monitores de ações e registros.
            signals.py: Manipuladores de sinais para tarefas relacionadas a monitores de ações.
            tasks.py: Tarefas assíncronas específicas para o dashboard.

# Bibliotecas Utilizadas

    Django: Framework web para desenvolvimento da aplicação. Utilizado para criar o backend da aplicação, gerenciamento de modelos e formulários, e roteamento de URLs.

    Celery: Biblioteca para execução de tarefas assíncronas e periódicas. Utilizada para verificar o valor das ações em intervalos regulares e enviar alertas.

    django_celery_beat: Extensão do Celery para o Django que permite o agendamento de tarefas periódicas utilizando a base de dados do Django.

    Redis: Servidor de mensagens que atua como broker para o Celery. Utilizado para gerenciar a comunicação entre o Celery e o Django.

    Pandas: Biblioteca para análise de dados, usada para manipular e processar dados financeiros das ações.

    Django REST framework (opcional): Biblioteca para criar APIs RESTful (não mencionada explicitamente, mas pode ser útil para integração de APIs).

# Funcionamento

    Modelos e Tarefas:
        StockMonitor: Modelo para definir os monitores de ações, incluindo símbolo, limites de alerta e perfil do usuário.
        Profile: Modelo para armazenar informações sobre o perfil do usuário e o período de monitoramento.

    Tarefas Periódicas:
        wake_up_monitor_task: Tarefa assíncrona que verifica o valor das ações e envia um e-mail se o valor ultrapassar os limites definidos.
        print_current_time: Exemplo de tarefa que imprime a hora atual (para testes).

    Sinais:
        post_save: Sinal para criar ou atualizar a tarefa periódica quando um StockMonitor é criado ou atualizado.
        post_delete: Sinal para remover a tarefa periódica quando um StockMonitor é deletado.

    Interface do Usuário:
        HTML/JavaScript: A interface permite que os usuários visualizem e editem o período de monitoramento. A alteração do período de monitoramento é feita por meio de uma lista suspensa, e as alterações são enviadas ao servidor por AJAX.

    Envio de E-mails:
        Utiliza a biblioteca django.core.mail para enviar e-mails de alerta quando os valores das ações atingem os limites predefinidos.

# Configuração do Ambiente para envio de e-mails aos usuários.

Para proteger informações sensíveis, o projeto utiliza um arquivo de configuração não incluídos no repositório:

Crie um arquivo chamado password.py na mesma pasta que o settings.py. Este arquivo deve conter a senha do e-mail:


### password.py
```
    email_host_password = 'sua_senha_de_email'
```

Alterações no settings.py

No arquivo settings.py, ajuste a configuração do e-mail para usar a senha definida em password.py:

python

### settings.py
```
    from tta_app.password import email_host_password  # Importa a senha do arquivo password.py
    
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.your-email-provider.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'your-email@example.com'
    EMAIL_HOST_PASSWORD = email_host_password  # Usa a senha do arquivo password.py
  
```

# Etapas de Configuração do Django e Bibliotecas

1. Configuração do Ambiente Virtual

Antes de instalar as dependências, é recomendável criar um ambiente virtual para isolar as bibliotecas do projeto.

```console
python3 -m venv venv
source venv/bin/activate  # Para sistemas Unix
venv\Scripts\activate  # Para Windows

```

2. Instalação das Dependências

Instale todas as dependências necessárias a partir do arquivo requirements.txt ou manualmente se as dependências não estiverem especificadas.

```console

pip install -r requirements.txt

```

3. Migração do Banco de dados - Django

Execute os comandos necessários para configurar corretamente o banco de dados 'Sqlite3' com o código.


```console
python manage.py makemigrations
python manage.py migrate

```

4. Configuração do django-celery-beat

```console
python manage.py migrate django_celery_beat
```

5. Criação de um super usuário.

```console
python manage.py createsuperuser

```

# Etapas de Execução:


## Iniciar o Servidor de Desenvolvimento 
```console
python manage.py runserver

```


## Iniciar o Worker do Celery 
```console
celery -A tta_app worker --loglevel=info

```


## Iniciar o Scheduler do Celery 
```console
celery -A tta_app beat --loglevel=info

```






