Summary:	Library for 1394 Digital Camera Specification
Name:		libdc1394
Version:	2.1.3
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://heanet.dl.sourceforge.net/libdc1394/%{name}-%{version}.tar.gz
# Source0-md5:	d8b2cbfae1b329fdeaa638da80427334
Patch0:		%{name}-usb_init.patch
Patch1:		%{name}-videodev-fix.patch
URL:		http://sourceforge.net/projects/libdc1394/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libraw1394-devel
BuildRequires:	libtool
BuildRequires:	libusbx-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdc1394 is a library that is intended to provide a high level
programming interface for application developers who wish to control
IEEE 1394 based cameras that conform to the 1394-based Digital Camera
Specification (found at http://www.1394ta.org/).

%package devel
Summary:	libdc1394 header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libdc1394 header files.

%prep
%setup -q
%patch0 -p2
%patch1 -p2

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/libdc1394.so.??
%attr(755,root,root) %{_libdir}/libdc1394.so.*.*.*
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdc1394.so
%{_libdir}/libdc1394.la
%{_includedir}/dc1394
%{_pkgconfigdir}/*.pc

