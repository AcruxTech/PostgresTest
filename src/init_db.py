from sqlalchemy import create_engine, Integer, BigInteger, Column
from sqlalchemy.ext.declarative import declarative_base
from config import DB_USER, DB_NAME, DB_PASS

engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}')
engine.connect()

Base = declarative_base()

class Invite(Base):
  __tablename__ = 'Invites'
  id = Column('id', BigInteger(), primary_key=True)
  member_id = Column('member_id', BigInteger(), nullable=False)
  amount_msg = Column('amount_msg', Integer(),  nullable=False)
  available_amount_msg = Column('available_amount_msg', Integer(), nullable=False)
  chat_id = Column('chat_id', BigInteger(), nullable=False)
  is_warned = Column('is_warned', Integer(), nullable=False)

Base.metadata.create_all(engine)