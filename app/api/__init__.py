from fastapi import APIRouter
from .ask import router as QueryRouter
from .upload_pdf import router as PdfRouter

routers = APIRouter()

router_list = [QueryRouter,PdfRouter]

for router in router_list:
    routers.include_router(router)
