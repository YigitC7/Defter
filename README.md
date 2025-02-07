# Defter

Bu bir not defteri programıdır. Sayfalar halinde not tutmanızı sağlar ve sadece Linux işletim sistemi için hazırlanmıştır. yazdığınız notlar Benim geliştirdiğim şifreli bir veri tabaınında tutulur. Bu veri tabanı kullanıcı klasöründe .defter içinde bulunur.
<br>
<p>Kurulum ve daha fazla ayrıntı için <a href="https://defter.netlify.app/">Web sitesini</a> ziyaret edin.<p>
<br>
  
![kapak](img.png)
<br>
### Yeni bir kütüphane olan Customtkinter kullanır
  
```python
  import customtkinter as ctk

  window = ctk.CTk()
  window.title(baslik_turkce_optimasyon())
  window.minsize(1200, 750)
  window.maxsize(1200, 750)
  window.geometry("1200x750+500+100")  # 'x' yerine '+' kullanılmalı
  window.configure(fg_color=main_tema.window)
  window.resizable(False, False)

  window.mainloop()
```
<br>

### Bütün renk kodları düzenli şekilde yazılmıştır

```python
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
```

<br>

### Pencere nesneleri x ve y konumları düzenli olarak sınıflandırılmıştır

```python
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
```

