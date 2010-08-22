%define libname	%mklibname uu 

Name:           uudeview
Version:        0.5.20
Release:        %{mkrel 12}
License:	GPLv2+
Group:          File tools
Source:         http://www.fpx.de/fp/Software/UUDeview/download/%{name}-%{version}.tar.bz2 
Patch:		%{name}-%{version}-library.ltx.patch	
Patch1:		uudeview-0.5.20-fix-str-fmt.patch
URL:            http://www.fpx.de/fp/Software/UUDeview/
Summary:        Help to transmit binary files over the internet
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:  tcl-devel
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
%patch1 -p0

%build
CFLAGS="%{optflags}" LDFLAGS="%ldflags" ./configure --prefix=%{_prefix} --libdir=%{_libdir}

%make
( cd doc/; make )

%install
rm -rf %{buildroot}
%makeinstall

mkdir -p %{buildroot}%{_mandir}/man1
cp man/*.1 %{buildroot}%{_mandir}/man1/
rm -rf %{buildroot}%{_prefix}/man

mkdir -p %{buildroot}%{_libdir}/
mkdir -p %{buildroot}%{_includedir}/
cp uulib/libuu.a %{buildroot}%{_libdir}/
cp uulib/fptools.h uulib/uudeview.h uulib/uuint.h %{buildroot}%{_includedir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc HISTORY IAFA-PACKAGE README doc uudeview.lsm
%{_mandir}/man*/*
%{_bindir}/*

%files -n %{libname}-static-devel
%defattr(-,root,root)
%doc README doc/structure.tex doc/test.txt doc/td*
%{_libdir}/*
%{_includedir}/*

