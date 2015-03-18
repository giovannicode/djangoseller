cat << EOF > /etc/supervisor/conf.d/gunicorn.conf
[program:gunicorn]
command=gunicorn -c /home/root/www/gunicorn/conf.py seller.wsgi
directory=/home/root/www/website
user=root
autostart=true
autorestart=true
stderr_logfile=/var/log/supervisor/gunicorn/err.log
stdout_logfile=/var/log/supervisor/gunicorn/out.log
EOF
