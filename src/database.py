from sqlalchemy                 import create_engine
from sqlalchemy.orm             import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@psql-container:5432/ubademy"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()