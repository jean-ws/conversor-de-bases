def binary_to_decimal(bin):
  
    lenght = len(bin)
    a = 0
  
    for n in bin:
        a += int(n) * (2 ** (lenght-1))
        lenght -= 1

        return str(a)


def binary_to_octal(bin):

    dec = int(binary_to_decimal(bin))
    b = []
    c = ''
  
    while int(dec / 8) > 0:
        b.append(str(dec % 8))
        dec = int(dec/8)

    b.append(str(dec % 8))

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

    return c