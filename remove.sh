if [[ "${UID}" != 0 ]] ; then
	echo -e "Lütfen bu scripti yönetici olarak çalıştırın: \n\tsudo bash ./notifcat.sh --install"
	exit 1
fi
rm -rf /usr/share/defter
rm -rf /usr/share/pixmaps/defter.png
rm -rf /usr/share/applications/Defter.desktop
clear
echo -e "\e[1;34mDefter Programı Kaldırılmıştır\033[0m"
