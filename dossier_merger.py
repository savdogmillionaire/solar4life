from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

input1 = open("PV Modules List 190313.pdf", "rb")
input2 = open("Dossier WithoutBatteries.pdf", "rb")

merger.append(input2)
merger.merge(position=2, fileobj=input1, pages=(0, 1))
merger.merge(position=4, fileobj=input1, pages=(0, 2))

output = open("Dossier WithoutBatteries - Copy.pdf", "wb")
merger.write(output)
