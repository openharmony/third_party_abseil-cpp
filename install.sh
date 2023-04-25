#!/bin/bash
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation version 2.1
# of the License.
#
# Copyright(c) 2023 Huawei Device Co., Ltd.

set -e
cd $1
if [ -d "abseil-cpp-20220623.1" ];then
    rm -rf abseil-cpp-20220623.1
fi
tar zxvf abseil-cpp-20220623.1.tar.gz
cd $1/abseil-cpp-20220623.1
exit 0