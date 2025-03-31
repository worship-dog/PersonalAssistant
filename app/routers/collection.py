from fastapi import APIRouter, Depends

from app.utils import get_db


router = APIRouter(
    tags=["collection"],
    dependencies=[Depends(get_db)]
)


@router.post("/collection")
def create_collection():
    pass


@router.get("/collection")
def get_collection():
    pass


@router.put("/collection")
def edit_collection():
    pass


@router.delete("/collection")
def del_collection():
    pass


@router.get("/collection/list")
def get_collection_list():
    pass
