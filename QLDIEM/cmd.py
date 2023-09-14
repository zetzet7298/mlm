from .models import DMKHOA
dmkhoa = DMKHOA.objects.all().values
print(dmkhoa)