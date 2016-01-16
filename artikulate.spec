%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Pronunciation trainer application for KDE
Name:		artikulate
Version:	15.12.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(QtGStreamer-1.0)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(Qt5GStreamer)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:	cmake(Qt5XmlPatterns)
BuildRequires:	cmake(Qt5QuickWidgets)

Requires:	kqtquickcharts

%description
Artikulate is a pronunciation trainer that aims at improving and perfecting
the pronunciation skills of the user.

%files
%doc COPYING*
%{_kde5_bindir}/artikulate_editor
%{_kde5_bindir}/artikulate
%{_kde5_applicationsdir}/org.kde.artikulate.desktop
%{_sysconfdir}/xdg/artikulate.knsrc
%{_kde5_datadir}/config.kcfg//artikulate.kcfg
%{_kde5_datadir}/artikulate/images/*.png
%{_kde5_datadir}/artikulate/languages/*.xml
%{_kde5_datadir}/artikulate/qml/*.qml
%{_kde5_datadir}/artikulate/schemes/*.xsd
%{_kde5_datadir}/artikulate/sounds/*.ogg
%{_kde5_docdir}/HTML/en/artikulate/
%{_kde5_iconsdir}/hicolor/*/*/artikulate*.*
%{_kde5_datadir}/appdata/org.kde.artikulate.appdata.xml


#----------------------------------------------------------------------------
%define core_major 0
%define libartikulatecore %mklibname artikulatecore %{core_major}

%package -n %{libartikulatecore}
Summary:	Runtime library for Artikulate
Group:		System/Libraries

%description -n %{libartikulatecore}
Runtime library for Artikulate.

%files -n %{libartikulatecore}
%{_kde5_libdir}/libartikulatecore.so.%{core_major}*

#----------------------------------------------------------------------------

%define profile_major 0
%define libartikulatelearnerprofile %mklibname artikulatelearnerprofile %{profile_major}

%package -n %{libartikulatelearnerprofile}
Summary:	Runtime library for Artikulate
Group:		System/Libraries

%description -n %{libartikulatelearnerprofile}
Runtime library for Artikulate.

%files -n %{libartikulatelearnerprofile}
%{_kde5_libdir}/libartikulatelearnerprofile.so.%{profile_major}*

#----------------------------------------------------------------------------

%define sound_major 0
%define libartikulatesound %mklibname artikulatesound %{sound_major}

%package -n %{libartikulatesound}
Summary:	Runtime library for Artikulate
Group:		System/Libraries

%description -n %{libartikulatesound}
Runtime library for Artikulate.

%files -n %{libartikulatesound}
%{_kde5_libdir}/libartikulatesound.so.%{sound_major}*

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# We don't have devel package so drop .so
rm %{buildroot}/%{_kde5_libdir}/libartikulate*.so
