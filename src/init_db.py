from sqlalchemy import create_engine, MetaData, Table, Integer, BigInteger, Column
from config import DB_USER, DB_NAME, DB_PASS

engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}')
engine.connect()

metadata = MetaData()

invites = Table('invites', metadata, 
  Column('id', BigInteger(), primary_key=True),
  Column('member_id', BigInteger(), nullable=False),
  Column('amount_msg', Integer(),  nullable=False),
  Column('available_amount_msg', Integer(), nullable=False),
  Column('chat_id', BigInteger(), nullable=False),
  Column('is_warned', Integer(), nullable=False)
)

metadata.create_all(engine)