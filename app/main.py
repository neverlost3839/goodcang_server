
from contextlib import asynccontextmanager
import json

import uvicorn
from app.config.settings import settings
from app.api.v1.api import api_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys

sys.stdout.reconfigure(encoding='utf-8')


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Starting {settings.PROJECT_NAME}...")
    # await seed_default_settings()
    yield
    print(f"Shutting down {settings.PROJECT_NAME}...")

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        lifespan=lifespan,
    )

    @app.get("/openapi.json", include_in_schema=False)
    async def custom_openapi():
        from fastapi.responses import Response
        openapi_dict = app.openapi()
        return Response(
            content=json.dumps(openapi_dict, ensure_ascii=False, indent=2),
            media_type="application/json; charset=utf-8"
        )

    app.include_router(api_router, prefix=settings.API_V1_STR)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app

app = create_app()


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)


