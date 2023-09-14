import cv2
import os
import sys
from pathlib import Path
import matplotlib.pyplot as plt
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
# path = 'xulyanh/road.jpg'
# img = cv2.imread(path)
# # cv2.imshow("image", img)
# #Chúng ta có thể thấy hình dạng, tức là chiều rộng, chiều cao và các kênh của hình ảnh bằng thuộc tính hình dạng.
# shape = img.shape
# print(shape)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Thư viện Matplotlib sử dụng định dạng màu RGB để đọc hình ảnh màu. Ở đây chúng tôi đang trình bày một ví dụ về đọc hình ảnh bằng thư viện này.
# plt.imshow(img)
# plt.waitforbuttonpress()
# plt.close('all')

#Để chuyển đổi BGR sang RGB, chúng ta sử dụng hàm:
# RBG_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(RBG_img)
# plt.waitforbuttonpress()
# plt.close('all')

#Mở ở chế độ thang độ xám
# img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# cv2.imshow('image', img)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()

# Cú pháp: cv2.imwrite(tên file, hình ảnh)
# Tham số:
# filename: Một chuỗi đại diện cho tên file. Tên tệp phải bao gồm định dạng hình ảnh như .jpg, .png, v.v.
# hình ảnh: Đây là hình ảnh sẽ được lưu.

# Giá trị trả về: Trả về true nếu hình ảnh được lưu thành công.
# import os
# directory = 'images'
# if not os.path.isdir(directory):
#     os.mkdir(directory)
# os.chdir(directory)
# cv2.imwrite('test.jpg', img)

# Cú pháp : cv2.addWeighted(img1, wt1, img2, wt2, gammaValue)
# Tham số : 
# img1 : Mảng hình ảnh đầu vào đầu tiên (Kênh đơn, 8 bit hoặc dấu phẩy động) 
# wt1 : Trọng lượng của các phần tử hình ảnh đầu vào đầu tiên được áp dụng cho hình ảnh cuối cùng 
# img2 : Mảng hình ảnh đầu vào thứ hai (Kênh đơn, 8 bit hoặc dấu phẩy động) 
# wt2 : Trọng lượng của các phần tử hình ảnh đầu vào thứ hai được áp dụng cho 
# gamma hình ảnh cuối cùng Giá trị : Đo ánh sáng

# img1 = cv2.imread('xulyanh/img1.jpg')
# img2 = cv2.imread('xulyanh/img2.jpg')
# img_weighted = cv2.addWeighted(img1, 0.5, img2, 0.4, 0)
# cv2.imshow('image', img_weighted)
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()

# # Phép trừ hình ảnh:
# # Cũng giống như phép cộng, chúng ta có thể trừ các giá trị pixel trong hai hình ảnh và hợp nhất chúng với sự trợ giúp của cv2.subtract(). Các hình ảnh phải có kích thước và độ sâu bằng nhau. 
# img1 = cv2.imread('xulyanh/subtract1.jpg')
# img2 = cv2.imread('xulyanh/subtract2.jpg')
# img_subtract = cv2.subtract(img1, img2)
# cv2.imshow('image', img_subtract)
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()
    
# Cú pháp: cv2.resize(source, dsize, dest, fx, fy, interpolation)
# nguồn: Mảng hình ảnh đầu vào (Kênh đơn, 8 bit hoặc dấu phẩy động) 
# dsize: Kích thước của mảng đầu ra
# dest: Mảng đầu ra (Tương tự kích thước và kiểu của mảng ảnh đầu vào) [tùy chọn]
# fx: Hệ số tỷ lệ dọc theo trục ngang [tùy chọn]
# fy: Hệ số tỷ lệ dọc theo trục tung [tùy chọn]
# nội suy: Một trong các phương pháp nội suy ở trên [tùy chọn]

