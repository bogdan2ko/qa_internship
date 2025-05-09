from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)


# для примеров фикстур
engine = create_engine("sqlite:///test.db", echo=False)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
