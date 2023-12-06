"""
File for all of our cupcakes routes
"""

from ninja import NinjaAPI, Schema
from typing import List

from cupcakes.models import Cupcake

api = NinjaAPI()


class CupcakePostIn(Schema):
    flavor: str
    rating: int
    size: str
    image: str

    class Config:
        extra = "forbid"


class CupcakePatchIn(Schema):
    flavor: str = None
    rating: int = None
    size: str = None
    image: str = None

    class Config:
        extra = "forbid"


class CupcakeOut(Schema):
    flavor: str
    size: str
    image: str


@api.get("/cupcakes", response=List[CupcakeOut])
def getAllCupcakes(request):
    cupcakes = Cupcake.objects.all()
    return cupcakes


@api.get("/cupcakes/{id}", response=CupcakeOut)
def getCupcake(request, id: int):
    cupcake = Cupcake.objects.get(id=id)
    return cupcake


@api.post("/cupcakes")
def createCupcake(request, payload: CupcakePostIn):
    cupcake = Cupcake.objects.create(**payload.dict())
    return {"id": cupcake.id}


@api.patch("/cupcakes/{id}", response=CupcakeOut)
def updateCupcake(request, id: int, payload: CupcakePatchIn):
    cupcake = Cupcake.objects.get(id=id)

    # exclude_unset prevents assignment of attributes that were not passed
    # in the payload
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(cupcake, attr, value)

    cupcake.save()

    return cupcake


@api.delete("/cupcakes/{id}")
def deleteCupcake(request, id: int):
    return
