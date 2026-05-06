from app.config import settings
from fastapi import FastAPI
from app.routers import category, posts  # Ikkala routerni ham chaqiramiz

app = FastAPI()

app.include_router(category.router, prefix="/categories", tags=["Categories"])
app.include_router(posts.router) # Posts routerini ham ulash

# Printlar faqat tekshirish uchun, keyinchalik o'chirib tashlang
print(settings.database_url)
print(settings.secret_key)