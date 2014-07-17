Summary:	Pronunciation trainer application for KDE
Name:		artikulate
Version:	4.13.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		artikulate-4.13.2-cmake-qtmobility.patch
BuildRequires:	boost-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(QtGStreamer-0.10)
BuildRequires:	pkgconfig(QtMultimediaKit)
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
%{_kde_docdir}/HTML/en/artikulate/
%{_kde_configdir}/artikulate.knsrc
%{_kde_datadir}/config.kcfg//artikulate.kcfg
%{_kde_iconsdir}/hicolor/*/*/artikulate*.*

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

%prep
%setup -q
%patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

# We don't have devel package so drop .so
rm %{buildroot}%{_kde_libdir}/libartikulate*.so

