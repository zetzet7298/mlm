echo "** Creating default DB"

mysql -u $MYSQL_ROOT_USERNAME -p$MYSQL_ROOT_PASSWORD --execute \
"CREATE DATABASE IF NOT EXISTS $MYSQL_DATABASE CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE DATABASE IF NOT EXISTS $MYSQL_DATABASE_TEST CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

echo "** Finished creating default DB"