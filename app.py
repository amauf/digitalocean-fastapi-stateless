from fastapi import FastAPI
from starlette.responses import FileResponse


app = FastAPI()


@app.get("/")
async def read_root():
    return FileResponse('template/index.html')

@app.get("/test")
async def test():
    return "hello world"