# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0

Name:           seatd
Version:        0.9.1
Release:        %autorelease
Summary:        Minimal seat management daemon
License:        MIT
URL:            https://sr.ht/~kennylevinsen/seatd/
VCS:            git:https://git.sr.ht/~kennylevinsen/seatd
#!RemoteAsset
Source0:        https://git.sr.ht/~kennylevinsen/seatd/archive/%{version}.tar.gz
Source1:        seatd.sysusers
BuildSystem:    meson

BuildOption(conf):  -Dlibseat-logind=systemd
BuildOption(conf):  -Dserver=enabled

%if %{with doc}
BuildOption(conf):  -Dman-pages=enabled
%else
BuildOption(conf):  -Dman-pages=disabled
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd-rpm-macros

%if %{with doc}
BuildRequires:  pkgconfig(scdoc)
%endif

%description
A seat management daemon, that does everything it needs to do.
Nothing more, nothing less. Depends only on libc.

%package     -n libseat
Summary:        Universal seat management library

%description -n libseat
A seat management library allowing applications to use whatever seat
management is available.

%package     -n libseat-devel
Summary:        Development files for libseat
Requires:       libseat = %{version}-%{release}

%description -n libseat-devel
The libseat-devel package contains libraries and header files for
developing applications that use libseat.

%install -a

install -D -m 0644 -pv contrib/systemd/%{name}.service \
    %{buildroot}%{_unitdir}/%{name}.service

install -D -m 0644 -pv %{SOURCE1} \
    %{buildroot}%{_sysusersdir}/%{name}.conf

%pre
%sysusers_create_package seatd %{SOURCE1}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files -n libseat
%license LICENSE
%doc README.md
%{_libdir}/libseat.so.*

%files -n libseat-devel
%{_includedir}/libseat.h
%{_libdir}/libseat.so
%{_libdir}/pkgconfig/libseat.pc

%files
%license LICENSE
%doc README.md
%{_bindir}/seatd
%{_bindir}/seatd-launch
%if %{with doc}
%{_mandir}/man1/seatd.1*
%{_mandir}/man1/seatd-launch.1*
%endif
%{_sysusersdir}/seatd.conf
%{_unitdir}/seatd.service

%changelog
%{?autochangelog}
