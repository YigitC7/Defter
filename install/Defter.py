import customtkinter as ctk
from os import getenv, mkdir, getlogin, path

kullanici_dizini = path.expanduser("~")
kullanici_adi = getlogin()

hakkinda_text = """ |Sürüm\t\t\t: 5.0
 |Karakter türü\t\t: UTF-8
 |Yazan\t\t\t: Yiğit Çıtak
 |Dil\t\t\t: Python
 |veri tabanı\t\t: .yigit
 |GUI kütüphanesi\t\t: Customtkinter
 |=======================================
 |Bu bir not defteri programıdır.
 |Sayfalar halinde not tutmanızı sağlar
 |ve sadece Linux işletim sistemi için
 |hazırlanmıştır. yazdığınız notlar
 |Benim geliştirdiğim şifreli bir
 |veri tabaınında tutulur. Bu veri tabanı
 |kullanıcı klasöründe .defter içinde bulunur.
 |"""

kisayol_text = """ |CTRL + F : Yazı Alanını Genişlet
 |CTRL + C : Kopyala
 |CTRL + V : Yapıştır
 |CTRL + X : Kes
 |CTRL + S : Kaydet
 |CTRL + T : Temalar"""

baslangic_ve_bittis_cizgisi = "===========[Defter"

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
	global Yeniden_baslatma_islemi
	Yeniden_baslatma_islemi = False
	global bildirim_2_konum
	bildirim_2_konum = False

	def kayit_fonk(event=None):
		pad_icerik = yazi_paneli.get("1.0","end").strip()
		global bildirim_2_konum
		if bildirim_2_konum == True:
			kayit_bildirim.place(x=1020,y=5)
		else:
			kayit_bildirim.place(x=103,y=110)
		kayit_bildirim.after(3000, lambda: kayit_bildirim.place_forget())
		try:
			pad_icerik_y0 = Sifrele(pad_icerik)
			file = open(f"{kullanici_dizini}/.defter/notlar/sayfa{sayfa_oku()}.yigit","w")
			file.write(pad_icerik_y0)
			file.close()
		except:
			pad_icerik_y0 = Sifrele(pad_icerik)
			file = open(f"{kullanici_dizini}/.defter/notlar/sayfa1.yigit","w")
			file.write(pad_icerik_y0)
			file.close()

	class colors:
		def __init__(self,
			   sayfalar="#5314CD",
			   genel="#5314CD",
			   window="#d9e997",
			   panel="#c7d492",
			   yazi_panel = "#000099",
			   title_text = "black",
			   info_text = "white",
			   kisa_text = "white",
			   button_text = "white",
			   sayfa_text = "white",
			   yazi_paneli_text = "white",
			   sayfa_numarasi_text = "black",
			   kayit_bildirim_text = "blue",
			   etkin_tema_text = "black"):
			self.sayfalar = sayfalar
			self.genel = genel
			self.window = window
			self.panel = panel
			self.yazi_panel = yazi_panel
			self.title_text = title_text
			self.info_text = info_text
			self.kisa_text = kisa_text
			self.button_text = button_text
			self.sayfa_text = sayfa_text
			self.yazi_paneli_text = yazi_paneli_text
			self.sayfa_numarasi_text = sayfa_numarasi_text
			self.kayit_bildirim_text = kayit_bildirim_text
			self.etkin_tema_text = etkin_tema_text

	tema_index1 = colors()
	tema_index2 = colors(
		sayfalar = "#041538",
		genel = "#363636",
		window = "#1c1c1c",
		panel = "#696969",
		yazi_panel = "#080808",
		title_text = "white",
		sayfa_numarasi_text = "white",
		kayit_bildirim_text = "#6495ed",
		etkin_tema_text = "white",
		yazi_paneli_text = "#dcdcdc"
		)
	tema_index3 = colors(
		sayfalar = "#9C9C9C",
		genel = "#dddddd",
		panel = "#808080",
		yazi_panel = "#2f2f2f",
		window = "#F5F5F5",
		kayit_bildirim_text = "#363636",
		kisa_text = "black",
		info_text = "black",
		sayfa_text = "white",
		button_text = "black",
		)

	try:
		mkdir(f"{kullanici_dizini}/.defter")
		mkdir(f"{kullanici_dizini}/.defter/notlar")
		print("Bilgi: Sistem kayıt dosyası oluşturuldu")
	except:
		print("Bilgi: Sistem kayıt dosyası algılandı")

	def tema_index_yaz(girdi):
		file = open(f"{kullanici_dizini}/.defter/tema_index.yigit","w")
		file.write(girdi)
		file.close()

	def tema_index_oku():
		file = open(f"{kullanici_dizini}/.defter/tema_index.yigit","r")
		file_yaz = file.read()
		return file_yaz
		file.close()

	def info_fonk(event=None):
		hakkinda = ctk.CTk()
		hakkinda.title("Defter | Hakkında")
		hakkinda.minsize(390,340)
		hakkinda.configure(fg_color=main_tema.window)

		info = ctk.CTkLabel(hakkinda,
			text=hakkinda_text,
			font=("italic",20),
			text_color=main_tema.info_text,
			justify="left",
			fg_color=main_tema.genel)
		info.pack(pady=20)

		hakkinda.mainloop()

	def kisayol_fonk():
		hakkinda = ctk.CTk()
		hakkinda.title("Defter | Kısayollar")
		hakkinda.minsize(390,340)
		hakkinda.configure(fg_color=main_tema.window)

		kisa = ctk.CTkLabel(hakkinda,
			text=kisayol_text,
			font=("italic",30),
			text_color=main_tema.kisa_text,
			justify="left",
			width=350,
			height=300,
			fg_color=main_tema.genel)
		kisa.pack(pady=20)

		hakkinda.mainloop()

	def tema_fonk(event=None):
		def geri(event = None):
			window.bind("<Control-t>",tema_fonk)
			window.title(baslik_turkce_optimasyon())
			tema_button.configure(text="Temalar",command=tema_fonk,width=40)

			if bildirim_2_konum == False:
				not_paneli.place(relx=1.0, rely=0.5, anchor='e')
				info_button.place(x=info_button_konum.x,y=info_button_konum.y)
				yazi_paneli.place(x=yazi_paneli_konum.x,y=yazi_paneli_konum.y)
				tema_yaziboyut_secenekleri.place(x=tema_yaziboyut_secenekleri_konum.x,y=tema_yaziboyut_secenekleri_konum.y)
				kayit_button.place(x=kayit_button_konum.x,y=kayit_button_konum.y)
				kisayol_button.place(x=kisayol_button_konum.x,y=kisayol_button_konum.y)
				tema_button.place(x=tema_button_konum.x,y=tema_button_konum.y)
				title.pack(pady=20)
				sayfa_numarasi.place(x=sayfa_numarasi_konum.x,y=sayfa_numarasi_konum.y)
			else:
				not_paneli.place_forget()
				yazi_paneli.configure(width=1198,height=650)
				yazi_paneli.place(y=yazi_paneli_konum.y-50)
				sayfa_numarasi.place(x=900,y=5)
				tema_yaziboyut_secenekleri.place(x=tema_yaziboyut_secenekleri_konum.x,y=tema_yaziboyut_secenekleri_konum.y)
				kayit_button.place(x=kayit_button_konum.x,y=kayit_button_konum.y)
				kisayol_button.place(x=kisayol_button_konum.x,y=kisayol_button_konum.y)
				tema_button.place(x=tema_button_konum.x,y=tema_button_konum.y)
				title.pack(pady=20)
				info_button.place(x=info_button_konum.x,y=info_button_konum.y)


			print("Bilgi: Tema ekranı 0")

			tema_alani.pack_forget()
			etkin_tema.pack_forget()

		tema_button.configure(text="Geri",command=geri,width=80)
		tema_button.place(x=10,y=10)

		window.title(f"{baslik_turkce_optimasyon()} | Temalar")
		window.bind("<Control-t>",geri)

		not_paneli.place_forget()
		info_button.place_forget()
		yazi_paneli.place_forget()
		tema_yaziboyut_secenekleri.place_forget()
		kayit_button.place_forget()
		kisayol_button.place_forget()
		title.pack_forget()
		sayfa_numarasi.place_forget()

		print("Bilgi: Tema ekranı 1")

		tema_alani = ctk.CTkScrollableFrame(window,
				height=450,
				width=650,
				fg_color=main_tema.panel)
		tema_alani.pack(pady=20)

		def tema1_fonk():
			tema_index_yaz("1")
			print("Tema: 1")
			global Yeniden_baslatma_islemi
			Yeniden_baslatma_islemi = True
			window.destroy()

		tema1_button = ctk.CTkButton(tema_alani,
				text="Klasik",
				fg_color=main_tema.genel,
				text_color=main_tema.button_text,
				width=600,
				height=50,
				font=("italic",35),
				command=tema1_fonk)
		tema1_button.pack(pady=5)

		def tema2_fonk():
			tema_index_yaz("2")
			print("Tema: 2")
			global Yeniden_baslatma_islemi
			Yeniden_baslatma_islemi = True
			window.destroy()

		tema2_button = ctk.CTkButton(tema_alani,
				text="Koyu",
				fg_color=main_tema.genel,
				text_color=main_tema.button_text,
				width=600,
				height=50,
				font=("italic",35),
				command=tema2_fonk)
		tema2_button.pack(pady=5)

		def tema3_fonk():
			tema_index_yaz("3")
			print("Tema: 3")
			global Yeniden_baslatma_islemi
			Yeniden_baslatma_islemi = True
			window.destroy()

		tema3_button = ctk.CTkButton(tema_alani,
				text="Açık",
				fg_color=main_tema.genel,
				text_color=main_tema.button_text,
				width=600,
				height=50,
				font=("italic",35),
				command=tema3_fonk)
		tema3_button.pack(pady=5)

		etkin_tema = ctk.CTkLabel(window,
				font=("italic",30),
				text_color=main_tema.etkin_tema_text)
		etkin_tema.pack(pady=25)

		if tema_index_oku() == "1":
			etkin_tema.configure(text="Etkin Tema: Klasik")
		elif tema_index_oku() == "2":
			etkin_tema.configure(text="Etkin Tema: Koyu")
		elif tema_index_oku() == "3":
			etkin_tema.configure(text="Etkin Tema: Açık")
		else:
			etkin_tema.configure(text="Tema bulunamadı :/")

	def full_panel_fonk(event=None):
		def geri(event=None):
			not_paneli.place(relx=1.0, rely=0.5, anchor='e')
			yazi_paneli.place(y=yazi_paneli_konum.y)
			yazi_paneli.configure(height=570,width=860)
			sayfa_numarasi.place(x=sayfa_numarasi_konum.x,y=sayfa_numarasi_konum.y)
			global bildirim_2_konum
			bildirim_2_konum =False
			window.bind("<Control-f>",full_panel_fonk)

		not_paneli.place_forget()
		yazi_paneli.configure(width=1198,height=650)
		yazi_paneli.place(y=yazi_paneli_konum.y-50)
		sayfa_numarasi.place(x=900,y=5)
		global bildirim_2_konum
		bildirim_2_konum = True
		window.bind("<Control-f>",geri)

	def sayfa_oku():
		file = open(f"{kullanici_dizini}/.defter/end.yigit","r")
		file_islenmis = file.read()
		return file_islenmis
		print(file_islenmis)
		file.close()

	try:
		print(f"sayfa geri döndü: {sayfa_oku()}")
	except:
		file887755 = open(f"{kullanici_dizini}/.defter/end.yigit","w")
		file887755.write("1")
		file887755.close()

	try:
		print(f"Yazı boyutu geri döndü: {text_size_oku()}")
	except:
		text_size_yaz("20")
		print("Yazı boyutu otomatik ayarlandı: 20")

	try:
		print(f"Tema index geri döndü: Tema {tema_index_oku()}")
	except:
		tema_index_yaz("1")

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

	if tema_index_oku() == "1":
		main_tema = tema_index1
	elif tema_index_oku() == "2":
		main_tema = tema_index2
	elif tema_index_oku() == "3":
		main_tema = tema_index3
	else:
		print("Hata: Tema index bug")

	window = ctk.CTk()
	window.title(baslik_turkce_optimasyon())
	window.minsize(1200,750)
	window.maxsize(1200,750)
	window.geometry("1200x750x500x100")
	window.configure(fg_color=main_tema.window)
	window.resizable(False, False)

	window.bind("<Control-s>",kayit_fonk)
	window.bind("<Control-h>",info_fonk)
	window.bind("<Control-t>",tema_fonk)
	window.bind("<Control-f>",full_panel_fonk)

	class konum:
		def __init__(self,x=1,y=1):
			self.x = x
			self.y = y

	not_paneli_konum = konum(x=600,y=100)
	info_button_konum = konum()
	yazi_paneli_konum = konum(x=1,y=150)
	tema_yaziboyut_secenekleri_konum = konum(x=1,y=50)
	kayit_button_konum = konum(x=235,y=10)
	kisayol_button_konum = konum(x=80,y=1)
	tema_button_konum = konum(x=160,y=1)
	sayfa_numarasi_konum = konum(x=3,y=110)

	title = ctk.CTkLabel(window,
		text="Defter",
		font=("italic",40),
		text_color=main_tema.title_text
		)
	title.pack(pady=20)

	not_paneli = ctk.CTkScrollableFrame(window,
		height=600,
		width=300,
		fg_color=main_tema.panel)
	not_paneli.place(relx=1.0, rely=0.5, anchor='e')

	info_button = ctk.CTkButton(window,
		text="Hakkında",
		fg_color=main_tema.genel,
		text_color=main_tema.button_text,
		width=40,
		command=info_fonk)
	info_button.place(
		x=info_button_konum.x,
		y=info_button_konum.y)

	kisayol_button = ctk.CTkButton(window,
		text="Kısayollar",
		fg_color=main_tema.genel,
		text_color=main_tema.button_text,
		width=40,
		command=kisayol_fonk)
	kisayol_button.place(
		x=kisayol_button_konum.x,
		y=kisayol_button_konum.y)

	tema_button = ctk.CTkButton(window,
		text="Temalar",
		fg_color=main_tema.genel,
		text_color=main_tema.button_text,
		width=40,
		command=tema_fonk)
	tema_button.place(
		x=tema_button_konum.x,
		y=tema_button_konum.y)

	yazi_paneli = ctk.CTkTextbox(window,
		height=570,
		width=860,
		fg_color=main_tema.yazi_panel,
		text_color=main_tema.yazi_paneli_text,
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
		text_color=main_tema.sayfa_numarasi_text)
	sayfa_numarasi.place(x=sayfa_numarasi_konum.x,y=sayfa_numarasi_konum.y)

	kayit_bildirim = ctk.CTkLabel(window,
		text="Kayıt edildi!",
		font=("italic",21),
		text_color=main_tema.kayit_bildirim_text)

	kayit_button = ctk.CTkButton(window,
		text="Kaydet",
		fg_color=main_tema.genel,
		text_color=main_tema.button_text,
		width=40,
		font=("italic",21),
		command=kayit_fonk)
	kayit_button.place(
		x=kayit_button_konum.x,
		y=kayit_button_konum.y,)

	for sayfa_index in range(1, 101):
		def sayfa_button_fonk(page_num):
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
				except:
					yazi_paneli.delete("1.0", "end")

				sayfa_numarasi.configure(text=f"Sayfa {page_num}")
				print(f"sayfa: {sayfa_oku()}")

			return page_fonk

		sayfa_button = ctk.CTkButton(not_paneli,
				text=f"Sayfa {sayfa_index}",
				fg_color=main_tema.sayfalar,
				text_color=main_tema.sayfa_text,
				width=500,height=50,
				command=sayfa_button_fonk(sayfa_index))
		sayfa_button.pack(pady=7)

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
	print(baslangic_ve_bittis_cizgisi)
	defter_program()
	while Yeniden_baslatma_islemi:
		defter_program()
	print(baslangic_ve_bittis_cizgisi)
