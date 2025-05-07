#!/bin/bash
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation version 2.1
# of the License.
#
# Copyright(c) 2023 Huawei Device Co., Ltd.

set -e
cd $1
{
flock -x 100
if [ -d "abseil-cpp" ];then
    rm -rf abseil-cpp
fi
tar zxvf $2/abseil-cpp-20230802.1.tar.gz
mv abseil-cpp-20230802.1 abseil-cpp
cd abseil-cpp
patch -p1 < $2/abseil-cpp-20210324.2-sw.patch
patch -p1 < $2/0001-add-loongarch-suopport-for-abseil-cpp.patch
patch -p1 < $2/0002-PR-1644-unscaledcycleclock-remove-RISC-V-support.patch
patch -p1 < $2/fix-mingw-complier-error.patch
patch -p1 < $2/backport-CVE-2025-0838.patch
flock -u 100
} 100<>lock_file.lock
exit 0