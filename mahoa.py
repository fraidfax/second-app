def mahoa(a):
	b = ""
	for i in a:
		a = ord(i)
		a += 2
		b = chr(a) + b
	return b
def giaima(a):
	b = ""
	for i in a:
		a = ord(i)
		a -= 2
		b = chr(a) + b
def introducion():
	print("Chương trình mã hóa thông tin")
	print("Chọn phương thức\n1.Mã Hóa\n2.Giải Mã")
	choose = int(input("Phương Thức: "))
	if choose == 1:
		a = input("Thông tin cần mã hóa: ")
		b = ""
		mahoa(a)
		print("Code Mã Hóa:" ,b)
	if choose == 2:
		a = input("Thông tin cần Giải Mã: ")
		b = ""

		print("Code Giải Mã:" ,b)