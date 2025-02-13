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
tar zxvf abseil-cpp-20230802.1.tar.gz
mv abseil-cpp-20230802.1 abseil-cpp
cd $1/abseil-cpp
patch -p1 < $1/abseil-cpp-20210324.2-sw.patch
patch -p1 < $1/0001-add-loongarch-suopport-for-abseil-cpp.patch
patch -p1 < $1/0002-PR-1644-unscaledcycleclock-remove-RISC-V-support.patch
patch -p1 < $1/fix-mingw-complier-error.patch
flock -u 100
} 100<>$1/lock_file.lock
exit 0