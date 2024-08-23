# from Models
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# from files
from api_routes import home, product


app = FastAPI()


# Connect to frontend

origins = [
    "http://localhost:5173",
    "localhost:5173"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


app.include_router(home.router)
app.include_router(product.router)


if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)