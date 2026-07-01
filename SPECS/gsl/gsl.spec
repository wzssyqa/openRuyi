# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define __install /var/lib/clang-wrap/install

Name:           gsl
Version:        2.8
Release:        %autorelease
Summary:        The GNU Scientific Library for numerical analysis
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/gsl/
VCS:            git:https://git.savannah.gnu.org/git/gsl.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/gsl/gsl-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --disable-static
BuildOption(conf):  CFLAGS="%{optflags} -ffp-contract=off"
BuildOption(conf):  CC=clang CXX=clang++

# https://lists.gnu.org/archive/html/bug-gsl/2026-05/msg00004.html
# Undefined behavior in gsl_pow_int
Patch0:         2000-Fix-undefined-behavior-in-gsl_pow_int.patch

BuildRequires:  pkgconfig
BuildRequires:  make
BuildRequires:  clang-wrap
BuildRequires:  llvm

%description
The GNU Scientific Library (GSL) is a collection of routines for
numerical analysis, written in C.

%package        devel
Summary:        Libraries and the header files for GSL development
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The gsl-devel package contains the header files necessary for
developing programs using the GSL (GNU Scientific Library).

%prep -a
%autosetup -p1

%conf -p
%ifarch riscv64
export EMIT_LLVMIR=-march=rva23u64
%elifarch x86_64
export EMIT_LLVMIR=-march=x86-64-v4
%else
export EMIT_LLVMIR=1
%endif
export PATH=/var/lib/clang-wrap:$PATH

%build -p
%ifarch riscv64
export EMIT_LLVMIR=-march=rva23u64
%elifarch x86_64
export EMIT_LLVMIR=-march=x86-64-v4
%else
export EMIT_LLVMIR=1
%endif
export PATH=/var/lib/clang-wrap:$PATH

%install -p
%ifarch riscv64
export EMIT_LLVMIR=-march=rva23u64
%elifarch x86_64
export EMIT_LLVMIR=-march=x86-64-v4
%else
export EMIT_LLVMIR=1
%endif
export PATH=/var/lib/clang-wrap:$PATH

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/gsl-histogram
%{_bindir}/../lib/llvmir-bin/gsl-histogram
%{_bindir}/../lib/llvmir-bin/gsl-histogram_cmd
%{_bindir}/gsl-randist
%{_bindir}/../lib/llvmir-bin/gsl-randist
%{_bindir}/../lib/llvmir-bin/gsl-randist_cmd
%{_libdir}/libgsl.so.28*
%{_libdir}/llvmir/libgsl.so.28*
%{_libdir}/libgslcblas.so.0*
%{_libdir}/llvmir/libgslcblas.so.0*
%{_mandir}/man1/gsl-histogram.1*
%{_mandir}/man1/gsl-randist.1*

%files devel
%{_bindir}/gsl-config
%{_libdir}/libgsl.so
%{_libdir}/libgslcblas.so
%{_libdir}/pkgconfig/gsl.pc
%{_mandir}/man1/gsl-config.1*
%{_mandir}/man3/gsl.3*
%{_infodir}/gsl-ref.info*
%{_datadir}/aclocal/gsl.m4
%{_includedir}/gsl/

%changelog
%{?autochangelog}
