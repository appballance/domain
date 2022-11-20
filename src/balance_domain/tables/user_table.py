from sqlalchemy.engine import Connectable


def user_table(connection: Connectable):
    connection.execute(
        "CREATE TABLE IF NOT EXISTS `TB_USER` (\
        `id` INT AUTO_INCREMENT NOT NULL, \
        `surname` VARCHAR(255) NOT NULL, \
        `fullname` VARCHAR(255) NOT NULL, \
        `email` VARCHAR(255) NOT NULL, \
        `password` VARCHAR(255) NOT NULL, \
         PRIMARY KEY(`id`))"
    )
