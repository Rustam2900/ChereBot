from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_("Yartilgan vaqti."), auto_now_add=True)
    updated_at = models.DateTimeField(_("O'zgartirilgan vaqti."), auto_now=True)

    class Meta:
        abstract = True

