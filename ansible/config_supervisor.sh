cat << EOF > /etc/supervisor/conf.d/gunicorn.conf
[program:gunicorn]
command=gunicorn -c /home/vagrant/www/gunicorn/conf.py seller.wsgi
directory=/home/vagrant/www/website
user=vagrant
autostart=true
autorestart=true
stderr_logfile=/var/log/supervisor/gunicorn/err.log
stdout_logfile=/var/log/supervisor/gunicorn/out.log
