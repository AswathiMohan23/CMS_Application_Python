from rest_framework import viewsets, status
from rest_framework.response import Response

from cms_app.models import BlogModel
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

    def list(self, request):
        try:
            blog_data = BlogModel.objects.filter(user=request.user.id)
            serializer = BlogSerializer(blog_data, many=True)
            return Response({"message": "blog retrieved", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, blog_id):
        try:

            request.data.update({'user': request.user.id})
            blog_data = BlogModel.objects.get(id=blog_id, user=request.user)
            serializer = BlogSerializer(blog_data, request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "blog edited", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_200_OK)

    def destroy(self, request, blog_id):
        try:
            blog_data = BlogModel.objects.get(id=blog_id)
            blog_data.delete()
            return Response({"message": "blog deleted", "status": 200, "data": {}},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)


