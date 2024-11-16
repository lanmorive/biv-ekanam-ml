import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dishka.integrations.fastapi import setup_dishka

from app.ioc import container
from app.controllers import router


def main():
    app = FastAPI(
        title="Классификация платежей. Хакатон BIV",
        docs_url="/docs",
        openapi_url='/openapi.json'
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)
    setup_dishka(container, app)

    return app


if __name__ == '__main__':
    uvicorn.run(main, host='localhost', port=8000)

# uvicorn main:main --host "localhost" --port 8000