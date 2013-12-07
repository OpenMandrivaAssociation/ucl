%define lib_major 1
%define lib_name %mklibname %name %{lib_major}
%define develname %mklibname -d %name

# virtual package to enforce naming convention

Summary:	The UCL Compression Library
Name:		ucl
Version:	1.03
Release:	12
License:	GPL
Group:		System/Libraries
URL:		http://www.oberhumer.com/opensource/ucl/
Source0:	http://www.oberhumer.com/opensource/ucl/download/%name-%version.tar.bz2

%description
UCL implements a number of algorithms with the following features:
- Decompression is simple and *very* fast. 
- Requires no memory for decompression. 
- The decompressors can be squeezed into less than 200 bytes of code. 
- Focuses on compression levels for generating pre-compressed data which
  achieve a quite competitive compression ratio. 
- Allows you to dial up extra compression at a speed cost in the compressor.
  The speed of the decompressor is not reduced. 
- Algorithm is thread safe. 
- Algorithm is lossless. 
UCL supports in-place decompression.


# main package (contains *.so.[major].* only)

%package -n	%{lib_name}
Summary:	The UCL Compression Library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{lib_name}
UCL implements a number of algorithms with the following features:
- Decompression is simple and *very* fast. 
- Requires no memory for decompression. 
- The decompressors can be squeezed into less than 200 bytes of code. 
- Focuses on compression levels for generating pre-compressed data which
  achieve a quite competitive compression ratio. 
- Allows you to dial up extra compression at a speed cost in the compressor.
  The speed of the decompressor is not reduced. 
- Algorithm is thread safe. 
- Algorithm is lossless. 
UCL supports in-place decompression.

This package contains the library needed to run programs dynamically
linked with %{name}.


# devel part of the bundle

%package -n	%{develname}
Summary:	The UCL Compression Library - development environment
Group:		Development/C
Requires:	%{lib_name} = %{version}-%release
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}ucl1-devel < 1.03-8

%description -n	%{develname}
UCL implements a number of algorithms with the following features:
- Decompression is simple and *very* fast. 
- Requires no memory for decompression. 
- The decompressors can be squeezed into less than 200 bytes of code. 
- Focuses on compression levels for generating pre-compressed data which
  achieve a quite competitive compression ratio. 
- Allows you to dial up extra compression at a speed cost in the compressor.
  The speed of the decompressor is not reduced. 
- Algorithm is thread safe. 
- Algorithm is lossless. 
UCL supports in-place decompression.

Install %{name} if you need to compile an application with %{lib_name}
support.

%prep 

%setup -q 

%build
%configure2_5x --enable-shared
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{lib_name}
%defattr(-,root,root)
%doc COPYING INSTALL NEWS README THANKS TODO
%{_libdir}/*.so.*

%files  -n %{develname}
%defattr(-,root,root)
%doc COPYING INSTALL NEWS README THANKS TODO
%{_libdir}/*.a
%{_libdir}/*.so
%dir %{_includedir}/ucl/
%{_includedir}/ucl/*.h




%changelog
* Sun Jun 05 2011 Funda Wang <fwang@mandriva.org> 1.03-8mdv2011.0
+ Revision: 682756
- rebuild

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.03-7mdv2010.0
+ Revision: 434493
- rebuild
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.03-5mdv2009.0
+ Revision: 255037
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.03-3mdv2008.1
+ Revision: 140924
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Dec 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.03-3mdv2007.0
+ Revision: 94911
- rebuild
- Import ucl

* Mon Dec 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.03-2mdv2007.1
- rebuild

* Sun Oct 03 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.03-1mdk
- New release 1.03

* Thu Jul 01 2004 Götz Waschk <waschk@linux-mandrake.com> 1.02-1mdk
- major 1
- source URL
- New release 1.02

