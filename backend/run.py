import uvicorn

from app import init_app

server = init_app()

if __name__ == "__main__":
    uvicorn.run("run:server", port=8080, host="0.0.0.0")