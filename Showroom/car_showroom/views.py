from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from core.views import CustomViewSet
from .models import (
    Car,
    CarShowroom,
    ShowroomSellCar,
    Customer,
    Transaction,
    Supplier,
    SupplierSellCar
)
from .serializers import (
    CarSerializer,
    CarShowroomSerializer,
    ShowroomSellCarSerializer,
    CustomerSerializer,
    TransactionSerializer,
    SupplierSerializer,
    SupplierSellCarSerializer
)


# Create your views here.
class CarViewSet(CustomViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    @action(detail=False, methods=['get'],)
    def get(self, request):
        return super(CarViewSet, self).get(request)

    @action(detail=False, methods=['post'])
    def post(self, request):
        return super(CarViewSet, self).post(request)

    @action(detail=True, methods=['put'])
    def put(self, request, pk=None):
        return super(CarViewSet, self).put(request, pk)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk):
        return super(CarViewSet, self).delete(request, pk)


class CarShowroomViewSet(CustomViewSet):
    queryset = CarShowroom.objects.all()
    serializer_class = CarShowroomSerializer

    @action(detail=False, methods=['get'])
    def get(self, request):
        return super(CarShowroomViewSet, self).get(request)

    @action(detail=False, methods=['post'])
    def post(self, request):
        return super(CarShowroomViewSet, self).post(request)

    @action(detail=True, methods=['put'])
    def put(self, request, pk=None):
        return super(CarShowroomViewSet, self).put(request, pk)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk):
        return super(CarShowroomViewSet, self).delete(request, pk)


class ShowroomSellCarViewSet(CustomViewSet):
    queryset = ShowroomSellCar.objects.all()
    serializer_class = ShowroomSellCarSerializer

    @action(detail=False, methods=['get'])
    def get(self, request):
        return super(ShowroomSellCarViewSet, self).get(request)

    @action(detail=False, methods=['post'])
    def post(self, request):
        return super(ShowroomSellCarViewSet, self).post(request)

    @action(detail=True, methods=['put'])
    def put(self, request, pk=None):
        return super(ShowroomSellCarViewSet, self).put(request, pk)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk):
        return super(ShowroomSellCarViewSet, self).delete(request, pk)


class CustomerViewSet(CustomViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=False, methods=['get'])
    def get(self, request):
        return super(CustomerViewSet, self).get(request)

    @action(detail=False, methods=['post'])
    def post(self, request):
        return super(CustomerViewSet, self).post(request)

    @action(detail=True, methods=['put'])
    def put(self, request, pk=None):
        return super(CustomerViewSet, self).put(request, pk)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk):
        return super(CustomerViewSet, self).delete(request, pk)


class TransactionViewSet(CustomViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=False, methods=['get'])
    def get(self, request):
        return super(TransactionViewSet, self).get(request)

    @action(detail=False, methods=['post'])
    def post(self, request):
        return super(TransactionViewSet, self).post(request)

    @action(detail=True, methods=['put'])
    def put(self, request, pk=None):
        return super(TransactionViewSet, self).put(request, pk)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk):
        return super(TransactionViewSet, self).delete(request, pk)


class SupplierSellCarViewSet(CustomViewSet):
    queryset = SupplierSellCar.objects.all()
    serializer_class = SupplierSellCarSerializer

    @action(detail=False, methods=['get'])
    def get(self, request):
        return super(SupplierSellCarViewSet, self).get(request)

    @action(detail=False, methods=['post'])
    def post(self, request):
        return super(SupplierSellCarViewSet, self).post(request)

    @action(detail=True, methods=['put'])
    def put(self, request, pk=None):
        return super(SupplierSellCarViewSet, self).put(request, pk)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk):
        return super(SupplierSellCarViewSet, self).delete(request, pk)


class SupplierViewSet(CustomViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    @action(detail=False, methods=['get'])
    def get(self, request):
        return super(SupplierViewSet, self).get(request)

    @action(detail=False, methods=['post'])
    def post(self, request):
        return super(SupplierViewSet, self).post(request)

    @action(detail=True, methods=['put'])
    def put(self, request, pk=None):
        return super(SupplierViewSet, self).put(request, pk)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk):
        return super(SupplierViewSet, self).delete(request, pk)
