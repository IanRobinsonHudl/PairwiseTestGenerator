# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.15.1)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x01\x1e\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x13\x00\x00\x00\x13\x08\x06\x00\x00\x00\x72\x50\x36\xcc\
\x00\x00\x00\x01\x73\x52\x47\x42\x00\xae\xce\x1c\xe9\x00\x00\x00\
\x04\x67\x41\x4d\x41\x00\x00\xb1\x8f\x0b\xfc\x61\x05\x00\x00\x00\
\x09\x70\x48\x59\x73\x00\x00\x0e\xc2\x00\x00\x0e\xc2\x01\x15\x28\
\x4a\x80\x00\x00\x00\xb3\x49\x44\x41\x54\x38\x4f\xad\x93\x81\x0d\
\x84\x20\x0c\x45\xcb\x8d\xc5\xed\xc3\xad\x83\xcb\xe8\x30\xdc\x2e\
\x9c\x2d\x54\xe5\xa8\xb4\x26\xbc\xa4\x26\x50\xf9\xad\xfd\xe2\xf2\
\x0e\x4c\xe2\x85\x8f\xef\xf2\x06\xe7\x1c\xc5\x67\xa3\xfd\x06\x2d\
\x7f\x80\x9d\x31\x29\xfa\xec\x63\xaa\xab\x1e\x2d\x7f\x8a\xa5\x98\
\x3d\x84\xbc\xd6\x65\x87\x96\xdf\x29\x62\x13\x84\x10\x12\x5b\x03\
\xa0\x09\x25\x42\x7f\x44\xcb\x33\xf3\xdd\x94\x60\x07\x1f\x41\xfd\
\x0d\xb8\x73\x10\xf7\xf1\x38\x06\x7f\xf9\x58\xcc\x30\xf8\x6b\xb1\
\x7b\x31\x8b\x83\x7f\xef\x90\x98\xd4\xb2\xea\xa0\x50\xac\xe9\x4c\
\xfb\xc3\xaf\x48\xc5\x4e\x31\xa1\x92\xd4\xf1\x88\x22\xa6\xcc\xc7\
\xda\x31\x89\x0d\xe7\x63\x31\xa2\xd2\xcc\xac\xe3\x81\x10\x32\x14\
\xb3\xde\x49\x66\xe2\xdd\x04\xf8\x01\xd5\xf7\xad\x74\xd2\xc1\x4d\
\x2d\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82\
"

qt_resource_name = b"\
\x00\x06\
\x07\x03\x7d\xc3\
\x00\x69\
\x00\x6d\x00\x61\x00\x67\x00\x65\x00\x73\
\x00\x08\
\x0a\x61\x5a\xa7\
\x00\x69\
\x00\x63\x00\x6f\x00\x6e\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x12\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x12\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x75\xa2\x00\xf9\x36\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
