from .serializers import *
from rest_framework.viewsets import ModelViewSet


class JobCRUD(ModelViewSet):

    queryset = Jobs.objects.all()
    serializer_class = JobSerializer

