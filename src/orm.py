from sqlalchemy import MetaData, Table, Column, String, Integer
from sqlalchemy.orm import mapper

from src.model import OrderLine

metadata = MetaData()

order_lines = Table(
    "order_lines",
    metadata,
    Column("orderid", String(255), primary_key=True),
    Column("sku", String(255), primary_key=True),
    Column("qty", Integer),
)


def start_mappers():
    mapper(OrderLine, order_lines)
    pass
