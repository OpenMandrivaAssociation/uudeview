%define name    uudeview
%define version 0.5.20
%define release %mkrel 7

%define libname %mklibname uu 

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:	GPL
Group:          File tools
Source:         http://www.fpx.de/fp/Software/UUDeview/download/%{name}-%{version}.tar.bz2 
Patch:		%{name}-%{version}-library.ltx.patch	
URL:            http://www.fpx.de/fp/Software/UUDeview/
Summary:        Help to transmit binary files over the internet
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:  tcl tcl-devel
BuildRequires:	transfig

%description
Uudeview handles uuencoding, xxencoding, and base-64 encoding (MIME),
used on internet to transmit binary files.
It can do automatic splitting of large encodes and automatic posting.
A must for anyone serious encoding/decoding.

%package -n     %{libname}-static-devel
Summary:        Static library for developing apps which will use %{name}
Group:          Development/C
Provides:       libuu-static-devel = %{version}-%{release}
Provides:       uu-static-devel = %{version}-%{release}

%description -n %{libname}-static-devel
Static library for %{name}

%prep

%setup -q

%patch -p0

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s ./configure --prefix=%{_prefix} --libdir=%_libdir

%make
( cd doc/; make )

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
cp man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1/
rm -rf $RPM_BUILD_ROOT/%_prefix/man

mkdir -p $RPM_BUILD_ROOT/%{_libdir}/
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/
cp uulib/libuu.a $RPM_BUILD_ROOT/%{_libdir}/
cp uulib/fptools.h uulib/uudeview.h uulib/uuint.h $RPM_BUILD_ROOT/%{_includedir}/

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc COPYING HISTORY IAFA-PACKAGE README doc uudeview.lsm
%{_mandir}/man*/*
%{_bindir}/*

%files -n %{libname}-static-devel
%defattr(-,root,root)
%doc COPYING README doc/structure.tex doc/test.txt doc/td*
%{_libdir}/*
%{_includedir}/*

