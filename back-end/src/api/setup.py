from fastapi import FastAPI
from src.api.middleware.spa_static_files import SpaStaticFiles
from os import path

routers = []


def create_fast_api_app() -> FastAPI:
    app = FastAPI()

    dist_path = path.abspath('../front-end/dist')
    app.mount("/app", SpaStaticFiles(directory=dist_path,
              html=True), name="Hacker News Crawler App")

    [app.include_router(r) for r in routers]

    return app
