from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    phone = PhoneNumberField(_("phone"), unique=True, null=True, blank=True)
    password = models.CharField(_("password"), max_length=128, blank=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, null=True, blank=True)
    birth_date = models.DateField(_("birth date"), null=True, blank=True)
    language = models.CharField(max_length=15, choices=settings.LANGUAGES, default='uz')
    telegram_id = models.BigIntegerField(null=True, blank=True, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    total_amount_spent = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)  # New field

    objects = UserManager()
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ('telegram_id',)

    class Meta:
        ordering = ('-id',)
        verbose_name = _("user")
        verbose_name_plural = _("users")
        swappable = "AUTH_USER_MODEL"
        # https://stackoverflow.com/questions/22025476/what-is-swappable-in-model-meta-for

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name


class Profile(models.Model):
    INDIVIDUAL = 'individual'
    LEGAL_ENTITY = 'legal_entity'
    PROFILE_TYPE_CHOICES = [
        (INDIVIDUAL, 'Individual'),
        (LEGAL_ENTITY, 'Legal Entity')
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_type = models.CharField(max_length=20, choices=PROFILE_TYPE_CHOICES)
    additional_field_for_individuals = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    registration_number = models.CharField(max_length=255, null=True, blank=True)

    # add some extra field

    def __str__(self):
        return f'Profile of {self.user.full_name} ({self.profile_type})'
