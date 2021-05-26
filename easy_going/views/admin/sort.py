from fastapi import APIRouter
from starlette.requests import Request

from easy_going.amis.base import PAGE as amis_base
from easy_going.libs.template import templates

router = APIRouter()

@router.get("/manage")
def ad_gdt(request: Request):
    from easy_going.amis.sort.manage import PAGE

    amis_page = {}
    amis_page.update(amis_base)
    amis_page.update(PAGE)
    return templates.TemplateResponse(
        "base.html", {"request": request, "amis_page": amis_page}
    )