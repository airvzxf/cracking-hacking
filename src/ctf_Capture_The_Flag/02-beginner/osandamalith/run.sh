#!/bin/bash

# https://osandamalith.com/2019/02/11/linux-reverse-engineering-ctfs-for-beginners/

APP_NAME="nix_5744af788e6cbdb29bb41e8b0e5f3cd5"
APP="./${APP_NAME}"

echo ""
echo "# ------------------------------------------------------"
echo "# file ${APP}"
file "${APP}"
echo "# ------------------------------------------------------"


echo ""
echo "# ------------------------------------------------------"
echo "# readelf -h ${APP}"
readelf -h "${APP}"
echo "# ------------------------------------------------------"


echo ""
echo "# ------------------------------------------------------"
echo "# e_size = e_shoff + (e_shnum * e_shentsize)"
E_SHOFF=$(readelf -h "${APP}" | grep "Start of section headers" | sed 's/[^0-9]*\([0-9]\+\).*/\1/')
echo "e_shoff:     ${E_SHOFF}"

E_SHNUM=$(readelf -h "${APP}" | grep "Number of section headers" | sed 's/[^0-9]*\([0-9]\+\).*/\1/')
echo "e_shnum:     ${E_SHNUM}"

E_SHENTSIZE=$(readelf -h "${APP}" | grep "Size of section headers" | sed 's/[^0-9]*\([0-9]\+\).*/\1/')
echo "e_shentsize: ${E_SHENTSIZE}"

E_SIZE=$((E_SHOFF + (E_SHNUM * E_SHENTSIZE)))
echo "e_size: ${E_SIZE} | It's equal to the file size if you use 'ls -l'"

ls -la "${APP}"
echo "# ------------------------------------------------------"


echo ""
echo "# ------------------------------------------------------"
echo "# readelf -S --wide ${APP}"
readelf -S --wide "${APP}"
echo "# ------------------------------------------------------"


echo ""
echo "# ------------------------------------------------------"
echo "# readelf -p .rodata ${APP} > ${APP_NAME}-rodata.txt"
readelf -p .rodata "${APP}" > "${APP_NAME}-rodata.txt"
echo "# ------------------------------------------------------"

echo ""
echo "# ------------------------------------------------------"
echo "# nm -D ${APP}"
nm -D "${APP}"
echo "# ------------------------------------------------------"


echo ""
echo "# ------------------------------------------------------"
echo "# strace ${APP} aaa"
strace "${APP}" aaa
echo "# ------------------------------------------------------"


echo ""
echo "# ------------------------------------------------------"
echo "# ltrace -i -C ${APP} aaa"
ltrace -i -C "${APP}" aaa
echo "# ------------------------------------------------------"


echo ""
echo "# ------------------------------------------------------"
echo "# objdump -f ${APP}"
objdump -f "${APP}"
echo "# ------------------------------------------------------"


echo ""
echo "# ------------------------------------------------------"
echo "# objdump -D -j .text ${APP}"
objdump -D -j .text "${APP}" | head -n 20
echo "# ------------------------------------------------------"


echo ""
echo "# ------------------------------------------------------"
echo "# Section of the code where it sum the ASCII characters"
echo "# objdump -S ..."
objdump -S --start-address=0x1276 --stop-address=0x129f "${APP}"
echo "# ------------------------------------------------------"


echo ""
echo "# ------------------------------------------------------"
echo "# gdb --args ${APP} abcde"
echo "# ------------------------------------------------------"
