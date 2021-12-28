from sqlalchemy import MetaData, Table, Column, String, Integer, Date
from sqlalchemy.orm import mapper

from src.model import OrderLine, Batch

metadata = MetaData()

order_lines = Table(
    "order_lines",
    metadata,
    Column("orderid", String(255), primary_key=True),
    Column("sku", String(255), primary_key=True),
    Column("qty", Integer),
)

batches = Table(
    "batches",
    metadata,
    Column("reference", String(255), primary_key=True),
    Column("sku", String(255), primary_key=True),
    Column("_purchased_qty", Integer),
    Column("eta", Date),
)


def start_mappers():
    mapper(OrderLine, order_lines)
    mapper(Batch, batches)
