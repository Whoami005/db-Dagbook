from django.db import models


class Geolocation(models.Model):
    name = models.CharField(
        max_length=300,
        help_text="Пример: Дагестанские авторы.",
        verbose_name="Категория"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория авторов"
        verbose_name_plural = "Категории авторов"
        ordering = ["name"]


class Lifetime(models.Model):
    name = models.CharField(
        max_length=300,
        help_text="Пример: Авторы времен Кавказской войны",
        verbose_name="Время творчества"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Время творчества"
        verbose_name_plural = "Время творчества"
        ordering = ["name"]


class Genre(models.Model):
    name = models.CharField(verbose_name="Жанр", max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ["name"]
