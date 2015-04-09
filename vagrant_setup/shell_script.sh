cat "env_vars" >> ".bashrc"
source /home/vagrant/.bashrc
python /home/vagrant/www/website/manage.py migrate
python /home/vagrant/www/website/manage.py collectstatic --noinput
