class Employee:
    def __init__(self,ho_ten,ngaysinh,ngay_vao_cty):
        self.ho_ten = ho_ten
        self.ngaysinh = ngaysinh
        self.ngay_vao_cty = ngay_vao_cty

    def in_thong_tin(self):
        print(f"Họ và tên: {self.ho_ten}")
        print(f"Ngày sinh:{self.ngaysinh} ")
        print(f"Ngày vào công ty: {self.ngay_vao_cty}")

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f'{self.day:02d}/{self.month:02d}/{self.year}')
day = int(input("Nhập ngày:"))
month = int(input("Nhập tháng:"))
year = int(input("Nhập năm:"))
date = Employee(day, month, year)
date.display()