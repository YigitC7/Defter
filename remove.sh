if [[ "${UID}" != 0 ]] ; then
	echo -e "Lütfen bu scripti yönetici olarak çalıştırın: \n\tsudo bash ./notifcat.sh --install"
	exit 1
fi
rm -rf install/Defter.py /usr/share/defter
rm -rf install/defter.png /usr/share/pixmaps/
rm -rf install/Defter.desktop /usr/share/applications/
clear
echo -e "\e[1;34mDefter Programı Kaldırılmıştır\033[0m"
