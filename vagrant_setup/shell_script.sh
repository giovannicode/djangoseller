#!/bin/bash
cat "env_vars.txt" >> ".bashrc"
#source /home/vagrant/.bashrc && /home/vagrant/www/website/manage.py migrate
#source /home/vagrant/.bashrc && /home/vagrant/www/website/manage.py collectstatic --noinput
export SECRET_KEY="spaghvprf#2rgbho_jo^0n(2(tv3w@lxxp9mf#j+k2q^@+3x5k"
export NAME='sellerdb'
export USER='seller1'
export PASSWORD='sellerpassword'
export EMAIL_HOST='smtp.gmail.com'
export EMAIL_PORT='587'
export EMAIL_HOST_USER='testemailecom@gmail.com'
export EMAIL_HOST_PASSWORD='djangomonster8'

python /home/vagrant/www/website/manage.py migrate
python /home/vagrant/www/website/manage.py collectstatic --noinput
python /home/vagrant/www/website/manage.py loaddata /home/vagrant/www/website/initial_data.json
