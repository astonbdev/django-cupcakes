"""
File for all of our cupcakes routes
"""

from typing import List

from ninja import NinjaAPI, ModelSchema, Schema
from ninja.security import APIKeyHeader

from django.shortcuts import get_object_or_404

from cupcakes.models import Cupcake


api = NinjaAPI()


class ApiKey(APIKeyHeader):
    param_name = "Authorization"

    def authenticate(self, request, key):
        if key == "cupcake":
            return key


header_key = ApiKey()


class CupcakePostSchema(ModelSchema):
    class Meta:
        model = Cupcake
        fields = ['flavor', 'rating', 'size', 'image']

    class Config:
        extra = "forbid"


# Or declare explicitly:
class CupcakePatchIn(Schema):
    flavor: str = None
    rating: int = None
    size: str = None
    image: str = None

    class Config:
        extra = "forbid"


class CupcakeOut(Schema):
    id: int
    flavor: str
    size: str
    image: str


class CupcakePostOut(Schema):
    id: int

# Include summary to provide custom info on dropdown header in docs:


@api.get("/cupcakes", response=List[CupcakeOut], summary="PLACEHOLDER")
def getAllCupcakes(request):
    cupcakes = Cupcake.objects.all()
    return cupcakes


@api.get("/cupcakes/{id}", response=CupcakeOut, auth=header_key)
def getCupcake(request, id: int):
    cupcake = Cupcake.objects.get(id=id)
    return cupcake


@api.post("/cupcakes", response=CupcakePostOut)
def createCupcake(request, payload: CupcakePostSchema):
    cupcake = Cupcake.objects.create(**payload.dict())
    return cupcake


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
    cupcake = get_object_or_404(Cupcake, id=id)
    cupcake.delete()

    return {"deleted": True}
