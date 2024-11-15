from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base, Libro
from fastapi import Depends
from pydantic import BaseModel

# Configuración de la base de datos
DATABASE_URL = "sqlite:///./libros.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Inicializar FastAPI
app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelos para las peticiones
class LibroCreate(BaseModel):
    titulo: str
    autor: str
    anio_publicacion: int
    isbn: str

class LibroOut(LibroCreate):
    id: int

# Rutas CRUD
@app.post("/libros/", response_model=LibroOut)
def crear_libro(libro: LibroCreate, db: Session = Depends(get_db)):
    nuevo_libro = Libro(**libro.dict())
    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)
    return nuevo_libro

@app.get("/libros/", response_model=list[LibroOut])
def obtener_libros(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Libro).offset(skip).limit(limit).all()

@app.get("/libros/{libro_id}", response_model=LibroOut)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = db.query(Libro).filter(Libro.id == libro_id).first()
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro

@app.put("/libros/{libro_id}", response_model=LibroOut)
def actualizar_libro(libro_id: int, libro: LibroCreate, db: Session = Depends(get_db)):
    libro_db = db.query(Libro).filter(Libro.id == libro_id).first()
    if libro_db is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    for key, value in libro.dict().items():
        setattr(libro_db, key, value)

    db.commit()
    return libro_db

@app.delete("/libros/{libro_id}")
def eliminar_libro(libro_id: int, db: Session = Depends(get_db)):
    libro_db = db.query(Libro).filter(Libro.id == libro_id).first()
    if libro_db is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    db.delete(libro_db)
    db.commit()
    return {"message": "Libro eliminado"}
