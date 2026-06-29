from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Status, Type, Category, Subcategory, CashFlowRecord
from .serializers import (
    StatusSerializer, TypeSerializer,
    CategorySerializer, SubcategorySerializer,
    CashFlowRecordSerializer,
)


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.select_related("type").all()
    serializer_class = CategorySerializer
    filterset_fields = ["type"]


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.select_related("category").all()
    serializer_class = SubcategorySerializer
    filterset_fields = ["category"]


class CashFlowRecordFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name="date", lookup_expr="gte")
    date_to = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = CashFlowRecord
        fields = ["status", "type", "category", "subcategory", "date_from", "date_to"]


class CashFlowRecordViewSet(viewsets.ModelViewSet):
    queryset = CashFlowRecord.objects.select_related(
        "status", "type", "category", "subcategory"
    ).all()
    serializer_class = CashFlowRecordSerializer
    filterset_class = CashFlowRecordFilter
