from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Car
from .serializers import CarSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

class CarList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer