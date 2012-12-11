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
BuildRequires:	tetex-latex

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



%changelog
* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 0.5.20-12mdv2011.0
+ Revision: 571829
- BR bin/latex
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Dec 06 2008 Adam Williamson <awilliamson@mandriva.org> 0.5.20-11mdv2009.1
+ Revision: 311052
- rebuild for new tcl
- don't package COPYING
- new license policy
- spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.5.20-9mdv2009.0
+ Revision: 255276
- rebuild

* Thu Mar 13 2008 Andreas Hasenack <andreas@mandriva.com> 0.5.20-7mdv2008.1
+ Revision: 187628
- rebuild for 2008.1

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 0.5.20-6mdv2008.0
+ Revision: 69962
- fix build
- use %%mkrel


* Wed Jan 04 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.20-5mdk
- rebuilt against soname aware deps (tcl/tk)
- fix deps

* Tue May 10 2005 Nicolas Chipaux <chipaux@mandriva.com> 0.5.20-4mdk
- Fix patch name
- Add BuildRequires

* Tue May 03 2005 Nicolas Chipaux <chipaux@mandriva.com> 0.5.20-3mdk
- Fix doc build on x86_64

* Thu Oct 28 2004 Laurent culioli <laurent@mandrake.org> 0.5.20-2mdk
- add libuu.a

* Mon Apr 19 2004 Michael Scherer <misc@mandrake.org> 0.5.20-1mdk 
- 0.5.20
- enhance Description
- rpmbuildupdate aware

* Wed Apr 09 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.5.18-2mdk
- rebuild ( dependencies )

* Sat Jan 11 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.5.18-1mdk
- 0.5.18

* Wed Mar 27 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.5.17-1mdk
- 0.5.17

* Wed Sep 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.5.15-1mdk
- 0.5.15

* Wed Feb 14 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.5.13-4mdk
- rebuild

* Thu Oct 05 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.5.13-3mdk
- used - even if i'm sux ;) - the srpm from Alexander Skwar <ASkwar@linux-mandrake.com> :
	Wed Oct  4 2000 Alexander Skwar <ASkwar@Linux-Mandrake.com> 0.5.13-3mdk
	- Ever wondered why the binary package is so small?  Well, some of us may
	like to have the executable, dunno about you.... (lenny sux)

* Tue Sep 19 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.5.13-2mdk
- bm & macros

* Tue Jun 13 2000 John Johnson <jjohnson@linux-mandrake.com> 0.5.13-1mdk
- Made Mandrake rpm

