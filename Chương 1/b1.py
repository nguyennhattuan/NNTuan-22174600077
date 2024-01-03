#Tạo lớp biểu diễn hình chữ nhật, chu vi , diện tích
class hcn:
    def __init__(self):
        self.dai = 0
        self.rong = 0
    
    def dl_canh_hcn(self):
        self.dai = float(input("Nhập chiều dài:"))
        self.rong = float(input("Nhập chiều rộng:"))

    def chuvi(self):
        chu_vi = (self.dai + self.rong) * 2
        return chu_vi
    
    def dientich(self):
        dien_tich = self.dai * self.rong
        return dien_tich
    
    def thongso(self):
        print("Thông số hình chữ nhật:")
        print(f'Chiều dài: {self.dai}')
        print(f'Chiều rộng: {self.rong}')
        print(f'Chu vi:{self.chuvi()}')
        print(f'Diện tích: {self.dientich()}')

Hinh_chu_nhat = hcn()
Hinh_chu_nhat.dl_canh_hcn()
Hinh_chu_nhat.thongso()

