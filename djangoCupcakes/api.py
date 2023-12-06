"""
File for all of our cupcakes routes
"""

from ninja import NinjaAPI, Schema
from cupcakes.models import Cupcake

api = NinjaAPI()


class CupcakeIn(Schema):
    flavor: str
    rating: int
    size: str
    image: str


@api.get("/cupcakes")
def getAllCupcakes(request):
    return


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
