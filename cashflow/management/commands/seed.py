from django.core.management.base import BaseCommand
from cashflow.models import Status, Type, Category, Subcategory, CashFlowRecord
from decimal import Decimal
from datetime import date


class Command(BaseCommand):
    help = "Заполняет базу начальными данными"

    def handle(self, *args, **options):
        # Статусы
        s_biz, _ = Status.objects.get_or_create(name="Бизнес")
        s_per, _ = Status.objects.get_or_create(name="Личное")
        s_tax, _ = Status.objects.get_or_create(name="Налог")

        # Типы
        t_in, _ = Type.objects.get_or_create(name="Пополнение")
        t_out, _ = Type.objects.get_or_create(name="Списание")

        # Категории (привязаны к типам)
        c_infra, _ = Category.objects.get_or_create(name="Инфраструктура", type=t_out)
        c_market, _ = Category.objects.get_or_create(name="Маркетинг", type=t_out)
        c_salary, _ = Category.objects.get_or_create(name="Зарплата", type=t_out)
        c_sales, _ = Category.objects.get_or_create(name="Продажи", type=t_in)
        c_invest, _ = Category.objects.get_or_create(name="Инвестиции", type=t_in)

        # Подкатегории
        Subcategory.objects.get_or_create(name="VPS", category=c_infra)
        Subcategory.objects.get_or_create(name="Proxy", category=c_infra)
        Subcategory.objects.get_or_create(name="Домены", category=c_infra)
        Subcategory.objects.get_or_create(name="Farpost", category=c_market)
        Subcategory.objects.get_or_create(name="Avito", category=c_market)
        Subcategory.objects.get_or_create(name="Разработчики", category=c_salary)
        Subcategory.objects.get_or_create(name="Менеджеры", category=c_salary)
        sub_b2b, _ = Subcategory.objects.get_or_create(name="B2B", category=c_sales)
        sub_b2c, _ = Subcategory.objects.get_or_create(name="B2C", category=c_sales)
        Subcategory.objects.get_or_create(name="Ангельские", category=c_invest)
        sub_grant, _ = Subcategory.objects.get_or_create(name="Гранты", category=c_invest)

        # Несколько тестовых записей
        if not CashFlowRecord.objects.exists():
            CashFlowRecord.objects.create(
                date=date(2025, 1, 15), status=s_biz, type=t_in,
                category=c_sales, subcategory=sub_b2b,
                amount=Decimal("150000.00"), comment="Оплата от клиента ООО Ромашка",
            )
            CashFlowRecord.objects.create(
                date=date(2025, 1, 20), status=s_biz, type=t_out,
                category=c_infra, subcategory=Subcategory.objects.get(name="VPS"),
                amount=Decimal("5000.00"), comment="Аренда сервера за январь",
            )
            CashFlowRecord.objects.create(
                date=date(2025, 2, 1), status=s_per, type=t_in,
                category=c_invest, subcategory=sub_grant,
                amount=Decimal("300000.00"),
            )
            CashFlowRecord.objects.create(
                date=date(2025, 2, 10), status=s_tax, type=t_out,
                category=c_salary, subcategory=Subcategory.objects.get(name="Разработчики"),
                amount=Decimal("80000.00"), comment="НДФЛ за январь",
            )
            CashFlowRecord.objects.create(
                date=date(2025, 3, 5), status=s_biz, type=t_out,
                category=c_market, subcategory=Subcategory.objects.get(name="Avito"),
                amount=Decimal("12000.00"), comment="Размещение объявлений",
            )

        self.stdout.write(self.style.SUCCESS("Данные успешно загружены!"))
