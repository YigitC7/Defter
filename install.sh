if [[ "${UID}" != 0 ]] ; then
	echo -e "Lütfen bu scripti yönetici olarak çalıştırın: \n\tsudo bash ./notifcat.sh --install"
	exit 1
fi
pip3 install tkinter customtkinter
mkdir /usr/share/defter
cp -r install/Defter.py /usr/share/defter
cp -r install/defter.png /usr/share/pixmaps/
cp -r install/Defter.desktop /usr/share/applications/
clear
echo -e "\e[1;34mDefter Sisteminize Yüklendi\033[0m"
