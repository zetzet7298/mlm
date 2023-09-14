from django.db import models
# Create your models here.

class ClientType(models.Model):
    class Meta:
        db_table = 'client_type'
    name = models.CharField(max_length=128)
    desc = models.TextField(null = True)
    is_disable = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)