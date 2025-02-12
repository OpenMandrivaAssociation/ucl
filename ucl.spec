%define major 1
%define libname %mklibname %name %{major}
%define develname %mklibname -d %name
%define _disable_rebuild_configure 1
%define _disable_lto 1

# virtual package to enforce naming convention

Summary:	The UCL Compression Library
Name:		ucl
Version:	1.03
Release:	21
License:	GPL
Group:		System/Libraries
URL:		https://www.oberhumer.com/opensource/ucl/
Source0:	http://www.oberhumer.com/opensource/ucl/download/%{name}-%{version}.tar.gz
# https://dev.openwrt.org/browser/packages/libs/ucl/patches/002-missing-macros.patch?rev=24363&format=txt
Patch0:		002-missing-macros.patch

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

%package -n	%{libname}
Summary:	The UCL Compression Library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
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
Requires:	%{libname} = %{version}-%{release}
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

Install %{name} if you need to compile an application with %{libname}
support.

%prep 

%setup -q 
%autopatch -p1

%build
%configure --enable-shared
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files  -n %{develname}
%doc COPYING INSTALL NEWS README THANKS TODO
%{_libdir}/*.so
%dir %{_includedir}/ucl/
%{_includedir}/ucl/*.h
