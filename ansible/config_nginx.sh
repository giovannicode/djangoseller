# Create nginx configuration file
cat << EOF > /etc/nginx/sites-available/website
server {

    listen 8080;    

    server_name 127.0.0.1;

    access_log off;

    location /static/ {
        alias /home/vagrant/www/static/;
    }

    location /media/ {
        alias /home/vagrant/www/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8001;
        proxy_set_header X-Forwarded-Host \$server_name;
        proxy_set_header x-Real-IP \$remote_addr;
        add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
    }
}
EOF

# Change nginx configuration file to new file
sudo ln -s /etc/nginx/sites-available/website /etc/nginx/sites-enabled/website
sudo rm /etc/nginx/sites-enabled/default

