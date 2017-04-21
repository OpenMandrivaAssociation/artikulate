%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Pronunciation trainer application for KDE
Name:		artikulate
Version:	17.04.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:	cmake(Qt5Multimedia)
Requires:	kqtquickcharts

%description
Artikulate is a pronunciation trainer that aims at improving and perfecting
the pronunciation skills of the user.

%files -f artikulate.lang
%doc COPYING*
%{_kde5_bindir}/artikulate_editor
%{_kde5_bindir}/artikulate
%{_kde5_applicationsdir}/org.kde.artikulate.desktop
%{_sysconfdir}/xdg/artikulate.knsrc
%{_kde5_datadir}/config.kcfg//artikulate.kcfg
%{_kde5_datadir}/artikulate/images/*.png
%{_kde5_datadir}/artikulate/languages/*.xml
%{_kde5_datadir}/artikulate/schemes/*.xsd
%{_kde5_datadir}/artikulate/sounds/*.ogg
%{_kde5_iconsdir}/hicolor/*/*/*artikulate*.*
%{_datadir}/metainfo/org.kde.artikulate.appdata.xml
%{_libdir}/qt5/plugins/artikulate/libsound/*.so
%doc %{_kde5_docdir}/HTML/en/artikulate/
%doc %lang(ca) %{_kde5_docdir}/HTML/ca/artikulate 
%doc %lang(de) %{_kde5_docdir}/HTML/de/artikulate 
%doc %lang(es) %{_kde5_docdir}/HTML/es/artikulate 
%doc %lang(et) %{_kde5_docdir}/HTML/et/artikulate 
%doc %lang(nl) %{_kde5_docdir}/HTML/nl/artikulate 
%doc %lang(pt_BR) %{_kde5_docdir}/HTML/pt_BR/artikulate 
%doc %lang(sv) %{_kde5_docdir}/HTML/sv/artikulate 
%doc %lang(uk) %{_kde5_docdir}/HTML/uk/artikulate 


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

%find_lang artikulate

# We don't have devel package so drop .so
rm %{buildroot}/%{_kde5_libdir}/libartikulate*.so
