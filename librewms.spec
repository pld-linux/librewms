Summary:	WMS viewer built on the top of RasterLite2
Summary(pl.UTF-8):	Przeglądarka WMS zbudowana w oparciu o RasterLite2
Name:		librewms
Version:	1.0.0a
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://www.gaia-gis.it/gaia-sins/librewms-sources/%{name}-%{version}.tar.gz
# Source0-md5:	883d7240890747630b40e58ec0500180
URL:		https://www.gaia-gis.it/fossil/librewms
BuildRequires:	librasterlite2-devel
BuildRequires:	libspatialite-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	wxGTK2-unicode-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibreWMS is an open source Geography application built on top of
SpatiaLite and RasterLite2. It's basically simple and really
light-weight, but it's an almost complete WMS 1.3.0 interactive GUI
client.

%description -l pl.UTF-8
LibreWMS to mająca otwarte źródła aplikacja geograficzna zbudowana w
oparciu o biblioteki SpatiaLite i RasterLite2. Jest zasadniczo prosta
i naprawdę lekka, ale jest prawie kompletnym graficznym, interaktywnym
klientem WMS 1.3.0.

%prep
%setup -q

%build
%configure \
	--with-wxconfig=/usr/bin/wx-gtk2-unicode-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
sed -ne '2,$p' gnome_resource/LibreWMS.desktop >$RPM_BUILD_ROOT%{_desktopdir}/LibreWMS.desktop
cp -p gnome_resource/LibreWMS.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS 
%attr(755,root,root) %{_bindir}/LibreWMS
%{_desktopdir}/LibreWMS.desktop
%{_pixmapsdir}/LibreWMS.png
