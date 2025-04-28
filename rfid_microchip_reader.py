# PChaturvedi 2025
# Reader module: WL-134 ISO11784/85
# Microchip module: ISO11784 FDX-B

import pyb

uart = pyb.UART(1, baudrate=9600, timeout_char=200)

def format_id(raw_bytes):

    string = str(raw_bytes)[6:19]
    chars = [None]*len(string)

    for i in range(len(string)):
        chars[i] = string[-(i+1)]

    new_string = "".join(str(x) for x in chars)

    country = int(new_string[0:3], 16)
    animal_id = int(new_string[3:], 16)

    return [f"{country:03d}", f"{animal_id:012d}"]

print("Ready to read...")

while True:
    while uart.any()>1:
        id = format_id(uart.read())
        print(f"----------\nCountry code: {id[0]}")
        print(f"ID: {id[1]}\n----------\n")

