if [[ "${UID}" != 0 ]] ; then
	echo -e "Lütfen bu scripti yönetici olarak çalıştırın: \n\tsudo bash ./install.sh"
	exit 1
fi
if ! command -v python3
then
    	clear
    	echo -e "\033[1;31m
Python3 sisteminizde bulunamadı!\033[1;33m
Gerekli araçların kurulumu için python3-pip paketi gereklidir :)

\033[1;31mPip3 Kurulumu:
\033[1;36m
Debian/Ubuntu
→ sudo apt install python3 python3-pip python3-venv
\033[1;32m
Arch Linux
→ sudo pacman -S python3 python3-pip
\033[1;36m
Fedora
→ sudo dnf install python3 python3-pip\033[0m
"
exit 1
fi
python3 -m venv myev # Pip için venv denilen bir araç kullanıyorum çünkü çoğu dağıtımlarda pip çalışmıyor.
source myev/bin/activate
pip install --upgrade pip
pip install tkinter
pip install customtkinter pyinstaller
pyinstaller --noconsole --onefile install/Defter.py # Programı derliyorum çünkü bunu yorumlamak için sürekli venv ektif etmeye gerek kalmasın.
sudo mkdir /usr/local/bin/defter
sudo cp -r dist/Defter /usr/local/bin/defter/Defter
sudo cp -r install/defter.png /usr/share/pixmaps/
sudo cp -r install/Defter.desktop /usr/share/applications/
clear
echo -e "\e[1;34mDefter 5.0 Sisteminize Yüklendi\033[0m"
