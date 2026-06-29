from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Status(models.Model):
    """Статус записи ДДС (Бизнес, Личное, Налог и т.д.)"""
    name = models.CharField("Название", max_length=100, unique=True)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Type(models.Model):
    """Тип операции (Пополнение, Списание и т.д.)"""
    name = models.CharField("Название", max_length=100, unique=True)

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Category(models.Model):
    """Категория, привязанная к типу операции"""
    name = models.CharField("Название", max_length=100)
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        related_name="categories",
        verbose_name="Тип",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]
        unique_together = ["name", "type"]

    def __str__(self):
        return f"{self.name} ({self.type.name})"


class Subcategory(models.Model):
    """Подкатегория, привязанная к категории"""
    name = models.CharField("Название", max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories",
        verbose_name="Категория",
    )

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        ordering = ["name"]
        unique_together = ["name", "category"]

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class CashFlowRecord(models.Model):
    """Запись о движении денежных средств"""
    date = models.DateField("Дата")
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name="records",
        verbose_name="Статус",
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.PROTECT,
        related_name="records",
        verbose_name="Тип",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="records",
        verbose_name="Категория",
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.PROTECT,
        related_name="records",
        verbose_name="Подкатегория",
    )
    amount = models.DecimalField(
        "Сумма",
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    comment = models.TextField("Комментарий", blank=True, default="")
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = "Запись ДДС"
        verbose_name_plural = "Записи ДДС"
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.date} | {self.type} | {self.category} | {self.amount} руб."
