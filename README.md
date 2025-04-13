

<div align="center">
	
# Defter
<img src="img/icon.png" alt="logo" width="128"/>

![Pyton GUI APP](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-1a1a1a?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-1e1e1e?logo=linux&logoColor=white&style=for-the-badge)
[![Codacity](https://img.shields.io/codacy/grade/bb3500c728344ef898cb6c66bc356f00?logo=codacy&logoColor=white&style=for-the-badge)](https://app.codacy.com/gh/YigitC7/Defter)

  <a>
    <img src="https://github.com/SabanGnc/SabanGnc/assets/139702707/cc75e47a-eda0-498f-bc38-1a9a3e6ea37c" alt="Github Stats" width="1200">
  </a>
  
</div>


![resim](img.png)

Bu bir not defteri programıdır. Sayfalar halinde not tutmanızı sağlar ve sadece Linux işletim sistemi için hazırlanmıştır. Yazdığınız notlar Benim geliştirdiğim şifreli bir veri tabaınında tutulur. Bu veri tabanı kullanıcı klasöründe .defter içinde bulunur.

## Kurulum

### İndrme
<a href="https://github.com/YigitC7/Defter/releases/download/6.0/Defter-6.0.deb">DEB pack indir</a>

### Manuel kurulum
```bash	
git clone https://github.com/YigitC7/Defter
cd Defter
python3 -m venv myev
source myev/bin/activate
pip install --upgrade pip
pip install customtkinter pyinstaller
pyinstaller --noconsole --onefile src/Defter.py
sudo mkdir /usr/local/bin/defter
sudo cp -r dist/Defter /usr/local/bin/defter/Defter
sudo cp -r img/icon.png /usr/share/pixmaps/defter.png
sudo cp -r install/Defter.desktop /usr/share/applications/
```
<p>Kaldırmak için</p>

```bash
sudo sh remove.sh
```

<br>

### Notların tutulduğu dizin içeriği

```
├──.defter\
       ├── end.yigit 
       ├── tema_index.yigit
       ├── texsize.yigit
       └── Notlar\
               ├── sayfa1.yigit
               ├── sayfa2.yigit
               ├── sayfa3.yigit
               ├── sayfa4.yigit
               ├── sayfa5.yigit
               ├── sayfa6.yigit
               ├── sayfa7.yigit
               ├── sayfa8.yigit
               ├── sayfa9.yigit
               ├── sayfa10.yigit
               ├── sayfa11.yigit
               └── sayfa12.yigit

```
```

end.yigit ──> En son kullanılan sayfa numarası yazar
tema_index.yigit ──> En son kullanılan tema numarası yazar
texsize.yigit ──> En son ayarlanan yazı boyutu yazar
sayfa1.yigit ──> Sayfa içeriği şifreli bir şekilde yazar

```
<br>

>Daha fazla ayrıntı için <a href="https://defter.netlify.app/">Web sitesini</a> ziyaret edin.
