from django.db import models

from category.models import Geolocation, Lifetime, Genre


class Authors(models.Model):
    name = models.TextField(verbose_name="ФИО",)
    nickname = models.CharField(blank=True, null=True, max_length=300, verbose_name="Прозвище")
    nationality = models.CharField(blank=True, null=True, max_length=300, verbose_name="Национальность")
    years_of_life = models.CharField(blank=True, null=True, max_length=300, verbose_name="Года жизни")
    biography = models.TextField(verbose_name="Биография")

    def user_directory_path(self, filename):
        return 'authors_photo/{0}/{1}'.format(self.name, filename)

    photo = models.ImageField(
        blank=True,
        null=True,
        verbose_name="Фото",
        upload_to=user_directory_path
    )
    geolocation = models.ForeignKey(
        Geolocation,
        on_delete=models.PROTECT,
        related_name="category",
        verbose_name="Категория",
    )
    lifetime = models.ForeignKey(
        Lifetime,
        on_delete=models.PROTECT,
        related_name="category",
        verbose_name="Время творчества",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ["name"]


class Books(models.Model):
    name = models.TextField(verbose_name="Название")

    def user_directory_path(self, filename):
        return 'books_photo/{0}/{1}'.format(self.name, filename)

    photo = models.ImageField(blank=True, null=True, verbose_name="Фото", upload_to=user_directory_path)
    short_description = models.TextField(verbose_name="Описание")
    book_translator = models.CharField(blank=True, null=True, max_length=255, verbose_name="Переводчик")
    year_of_writing = models.IntegerField(blank=True, null=True, verbose_name="Год написания")
    publisher_name = models.CharField(blank=True, null=True, max_length=255, verbose_name="Издательство")
    city_of_publication = models.CharField(
        blank=True,
        null=True,
        max_length=300,
        verbose_name="Город издания"
    )
    year_of_publishing = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Год издания"
    )
    authors = models.ManyToManyField(
        Authors,
        related_name="books",
        verbose_name="Авторы",
    )

    def user_directory_path_book(self, filename):
        return 'books_file/{0}/{1}'.format(self.name, filename)

    file_book = models.FileField(verbose_name="Книга", upload_to=user_directory_path_book)
    genre = models.ForeignKey(
        Genre,
        verbose_name="Жанр",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["name"]
