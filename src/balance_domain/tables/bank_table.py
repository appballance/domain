from sqlalchemy.engine import Connectable


def bank_table(connection: Connectable):
    connection.execute(
        "CREATE TABLE IF NOT EXISTS `TB_BANK` (\
        `id` INT AUTO_INCREMENT NOT NULL, \
        `token` VARCHAR(255) NOT NULL, \
        `user_id` INT NOT NULL, \
        PRIMARY KEY(`id`), \
        FOREIGN KEY(`user_id`) REFERENCES `TB_USER`(`id`) ON DELETE CASCADE )"
    )
