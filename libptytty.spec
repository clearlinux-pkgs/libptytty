#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v12
# autospec commit: 381dfd8
#
Name     : libptytty
Version  : 2.0
Release  : 1
URL      : http://dist.schmorp.de/libptytty/libptytty-2.0.tar.gz
Source0  : http://dist.schmorp.de/libptytty/libptytty-2.0.tar.gz
Summary  : OS independent and secure pty/tty and utmp/wtmp/lastlog handling
Group    : Development/Tools
License  : GPL-2.0
Requires: libptytty-lib = %{version}-%{release}
Requires: libptytty-license = %{version}-%{release}
BuildRequires : buildreq-cmake
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
libptytty - OS independent and secure pty/tty and utmp/wtmp/lastlog
handling

%package dev
Summary: dev components for the libptytty package.
Group: Development
Requires: libptytty-lib = %{version}-%{release}
Provides: libptytty-devel = %{version}-%{release}
Requires: libptytty = %{version}-%{release}

%description dev
dev components for the libptytty package.


%package lib
Summary: lib components for the libptytty package.
Group: Libraries
Requires: libptytty-license = %{version}-%{release}

%description lib
lib components for the libptytty package.


%package license
Summary: license components for the libptytty package.
Group: Default

%description license
license components for the libptytty package.


%prep
%setup -q -n libptytty-2.0
cd %{_builddir}/libptytty-2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719347255
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1719347255
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libptytty
cp %{_builddir}/libptytty-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libptytty/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libptytty.h
/usr/lib64/libptytty.so
/usr/lib64/pkgconfig/libptytty.pc
/usr/share/man/man3/libptytty.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libptytty.so.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libptytty/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
