from django.core.management.base import BaseCommand, CommandError
from QLDIEM.models import *

class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        #1.1. Liệt kê danh sách các môn học gồm các thông tin: Mã môn, Tên môn, Số tiết 
        result = DMMH.objects.all().values()
        #1.2 Liệt kê danh sách các môn học có tên bắt đầu bằng chữ “T”, gồm các thông tin: Mã môn, Tên môn, Số tiết Câu lệnh: 
        result = DMMH.objects.filter(tenmh__startswith='T').values()
        #1.3. Liệt kê danh sách những sinh viên có chữ cái cuối cùng trong tên là I, gồm các thông tin: Họ tên sinh viên, Ngày sinh, Phái.
        result = DMSV.objects.filter(tensv__endswith='i').values('hosv', 'tensv', 'ngaysinh', 'phai')
        # 1.4.   Danh sách những khoa có ký tự thứ hai của tên khoa có chứa chữ N, gồm các thông tin: Mã khoa, Tên khoa. 
        result = DMKHOA.objects.filter(tenkhoa__regex=r'^.n{1}').values('makhoa','tenkhoa')
# 1.5.   Liệt kê những sinh viên mà họ có chứa chữ Thị. 
        result = DMSV.objects.filter(hosv__icontains='thị').values()
# 1.6.   Cho biết danh sách những sinh viên có ký tự đầu tiên của tên nằm trong khoảng từ a đến m, gồm các thông tin: Mã sinh viên, Họ tên sinh viên, Phái, Học bổng. 
        result = DMSV.objects.extra(where=["tensv rlike '^[a-m]'"]).values('masv', 'hosv', 'phai', 'hocbong')
# 1.7.   Liệt kê các sinh viên có học bổng từ 150000 trở lên và sinh ở Hà Nội, gồm các thông tin: Họ tên sinh viên, Mã khoa, Nơi sinh, Học bổng.
        from django.db.models import Q
        result = DMSV.objects.filter(Q(hocbong__gte=80000) & Q(noisinh='Hà nội')).values('hosv', 'tensv', 'khoa_id', 'noisinh', 'hocbong')
# 1.8.   Danh sách các sinh viên của khoa AV văn và khoa VL, gồm các thông tin: Mã sinh viên, Mã khoa, Phái. 
        from django.db.models import Q
        result = DMSV.objects.filter(Q(khoa_id='AV') | Q(khoa_id='VL')).values('masv', 'khoa_id', 'phai')
# 1.9.   Cho  biết  những  sinh  viên  có  ngày  sinh  từ ngày  01/01/1992  đến   ngày  05/06/1993 gồm các thông tin: Mã sinh viên, Ngày sinh, Nơi sinh, Học bổng.
        result = DMSV.objects.filter(ngaysinh__range=('1992-01-01', '1993-06-05')).values()
# 1.10.   Danh sách những sinh viên có học bổng từ  80.000 đến 150.000, gồm các thông tin: Mã sinh viên, Ngày sinh, Phái, Mã khoa. 
        result = DMSV.objects.filter(hocbong__range=(80000, 150000)).values()
# 1.11.   Cho biết những môn học có số tiết lớn hơn 30 và nhỏ hơn 50, gồm các thông tin: Mã môn học, Tên môn học, Số tiết. 
        result = DMMH.objects.filter(sotiet__range=(31,49)).values()
# 1.12.   Liệt kê những sinh viên nam của khoa Anh văn  và khoa tin học, gồm các thông tin: Mã sinh viên, Họ tên sinh viên, tên khoa, Phái.  
        from django.db.models import Q
        result = DMSV.objects.filter(Q(phai=False) & (Q(khoa_id='AV') | Q(khoa_id='TH'))).values()
# 1.13.   Liệt kê những sinh viên có điểm thi môn sơ sở dữ liệu nhỏ hơn 5, gồm thông tin: Mã sinh viên, Họ tên, phái, điểm 
        result = DMSV.objects.filter(Q(ketqua__diem__lt=5) & Q(ketqua__mh__tenmh='Cơ sở dữ liệu')).values().query
# 1.14.   Liệt kê những sinh viên học khoa Anh văn mà không có học bổng, gồm thông tin: 
# Mã sinh viên, Họ và tên, tên khoa, Nơi sinh, Học bổng 
        from django.db.models import Q
        result = DMSV.objects.filter(Q(khoa_id='AV') & Q(hocbong=0)).values()
        # 2.1. Cho biết danh sách những sinh viên gồm các thông tin: Họ tên sinh viên, Ngày sinh, Nơi sinh. Danh sách được sắp xếp tăng dần theo tên sinh viên. 
        result = DMSV.objects.order_by('tensv').values()
# 2.2. Cho biết danh sách những sinh viên mà tên có chứa ký tự nằm trong khoảng từ a đến m, gồm các thông tin: Họ tên sinh viên, Ngày sinh, Nơi sinh. Danh sách được sắp xếp tăng dần theo tên sinh viên. 
        result = DMSV.objects.extra(where=["tensv rlike '^[a-m]'"]).order_by('tensv').values()
        # 2.3. Liệt kê danh sách sinh viên, gồm các thông tin sau: Mã sinh viên, Họ sinh viên, Tên sinh viên, Học bổng. Danh sách sẽ được sắp xếp theo thứ tự Mã sinh viên tăng dần. 
        result = DMSV.objects.order_by('masv').values()
# 2.4. Thông tin các sinh viên gồm: Họ tên sinh viên, Ngày sinh, Học bổng. Thông tin sẽ được sắp xếp theo thứ tự Ngày sinh tăng dần và Học bổng giảm dần. 
        result = DMSV.objects.order_by('ngaysinh', '-hocbong').values()
# 2.5. Cho biết danh sách các sinh viên có học bổng lớn hơn 100,000, gồm các thông tin: Mã sinh viên, Họ tên sinh viên, Mã khoa, Học bổng. Danh sách sẽ được sắp xếp theo thứ tự Mã khoa giảm dần. 
        result = DMSV.objects.filter(Q(hocbong__gt=100000)).order_by('-khoa_id').values()
        # 1.1. Danh sách sinh viên có nơi sinh ở Hà Nội  và  sinh vào  tháng 02, gồm các thông tin: Họ sinh viên, Tên sinh viên, Nơi sinh, Ngày sinh Câu lệnh: 
        from django.db.models import Q
        result = DMSV.objects.filter(Q(noisinh='Hà nội') & Q(ngaysinh__month=2)).values()
        # 1.2. Cho biết những sinh viên có tuổi lớn hơn 20, thông tin gồm: Họ tên sinh viên, Tuổi, Học bổng. 
        # result = DMSV.objects.extra(where=["year(getdate()) - year(ngaysinh)"]).values()
        from django.db.models.functions import ExtractYear, Now
        result = DMSV.objects.annotate(age=ExtractYear(Now()) - ExtractYear('ngaysinh')).filter(age__gt=20).values('hosv', 'tensv', 'age', 'hocbong')
# 1.3. Danh sách những sinh viên có tuổi từ 20 đến 25, thông tin gồm: Họ tên sinh viên, Tuổi, Tên khoa. 
        from django.db.models.functions import Now, ExtractYear
        result = DMSV.objects.annotate(age=ExtractYear(Now())-ExtractYear('ngaysinh')).filter(age__range=(20,30)).values()
# 1.4. Danh  sách sinh viên sinh vào mùa xuân  năm 1990, gồm các thông tin:  Họ tên sinh viên, Phái, Ngày sinh. (dùng hàm datepart(“q”,ngaysinh))
# 2.1.	Cho biết thông tin về mức học bổng của các sinh viên, gồm: Mã sinh viên, Phái, Mã khoa, Mức học bổng. Trong đó, mức học bổng sẽ hiển thị là “Học bổng cao” nếu giá trị của học bổng lớn hơn 150,000 và ngược lại hiển thị là “Mức trung bình” Câu lệnh: 
        from django.db.models import Case, When, Value
        result = DMSV.objects.annotate(muchocbong=Case(
            When(hocbong__gte=150000, then=Value('Học bổng cao')),
            default=Value('Mức trung bình')
        )).values('masv', 'phai', 'khoa_id', 'muchocbong')
#2.2.	Cho biết kết quả điểm thi của các sinh viên, gồm các thông tin: Họ tên sinh viên, Mã môn học, lần thi, điểm, kết quả (nếu điểm nhỏ hơn 5 thì rớt ngược lại đậu). 
        from django.db.models import When, Case, Value
        result = KETQUA.objects.annotate(ketqua=Case(
            When(diem__lt=5, then=Value('rớt')),
            default=Value('đậu')
        )).select_related('sv').values('sv__hosv', 'sv__tensv', 'mh_id', 'lanthi', 'diem', 'ketqua')
#3.1.	Cho biết tổng số sinh viên của toàn trường. 
        result = DMSV.objects.count()
        # 3.2.	Cho biết tổng sinh viên và tổng sinh viên nữ. 
        result = DMSV.objects.filter(phai=True).count()
# 3.3.	Cho biết tổng số sinh viên của từng khoa. 
        from django.db.models import Count
        result = DMSV.objects.select_related('khoa').values('khoa_id', 'khoa__tenkhoa').annotate(count=Count('masv'))
        #3.4.	Cho biết số lượng sinh viên học từng môn (dùng Distinct loại trùng nhau) Câu lệnh: 
        from django.db.models import Count
        result = DMSV.objects.select_related('ketqua', 'ketqua.mh').values('ketqua__mh__tenmh').annotate(count=Count('ketqua__sv_id', distinct=True))
# 3.5.	Cho biết số lượng môn học mà mỗi sinh viên đã học.
        result = DMSV.objects.select_related('ketqua__mh', 'ketqua').values('masv', 'hosv','tensv').annotate(Count('ketqua__mh_id', distinct=True)).query
# 3.6.	Cho biết học bổng cao nhất của mỗi khoa. 
        from django.db.models import Max
        result = DMSV.objects.select_related('khoa').values('khoa__makhoa', 'khoa__tenkhoa').annotate(Max('hocbong'))
# 3.7.	Cho biết tổng số sinh viên nam và tổng số sinh viên nữ của mỗi khoa. 
        from django.db.models import Count, Case, When, Value, Sum
        # .annotate(count_g=Count(''))
        result = DMSV.objects.select_related('khoa').values('khoa__makhoa', 'khoa__tenkhoa').annotate(count_b=Sum(Case(
            When(phai=0, then=Value(1)), default=Value(0)
        )), count_g=Sum(Case(
            When(phai=1, then=Value(1)), default=Value(0)
        )))
        #3.8 Cho biết số lượng sinh viên theo từng độ tuổi.
        from django.db.models.functions import ExtractYear, Now
        result = DMSV.objects.annotate(tuoi=ExtractYear(Now())-ExtractYear('ngaysinh')).values('tuoi').annotate(count=Count('masv'))
# 3.9.  Cho biết số lượng sinh viên đậu và số lượng sinh viên rớt của từng môn trong lần thi 1. 
        from django.db.models import Sum, Q
        result = DMMH.objects.select_related('ketqua').values('mamh','tenmh').annotate(total_dau=Sum(Case(
            When(Q(ketqua__lanthi=1) & Q(ketqua__diem__gt=5), then=Value(1)), default=Value(0)
        )), total_rot=Sum(Case(
            When(Q(ketqua__lanthi=1) & Q(ketqua__diem__lte=5), then=Value(1)), default=Value(0)
        )))
        #1.1.	Cho biết năm sinh nào có 2 sinh viên đang theo học tại trường. 
        result = DMSV.objects.annotate(namsinh=(ExtractYear('ngaysinh'))).values('namsinh').annotate(count=Count('namsinh')).filter(count=2)
        # 1.2.	Cho biết nơi nào có hơn 2 sinh viên đang theo học tại trường. 
        result = DMSV.objects.values('noisinh').annotate(count=Count('noisinh')).filter(count=2)
# 1.3.	Cho biết môn nào có trên 3 sinh viên dự thi. 
        result = KETQUA.objects.select_related('mh').values('mh__mamh', 'mh__tenmh').annotate(count=Count('sv_id', distinct=True)).filter(count__gt=3)
# 1.4.	Cho biết sinh viên thi lại trên 2 lần. 
        result = KETQUA.objects.select_related('sv').values('sv__tensv').filter(lanthi=2).annotate(count=Count('sv_id',distinct=False)).filter(count__gte=2)
# 1.5.	Cho biết sinh viên nam có điểm trung bình lần 1 trên 7.0 
        from django.db.models import Avg
        result = KETQUA.objects.select_related('sv').values('sv__tensv').filter(lanthi=1).annotate(avg=Avg('diem')).filter(avg__gt=7)
# 1.6.	Cho biết danh sách sinh viên rớt trên 2 môn ở lần thi 1. 
        result = KETQUA.objects.filter(lanthi=1).values('sv__tensv').annotate(sum=Sum(Case(
            When(diem__lte=5,then=Value(1))
        ))).filter(sum__gte=2)
# 1.7.	Cho biết khoa nào có nhiều hơn 2 sinh viên nam. 
        result = DMSV.objects.select_related('khoa').values('khoa__tenkhoa').filter(phai=0).annotate(count=Count('masv'))
# 1.8.	Cho biết khoa có 2 sinh đạt học bổng từ 100.000 đến 200.000.
        result = DMSV.objects.select_related('khoa').values('khoa__tenkhoa').annotate(count=Sum(Case(
            When(hocbong__range=(100000,200000), then=Value(1))
        ))).filter(count__gte=2)
# 1.9.	Cho biết sinh viên nam học trên từ 3 môn trở lên 
        result = KETQUA.objects.select_related('sv').values('sv__tensv').filter(sv__phai=0).annotate(count=Count('mh_id', distinct=True)).filter(count__gte=3)
# 1.10.	Cho biết sinh viên có điểm trung bình lần 1 từ 7 trở lên nhưng không có môn nào dưới 5. 
        result = KETQUA.objects.select_related('sv').values('sv__masv','sv__tensv').filter(Q(lanthi=1)).annotate(avg=Avg('diem')).filter(Q(avg__gte=7))
# 1.11.	Cho biết môn không có sinh viên rớt ở lần 1. (rớt là điểm <5)
        result = KETQUA.objects.select_related('mh').values('mh__tenmh').filter(lanthi=1).annotate(count=Sum(Case(
            When(diem__lt=5, then=Value(1)), default=Value(0)
        ))).filter(count=0)
# 1.12.	Cho biết sinh viên đăng ký học hơn 3 môn mà thi lần 1 không bị rớt môn nào. 
        result = KETQUA.objects.select_related('mh','sv').filter(lanthi=1).values('sv__tensv').annotate(monrot=Sum(Case(
            When(Q(lanthi=1) & Q(diem__lt=5), then=Value(1)), default=Value(0)
        )), mondangky=Count('sv_id')).filter(Q(monrot=0) & Q(mondangky__gte=3))
#2.1	Cho biết sinh viên nào có học bổng cao nhất.
        from django.db.models import Subquery
        max = DMSV.objects.aggregate(Max('hocbong'))
        result = DMSV.objects.values('tensv').filter(hocbong=max['hocbong__max']).first()
        print(result)
        
        