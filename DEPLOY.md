# 🚀 Guia de Deploy - Fernanda Doces

## Opção 1: Railway (Recomendado)

### Pré-requisitos
- Conta no [Railway](https://railway.app/)
- Projeto no GitHub (com branches: `main` e `development`)

### Passo a Passo

#### 1. Configure o repositório
```bash
# Certifique-se de ter um .gitignore completo
git add .
git commit -m "Ready for production"
git push origin main
```

#### 2. No painel do Railway
1. Clique em "Create New Project"
2. Selecione "GitHub" e conecte seu repositório
3. Selecione a branch `main`

#### 3. Configure as variáveis de ambiente
Em **Settings → Variables**:

```
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=gere-uma-chave-secreta-forte
ALLOWED_HOSTS=seu-app-name.up.railway.app
CSRF_TRUSTED_ORIGINS=https://seu-app-name.up.railway.app
DATABASE_URL=seu-banco-postgresql-railway
WHATSAPP_NUMBER=5532984069242
```

#### 4. Configure o banco de dados
1. Clique em "Add Service"
2. Selecione "PostgreSQL"
3. Railway vai gerar `DATABASE_URL` automaticamente

#### 5. Execute migrações
```bash
# Via Railway CLI
railway run python manage.py migrate
railway run python manage.py createsuperuser
railway run python manage.py collectstatic --noinput
```

#### 6. Deploy automático
- Railway faz deploy automático quando você faz push para `main`
- Acesse: `https://seu-app-name.up.railway.app`

---

## Opção 2: Heroku (Alternativa)

### Pré-requisitos
- Conta no [Heroku](https://heroku.com/)
- Heroku CLI instalado

### Passo a Passo

#### 1. Crie um arquivo `Procfile`
```
web: gunicorn core.wsgi --log-file -
release: python manage.py migrate
```

#### 2. Configure para Heroku
```bash
# Login
heroku login

# Crie app
heroku create seu-app-name

# Configure variáveis
heroku config:set DJANGO_DEBUG=False
heroku config:set DJANGO_SECRET_KEY=sua-chave-secreta
heroku config:set ALLOWED_HOSTS=seu-app-name.herokuapp.com

# Deploy
git push heroku main
```

---

## Opção 3: VPS/Servidor Próprio

### Pré-requisitos
- VPS com Ubuntu 20.04+
- SSH access
- Domínio configurado

### Instalação

#### 1. Conecte ao servidor
```bash
ssh user@seu-ip
```

#### 2. Instale dependências
```bash
sudo apt update
sudo apt install python3-pip python3-venv postgresql postgresql-contrib nginx supervisor
```

#### 3. Clone o projeto
```bash
cd /home/user
git clone seu-repositorio fernanda_doces
cd fernanda_doces
```

#### 4. Setup Django
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure .env
nano .env
```

#### 5. Configure banco PostgreSQL
```bash
sudo -u postgres psql
CREATE DATABASE fernanda_doces;
CREATE USER fernanda WITH PASSWORD 'sua-senha-forte';
ALTER ROLE fernanda SET client_encoding TO 'utf8';
ALTER ROLE fernanda SET default_transaction_isolation TO 'read committed';
ALTER ROLE fernanda SET default_transaction_deferrable TO on;
ALTER ROLE fernanda SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE fernanda_doces TO fernanda;
\q
```

#### 6. Configure .env para produção
```bash
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=super-chave-secreta-forte
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
DATABASE_URL=postgresql://fernanda:senha@localhost:5432/fernanda_doces
```

#### 7. Rode migrações
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

#### 8. Configure Gunicorn
Create `/home/user/fernanda_doces/gunicorn_config.py`:
```python
import multiprocessing

bind = '127.0.0.1:8000'
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
timeout = 30
```

#### 9. Configure Supervisor
Create/edit `/etc/supervisor/conf.d/fernanda_doces.conf`:
```ini
[program:fernanda_doces]
directory=/home/user/fernanda_doces
command=/home/user/fernanda_doces/venv/bin/gunicorn \
    --config gunicorn_config.py \
    core.wsgi:application
user=user
autostart=true
autorestart=true
startsecs=10
stopwaitsecs=10
stdout_logfile=/home/user/fernanda_doces/logs/gunicorn.log
stderr_logfile=/home/user/fernanda_doces/logs/error.log
```

```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start fernanda_doces
```

#### 10. Configure Nginx
Create `/etc/nginx/sites-available/fernanda_doces`:
```nginx
upstream fernanda_doces {
    server 127.0.0.1:8000;
}

server {
    listen 80;
    server_name seu-dominio.com www.seu-dominio.com;

    client_max_body_size 10M;

    location /static/ {
        alias /home/user/fernanda_doces/staticfiles/;
    }

    location /media/ {
        alias /home/user/fernanda_doces/media/;
    }

    location / {
        proxy_pass http://fernanda_doces;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/fernanda_doces /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### 11. SSL com Let's Encrypt
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d seu-dominio.com -d www.seu-dominio.com
```

---

## Checklist de Segurança

- [ ] DEBUG = False
- [ ] SECRET_KEY alterada
- [ ] ALLOWED_HOSTS configurado
- [ ] CSRF_TRUSTED_ORIGINS definido
- [ ] Banco de dados com senha forte
- [ ] SSL/HTTPS configurado
- [ ] Backups automáticos do banco
- [ ] Logs monitora​dos
- [ ] Firewall habilitado
- [ ] Atualizações de segurança aplicadas

---

## Monitoramento

### Logs no Rail
```bash
railway logs
```

### Logs em VPS
```bash
# Gunicorn
tail -f /home/user/fernanda_doces/logs/gunicorn.log

# Nginx
sudo tail -f /var/log/nginx/error.log

# Django
tail -f /home/user/fernanda_doces/logs/django.log
```

### Backups
```bash
# PostgreSQL backup
pg_dump fernanda_doces > backup-$(date +%Y%m%d).sql

# Restore
psql fernanda_doces < backup-20260414.sql
```

---

## Troubleshooting

### Erro: "Static files not found"
```bash
python manage.py collectstatic --noinput
# Em produção: certifique-se que STATIC_ROOT está configurado
```

### Erro: "Database connection refused"
```bash
# Verifique DATABASE_URL
python manage.py dbshell

# Ou teste migração
python manage.py migrate --verbosity 3
```

### App crashes no Railway
```bash
railway logs  # Leia os logs
# Geralmente causado por variáveis de ambiente faltantes
```

---

## Performance

### Cache
```python
# settings.py (em produção)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

### CDN
Configure cloudflare para servir arquivos estáticos

### Compressão
```python
# settings.py
MIDDLEWARE += ['django.middleware.gzip.GZipMiddleware']
```

---

Dúvidas? Entre em contato! 📞
