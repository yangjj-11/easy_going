"""The FastAPI App.
"""

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.requests import Request
from starlette.staticfiles import StaticFiles

from easy_going.utils.config import static_dir
from easy_going.views.admin import router as admin_router


app = FastAPI(
    title= "yjj",
    version="0.0.0",
    description="后台管理面板",
    openapi_url="/api/v1/openapi.json",
)
app.mount("/static", StaticFiles(directory=static_dir), name="static")
app.include_router(admin_router, prefix="/admin")


@app.get("/", responses={200: {"content": {"text/html": {}}}})
def index(request: Request):
    return RedirectResponse(url="/admin")
