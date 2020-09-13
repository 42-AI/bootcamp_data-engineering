#! /bin/bash
yum install -y mysql
export MYSQL_HOST=${rds_address}

mysql -u ${rds_user} -p${rds_password} -D ${rds_db} -e "CREATE USER IF NOT EXISTS 'wordpress' IDENTIFIED BY 'wordpress-pass';"
mysql -u ${rds_user} -p${rds_password} -D ${rds_db} -e "GRANT ALL PRIVILEGES ON wordpress.* TO wordpress;"
mysql -u ${rds_user} -p${rds_password} -D ${rds_db} -e "FLUSH PRIVILEGES;"

yum install -y httpd
service httpd start

wget https://wordpress.org/latest.tar.gz
tar -xzf latest.tar.gz

cd wordpress
cp wp-config-sample.php wp-config.php

sed -e "s/'database_name_here'/'${rds_db}'/g" wp-config.php > tmp.txt; mv tmp.txt wp-config.php
sed -e "s/'username_here'/'${rds_user}'/g" wp-config.php > tmp.txt; mv tmp.txt wp-config.php
sed -e "s/'password_here'/'${rds_password}'/g" wp-config.php > tmp.txt; mv tmp.txt wp-config.php
sed -e "s/'localhost'/'${rds_address}'/g" wp-config.php > tmp.txt; mv tmp.txt wp-config.php

sed -e "/.*'put your unique phrase here'.*/d" wp-config.php > tmp.txt; mv tmp.txt wp-config.php
curl https://api.wordpress.org/secret-key/1.1/salt >> wp-config.php

amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
cd /home/ec2-user
cp -r /wordpress/* /var/www/html/
service httpd restart