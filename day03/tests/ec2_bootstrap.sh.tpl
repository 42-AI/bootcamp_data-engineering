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

sed -e "s/DB_NAME.*/toto/g" 1.txt > 2.txt
define( 'DB_NAME', 'database_name_here' );
define( 'DB_USER', 'username_here' );
define( 'DB_PASSWORD', 'password_here' );
define( 'DB_HOST', 'localhost' );

# define( 'AUTH_KEY',         'put your unique phrase here' );
# define( 'SECURE_AUTH_KEY',  'put your unique phrase here' );
# define( 'LOGGED_IN_KEY',    'put your unique phrase here' );
# define( 'NONCE_KEY',        'put your unique phrase here' );
# define( 'AUTH_SALT',        'put your unique phrase here' );
# define( 'SECURE_AUTH_SALT', 'put your unique phrase here' );
# define( 'LOGGED_IN_SALT',   'put your unique phrase here' );
# define( 'NONCE_SALT',       'put your unique phrase here' );


# amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
# cd /home/ec2-user
# cp -r wordpress/* /var/www/html/
# service httpd restart