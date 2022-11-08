import aspose.words as aw

#cria objeto da classe Document
doc = aw.DocumentBuilder()

#cria objeto da classe DocumentBuilder
builder = aw.DocumentBuilder(doc)

#muda fonte (formatação)
builder.font.size = 12
builder.font.name = "Arial"

#formatação de parágrafo
builder.paragraph_format.first_line_indent = 8
builder.paragraph_format.alignment = aw.ParagraphAlignment.JUSTIFY
builder.paragraph_format.keep_together = True

#escrevendo
builder.writeln("Meu texto. Bsdas dasdas dadasd")

#salva o doc
doc.save("arquivo.doc")