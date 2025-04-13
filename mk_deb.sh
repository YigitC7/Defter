#!/bin/bash

# Değişkenler
PACKAGE_NAME="defter"  # Paket isimleri genellikle küçük harfli olur
PACKAGE_VERSION="6.0"
PACKAGE_DIR="$PACKAGE_NAME-$PACKAGE_VERSION"

# Paket dizinlerini oluştur
mkdir -p "$PACKAGE_DIR/DEBIAN"
mkdir -p "$PACKAGE_DIR/usr/bin"
mkdir -p "$PACKAGE_DIR/usr/share/icons/hicolor/512x512/apps"  # 512x512 boyutu için
mkdir -p "$PACKAGE_DIR/usr/share/applications"

# Kontrol dosyasını oluştur
cat << EOF > "$PACKAGE_DIR/DEBIAN/control"
Package: $PACKAGE_NAME
Version: $PACKAGE_VERSION
Section: utils
Priority: optional
Architecture: amd64
Depends: libgtk-3-0, libwebkit2gtk-4.0-37
Maintainer: YigitC7 <yigitcitak.1817@gmail.com>
Description: Sayfalar halinde not tutmanın en güvenli yolu!
EOF

# Masaüstü dosyasını oluştur
cat << EOF > "$PACKAGE_DIR/usr/share/applications/$PACKAGE_NAME.desktop"
[Desktop Entry]
Version=$PACKAGE_VERSION
Type=Application
Name=Defter
Exec=/usr/bin/Defter
Icon=$PACKAGE_NAME
Terminal=false
Categories=Utility;Application;
EOF

# Dosyaları yerleştirme
cp -r dist/Defter "$PACKAGE_DIR/usr/bin/Defter"
chmod +x "$PACKAGE_DIR/usr/bin/Defter"  # Çalıştırma izni ver
cp -f img/icon.png "$PACKAGE_DIR/usr/share/icons/hicolor/512x512/apps/$PACKAGE_NAME.png"

# Ek ikon boyutları için gerekirse symbolic link oluşturabilirsiniz
# Örneğin 128x128 için:
mkdir -p "$PACKAGE_DIR/usr/share/icons/hicolor/128x128/apps"
ln -s "../../512x512/apps/$PACKAGE_NAME.png" "$PACKAGE_DIR/usr/share/icons/hicolor/128x128/apps/$PACKAGE_NAME.png"

# Deb paketi oluştur
dpkg-deb --build "$PACKAGE_DIR"

echo "Dizin yapısı oluşturuldu: $PACKAGE_DIR"
echo "Defter deb paketi oluşturuldu: ${PACKAGE_DIR}.deb"
