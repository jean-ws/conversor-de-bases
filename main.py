from binary_to import *
from dec_to import *
<<<<<<< HEAD
from octal_to import *
from hex_to import *
from write_txt import *
from read_txt import *

def read_txt(txt_name):
    lista_de_linhas = read_lines(txt_name)
    for line in lista_de_linhas:
        espaco = line.find(" ")
        exercicio = line[:espaco-1]
        value_and_base = line[espaco+1:]
        base = int(read_base(value_and_base))
        valor = read_value(value_and_base)
        
        #esta lista conterá cada linha que será escrita no txt.
        lines = []
        if base == 2:
            write_enunciado(base, valor, lines, exercicio)
            lixo = binary_to_decimal(valor,lines)
            lixo = binary_to_octal(valor, lines)
            lixo = binary_to_hex(valor,lines)
            write_txt(lines)
        
        elif base == 10: 
            write_enunciado(base, valor, lines, exercicio)
            lixo = dec_to_bin(valor,lines)
            lixo = dec_to_octal(valor,lines)
            lixo = dec_to_hex(valor,lines)
            write_txt(lines)
        
        elif base == 8: 
            write_enunciado(base, valor, lines, exercicio)
            lixo = octal_to_dec(valor,lines)
            lixo = octal_to_bin(valor,lines)
            lixo = octal_to_hex(valor,lines)
            write_txt(lines)
        
        elif base == 16:
            write_enunciado(base, valor, lines, exercicio)
            lixo = hex_to_dec(valor,lines)
            lixo = hex_to_bin(valor,lines)
            lixo = hex_to_octal(valor,lines)
            write_txt(lines)

read_txt("ex.txt")
=======

teste = binary_to_decimal('100')
print(teste)

teste = binary_to_octal('1000')
print(teste)

teste = binary_to_hex('110011101010')
print(teste)


teste = dec_to_bin('285')
print(teste)

teste = dec_to_octal('285')
print(teste)

teste = dec_to_hex('285')
print(teste)
>>>>>>> d5f15c2ac10841b14f29ca90c73c44683d3ca51a
