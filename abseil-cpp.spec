# Force out of source build
%undefine __cmake_in_source_build

# Installed library version
%global lib_version 2308.0.0

Name:           abseil-cpp
Version:        20230802.1
Release:        5
Summary:        C++ Common Libraries

License:        Apache-2.0
URL:            https://abseil.io
Source0:        https://github.com/abseil/abseil-cpp/archive/%{version}/%{name}-%{version}.tar.gz

Patch1:         abseil-cpp-20210324.2-sw.patch
Patch100:	0001-add-loongarch-suopport-for-abseil-cpp.patch
Patch101:       0002-PR-1644-unscaledcycleclock-remove-RISC-V-support.patch

BuildRequires:  cmake ninja-build
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
%cmake -S %{_vpath_srcdir} -B  %{_vpath_builddir} -GNinja \
      -DCMAKE_BUILD_TYPE:STRING=None \
      -DCMAKE_CXX_STANDARD:STRING=17 \
      -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed" \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo

%__cmake --build %{_vpath_builddir} %{?_smp_mflags} --verbose

%install
DESTDIR="%{buildroot}" %__cmake --install "%{_vpath_builddir}"

%files
%license LICENSE
%doc FAQ.md README.md UPGRADES.md
# All shared libraries except installed TESTONLY libraries; see the %%files
# list for the -testing subpackage for those.
%{_libdir}/libabsl_bad_any_cast_impl.so.%{lib_version}
%{_libdir}/libabsl_bad_optional_access.so.%{lib_version}
%{_libdir}/libabsl_bad_variant_access.so.%{lib_version}
%{_libdir}/libabsl_base.so.%{lib_version}
%{_libdir}/libabsl_city.so.%{lib_version}
%{_libdir}/libabsl_civil_time.so.%{lib_version}
%{_libdir}/libabsl_cord.so.%{lib_version}
%{_libdir}/libabsl_cord_internal.so.%{lib_version}
%{_libdir}/libabsl_cordz_functions.so.%{lib_version}
%{_libdir}/libabsl_cordz_handle.so.%{lib_version}
%{_libdir}/libabsl_cordz_info.so.%{lib_version}
%{_libdir}/libabsl_cordz_sample_token.so.%{lib_version}
%{_libdir}/libabsl_crc32c.so.%{lib_version}
%{_libdir}/libabsl_crc_cord_state.so.%{lib_version}
%{_libdir}/libabsl_crc_cpu_detect.so.%{lib_version}
%{_libdir}/libabsl_crc_internal.so.%{lib_version}
%{_libdir}/libabsl_debugging_internal.so.%{lib_version}
%{_libdir}/libabsl_demangle_internal.so.%{lib_version}
%{_libdir}/libabsl_die_if_null.so.%{lib_version}
%{_libdir}/libabsl_examine_stack.so.%{lib_version}
%{_libdir}/libabsl_exponential_biased.so.%{lib_version}
%{_libdir}/libabsl_failure_signal_handler.so.%{lib_version}
%{_libdir}/libabsl_flags.so.%{lib_version}
%{_libdir}/libabsl_flags_commandlineflag.so.%{lib_version}
%{_libdir}/libabsl_flags_commandlineflag_internal.so.%{lib_version}
%{_libdir}/libabsl_flags_config.so.%{lib_version}
%{_libdir}/libabsl_flags_internal.so.%{lib_version}
%{_libdir}/libabsl_flags_marshalling.so.%{lib_version}
%{_libdir}/libabsl_flags_parse.so.%{lib_version}
%{_libdir}/libabsl_flags_private_handle_accessor.so.%{lib_version}
%{_libdir}/libabsl_flags_program_name.so.%{lib_version}
%{_libdir}/libabsl_flags_reflection.so.%{lib_version}
%{_libdir}/libabsl_flags_usage.so.%{lib_version}
%{_libdir}/libabsl_flags_usage_internal.so.%{lib_version}
%{_libdir}/libabsl_graphcycles_internal.so.%{lib_version}
%{_libdir}/libabsl_hash.so.%{lib_version}
%{_libdir}/libabsl_hashtablez_sampler.so.%{lib_version}
%{_libdir}/libabsl_int128.so.%{lib_version}
%{_libdir}/libabsl_kernel_timeout_internal.so.%{lib_version}
%{_libdir}/libabsl_leak_check.so.%{lib_version}
%{_libdir}/libabsl_log_entry.so.%{lib_version}
%{_libdir}/libabsl_log_flags.so.%{lib_version}
%{_libdir}/libabsl_log_globals.so.%{lib_version}
%{_libdir}/libabsl_log_initialize.so.%{lib_version}
%{_libdir}/libabsl_log_internal_check_op.so.%{lib_version}
%{_libdir}/libabsl_log_internal_conditions.so.%{lib_version}
%{_libdir}/libabsl_log_internal_format.so.%{lib_version}
%{_libdir}/libabsl_log_internal_globals.so.%{lib_version}
%{_libdir}/libabsl_log_internal_log_sink_set.so.%{lib_version}
%{_libdir}/libabsl_log_internal_message.so.%{lib_version}
%{_libdir}/libabsl_log_internal_nullguard.so.%{lib_version}
%{_libdir}/libabsl_log_internal_proto.so.%{lib_version}
%{_libdir}/libabsl_log_severity.so.%{lib_version}
%{_libdir}/libabsl_log_sink.so.%{lib_version}
%{_libdir}/libabsl_low_level_hash.so.%{lib_version}
%{_libdir}/libabsl_malloc_internal.so.%{lib_version}
%{_libdir}/libabsl_periodic_sampler.so.%{lib_version}
%{_libdir}/libabsl_random_distributions.so.%{lib_version}
%{_libdir}/libabsl_random_internal_distribution_test_util.so.%{lib_version}
%{_libdir}/libabsl_random_internal_platform.so.%{lib_version}
%{_libdir}/libabsl_random_internal_pool_urbg.so.%{lib_version}
%{_libdir}/libabsl_random_internal_randen.so.%{lib_version}
%{_libdir}/libabsl_random_internal_randen_hwaes.so.%{lib_version}
%{_libdir}/libabsl_random_internal_randen_hwaes_impl.so.%{lib_version}
%{_libdir}/libabsl_random_internal_randen_slow.so.%{lib_version}
%{_libdir}/libabsl_random_internal_seed_material.so.%{lib_version}
%{_libdir}/libabsl_random_seed_gen_exception.so.%{lib_version}
%{_libdir}/libabsl_random_seed_sequences.so.%{lib_version}
%{_libdir}/libabsl_raw_hash_set.so.%{lib_version}
%{_libdir}/libabsl_raw_logging_internal.so.%{lib_version}
%{_libdir}/libabsl_scoped_set_env.so.%{lib_version}
%{_libdir}/libabsl_spinlock_wait.so.%{lib_version}
%{_libdir}/libabsl_stacktrace.so.%{lib_version}
%{_libdir}/libabsl_status.so.%{lib_version}
%{_libdir}/libabsl_statusor.so.%{lib_version}
%{_libdir}/libabsl_str_format_internal.so.%{lib_version}
%{_libdir}/libabsl_strerror.so.%{lib_version}
%{_libdir}/libabsl_strings.so.%{lib_version}
%{_libdir}/libabsl_strings_internal.so.%{lib_version}
%{_libdir}/libabsl_string_view.so.%{lib_version}
%{_libdir}/libabsl_symbolize.so.%{lib_version}
%{_libdir}/libabsl_synchronization.so.%{lib_version}
%{_libdir}/libabsl_throw_delegate.so.%{lib_version}
%{_libdir}/libabsl_time.so.%{lib_version}
%{_libdir}/libabsl_time_zone.so.%{lib_version}

%files devel
%{_includedir}/absl
%{_libdir}/cmake/absl
%{_libdir}/libabsl_*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Aug 01 2024 xinghe <xinghe2@h-partners.com> - 20230802.1-5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix license

* Fri May 31 2024 laokz <zhangkai@iscas.ac.cn> - 20230802.1-4
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:Fix riscv64 'rdcycle' illegal instructor error

* Wed Mar  6 2024 Wenlong Zhang <zhangwenlong@loongson.cn> - 20230802.1-3
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:Fix build error for loongarch64

* Tue Jan 23 2024 xinghe <xinghe2@h-partners.com> - 20230802.1-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:optimize redundant dependence

* Mon Dec 25 2023 xinghe <xinghe2@h-partners.com> - 20230802.1-1
- Type:requirement
- ID:NA
- SUG:NA
- DESC:update to 20230802.1

* Thu Jul 27 2023 gaihuiying <eaglegai@163.com> - 20230125.3-1
- Type:requirement
- ID:NA
- SUG:NA
- DESC:update to 20230125.3

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
