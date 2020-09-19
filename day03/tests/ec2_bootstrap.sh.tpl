#! /bin/bash
yum install -y mysql
export MYSQL_HOST=${rds_address}
echo "export MYSQL_HOST=${rds_address}" > /home/ec2-user/.bashrc

mysql --user=${rds_user} --password=${rds_password} --database=${rds_db} -e "CREATE USER IF NOT EXISTS 'wordpress' IDENTIFIED BY 'wordpress-pass';"
mysql --user=${rds_user} --password=${rds_password} --database=${rds_db} -e "GRANT ALL PRIVILEGES ON wordpress.* TO wordpress;"
mysql --user=${rds_user} --password=${rds_password} --database=${rds_db} -e "FLUSH PRIVILEGES;"

yum install -y httpd
service httpd start

wget https://wordpress.org/latest.tar.gz
tar -xzf latest.tar.gz

cd wordpress
cp wp-config-sample.php wp-config.php

sed -i "s/'database_name_here'/'${rds_db}'/g" wp-config.php
sed -i "s/'username_here'/'wordpress'/g" wp-config.php
sed -i "s/'password_here'/'wordpress-pass'/g" wp-config.php
sed -i "s/'localhost'/'${rds_address}'/g" wp-config.php


sed -i "/.*'put your unique phrase here'.*/d" wp-config.php
curl https://api.wordpress.org/secret-key/1.1/salt > salt.txt
sed -i '48 r salt.txt' wp-config.php
sed -i 's/\r//g' wp-config.php

sed -i "7i\$output = shell_exec('curl ifconfig.me');" wp-blog-header.php
sed -i "8iecho \"<p style='color:red'>(\$output)</p>\";" wp-blog-header.php

amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
cp -r /wordpress/* /var/www/html/
service httpd restart
