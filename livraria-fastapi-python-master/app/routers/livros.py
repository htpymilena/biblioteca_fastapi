from fastapi import APIRouter, HTTPException
from app.schemas.livro import LivroSchema
from app.database.conection import SessionLocal
from app.database.models import LivroModel
from app.schemas.livro import LivroCreate

router = APIRouter(
    prefix="/livros",
    tags=["livros"],
)


@router.get("/livros")
async def listar_livros():
    return {"Livros: ": Livros}
    db = SessionLocal()
    livros = db.query(Livro).all()
    db.close()
    return {"livros": livros}
    
@router.post("/livros")
async def adicionar_livro(livro: LivroSchema):
    Livros.append(livro)
    return {"message": "Livro adicionado com sucesso", "livros": Livros}

@router.put("/livros/{index}")
async def atualizar_livro(index: int, new_livro: LivroSchema):

    if index > len(Livros) or index < 0:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    Livros[index] = new_livro
    return {"message": "Livro autualizado com sucesso!", "livros": Livros}

@router.delete("/livros/{index}")
async def deletar_livro(index: int):
    if index > len(Livros) or index < 0:
            raise HTTPException(status_code=404, detail="Livro não encontrado")
    
    Livros.pop(index)
    return {"message": "Livro Deletado com sucesso!", "livros": Livros}


