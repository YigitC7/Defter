if [[ "${UID}" != 0 ]] ; then
	echo -e "Lütfen bu scripti yönetici olarak çalıştırın: \n\tsudo bash ./install.sh"
	exit 1
fi
if ! command -v pip && ! command -v venv
then
    	clear
    	echo -e "\033[1;31m
Pip3 sisteminizde bulunamadı!\033[1;33m
Gerekli araçların kurulumu için python3-pip paketi gereklidir :)

\033[1;31mPip3 Kurulumu:
\033[1;36m
Debian/Ubuntu
→ sudo apt install python3-pip
\033[1;32m
Arch Linux
→ sudo pacman -S python3-pip
\033[1;36m
Fedora
→ sudo yum install python3-pip\033[0m
"
exit 1
fi
python3 -m venv lib # Pip için venv denilen bir araç kullanıyorum çünkü çoğu dağıtımlarda pip çalışmıyor.
source lib/bin/activate
pip install tkinter customtkinter pyinstaller
pyinstaller --noconsole --onefile install/Defter.py # Programı derliyorum çünkü bunu yorumlamak için sürekli venv ektif etmeye gerek kalmasın.
mkdir /usr/share/defter
cp -r install/dist/Defter /usr/share/defter
cp -r install/defter.png /usr/share/pixmaps/
cp -r install/Defter.desktop /usr/share/applications/
clear
echo -e "\e[1;34mDefter Sisteminize Yüklendi\033[0m"
