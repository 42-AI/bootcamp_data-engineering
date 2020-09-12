#! /bin/bash
yum install -y mysql
export MYSQL_HOST=${rds_address}

mysql -u ${rds_user} -p${rds_password} -D ${rds_db} -e "CREATE USER IF NOT EXISTS 'wordpress' IDENTIFIED BY 'wordpress-pass';"
mysql -u ${rds_user} -p${rds_password} -D ${rds_db} -e "GRANT ALL PRIVILEGES ON wordpress.* TO wordpress;"
mysql -u ${rds_user} -p${rds_password} -D ${rds_db} -e "FLUSH PRIVILEGES;"

yum install -y httpd
service httpd start