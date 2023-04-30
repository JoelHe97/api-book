from django.db import models

# link gettext - > https://docs.djangoproject.com/en/4.1/topics/i18n/translation/
from django.utils.translation import gettext as _


# _("") -> Utilizado para poder traducir a otros idiomas


class CustomUser(models.Model):
    id = models.CharField(primary_key=True, unique=True, verbose_name=_("User id"))
    location = models.CharField(
        max_length=200, null=True, blank=True, verbose_name=_("Geographic location")
    )

    age = models.CharField(
        max_length=200, null=True, blank=True, verbose_name=_("User biological age")
    )

    def __str__(self):
        """
        Método para devolver un string que represente al objeto
        """
        return self.id

    class Meta:
        """
        Clase Meta:
        Clase de Django para agregar opciones adicionales a nuestro modelo.
        Link: https://docs.djangoproject.com/en/4.1/ref/models/options/
        """

        # Texto que aparecerá en nuestra aplicación.
        verbose_name = "User"

        # Texto que aparecerá en nuestra aplicación en plural.
        verbose_name_plural = "Users"
