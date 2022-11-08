<<<<<<< HEAD
def binary_to_decimal(bin, lines):
    lines.append("\n")
=======
def binary_to_decimal(bin):
  
>>>>>>> d5f15c2ac10841b14f29ca90c73c44683d3ca51a
    lenght = len(bin)
    a = 0
  
    for n in bin:
        a += int(n) * (2 ** (lenght-1))
<<<<<<< HEAD

        line = n + " x 2^" + str(lenght-1) + " = " + str(a)
        lines.append(str(line))

        lenght -= 1

    line = "Resultado: " + str(a) + " (base 10)"
    lines.append(line)
    return str(a)


def binary_to_octal(bin, lines):
    lines.append("\n")
    lenght = len(bin)
    a = 0
  
    for n in bin:
        a += int(n) * (2 ** (lenght-1))

        lenght -= 1

    dec = a
    b = []
    c = ''
    
    while int(dec / 8) > 0:
        
        line = str(dec) + "/ 8 = " + str(int(dec/8)) + " | Resto: " + str(dec % 8)
        lines.append(line)
        
=======
        lenght -= 1

        return str(a)


def binary_to_octal(bin):

    dec = int(binary_to_decimal(bin))
    b = []
    c = ''
  
    while int(dec / 8) > 0:
>>>>>>> d5f15c2ac10841b14f29ca90c73c44683d3ca51a
        b.append(str(dec % 8))
        dec = int(dec/8)

    b.append(str(dec % 8))

<<<<<<< HEAD
    line = str(dec) + "/ 8 = " + str(int(dec/8)) + " | Resto: " + str(dec % 8)
    lines.append(line)

    for i in range (len(b)-1,-1,-1):
        c += b[i]

    line = "Resultado: " + str(c) + " (base 8)"
    lines.append(line)
    return c

def binary_to_hex(bin, lines):
    lines.append("\n")
    lenght = len(bin)
    a = 0
  
    for n in bin:
        a += int(n) * (2 ** (lenght-1))

        lenght -= 1

    dec = a
    b = []
    c = ''

    if int(dec/16) > 0:
        while int(dec / 16) > 0:
            
            line = str(dec) + "/ 16 = " + str(int(dec/16)) + " | Resto: " + str(dec % 16)
            lines.append(line)
            b.append(dec % 16)
            dec = int(dec/16)
        
        line = str(dec) + "/ 16 = " + str(int(dec/16)) + " | Resto: " + str(dec % 16)
        lines.append(line)
        b.append(dec % 16)

        #inverte a ordem (reverse)
        for i in range (len(b)-1,-1,-1):
            n = b[i]
            #correspondente em hexadecimal
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
            if b == 13:
                c = 'D'
            if b == 14:
                c = 'E'
            if b == 15:
                c = 'F'
        else:
            c = str(dec)
        
        line = str(dec) + " (base 10) é " + c + " (base 16)"
        lines.append(line)
        
    line = "Resultado: " + c + " (base 16)"
    lines.append(line)
=======
    for i in range (len(b)-1,-1,-1):
        c += b[i]
    
    return c

def binary_to_hex(bin):
  
    dec = int(binary_to_decimal(bin))
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