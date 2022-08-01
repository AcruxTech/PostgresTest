from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from config import DB_USER, DB_NAME, DB_PASS
from init_db import Invite

engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}')
engine.connect()

session = Session(bind=engine)

invite = Invite(
  member_id = 123,
  amount_msg = 1,
  available_amount_msg = 1.5,
  chat_id = 321,
  is_warned = 1
)
session.add(invite)
session.commit()

session = Session(bind=engine) 
invite = session.query(Invite).filter(Invite.member_id == 123).first()
print(invite.id)