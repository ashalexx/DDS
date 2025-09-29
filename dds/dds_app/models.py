from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator


class Status(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название статуса")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.name


class TransactionType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Тип операции")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Тип операции"
        verbose_name_plural = "Типы операций"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название категории")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название подкатегории")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        unique_together = ['name', 'category']  # Уникальность

    def __str__(self):
        return f"{self.category.name} - {self.name}"


# Основная модель
class FinancialRecord(models.Model):
    created_date = models.DateField(
        verbose_name="Дата создания записи",
        default=timezone.now,
        help_text="Формат: ДД.ММ.ГГГГ"
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name="Статус"
    )
    transaction_type = models.ForeignKey(
        TransactionType,
        on_delete=models.PROTECT,
        verbose_name="Тип операции"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Категория"
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.PROTECT,
        verbose_name="Подкатегория"
    )
    amount = models.DecimalField(
        max_digits=12,  # знаки до запятой
        decimal_places=2,  # знаки после запятой
        verbose_name="Сумма (рубли)",
        validators=[MinValueValidator(0.01)]  # меньше 1 копейки нельзя
    )
    comment = models.TextField(
        verbose_name="Комментарий",
        blank=True,
        null=True,
        help_text="Необязательное поле"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Финансовая запись"
        verbose_name_plural = "Финансовые записи"
        ordering = ['-created_date', '-created_at']
        # 1. Сначала сортирует по created_date (новые даты вперед)
        # 2. Если даты одинаковые, сортирует по created_at (новые записи вперед)

    def __str__(self):
        return f"{self.created_date} - {self.transaction_type} - {self.amount} руб."

    def save(self, *args, **kwargs):
        if self.subcategory.category != self.category:
            raise ValueError("Подкатегория должна принадлежать выбранной категории")
        super().save(*args, **kwargs)
