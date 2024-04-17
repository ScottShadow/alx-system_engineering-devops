sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
#add
server-id = 2
log_bin = /var/log/mysql/mysql-bin.log

#SQL for server 2
CHANGE MASTER TO
MASTER_HOST='54.85.131.209',
MASTER_USER='replica_user',
MASTER_PASSWORD='betty',
MASTER_LOG_FILE='mysql-bin.000001',
MASTER_LOG_POS=1616;
START SLAVE;
SHOW SLAVE STATUS\G;
