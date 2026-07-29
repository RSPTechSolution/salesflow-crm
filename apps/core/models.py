from django.db import models


class BaseModel(models.Model):
    """
    Base Model that provides all common timestamp fields
    for all models in the project
    """

    created_at = models.DateTimeField(
        auto_now_add=True, help_text="The date and time when this record was created"
    )

    updated_at = models.DateTimeField(
        auto_now=True, help_text="The date and time when this record was updated"
    )

    class Meta:
        abstract = True
