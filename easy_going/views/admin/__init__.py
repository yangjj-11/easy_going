from fastapi import APIRouter
from starlette.requests import Request

from easy_going.amis.base import PAGE as amis_base
from easy_going.libs.template import templates
from easy_going.views.admin import sort

router = APIRouter()
router.include_router(sort.router, prefix="/sort")


@router.get("/")
def admin_index(request: Request):
    amis_page = {}
    amis_page.update(amis_base)
    return templates.TemplateResponse(
        "base.html", {"request": request, "amis_page": amis_page}
    )
