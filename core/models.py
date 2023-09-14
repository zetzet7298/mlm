from django.db import models

# Create your models here.
class Menu(models.Model):
    class Meta:
        db_table = 'menu'
    name = models.CharField(max_length = 128)
    url = models.CharField(max_length=128, unique=True)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True)

class MultiLevel(models.Model):
    class Meta:
        db_table = 'multi_level'
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255, default=None)
    password1 = models.CharField(max_length = 255, default=None)
    password2 = models.CharField(max_length = 255, default=None)
    # direct_user_id = models.BigIntegerField()
    # indirect_user_id = models.BigIntegerField()
    direct_user = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, related_name='user')
    indirect_user = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, related_name='user2')
     