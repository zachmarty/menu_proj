from django.db import models
from autoslug import AutoSlugField

class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", unique=True)
    parent = models.ForeignKey(
        "self",
        to_field = 'id',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Родительская вкладка",
    )
    slug = AutoSlugField(populate_from = 'name', editable = True, blank = False, always_update = True)

    def __str__(self) -> str:
        return f"{self.id} {self.name}"

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"
        ordering = ("name",)
