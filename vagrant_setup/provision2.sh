# Install django website dependencies
echo "Install Django website dependencies"
sudo pip install pillow >/dev/null 2>&1
sudo pip install django-bootstrap-form >/dev/null 2>&1
sudo pip install django-floppyforms >/dev/null 2>&1
sudo pip install stripe >/dev/null 2>&1

#start gunicorn 
echo "Start gunicorn with supervisor"
sudo supervisorctl reread
sudo supervisorctl update

# Install frontend frameworks
sudo npm install -g bower
