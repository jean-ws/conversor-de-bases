def write_txt(lines):
    with open('lista.txt', 'a', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            f.write('\n')


def write_enunciado(base, valor, lines, ex):
    with open('lista.txt', 'a', encoding='utf-8') as f:
        f.write("\n" + ex + ") ")
        f.write(str(valor) + " (base " + str(base) + ")")
