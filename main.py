import logging

logging.basicConfig(filename="log.log", level=logging.INFO)

text = input("Text: ")

letters = []

for letter in text:
    letters.append(letter)


def write_chars(chars: list):
    logging.info("creating and opening bootloader.asm")
    with open("bootloader.asm", "w") as bl: # open the boot loader file
        logging.info("entering tty mode")
        bl.write("mov ah, 0x0e\n")
        for i in chars:
            logging.info(f"writing letter {i}")
            bl.writelines(f"mov al, '{i}'\n") # get letter
            bl.writelines("int 0x10\n") # show letter
        logging.info("creating infinite loop")
        bl.writelines("""
        jmp $\n
times 510 - ($-$$) db 0\n
dw 0xaa55\n""") # infinite loop

write_chars(letters)
logging.info("bootloader.asm created")