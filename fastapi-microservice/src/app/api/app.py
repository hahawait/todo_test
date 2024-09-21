import logging

import sentry_sdk
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from app.api.docs import secure_docs
from config import get_config

from app.api.comments.handlers import router as comments_router
from logic.providers.base import BaseProvider
from logic.providers.comments import CommentsProvider


def create_app() -> FastAPI:
    config = get_config()
    logging.basicConfig(level=config.app.LOG_LEVEL)

    if config.app.is_dev or config.app.is_production:
        sentry_sdk.init(
            dsn=config.app.SENTRY_DSN,
            environment=config.app.MODE,
            traces_sample_rate=1.0,
        )

    fastapi_params = dict(
        title=config.app.TITLE,
        description=config.app.DESCRIPTION,
        version=config.app.VERSION,
    )

    if config.app.is_production:
        app = FastAPI(
            **fastapi_params,
            docs_url=None,
            redoc_url=None,
            openapi_url=None,
            debug=True,
        )
        secure_docs(
            app=app,
            admin_username=config.app.ADMIN_USERNAME,
            admin_password=config.app.ADMIN_PASSWORD,
            **fastapi_params
        )
    else:
        app = FastAPI(**fastapi_params, debug=True)

    container = make_async_container(BaseProvider(), CommentsProvider())
    setup_dishka(container, app)

    app.include_router(comments_router)
    return app
