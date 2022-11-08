def octal_to_dec(octal, lines):
    lines.append("\n")
    lenght = len(octal)
    a = 0
    
    for n in octal:
        line = n + "* (8 ^ " + str((lenght-1)) + ") = " + str(int(n) * (8 ** (lenght-1)))
        lines.append(line)
        a += int(n) * (8 ** (lenght-1))
        lenght -= 1

    line = "Resultado: " + str(a) + " (base 10)"
    lines.append(line)
    return str(a)


def octal_to_bin(octal, lines):
    lines.append("\n")
    lenght = len(octal)
    a = 0
    
    for n in octal:
        a += int(n) * (8 ** (lenght-1))
        lenght -= 1
        
    dec = a

    b = []
    bin = ''

    if int(dec/2) > 0:
        while int(dec / 2) > 0:
            line = str(dec) + "/ 2 = " + str(int(dec/2)) + " | Resto: " + str(dec % 2)
            lines.append(line)
            b.append(dec % 2)
            dec = int(dec/2)
            
        line = str(dec) + "/ 2 = " + str(int(dec/2)) + " | Resto: " + str(dec % 2)
        lines.append(line)
        b.append(dec % 2)
    
        for i in range (len(b)-1,-1,-1):
            bin += str(b[i])

    else:
        bin = str(dec)
        
    line = "Resultado: " + bin + " (base 2)"
    lines.append(line)
    return bin


def octal_to_hex(octal, lines):
    lines.append("\n")
    lenght = len(octal)
    a = 0
    
    for n in octal:
        a += int(n) * (8 ** (lenght-1))
        lenght -= 1
        
    dec = int(a)
    b = []
    hex = ''

    if int(dec/16) > 0:
        while int(dec / 16) > 0:
            line = str(dec) + "/ 16 = " + str(int(dec/16)) + " | Resto: " + str(dec % 16)
            lines.append(line)
            b.append(dec % 16)
            dec = int(dec/16)
    
        b.append(dec % 16)
        
        for i in range (len(b)-1,-1,-1):
    
            n = b[i]
    
            if n > 9:
                if n == 10:
                    n = 'A'
                if n == 11:
                    n = 'B'
                if n == 12:
                    n = 'C'
                if n == 13:
                    n = 'D'
                if n == 14:
                    n = 'E'
                if n == 15:
                    n = 'F'
    
                hex += n
          
            else:
                hex += str(n)

    else:
        if dec > 9:
            if dec == 10:
                hex = 'A'
            if dec == 11:
                hex = 'B'
            if dec == 12:
                hex = 'C'
            if dec == 13:
                hex = 'D'
            if dec == 14:
                hex = 'E'
            if dec == 15:
                hex = 'F'
        else:  
            hex = str(dec)
            
    line = "Resultado: " + hex + " (base 16)"
    lines.append(line)
    return hex