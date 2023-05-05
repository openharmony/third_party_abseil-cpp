# Force out of source build
%undefine __cmake_in_source_build

# Installed library version
%global lib_version 2206.0.0

Name:           abseil-cpp
Version:        20220623.1
Release:        3
Summary:        C++ Common Libraries

License:        ASL 2.0
URL:            https://abseil.io
Source0:        https://github.com/abseil/abseil-cpp/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:         backport-Do-not-leak-maes-msse4.1-into-pkgconfig.patch
Patch1:         abseil-cpp-20210324.2-sw.patch
%ifarch loongarch64
Patch100:	0001-add-loongarch-suopport-for-abseil-cpp.patch
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%description
Abseil is an open-source collection of C++ library code designed to augment
the C++ standard library. The Abseil library code is collected from
Google's own C++ code base, has been extensively tested and used in
production, and is the same code we depend on in our daily coding lives.

In some cases, Abseil provides pieces missing from the C++ standard; in
others, Abseil provides alternatives to the standard for special needs we've
found through usage in the Google code base. We denote those cases clearly
within the library code we provide you.

Abseil is not meant to be a competitor to the standard library; we've just
found that many of these utilities serve a purpose within our code base,
and we now want to provide those resources to the C++ community as a whole.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts: grpc < 1.31.0-5

%description devel
Development headers for %{name}

%prep
%autosetup -p1

%build
%cmake

%install
%make_install

%files
%license LICENSE
%doc FAQ.md README.md UPGRADES.md
%{_libdir}/libabsl_*.so.%{lib_version}

%files devel
%{_includedir}/absl
%{_libdir}/cmake/absl
%{_libdir}/libabsl_*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon Nov 14 2022 Wenlong Zhang <zhangwenlong@loongson.cn> - 20220623.1-3
- add loongarch support for abseil-cpp

* Fri Nov 11 2022 wuzx<wuzx1226@qq.com> - 20220623.1-2
- Type:feature
- CVE:NA
- SUG:NA
- DESC:Add sw64 architecture

* Wed Nov 02 2022 xinghe <xinghe2@h-partners.com> - 20220623.1-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: update to 20220623.1

* Wed Jun 23 2021 gaihuiying <gaihuiying1@huawei.com> - 20210324.2-1
- package init
