"""
File for all of our cupcakes routes
"""

from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/cupcakes")
def getAllCupcakes(request):
    return


@api.get("/cupcakes/{id}")
def getCupcake(request, id: int):
    return


@api.post("/cupcakes/{id}")
def createCupcake(request, id: int):
    return


@api.patch("/cupcakes/{id}")
def updateCupcake(request, id: int):
    return


@api.delete("/cupcakes/{id}")
def deleteCupcake(request, id: int):
    return
