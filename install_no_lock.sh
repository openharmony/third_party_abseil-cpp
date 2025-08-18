#!/bin/bash
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation version 2.1
# of the License.
#
# Copyright(c) 2023 Huawei Device Co., Ltd.

set -e
cd $1
if [ -d "abseil-cpp" ];then
    echo "abseil-cpp exists"
    exit 0
fi
tar zxvf $2/abseil-cpp-20250127.0.tar.gz
mv abseil-cpp-20250127.0 abseil-cpp
cd abseil-cpp
patch -p1 < $2/fix-mingw-complier-error.patch
patch -p1 < $2/adapter-ohos.patch
patch -p1 < $2/fix-mac-complier-error.patch
sed -i '/find_library/d' ./absl/base/CMakeLists.txt
exit 0
