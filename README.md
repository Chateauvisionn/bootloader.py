# bootloader.py
bootloader.py is a python program that you can use to create a bootloader that print text.
## Setup
### Git
Clone the repository with 
```git clone https://github.com/chateauvisionn/bootloader.py.git/```

### Add to path
#### Windows
Run `add_to_path.py` script in `win\path\`
#### Linux
Run `add_to_path.py` script in `linux\path\`

## Usage
Run `main.py` with `python main.py` or `python3 main.py` and type the text you want:

```Text: test```

bootloader.asm:
```
mov ah, 0x0e
mov al, 't'
int 0x10
mov al, 'e'
int 0x10
mov al, 's'
int 0x10
mov al, 't'
int 0x10

        
jmp $

times 510 - ($-$$) db 0

dw 0xaa55
```


## Compiling and running
To compile assembly files, use [nasm](https://www.nasm.us/).
Compile `bootloader.asm` with `nasm -fbin bootloader.asm -o bootloader.bin`

And run it with [qemu](https://www.qemu.org/):

`qemu bootloader.bin` or `qemu-system-x86_64 bootloader.bin`