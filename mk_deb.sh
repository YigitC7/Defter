#!/bin/bash

# Değişkenler
PACKAGE_NAME="Defter"
PACKAGE_VERSION="6.0"
PACKAGE_DIR="$PACKAGE_NAME-$PACKAGE_VERSION"

# Paket dizinlerini oluştur
mkdir -p "$PACKAGE_DIR/DEBIAN"
mkdir -p "$PACKAGE_DIR/usr/local/bin"
mkdir -p "$PACKAGE_DIR/usr/local/bin/defter"
mkdir -p "$PACKAGE_DIR/usr/share/icons"
mkdir -p "$PACKAGE_DIR/usr/local/share/applications"

# Kontrol dosyasını oluştur (boş)
cat << EOF > "$PACKAGE_DIR/DEBIAN/control"
Package: $PACKAGE_NAME
Version: $PACKAGE_VERSION
Section: utils
Priority: optional
Architecture: amd64
Depends: 
Maintainer: YigitC7 <yigitcitak.1817@gmail.com>
Description: Sayfalar halinde not tutmanın en güvenli yolu!
EOF

# Masaüstü dosyasını oluştur (boş)
cat << EOF > "$PACKAGE_DIR/usr/local/share/applications/$PACKAGE_NAME.desktop"
[Desktop Entry]
Version=6.0
Type=Application
Name=Defter
Exec=/usr/local/bin/defter/Defter
Icon=/usr/local/bin/defter/icon.png
Terminal=false
Categories=Utility;Application;
EOF

# Dosyaları yerleştirme
cp -r dist/Defter $PACKAGE_DIR/usr/local/bin/defter/Defter
cp -f img/icon.png $PACKAGE_DIR/usr/local/bin/defter/icon.png

# Deb yapmak
dpkg-deb --build $PACKAGE_DIR

echo "Dizin yapısı oluşturuldu: $PACKAGE_DIR"
echo "Defter deb paketi oluşturuldu"
