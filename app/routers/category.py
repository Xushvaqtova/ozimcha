from fastapi import APIRouter
from app.schemas import CategorySchema # Schemadan olamiz

router = APIRouter()
categories = []

@router.post("/")
def create_category(category: CategorySchema): # Schema ishlatildi
    categories.append(category)
    return category

@router.get("/")
def get_categories():
    return categories