# Force out of source build
%undefine __cmake_in_source_build

# Installed library version
%global lib_version 2103.0.1

Name:           abseil-cpp
Version:        20210324.2
Release:        1
Summary:        C++ Common Libraries

License:        ASL 2.0
URL:            https://abseil.io
Source0:        https://github.com/abseil/abseil-cpp/archive/%{version}/%{name}-%{version}.tar.gz

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
* Wed Jun 23 2021 gaihuiying <gaihuiying1@huawei.com> - 20210324.2-1
- package init
