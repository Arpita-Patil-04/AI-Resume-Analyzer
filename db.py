from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker 

DATABASE_URL = "mysql+pymysql://2CrZ7EGq6Nd9YHW.root:jZdygu8DIUf9i0zA@gateway01.ap-southeast-1.prod.alicloud.tidbcloud.com:4000/test?"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
) 

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()