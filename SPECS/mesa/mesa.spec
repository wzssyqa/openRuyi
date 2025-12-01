# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Icenowy Zheng <uwu@icenowy.me>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Mesa contains some features not applicable to Linux that must be disabled
%global __meson_auto_features disabled

Name:           mesa
Summary:        The Mesa 3D graphics library
Version:        25.3.0
Release:        %autorelease
License:        MIT
URL:            https://mesa3d.org/
VCS:            git:https://gitlab.freedesktop.org/mesa/mesa
#!RemoteAsset
Source:         https://archive.mesa3d.org/mesa-%{version}.tar.xz
BuildSystem:    meson

# TODO: enable real drivers / window systems support - Icenowy
BuildOption(conf):  -Degl=disabled
BuildOption(conf):  -Dglx=disabled
BuildOption(conf):  -Dgbm=enabled
BuildOption(conf):  -Dgallium-drivers=
BuildOption(conf):  -Dvulkan-drivers=
BuildOption(conf):  -Dplatforms=
BuildOption(conf):  -Dxmlconfig=disabled

BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-mako
BuildRequires:  python3-PyYAML
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libdrm)

%description
Mesa is a 3D graphics library containing implementation of OpenGL (along with
related APIs such as OpenGL ES / EGL), Vulkan and some other arbitary
acceleration APIs (e.g. libva).

%package     -n libgbm
Summary:        The GBM buffer management library

%description -n libgbm
GBM is a graphics buffer management library mainly for allocating graphics
buffers without the invocation of window systems (useful for display servers
themselves, headless multiple-application graphics acceleration, etc).

This package contains the libgbm entry point library, which just behaves as
a loader of different backends. Backends are provided by either Mesa or
other proprietary vendors.

%package     -n libgbm-devel
Summary:        Development files for libgbm
Requires:       libgbm = %{version}-%{release}

%description -n libgbm-devel
This package contains development files for libgbm, for either calling it or
implementing backends for it.

%files -n libgbm
%{_libdir}/libgbm.so.1*

%files -n libgbm-devel
%{_libdir}/libgbm.so
%{_includedir}/gbm.h
%{_includedir}/gbm_backend_abi.h
%{_libdir}/pkgconfig/gbm.pc

%changelog
%{?autochangelog}
