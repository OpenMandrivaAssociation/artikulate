%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Pronunciation trainer application for KDE
Name:		artikulate
Version:	25.12.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildRequires:	boost-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	pkgconfig(libxml-2.0)
# Old libraries that have been removed while porting to Plasma 6
%define libartikulatecore %mklibname artikulatecore 0
%define libartikulatelearnerprofile %mklibname artikulatelearnerprofile 0
%define libartikulatesound %mklibname artikulatesound 0
Obsoletes:	%{libartikulatecore} < %{EVRD}
Obsoletes:	%{libartikulatelearnerprofile} < %{EVRD}
Obsoletes:	%{libartikulatesound} < %{EVRD}

%description
Artikulate is a pronunciation trainer that aims at improving and perfecting
the pronunciation skills of the user.

%files -f artikulate.lang
%doc COPYING*
%{_bindir}/artikulate_editor
%{_bindir}/artikulate
%{_datadir}/applications/org.kde.artikulate.desktop
%{_datadir}/knsrcfiles/artikulate.knsrc
%{_datadir}/config.kcfg//artikulate.kcfg
%{_datadir}/icons/hicolor/*/*/*artikulate*.*
%{_datadir}/metainfo/org.kde.artikulate.appdata.xml
# No point in splitting those into libpackages, nothing uses them
# and nothing can use them (no headers)
%{_libdir}/libartikulatecore.so.0
%{_libdir}/libartikulatelearnerprofile.so.0
