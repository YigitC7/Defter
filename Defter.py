import customtkinter as ctk
from os import getenv
from os import mkdir
import os

kullanici_dizini = os.path.expanduser("~")


hakkinda_text = """ |
 |Sürüm\t\t: 1.0
 |Yazan\t\t: Yiğit çıtak
 |dil\t\t: Python
 |veri tabanı\t: .yigit
 |kütüphane\t: customtkinter
 |=======================================
 |Bu bir not defteri programıdır.
 |Sayfalar halinde not tutmanızı sağlar
 |ve sadece Linux (KDE Plasma uyumlu) işletim
 |sistemi için hazırlanmıştır. yazdığınız notlar
 |Benim geliştirdiğim şifreli bir
 |veri tabaınında tutulur. Bu veri tabanı
 |kullanıcı klasöründe .defter içinde bulunur.
 |"""

def Sifrele(sifrelenecek_girdi):
	sifreleniyor1 = sifrelenecek_girdi.replace("q","y0y")

	sifreleniyor2 = sifreleniyor1.replace("w","y00y")

	sifreleniyor3 = sifreleniyor2.replace("e","y000y")

	sifreleniyor4 = sifreleniyor3.replace("r","y0000y")

	sifreleniyor5 = sifreleniyor4.replace("t","y00000y")

	sifreleniyor6 = sifreleniyor5.replace("y","y000000y")

	sifreleniyor7 = sifreleniyor6.replace("u","y0000000y")

	sifreleniyor8 = sifreleniyor7.replace("ı","y00000000y")

	sifreleniyor9 = sifreleniyor8.replace("o","y000000000y")

	sifreleniyor10 = sifreleniyor9.replace("p","y0000000000y")

	sifreleniyor11 = sifreleniyor10.replace("ğ","y00000000000y")

	sifreleniyor12 = sifreleniyor11.replace("ü","y000000000000y")

	sifreleniyor13 = sifreleniyor12.replace("a","y0000000000000y")

	sifreleniyor14 = sifreleniyor13.replace("s","y00000000000000y")

	sifreleniyor15 = sifreleniyor14.replace("d","y000000000000000y")

	sifreleniyor16 = sifreleniyor15.replace("f","y0000000000000000y")

	sifreleniyor17 = sifreleniyor16.replace("g","y00000000000000000y")

	sifreleniyor18 = sifreleniyor17.replace("h","y000000000000000000y")

	sifreleniyor19 = sifreleniyor18.replace("j","y0000000000000000000y")

	sifreleniyor20 = sifreleniyor19.replace("k","y00000000000000000000y")

	sifreleniyor21 = sifreleniyor20.replace("l","y000000000000000000000y")

	sifreleniyor22 = sifreleniyor21.replace("ş","y0000000000000000000000y")

	sifreleniyor23 = sifreleniyor22.replace("i","y00000000000000000000000y")

	sifreleniyor24 = sifreleniyor23.replace("z","y000000000000000000000000y")

	sifreleniyor25 = sifreleniyor24.replace("x","y0000000000000000000000000y")

	sifreleniyor26 = sifreleniyor25.replace("c","y00000000000000000000000000y")

	sifreleniyor27 = sifreleniyor26.replace("v","y000000000000000000000000000y")

	sifreleniyor28 = sifreleniyor27.replace("b","y0000000000000000000000000000y")

	sifreleniyor29 = sifreleniyor28.replace("n","y00000000000000000000000000000y")

	sifreleniyor30 = sifreleniyor29.replace("m","y000000000000000000000000000000y")

	sifreleniyor31 = sifreleniyor30.replace("ö","y0000000000000000000000000000000y")

	sifrelendi = sifreleniyor31.replace("ç","y00000000000000000000000000000000y")
	return sifrelendi


def coz(cozulecek_girdi):
	cozuluyor1 = cozulecek_girdi.replace("y000000y0y000000y","q")

	cozuluyor2 = cozuluyor1.replace("y000000y00y000000y","w")

	cozuluyor3 = cozuluyor2.replace("y000000y000y000000y","e")

	cozuluyor4 = cozuluyor3.replace("y000000y0000y000000y","r")

	cozuluyor5 = cozuluyor4.replace("y000000y00000y000000y","t")

	cozuluyor6 = cozuluyor5.replace("y000000y","y")

	cozuluyor7 = cozuluyor6.replace("y0000000y","u")

	cozuluyor8 = cozuluyor7.replace("y00000000y","ı")

	cozuluyor9 = cozuluyor8.replace("y000000000y","o")

	cozuluyor10 = cozuluyor9.replace("y0000000000y","p")

	cozuluyor11 = cozuluyor10.replace("y00000000000y","ğ")

	cozuluyor12 = cozuluyor11.replace("y000000000000y","ü")

	cozuluyor13 = cozuluyor12.replace("y0000000000000y","a")

	cozuluyor14 = cozuluyor13.replace("y00000000000000y","s")

	cozuluyor15 = cozuluyor14.replace("y000000000000000y","d")

	cozuluyor16 = cozuluyor15.replace("y0000000000000000y","f")

	cozuluyor17 = cozuluyor16.replace("y00000000000000000y","g")

	cozuluyor18 = cozuluyor17.replace("y000000000000000000y","h")

	cozuluyor19 = cozuluyor18.replace("y0000000000000000000y","j")

	cozuluyor20 = cozuluyor19.replace("y00000000000000000000y","k")

	cozuluyor21 = cozuluyor20.replace("y000000000000000000000y","l")

	cozuluyor22 = cozuluyor21.replace("y0000000000000000000000y","ş")

	cozuluyor23 = cozuluyor22.replace("y00000000000000000000000y","i")

	cozuluyor24 = cozuluyor23.replace("y000000000000000000000000y","z")

	cozuluyor25 = cozuluyor24.replace("y0000000000000000000000000y","x")

	cozuluyor26 = cozuluyor25.replace("y00000000000000000000000000y","c")

	cozuluyor27 = cozuluyor26.replace("y000000000000000000000000000y","v")

	cozuluyor28 = cozuluyor27.replace("y0000000000000000000000000000y","b")

	cozuluyor29 = cozuluyor28.replace("y00000000000000000000000000000y","n")

	cozuluyor30 = cozuluyor29.replace("y000000000000000000000000000000y","m")

	cozuluyor31 = cozuluyor30.replace("y0000000000000000000000000000000y","ö")

	cozuldu = cozuluyor31.replace("y00000000000000000000000000000000y","ç")
	return cozuldu


def text_size_yaz(size=""):
	file = open(f"{kullanici_dizini}/.defter/textsize.yigit","w")
	file.write(size)
	file.close()

def text_size_oku():
	file = open(f"{kullanici_dizini}/.defter/textsize.yigit","r")
	file_okundu = file.read()
	return file_okundu
	file.close()


def defter_program():
	def kayit_fonk():
		pad_icerik = yazi_paneli.get("1.0","end").strip()
		try:
			pad_icerik_y0 = Sifrele(pad_icerik)
			file = open(f"{kullanici_dizini}/.defter/notlar/sayfa{sayfa_oku()}.yigit","w")
			file.write(pad_icerik_y0)
			file.close()
		except:
			if sayfa_oku() ==  "1":
				pad_icerik_y0 = Sifrele(pad_icerik)
				file = open(f"{kullanici_dizini}/.defter/notlar/sayfa1.yigit","w")
				file.write(pad_icerik_y0)
				file.close()

	color_sayfalar = "#5314CD"
	color_genel = "#5314CD"
	color_window = "#d9e997"

	try:
		mkdir(f"{kullanici_dizini}/.defter")
		mkdir(f"{kullanici_dizini}/.defter/notlar")
		print("Bilgi: Sistem kayıt dosyası oluşturuldu")
	except:
		print("Bilgi: Sistem kayıt dosyası algılandı")

	def info_fonk():
		hakkinda = ctk.CTk()
		hakkinda.title("Defter | Hakkında")
		hakkinda.minsize(390,340)
		hakkinda.configure(fg_color=color_window)

		info = ctk.CTkLabel(hakkinda,
			text=hakkinda_text,
			font=("italic",20),
			text_color="white",
			justify="left",
			fg_color=color_genel)
		info.pack(pady=20)

		hakkinda.mainloop()

	def sayfa_oku():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","r")
		file_islenmis = file.read()
		return file_islenmis
		print(file_islenmis)
		file.close()

	try:
		print(f"Geri döndü: {sayfa_oku()}")
	except:
		file8877 = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file8877.write("1")
		file8877.close()

	try:
		print(f"yazı boyutu {text_size_oku()}")
	except:
		text_size_yaz("20")
		print("yazı boyutu ayarlandı: 20")

	window = ctk.CTk()
	window.title("Y.Ç | Defter 1.0")
	window.minsize(1200,750)
	window.maxsize(1200,7500)
	window.geometry("1200x750x500x100")
	window.configure(fg_color=color_window)
	window.resizable(False, False)

	class konum:
		def __init__(self,x=0,y=0):
			self.x = x
			self.y = y

	not_paneli_konum = konum(x=600,y=100)
	info_button_konum = konum(x=1,y=1)
	yazi_paneli_konum = konum(x=1,y=150)
	tema_yaziboyut_secenekleri_konum = konum(x=1,y=50)
	kayit_button_konum = konum(x=80,y=1)

	title = ctk.CTkLabel(window,
		text="Defter",
		font=("italic",40),
		text_color="black"
		).pack(pady=20)


	not_paneli = ctk.CTkScrollableFrame(window,
		height=600,
		width=300,
		fg_color="#c7d492")
	not_paneli.place(relx=1.0, rely=0.5, anchor='e')

	def sayfa1_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("1")
		file.close()
		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa1.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 1")
		print(sayfa_oku())
	sayfa1_button = ctk.CTkButton(not_paneli,
		text="Sayfa 1",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa1_fonk)
	sayfa1_button.pack(pady=7)

	def sayfa2_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("2")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa2.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 2")
		print(sayfa_oku())
	sayfa2_button = ctk.CTkButton(not_paneli,
		text="Sayfa 2",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa2_fonk)
	sayfa2_button.pack(pady=7)


	def sayfa3_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("3")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa3.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 3")
		print(sayfa_oku())
	sayfa3_button = ctk.CTkButton(not_paneli,
		text="Sayfa 3",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa3_fonk)
	sayfa3_button.pack(pady=7)

	def sayfa4_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("4")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa4.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 4")
		print(sayfa_oku())
	sayfa4_button = ctk.CTkButton(not_paneli,
		text="Sayfa 4",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa4_fonk)
	sayfa4_button.pack(pady=7)

	def sayfa5_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("5")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa5.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 5")
		print(sayfa_oku())
	sayfa5_button = ctk.CTkButton(not_paneli,
		text="Sayfa 5",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa5_fonk)
	sayfa5_button.pack(pady=7)

	def sayfa6_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("6")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa6.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 6")
		print(sayfa_oku())
	sayfa6_button = ctk.CTkButton(not_paneli,
		text="Sayfa 6",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa6_fonk)
	sayfa6_button.pack(pady=7)

	def sayfa7_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("7")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa7.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 7")
		print(sayfa_oku())
	sayfa7_button = ctk.CTkButton(not_paneli,
		text="Sayfa 7",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa7_fonk)
	sayfa7_button.pack(pady=7)

	def sayfa8_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("8")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa8.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 8")
		print(sayfa_oku())
	sayfa8_button = ctk.CTkButton(not_paneli,
		text="Sayfa 8",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa8_fonk)
	sayfa8_button.pack(pady=7)

	def sayfa9_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("9")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa9.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 9")
		print(sayfa_oku())
	sayfa9_button = ctk.CTkButton(not_paneli,
		text="Sayfa 9",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa9_fonk)
	sayfa9_button.pack(pady=7)

	def sayfa10_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("10")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa10.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 10")
		print(sayfa_oku())
	sayfa10_button = ctk.CTkButton(not_paneli,
		text="Sayfa 10",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa10_fonk)
	sayfa10_button.pack(pady=7)

	def sayfa11_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("11")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa11.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 11")
		print(sayfa_oku())
	sayfa11_button = ctk.CTkButton(not_paneli,
		text="Sayfa 11",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa11_fonk)
	sayfa11_button.pack(pady=7)

	def sayfa12_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("12")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa12.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 12")
		print(sayfa_oku())
	sayfa12_button = ctk.CTkButton(not_paneli,
		text="Sayfa 12",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa12_fonk)
	sayfa12_button.pack(pady=7)

	def sayfa13_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("13")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa13.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 13")
		print(sayfa_oku())
	sayfa13_button = ctk.CTkButton(not_paneli,
		text="Sayfa 13",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa13_fonk)
	sayfa13_button.pack(pady=7)

	def sayfa14_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("14")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa14.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 14")
		print(sayfa_oku())
	sayfa14_button = ctk.CTkButton(not_paneli,
		text="Sayfa 14",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa14_fonk)
	sayfa14_button.pack(pady=7)

	def sayfa15_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("15")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa15.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 15")
		print(sayfa_oku())
	sayfa15_button = ctk.CTkButton(not_paneli,
		text="Sayfa 15",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa15_fonk)
	sayfa15_button.pack(pady=7)

	def sayfa16_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("16")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa16.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 16")
		print(sayfa_oku())
	sayfa16_button = ctk.CTkButton(not_paneli,
		text="Sayfa 16",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa16_fonk)
	sayfa16_button.pack(pady=7)

	def sayfa17_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("17")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa17.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 17")
		print(sayfa_oku())
	sayfa17_button = ctk.CTkButton(not_paneli,
		text="Sayfa 17",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa17_fonk)
	sayfa17_button.pack(pady=7)

	def sayfa18_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("18")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa18.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 18")
		print(sayfa_oku())
	sayfa18_button = ctk.CTkButton(not_paneli,
		text="Sayfa 18",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa18_fonk)
	sayfa18_button.pack(pady=7)

	def sayfa19_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("19")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa19.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 19")
		print(sayfa_oku())
	sayfa19_button = ctk.CTkButton(not_paneli,
		text="Sayfa 19",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa19_fonk)
	sayfa19_button.pack(pady=7)

	def sayfa20_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("20")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa20.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 20")
		print(sayfa_oku())
	sayfa20_button = ctk.CTkButton(not_paneli,
		text="Sayfa 20",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa20_fonk)
	sayfa20_button.pack(pady=7)

	def sayfa21_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("21")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa21.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 21")
		print(sayfa_oku())
	sayfa21_button = ctk.CTkButton(not_paneli,
		text="Sayfa 21",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa21_fonk)
	sayfa21_button.pack(pady=7)

	def sayfa22_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("22")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa22.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 22")
		print(sayfa_oku())
	sayfa22_button = ctk.CTkButton(not_paneli,
		text="Sayfa 22",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa22_fonk)
	sayfa22_button.pack(pady=7)

	def sayfa23_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("23")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa23.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 23")
		print(sayfa_oku())
	sayfa23_button = ctk.CTkButton(not_paneli,
		text="Sayfa 23",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa23_fonk)
	sayfa23_button.pack(pady=7)

	def sayfa24_fonk():
		file = open(f"{kullanici_dizini}/.defter//end.yigit","w")
		file.write("24")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa24.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 24")
		print(sayfa_oku())
	sayfa24_button = ctk.CTkButton(not_paneli,
		text="Sayfa 24",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa24_fonk)
	sayfa24_button.pack(pady=7)

	def sayfa25_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("25")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa25.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 25")
		print(sayfa_oku())
	sayfa25_button = ctk.CTkButton(not_paneli,
		text="Sayfa 25",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa25_fonk)
	sayfa25_button.pack(pady=7)

	def sayfa26_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("26")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa26.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 26")
		print(sayfa_oku())
	sayfa26_button = ctk.CTkButton(not_paneli,
		text="Sayfa 26",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa26_fonk)
	sayfa26_button.pack(pady=7)

	def sayfa27_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("27")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa27.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 27")
		print(sayfa_oku())
	sayfa27_button = ctk.CTkButton(not_paneli,
		text="Sayfa 27",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa27_fonk)
	sayfa27_button.pack(pady=7)

	def sayfa28_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("28")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa28.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 28")
		print(sayfa_oku())
	sayfa28_button = ctk.CTkButton(not_paneli,
		text="Sayfa 28",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa28_fonk)
	sayfa28_button.pack(pady=7)

	def sayfa29_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("29")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa29.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 29")
		print(sayfa_oku())
	sayfa29_button = ctk.CTkButton(not_paneli,
		text="Sayfa 29",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa29_fonk)
	sayfa29_button.pack(pady=7)

	def sayfa30_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("30")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa30.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 30")
		print(sayfa_oku())
	sayfa30_button = ctk.CTkButton(not_paneli,
		text="Sayfa 30",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa30_fonk)
	sayfa30_button.pack(pady=7)

	def sayfa31_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("31")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa31.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 31")
		print(sayfa_oku())
	sayfa31_button = ctk.CTkButton(not_paneli,
		text="Sayfa 31",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa31_fonk)
	sayfa31_button.pack(pady=7)

	def sayfa32_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("32")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa32.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 32")
		print(sayfa_oku())
	sayfa32_button = ctk.CTkButton(not_paneli,
		text="Sayfa 32",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa32_fonk)
	sayfa32_button.pack(pady=7)

	def sayfa33_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("33")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa33.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 33")
		print(sayfa_oku())
	sayfa33_button = ctk.CTkButton(not_paneli,
		text="Sayfa 33",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa33_fonk)
	sayfa33_button.pack(pady=7)

	def sayfa34_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("34")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa34.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 34")
		print(sayfa_oku())
	sayfa34_button = ctk.CTkButton(not_paneli,
		text="Sayfa 34",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa34_fonk)
	sayfa34_button.pack(pady=7)

	def sayfa35_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("35")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa35.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 35")
		print(sayfa_oku())
	sayfa33_button = ctk.CTkButton(not_paneli,
		text="Sayfa 35",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa35_fonk)
	sayfa33_button.pack(pady=7)

	def sayfa36_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("36")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa36.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 36")
		print(sayfa_oku())
	sayfa30_button = ctk.CTkButton(not_paneli,
		text="Sayfa 36",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa36_fonk)
	sayfa30_button.pack(pady=7)

	def sayfa37_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("37")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa37.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 37")
		print(sayfa_oku())
	sayfa31_button = ctk.CTkButton(not_paneli,
		text="Sayfa 37",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa37_fonk)
	sayfa31_button.pack(pady=7)

	def sayfa38_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("38")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa38.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 38")
		print(sayfa_oku())
	sayfa32_button = ctk.CTkButton(not_paneli,
		text="Sayfa 38",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa38_fonk)
	sayfa32_button.pack(pady=7)

	def sayfa39_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("39")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa39.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 39")
		print(sayfa_oku())
	sayfa33_button = ctk.CTkButton(not_paneli,
		text="Sayfa 39",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa39_fonk)
	sayfa33_button.pack(pady=7)

	def sayfa40_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("40")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa40.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 40")
		print(sayfa_oku())
	sayfa34_button = ctk.CTkButton(not_paneli,
		text="Sayfa 40",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa40_fonk)
	sayfa34_button.pack(pady=7)

	def sayfa41_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("41")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa41.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 41")
		print(sayfa_oku())
	sayfa34_button = ctk.CTkButton(not_paneli,
		text="Sayfa 41",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa41_fonk)
	sayfa34_button.pack(pady=7)

	def sayfa42_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("42")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa42.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 42")
		print(sayfa_oku())
	sayfa34_button = ctk.CTkButton(not_paneli,
		text="Sayfa 42",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa42_fonk)
	sayfa34_button.pack(pady=7)

	def sayfa43_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("43")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa43.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 43")
		print(sayfa_oku())
	sayfa34_button = ctk.CTkButton(not_paneli,
		text="Sayfa 43",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa43_fonk)
	sayfa34_button.pack(pady=7)

	def sayfa44_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("44")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa44.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 44")
		print(sayfa_oku())
	sayfa34_button = ctk.CTkButton(not_paneli,
		text="Sayfa 44",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa44_fonk)
	sayfa34_button.pack(pady=7)

	def sayfa45_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("45")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa45.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 45")
		print(sayfa_oku())
	sayfa34_button = ctk.CTkButton(not_paneli,
		text="Sayfa 45",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa45_fonk)
	sayfa34_button.pack(pady=7)

	def sayfa46_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("46")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa46.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 46")
		print(sayfa_oku())
	sayfa34_button = ctk.CTkButton(not_paneli,
		text="Sayfa 46",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa46_fonk)
	sayfa34_button.pack(pady=7)

	def sayfa47_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("47")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa47.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 47")
		print(sayfa_oku())
	sayfa34_button = ctk.CTkButton(not_paneli,
		text="Sayfa 47",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa47_fonk)
	sayfa34_button.pack(pady=7)

	def sayfa48_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("48")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa48.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 48")
		print(sayfa_oku())
	sayfa34_button = ctk.CTkButton(not_paneli,
		text="Sayfa 48",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa48_fonk)
	sayfa34_button.pack(pady=7)

	def sayfa49_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("49")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa49.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 49")
		print(sayfa_oku())
	sayfa34_button = ctk.CTkButton(not_paneli,
		text="Sayfa 49",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa49_fonk)
	sayfa34_button.pack(pady=7)

	def sayfa50_fonk():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file.write("50")
		file.close()

		try:
			file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa50.yigit","r")
			file2_islenmis = file2.read()
			file2_islenmis2 = coz(file2_islenmis)
			yazi_paneli.delete("1.0","end")
			yazi_paneli.insert("1.0",file2_islenmis2)
			file2.close()
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text="Sayfa 50")
		print(sayfa_oku())
	sayfa34_button = ctk.CTkButton(not_paneli,
		text="Sayfa 50",
		fg_color=color_sayfalar,
		text_color="white",
		width=500,
		height=50,
		command=sayfa50_fonk)
	sayfa34_button.pack(pady=7)



	info_button = ctk.CTkButton(window,
		text="Hakkında",
		fg_color=color_genel,
		text_color="white",
		width=40,
		command=info_fonk)
	info_button.place(
		x=info_button_konum.x,
		y=info_button_konum.y)

	yazi_paneli = ctk.CTkTextbox(window,
		height=570,
		width=860,
		fg_color="#000099",
		text_color="white",
		wrap="word",
		font=("italic",int(text_size_oku()))
		)
	yazi_paneli.place(
		x=yazi_paneli_konum.x,
		y=yazi_paneli_konum.y,)

	def yaziboyut_fonk(cuhice):
		if cuhice == "10":
			yazi_paneli.configure(font=("italic",10))
			text_size_yaz("10")

		elif cuhice == "20":
			yazi_paneli.configure(font=("italic",20))
			text_size_yaz("20")

		elif cuhice == "30":
			yazi_paneli.configure(font=("italic",30))
			text_size_yaz("30")

		elif cuhice == "40":
			yazi_paneli.configure(font=("italic",40))
			text_size_yaz("40")

		elif cuhice == "50":
			yazi_paneli.configure(font=("italic",50))
			text_size_yaz("50")

	tema_yaziboyut_secenekleri = ctk.CTkComboBox(window,
		values=["10","20","30","40","50"],
		command=yaziboyut_fonk)
	tema_yaziboyut_secenekleri.set(f"Yazı boyutu: {text_size_oku()}")
	tema_yaziboyut_secenekleri.place(
		x=tema_yaziboyut_secenekleri_konum.x,
		y=tema_yaziboyut_secenekleri_konum.y)

	sayfa_numarasi = ctk.CTkLabel(window,
		text="Sayfa 1",
		font=("italic",20),
		text_color="black")
	sayfa_numarasi.place(x=3,y=110)


	kayit_button = ctk.CTkButton(window,
		text="Kaydet",
		fg_color=color_genel,
		text_color="white",
		width=40,
		command=kayit_fonk)
	kayit_button.place(
		x=kayit_button_konum.x,
		y=kayit_button_konum.y,)

	try:
		if sayfa_oku() == "1":
			sayfa1_fonk()
		elif sayfa_oku() == "2":
			sayfa2_fonk()
		elif sayfa_oku() == "3":
			sayfa3_fonk()
		elif sayfa_oku() == "4":
			sayfa4_fonk()
		elif sayfa_oku() == "5":
			sayfa5_fonk()
		elif sayfa_oku() == "6":
			sayfa6_fonk()
		elif sayfa_oku() == "7":
			sayfa7_fonk()
		elif sayfa_oku() == "8":
			sayfa8_fonk()
		elif sayfa_oku() == "9":
			sayfa9_fonk()
		elif sayfa_oku() == "10":
			sayfa10_fonk()
		elif sayfa_oku() == "11":
			sayfa11_fonk()
		elif sayfa_oku() == "12":
			sayfa12_fonk()
		elif sayfa_oku() == "13":
			sayfa13_fonk()
		elif sayfa_oku() == "14":
			sayfa14_fonk()
		elif sayfa_oku() == "15":
			sayfa15_fonk()
		elif sayfa_oku() == "16":
			sayfa16_fonk()
		elif sayfa_oku() == "17":
			sayfa17_fonk()
		elif sayfa_oku() == "18":
			sayfa18_fonk()
		elif sayfa_oku() == "19":
			sayfa19_fonk()
		elif sayfa_oku() == "20":
			sayfa20_fonk()
		elif sayfa_oku() == "21":
			sayfa21_fonk()
		elif sayfa_oku() == "22":
			sayfa22_fonk()
		elif sayfa_oku() == "23":
			sayfa23_fonk()
		elif sayfa_oku() == "24":
			sayfa24_fonk()
		elif sayfa_oku() == "25":
			sayfa25_fonk()
		elif sayfa_oku() == "26":
			sayfa26_fonk()
		elif sayfa_oku() == "27":
			sayfa27_fonk()
		elif sayfa_oku() == "28":
			sayfa28_fonk()
		elif sayfa_oku() == "29":
			sayfa29_fonk()
		elif sayfa_oku() == "30":
			sayfa30_fonk()
		elif sayfa_oku() == "31":
			sayfa31_fonk()
		elif sayfa_oku() == "32":
			sayfa32_fonk()
		elif sayfa_oku() == "33":
			sayfa33_fonk()
		elif sayfa_oku() == "34":
			sayfa34_fonk()
		elif sayfa_oku() == "35":
			sayfa35_fonk()
		elif sayfa_oku() == "36":
			sayfa36_fonk()
		elif sayfa_oku() == "37":
			sayfa37_fonk()
		elif sayfa_oku() == "38":
			sayfa38_fonk()
		elif sayfa_oku() == "39":
			sayfa39_fonk()
		elif sayfa_oku() == "40":
			sayfa40_fonk()
		elif sayfa_oku() == "41":
			sayfa41_fonk()
		elif sayfa_oku() == "42":
			sayfa42_fonk()
		elif sayfa_oku() == "43":
			sayfa43_fonk()
		elif sayfa_oku() == "44":
			sayfa44_fonk()
		elif sayfa_oku() == "45":
			sayfa45_fonk()
		elif sayfa_oku() == "46":
			sayfa46_fonk()
		elif sayfa_oku() == "47":
			sayfa47_fonk()
		elif sayfa_oku() == "48":
			sayfa48_fonk()
		elif sayfa_oku() == "49":
			sayfa49_fonk()
		elif sayfa_oku() == "50":
			sayfa50_fonk()
	except:
		pass

	window.mainloop()

if __name__ == "__main__":
	defter_program()
