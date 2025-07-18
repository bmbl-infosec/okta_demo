from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve static files from the 'static' folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Root route returns the index.html file
@app.get("/")
def read_root():
    return FileResponse("static/index.html")
