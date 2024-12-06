from fastapi import Query, Depends, APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def root(
    name: str = Query(..., description="Имя для отображения в приветствии"), 
    message: str = Query(..., description="Сообщение для отображения")
):
    return f"<h2>Hello {name}! {message}!</h2>"