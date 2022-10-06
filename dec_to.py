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

    return c