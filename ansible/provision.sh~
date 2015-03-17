# Set up postgres DB
echo "Setup postgres"
sudo -u postgres psql <<< "
CREATE DATABASE sellerdb;
CREATE USER seller1 WITH PASSWORD 'sellerpassword';
GRANT ALL PRIVILEGES ON DATABASE sellerdb TO seller1;
"
