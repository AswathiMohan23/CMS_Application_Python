from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from cms_app.serializer import BlogSerializer


class Blog(viewsets.ViewSet):
    serializer_class = BlogSerializer

    def create(self, request):
        try:
            request.data.update({'user': request.user.id})
            serializer = BlogSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "blog added", "status": 200, "data": {}},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)
