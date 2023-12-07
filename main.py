from fastapi import FastAPI
from routes.routes import book
from seedDataBase import seed_db
app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello World"}

app.include_router(book)

@app.get("/seed-database")
def seed_database():
    seed_db()
    return {"message": "Database seeded successfully!"}


