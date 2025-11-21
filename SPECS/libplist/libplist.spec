# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:     libplist
Version:  2.7.0
Release:  %autorelease
Summary:  Library for manipulating Apple Binary and XML Property Lists

License:  LGPL-2.0-or-later
URL:      https://www.libimobiledevice.org/
VCS:      git:https://github.com/libimobiledevice/libplist
#!RemoteAsset
Source:   https://github.com/libimobiledevice/libplist/releases/download/%{version}/libplist-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  make
BuildOption(conf): --disable-static
BuildSystem:    autotools

%description
libplist is a library for manipulating Apple Binary and XML Property Lists

%package  devel
Summary:  Development package for libplist
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
%{name}, development headers and libraries.

%package  -n python3-libplist
Summary:  Python3 bindings for libplist
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3

%description -n python3-libplist
%{name}, python3 libraries and bindings.

%conf -p
export PYTHON_VERSION="3"

%files
%license COPYING.LESSER
%doc AUTHORS README.md
%{_bindir}/plistutil
%{_libdir}/libplist-2.0.so.*
%{_libdir}/libplist++-2.0.so.*
%{_mandir}/man1/plistutil.*

%files devel
%{_libdir}/pkgconfig/libplist-*.pc
%{_libdir}/pkgconfig/libplist++-*.pc
%{_libdir}/libplist-*.so
%{_libdir}/libplist++-*.so
%{_includedir}/plist

%files -n python3-libplist
%{python3_sitearch}/plist.so

%changelog
%{?autochangelog}
