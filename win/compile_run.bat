@echo off

qemu -fbin "../bootloader.asm" -o "bootloader.bin"
& "C:\Program Files\qemu\qemu-system-x86_64.exe" "bootloader.bin"