if [[ "${UID}" != 0 ]] ; then
	echo -e "Lütfen bu scripti yönetici olarak çalıştırın: \n\tsudo bash ./remove.sh"
	exit 1
fi
sudo rm -rf /usr/local/bin/defter
sudo rm -rf /usr/share/pixmaps/defter.png
sudo rm -rf /usr/share/applications/Defter.desktop
clear
echo -e "\e[1;34mDefter Programı Kaldırılmıştır\033[0m"
