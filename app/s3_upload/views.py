from django.shortcuts import render

from s3_upload.serializers import FilesSerializer
from rest_framework.response import Response


from rest_framework.generics import CreateAPIView

# Create your views here.


class UploadFielView(CreateAPIView):
    serializer_class = FilesSerializer

    def get_serializer_context(self):
        return {"request": self.request}

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(f"REQUEST {request}")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        gallery = serializer.save()
        serializer = self.get_serializer(gallery)
        return Response({
            "status": True,
            "message": "Upload successfull",
            "data": serializer.data
        })


class TrialView(CreateAPIView):
    serializer_class = FilesSerializer

    def get_serializer_context(self):
        return {"request": self.request}

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # gallery = serializer.save()
        # serializer = self.get_serializer(gallery)
        print(f"MYDATTATA {request.data}")
        return Response({
            "status": True,
            "message": "Upload successfull",
            "data": request.data
        })