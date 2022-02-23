text = input("Text: ")

letters = []

for letter in text:
    letters.append(letter)


def write_chars(chars: list):
    with open("bootloader.asm", "w") as bl: # open the boot loader file
        bl.write("mov ah, 0x0e\n")
        for i in chars:
            bl.writelines(f"mov al, '{i}'\n") # get letter
            bl.writelines("int 0x10\n") # show letter
        bl.writelines("""
        \njmp $\n
times 510 - ($-$$) db 0\n
dw 0xaa55\n""")

write_chars(letters)
