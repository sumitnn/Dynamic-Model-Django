
from django.db import models

class DynamicModelDetails(models.Model):
    model_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    fields = models.JSONField()
    value=models.JSONField(null=True,blank=True)

    def __str__(self):
        return self.model_name
