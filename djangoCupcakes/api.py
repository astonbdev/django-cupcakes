"""
File for all of our cupcakes routes
"""

from ninja import NinjaAPI, Schema
from typing import List

from cupcakes.models import Cupcake

api = NinjaAPI()


class CupcakeIn(Schema):
    flavor: str
    rating: int
    size: str
    image: str


class CupcakeOut(Schema):
    flavor: str
    size: str
    image: str


@api.get("/cupcakes", response=List[CupcakeOut])
def getAllCupcakes(request):
    cupcakes = Cupcake.objects.all()
    return cupcakes


@api.get("/cupcakes/{id}")
def getCupcake(request, id: int):
    return


@api.post("/cupcakes")
def createCupcake(request, payload: CupcakeIn):
    cupcake = Cupcake.objects.create(**payload.dict())
    return {"id": cupcake.id}


@api.patch("/cupcakes/{id}")
def updateCupcake(request, id: int):
    return


@api.delete("/cupcakes/{id}")
def deleteCupcake(request, id: int):
    return
