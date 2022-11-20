from sqlalchemy.engine import Connectable

from balance_domain.tables.user_table import user_table
from balance_domain.tables.bank_table import bank_table


def create_tables(connection: Connectable):
    user_table(connection)
    bank_table(connection)
