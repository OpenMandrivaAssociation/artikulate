%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Pronunciation trainer application for KDE
Name:		artikulate
Version:	15.08.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(QtGStreamer-1.0)
Requires:	kqtquickcharts

%description
Artikulate is a pronunciation trainer that aims at improving and perfecting
the pronunciation skills of the user.

%files
%doc COPYING*
%{_kde_bindir}/artikulate
%{_kde_appsdir}/artikulate/
%{_kde_appsdir}/artikulateui.rc
%{_kde_applicationsdir}/artikulate.desktop
%{_kde_configdir}/artikulate.knsrc
%{_kde_datadir}/config.kcfg//artikulate.kcfg
%{_kde_docdir}/HTML/en/artikulate/
%{_kde_iconsdir}/hicolor/*/*/artikulate*.*
%{_datadir}/appdata/artikulate.appdata.xml

#----------------------------------------------------------------------------

%define core_major 4
%define libartikulatecore %mklibname artikulatecore %{core_major}

%package -n %{libartikulatecore}
Summary:	Runtime library for Artikulate
Group:		System/Libraries

%description -n %{libartikulatecore}
Runtime library for Artikulate.

%files -n %{libartikulatecore}
%{_kde_libdir}/libartikulatecore.so.%{core_major}*

#----------------------------------------------------------------------------

%define profile_major 4
%define libartikulatelearnerprofile %mklibname artikulatelearnerprofile %{profile_major}

%package -n %{libartikulatelearnerprofile}
Summary:	Runtime library for Artikulate
Group:		System/Libraries

%description -n %{libartikulatelearnerprofile}
Runtime library for Artikulate.

%files -n %{libartikulatelearnerprofile}
%{_kde_libdir}/libartikulatelearnerprofile.so.%{profile_major}*

#----------------------------------------------------------------------------

%define sound_major 4
%define libartikulatesound %mklibname artikulatesound %{sound_major}

%package -n %{libartikulatesound}
Summary:	Runtime library for Artikulate
Group:		System/Libraries

%description -n %{libartikulatesound}
Runtime library for Artikulate.

%files -n %{libartikulatesound}
%{_kde_libdir}/libartikulatesound.so.%{sound_major}*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

# We don't have devel package so drop .so
rm %{buildroot}%{_kde_libdir}/libartikulate*.so
