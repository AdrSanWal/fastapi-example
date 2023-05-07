from pydantic import BaseModel

from main import app


@app.get("/users")
async def users():
    return "!Hola Mundo!"
