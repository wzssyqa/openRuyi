# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap_complete_nushell
%global full_version 4.5.8
%global pkgname clap-complete-nushell-4.0

Name:           rust-clap-complete-nushell-4.0
Version:        4.5.8
Release:        %autorelease
Summary:        Rust crate "clap_complete_nushell"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap
#!RemoteAsset:  sha256:0a0c951694691e65bf9d421d597d68416c22de9632e884c28412cb8cd8b73dce
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(clap-4.0/std) >= 4.6.1
Requires:       crate(clap-complete-4.0/default) >= 4.5.58
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "clap_complete_nushell"

%package     -n %{name}+unstable-shell-tests
Summary:        Generator library used with clap for Nushell completion scripts - feature "unstable-shell-tests"
Requires:       crate(%{pkgname})
Requires:       crate(completest-0.4/default) >= 0.4.0
Requires:       crate(completest-nu-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/unstable-shell-tests)

%description -n %{name}+unstable-shell-tests
This metapackage enables feature "unstable-shell-tests" for the Rust clap_complete_nushell crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
