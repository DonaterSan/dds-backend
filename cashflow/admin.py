from django.contrib import admin
from .models import Status, Type, Category, Subcategory, CashFlowRecord


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "type"]
    list_filter = ["type"]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    list_filter = ["category__type", "category"]


@admin.register(CashFlowRecord)
class CashFlowRecordAdmin(admin.ModelAdmin):
    list_display = ["date", "status", "type", "category", "subcategory", "amount"]
    list_filter = ["status", "type", "category"]
