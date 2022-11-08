<<<<<<< HEAD
def dec_to_bin(dec_str,lines):
    lines.append("\n")
    dec = int(dec_str)
    b = []
    c = ''

    if int(dec/2) > 0:
        while int(dec / 2) > 0:
            line = str(dec) + "/ 2 = " + str(int(dec/2)) + " | Resto: " + str(dec % 2)
            lines.append(line)
            b.append(dec % 2)
            dec = int(dec/2)
    
        b.append(dec % 2)
    
        for i in range (len(b)-1,-1,-1):
            c += str(b[i])

    else:
        c = str(dec)
        
    line = "Resultado: " + c + " (base 2)"
    lines.append(line)
    return c


def dec_to_octal(dec_str, lines):
    lines.append("\n")
    dec = int(dec_str)
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


def dec_to_hex(dec_str, lines):
    lines.append("\n")
    dec = int(dec_str)
    b = []
    c = ''

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
    
                c += n
          
            else:
                c += str(n)

    else:
        if dec > 9:
            if dec == 10:
                c = 'A'
            if dec == 11:
                c = 'B'
            if dec == 12:
                c = 'C'
            if dec == 13:
                c = 'D'
            if dec == 14:
                c = 'E'
            if dec == 15:
                c = 'F'
        else:  
            c = str(dec)
            
    line = "Resultado: " + c + " (base 16)"
    lines.append(line)
=======
def dec_to_bin(dec_str):

    dec = int(dec_str)
    b = []
    c = ''
    
    while int(dec / 2) > 0:
        b.append(dec % 2)
        dec = int(dec/2)

    b.append(dec % 2)

    for i in range (len(b)-1,-1,-1):
        c += str(b[i])
    
    return c


def dec_to_octal(dec_str):

    dec = int(dec_str)
    b = []
    c = ''
  
    while int(dec / 8) > 0:
        b.append(str(dec % 8))
        dec = int(dec/8)

    b.append(str(dec % 8))

    for i in range (len(b)-1,-1,-1):
        c += b[i]
    
    return c


def dec_to_hex(dec_str):

    dec = int(dec_str)
    b = []
    c = ''
    
    while int(dec / 16) > 0:
        b.append(dec % 16)
        dec = int(dec/16)

    b.append(dec % 16)

    for i in range (len(b)-1,-1,-1):
    
        n = b[i]
    
        if n > 9:
            match n:
                case 10:
                    n = 'A'
                case 11:
                    n = 'B'
                case 12:
                   n = 'C'
                case 13:
                    n = 'D'
                case 14:
                    n = 'E'
                case 15:
                    n = 'F'
                case other:
                    n = '-'

            c += n
      
        else:
            c += str(n)

>>>>>>> d5f15c2ac10841b14f29ca90c73c44683d3ca51a
    return c