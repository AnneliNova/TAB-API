from django.shortcuts import render
from rest_framework.views import APIView
from .models import Chair, Table
from .serializer import ChairSerializer
from rest_framework.response import Response


class ChairView(APIView):
    def get(self, request):
        output = [
            {
                "id": obj.id,
                "name": obj.name,
                "price": obj.price,
                "quantity": obj.quantity
            } for obj in Chair.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = ChairSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
