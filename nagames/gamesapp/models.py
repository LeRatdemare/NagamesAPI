from django.db import models

# Create your models here.
class GameSession(models.Model):
    title = models.fields.CharField(max_length=100)
    admin = models.fields.CharField(max_length=100)
    password = models.fields.CharField(max_length=255)
    active = models.fields.BooleanField(default=True)
    creation_date = models.fields.DateTimeField(auto_now_add=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return f'Session de {self.admin}'