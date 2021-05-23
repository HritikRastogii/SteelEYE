from sqlalchemy.orm import sessionmaker
from database import engine
from sqlalchemy import or_

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()
from models import Trade, TradeDetails

our_user = session.query(Trade).filter_by(tradeId='oorrt').first()
search = "owais"
LIMIT = 10
OFFSET = 3
print(session.query(Trade).offset(OFFSET).limit(LIMIT).all())
# objs = session.query(Trade).filter(
#     (Trade.counterparty == search) | (Trade.instrumentId == search) | (Trade.instrumentName == search) |
#     (Trade.trader == search)).slice(OFFSET, LIMIT)
# objs= objs.all()
# for i in objs:
#     print(i.id)

objs = session.query(Trade).join(TradeDetails).filter(TradeDetails.price >= 3).all()