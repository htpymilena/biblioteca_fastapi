from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "sqlite:///./livraria.db"  
DATABASE_URL = "sqlite:////data/banco.db"  # Usando 4 barras (caminho absoluto)


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Necessário para SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()