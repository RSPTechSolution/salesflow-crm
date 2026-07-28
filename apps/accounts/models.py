from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model for the SalesFlow CRM.

    We inherit from AbstractUser so we keep Django's built-in
    authentication features while allowing us to add custom
    fields in the future.
    """

    pass
