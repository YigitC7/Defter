#!/bin/bash

# Gerekli dosyaların ve bilgilerinin kontrolü
PROGRAM_NAME="Defter"
ICON_FILE="icon.png"

if [[ ! -f $PROGRAM_NAME || ! -f $ICON_FILE ]]; then
    echo "Hata: $PROGRAM_NAME veya $ICON_FILE bulunamadı!"
    exit 1
fi

# RPM yapılandırma dizinini oluştur
echo "RPM yapılandırma dizinleri oluşturuluyor..."
rpmdev-setuptree

# Dosyaları SOURCES dizinine kopyala
echo "Gerekli dosyalar kopyalanıyor..."
cp "$PROGRAM_NAME" ~/rpmbuild/SOURCES/
cp "$ICON_FILE" ~/rpmbuild/SOURCES/

# Spec dosyasını oluştur
SPEC_FILE=~/rpmbuild/SPECS/$PROGRAM_NAME.spec
echo "Spec dosyası oluşturuluyor: $SPEC_FILE"

cat > "$SPEC_FILE" << EOF
Name:           $PROGRAM_NAME
Version:        1.0
Release:        1%{?dist}
Summary:        $PROGRAM_NAME programı

License:        None
URL:            https://github.com/YigitC7
Source0:        $PROGRAM_NAME
Source1:        $ICON_FILE

BuildArch:      x86_64

%description
Bu, $PROGRAM_NAME adlı bir programdır.

%prep

%build

%install
# Yükleme dizinlerini oluştur
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/usr/share/icons

# Dosyaları kopyala
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/$PROGRAM_NAME
install -m 0644 %{SOURCE1} %{buildroot}/usr/share/icons/$PROGRAM_NAME.png

# Masaüstü girişini oluştur
cat > %{buildroot}/usr/share/applications/$PROGRAM_NAME.desktop << DESKTOP_ENTRY
[Desktop Entry]
Name=$PROGRAM_NAME
Exec=/usr/bin/$PROGRAM_NAME
Icon=/usr/share/icons/$PROGRAM_NAME.png
Type=Application
Categories=Utility;
DESKTOP_ENTRY

%files
/usr/bin/$PROGRAM_NAME
/usr/share/icons/$PROGRAM_NAME.png
/usr/share/applications/$PROGRAM_NAME.desktop

%changelog
* Sun Dec 22 2024 Yiğit Çıtak <yigitcitak.1817@gmail.com> - 1.0-1
- İlk sürüm.
EOF

# RPM paketini oluştur
echo "RPM paketi oluşturuluyor..."
rpmbuild -ba "$SPEC_FILE"

# Çıktı paketi bilgisi
OUTPUT_PACKAGE=~/rpmbuild/RPMS/x86_64/${PROGRAM_NAME}-1.0-1.x86_64.rpm
if [[ -f $OUTPUT_PACKAGE ]]; then
    echo "Paket başarıyla oluşturuldu: $OUTPUT_PACKAGE"
else
    echo "Paket oluşturulamadı!"
    exit 1
fi
