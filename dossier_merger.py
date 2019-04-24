from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

input1 = open("Hartley SLD version 3.pdf", "rb")
input2 = open("Hartley Lifecare Dossier WithoutBatteries UPDATED.pdf", "rb")

merger.append(input2)
merger.merge(position=14, fileobj=input1, pages=(0, 1))

output = open("Hartley Lifecare Dossier WithoutBatteries UPDATED 2.pdf", "wb")
merger.write(output)
