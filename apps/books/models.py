from django.db import models
from apps.users.models import CustomUser

# link gettext - > https://docs.djangoproject.com/en/4.1/topics/i18n/translation/
from django.utils.translation import gettext as _


# _("") -> Utilizado para poder traducir a otros idiomas


class Book(models.Model):
    id = models.CharField(primary_key=True, unique=True, verbose_name=_("Book id"))
    title = models.CharField(
        max_length=300, null=False, blank=False, verbose_name=_("Title of the book")
    )

    author = models.CharField(
        max_length=200, null=True, blank=True, verbose_name=_("Author of the book")
    )
    year_publication = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Year of publication"),
    )
    publisher = models.TextField(null=True, blank=True, verbose_name=_("Publisher name")
    )
    image_1 = models.URLField( null=True, blank=True, verbose_name=_("Book image 1"))
    image_2 = models.URLField( null=True, blank=True, verbose_name=_("Book image 2"))
    image_3 = models.URLField( null=True, blank=True, verbose_name=_("Book image 3"))

    def __str__(self):
        """
        Método para devolver un string que represente al objeto
        """
        return self.title

    class Meta:
        """
        Clase Meta:
        Clase de Django para agregar opciones adicionales a nuestro modelo.
        Link: https://docs.djangoproject.com/en/4.1/ref/models/options/
        """

        # Texto que aparecerá en nuestra aplicación.
        verbose_name = "Book"

        # Texto que aparecerá en nuestra aplicación en plural.
        verbose_name_plural = "Books"


class Rating(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name=_("User")
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name=_("Book"))
    rating = models.PositiveSmallIntegerField(
        null=False, blank=False, verbose_name=_("Rating")
    )

    class Meta:
        """
        Clase Meta:
        Clase de Django para agregar opciones adicionales a nuestro modelo.
        Link: https://docs.djangoproject.com/en/4.1/ref/models/options/
        """

        # Texto que aparecerá en nuestra aplicación.
        verbose_name = "Rating"

        # Texto que aparecerá en nuestra aplicación en plural.
        verbose_name_plural = "Ratings"
