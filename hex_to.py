from dec_to import *

def hex_to_dec(hex, lines):
    lines.append("\n")
    lenght = len(hex)
    b = 0
    
    for n in hex:

        if n == 'A':
            a = 10
        elif n == 'B':
            a = 11
        elif n == 'C':
            a = 12
        elif n == 'D':
            a = 13
        elif n == 'E':
            a = 14    
        elif n == 'F':
            a = 15
        else:
            a = int(n)

        aux = a * (16 ** (lenght-1)) 
        line = str(a) + " * (16^" + str((lenght-1)) + ") = " + str(aux)
        lines.append(line)
        b += aux
        lenght -= 1

    line = "Resultado: " + str(b) + " (base 10)"
    lines.append(line)
    return b

def hex_to_bin(hex, lines):
    lines.append("\n")
    lenght = len(hex)
    b = 0
    
    for n in hex:

        if n == 'A':
            a = 10
        elif n == 'B':
            a = 11
        elif n == 'C':
            a = 12
        elif n == 'D':
            a = 13
        elif n == 'E':
            a = 14    
        elif n == 'F':
            a = 15
        else:
            a = int(n)

        aux = a * (16 ** (lenght-1)) 
        line = str(a) + " * (16^" + str((lenght-1)) + ") = " + str(aux)
        b += aux
        lenght -= 1

    dec = b
    b = []
    bin = ''

    if int(dec/2) > 0:
        while int(dec / 2) > 0:
            line = str(dec) + " / 2 = " + str(int(dec/2)) + " | Resto: " + str(dec % 2)
            lines.append(line)
            b.append(dec % 2)
            dec = int(dec/2)
    
        b.append(dec % 2)
    
        for i in range (len(b)-1,-1,-1):
            bin += str(b[i])

    else:
        bin = str(dec)
        
    line = "Resultado: " + bin + " (base 2)"
    lines.append(line)
    return bin

def hex_to_octal(hex, lines):
    lines.append("\n")
    lenght = len(hex)
    b = 0
    
    for n in hex:

        if n == 'A':
            a = 10
        elif n == 'B':
            a = 11
        elif n == 'C':
            a = 12
        elif n == 'D':
            a = 13
        elif n == 'E':
            a = 14    
        elif n == 'F':
            a = 15
        else:
            a = int(n)

        aux = a * (16 ** (lenght-1)) 
        line = str(a) + " * (16^" + str((lenght-1)) + ") = " + str(aux)
        b += aux
        lenght -= 1

    dec = b
    b = []
    c = ''

    if int(dec/8) > 0:
        while int(dec / 8) > 0:
            line = str(dec) + "/ 8 = " + str(int(dec/8)) + " | Resto: " + str(dec % 8)
            lines.append(line)
            b.append(str(dec % 8))
            dec = int(dec/8)
    
        b.append(str(dec % 8))
    
        for i in range (len(b)-1,-1,-1):
            c += b[i]

    else: 
        c = str(dec)

    line = "Resultado: " + c + " (base 8)"
    lines.append(line)
    return c