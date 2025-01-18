import customtkinter as ctk
from os import getenv
from os import mkdir
import os

kullanici_dizini = os.path.expanduser("~")
kullanici_adi = os.getlogin()

hakkinda_text = """ |
 |Sürüm\t\t: 3.0
 |Yazan\t\t: Yiğit çıtak
 |Dil\t\t: Python
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
kisayol_text = """
 |CTRL + C : Kopyala
 |CTRL + V : Yapıştır
 |CTRL + X : Kes
 |CTRL + S : Kaydet"""

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

	def kayit_fonk(event=None):
		pad_icerik = yazi_paneli.get("1.0","end").strip()
		kayit_bildirim.place(x=103,y=110)
		kayit_bildirim.after(3000, lambda: kayit_bildirim.place_forget())
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

	def info_fonk(event=None):
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

	def kisayol_fonk():
		hakkinda = ctk.CTk()
		hakkinda.title("Defter | Kısayollar")
		hakkinda.minsize(390,340)
		hakkinda.configure(fg_color=color_window)

		info = ctk.CTkLabel(hakkinda,
			text=kisayol_text,
			font=("italic",30),
			text_color="white",
			justify="left",
			width=350,
			height=300,
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

	def baslik_turkce_optimasyon(kullanici_adi=kullanici_adi):
		if not kullanici_adi.isalpha():
			return f"{kullanici_adi} Defteri"

		sesli_harfler = "aeıioöuü"
		son_harfi = kullanici_adi[-1]

		if son_harfi in sesli_harfler:
			sonuc = f"{kullanici_adi}'nın defteri"
			return sonuc.capitalize()
		else:
			sonuc = f"{kullanici_adi}'in defteri"
			return sonuc.capitalize()

	window = ctk.CTk()
	window.title(baslik_turkce_optimasyon())
	window.minsize(1200,750)
	window.maxsize(1200,7500)
	window.geometry("1200x750x500x100")
	window.configure(fg_color=color_window)
	window.resizable(False, False)

	window.bind("<Control-s>",kayit_fonk)
	window.bind("<Control-h>",info_fonk)

	class konum:
		def __init__(self,x=0,y=0):
			self.x = x
			self.y = y

	not_paneli_konum = konum(x=600,y=100)
	info_button_konum = konum(x=1,y=1)
	yazi_paneli_konum = konum(x=1,y=150)
	tema_yaziboyut_secenekleri_konum = konum(x=1,y=50)
	kayit_button_konum = konum(x=175,y=10)
	kisa_button_konum = konum(x=80,y=1)

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

	info_button = ctk.CTkButton(window,
		text="Hakkında",
		fg_color=color_genel,
		text_color="white",
		width=40,
		command=info_fonk)
	info_button.place(
		x=info_button_konum.x,
		y=info_button_konum.y)

	kisayol_button = ctk.CTkButton(window,
		text="Kısayollar",
		fg_color=color_genel,
		text_color="white",
		width=40,
		command=kisayol_fonk)
	kisayol_button.place(
		x=kisa_button_konum.x,
		y=kisa_button_konum.y)

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
		yazi_paneli.configure(font=("italic",int(cuhice)))
		text_size_yaz(cuhice)


	tema_values_l = [str(tema_values_i) for tema_values_i in range(10,41,2)]

	tema_values_l = tema_values_l
	tema_yaziboyut_secenekleri = ctk.CTkComboBox(window,
		values=tema_values_l,
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

	kayit_bildirim = ctk.CTkLabel(window,
							   text="Kayıt edildi!",
							   font=("italic",21),
							   text_color="blue")

	kayit_button = ctk.CTkButton(window,
		text="Kaydet",
		fg_color=color_genel,
		text_color="white",
		width=40,
		font=("italic",21),
		command=kayit_fonk)
	kayit_button.place(
		x=kayit_button_konum.x,
		y=kayit_button_konum.y,)

	for i in range(1, 101):
		def create_page_function(page_num):
			def page_fonk():
				file = open(f"{kullanici_dizini}/.defter/end.yigit", "w")
				file.write(str(page_num))
				file.close()
				try:
					file2 = open(f"{kullanici_dizini}/.defter/notlar/sayfa{page_num}.yigit", "r")
					file2_islenmis = file2.read()
					file2_islenmis2 = coz(file2_islenmis)
					yazi_paneli.delete("1.0", "end")
					yazi_paneli.insert("1.0", file2_islenmis2)
					file2.close()
				except FileNotFoundError:
					yazi_paneli.delete("1.0", "end")
				sayfa_numarasi.configure(text=f"Sayfa {page_num}")
				print(sayfa_oku())
			return page_fonk

		button = ctk.CTkButton(not_paneli,
						 text=f"Sayfa{i}",
						 fg_color=color_sayfalar,
						 text_color="white",
						 width=500,height=50,
						 command=create_page_function(i))
		button.pack(pady=7)

	def sayfa_geri_dondur():
		try:
			file = open(f"{kullanici_dizini}/.defter/notlar/sayfa{sayfa_oku()}.yigit","r")
			file_oku = file.read()
			file_islenmis = coz(file_oku)
			file.close()
			yazi_paneli.insert("1.0",file_islenmis)
		except:
			yazi_paneli.delete("1.0","end")

		sayfa_numarasi.configure(text=f"Sayfa {sayfa_oku()}")

	sayfa_geri_dondur()
	window.mainloop()

if __name__ == "__main__":
	defter_program()
