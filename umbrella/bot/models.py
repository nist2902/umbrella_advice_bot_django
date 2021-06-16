from django.contrib.auth import get_user_model
from django.db import models

class Customer(models.Model):
    chat_id = models.IntegerField(
        verbose_name='Идентификатор чата',
        primary_key=True
    )
    username = models.CharField(
        verbose_name='Юзернейм',
        max_length=32,
        null=True,
        blank=True
    )
    join_date = models.DateTimeField(
        verbose_name='Когда присоеденился',
        auto_now_add=True,
        db_index=True
    )
    city = models.CharField(
        verbose_name='Отслеживаемый город',
        max_length=50
    )
    notification_time = models.TimeField(
        verbose_name='Время оповещений'
    )
    active_user = models.BooleanField(
        verbose_name='Оповещения активированы'
    )

    class Meta:
        ordering = ["-join_date"]

    def __str__(self):
        return self.chat_id
