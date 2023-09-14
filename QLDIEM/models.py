from django.db import models

# Create your models here.
class DMKHOA(models.Model):
    makhoa = models.CharField(max_length=2, primary_key= True)
    tenkhoa = models.CharField(max_length=20)

class DMSV(models.Model):
    masv = models.CharField(max_length = 3, primary_key = True)
    hosv = models.CharField(max_length = 30)
    tensv = models.CharField(max_length = 10)
    phai = models.BooleanField(default = 0)
    ngaysinh = models.DateField()
    noisinh = models.CharField(max_length = 25)
    khoa = models.ForeignKey("DMKHOA", db_column='makhoa' ,on_delete=models.CASCADE)
    hocbong = models.FloatField()

class DMMH(models.Model):
    mamh = models.CharField(max_length=2, primary_key=True)
    tenmh = models.CharField(max_length=30)
    sotiet = models.SmallIntegerField()
    # created_at = models.DateTimeField(auto_now = True)
    # updated_at = models.DateTimeField(auto_now = True)

class KETQUA(models.Model):
    sv = models.ForeignKey('DMSV', db_column='masv', on_delete=models.CASCADE, db_index=True, related_name='ketqua')
    mh = models.ForeignKey('DMMH', db_column='mamh', on_delete=models.CASCADE, db_index=True, related_name='ketqua')
    lanthi = models.SmallIntegerField()
    diem = models.DecimalField(max_digits=4, decimal_places=2)
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['sv', 'mh'], name='unique_masv_mamh_combination'
    #         )
    #     ]