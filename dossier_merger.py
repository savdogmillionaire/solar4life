from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

name = "Mohit Sharma"

SLD_file = "%s SLD.pdf" % name
SPE_file = "%s SPE.pdf" % name
Components_file = "%s Components List.pdf" % name
Panel_datasheet = "%s Panel Datasheet.pdf" % name
Panel_warranty = "%s Panel Warranty.pdf" % name
Inverter_datasheet = "%s Inverter Datasheet.pdf" % name
Inverter_warranty = "%s Inverter Warranty.pdf" % name

# Single Line Diagram
input1 = open(SLD_file, "rb")
# System Performance Estimate
input2 = open(SPE_file, "rb")
# Components List
input3 = open(Components_file, "rb")
# Panel Datasheet
input4 = open(Panel_datasheet, "rb")
# Panel Warranty
input5 = open(Panel_warranty, "rb")
# Inverter Datasheet
input6 = open(Inverter_datasheet, "rb")
# Inverter Warranty
input7 = open(Inverter_warranty, "rb")

# Output dossier document
output_pdf = "%s Dossier WithoutBatteries.pdf" % name
output1 = open(output_pdf, "rb")

merger.append(input1)
merger.merge(position=14, fileobj=input1, pages=(0, 1))

merger.write(output1)
