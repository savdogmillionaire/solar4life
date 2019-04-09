import os
import webbrowser
import numpy as np
from reportlab.pdfgen import canvas
import sqlite3

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, PageBreak
from reportlab.lib.colors import yellow, red, black, white



def create_VRC(fname, name, address):
    """"""
    filename = os.path.join(fname + ".pdf")
    c = canvas.Canvas(filename)
    c.setLineWidth(.3)
    c.setFont('Helvetica', 12)

    # establish connecttion to database
    conn = sqlite3.connect('VRCtable.db')
    cur = conn.cursor()

    ## main meat of the program. uses classes and arrays to somwhat efficiently calculate values
    def calcs():

        ## cable parameters
        class cable_params:
            CC_to_POA_Cable_Thickness_mm2 = 16
            CC_to_POA_Distance_m = 10
            POA_to_MB_Cable_Thickness_mm2 = 16
            POA_to_MB_Distance_m = 15
            MB_to_INV_Cable_Thickness_mm2 = 6
            MB_to_INV_Distance_m = 5
            MB_to_SB_Cable_Thickness_mm2 = 0
            MB_to_SB_Distance_m = 0
            Type_of_Service = 'overhead'
            material = 'Cu'

        ##finds ccc based on cable diameter and phase and calculates for each portion
        ##cc to poa
        invname = 'ABB PVI-20.0-TL-OUTD'
        cur.execute("SELECT MaxACCurrent FROM Inverterspecifications where Inverter = '%s' " % invname)
        a = cur.fetchone()[0]

        cur.execute('SELECT single_phase FROM cccarray where conductor_size = %d'
                    % cable_params.CC_to_POA_Cable_Thickness_mm2)
        b1 = cur.fetchone()[0]

        if cable_params.Type_of_Service == 'underground':
            cc_poa_ccc = [0.]
        else:
            cc_poa_ccc = ((a * cable_params.CC_to_POA_Distance_m) / b1)

        ##poa to mb
        cur.execute('SELECT single_phase FROM cccarray where conductor_size = %d'
                    % cable_params.POA_to_MB_Cable_Thickness_mm2)
        b2 = cur.fetchone()[0]
        poa_mb_ccc = ((a * cable_params.POA_to_MB_Distance_m) / b2)

        ##mb to inverter
        cur.execute('SELECT single_phase FROM cccarray where conductor_size = %d'
                    % cable_params.POA_to_MB_Cable_Thickness_mm2)
        b3 = cur.fetchone()[0]
        mb_inv_ccc = ((a * cable_params.MB_to_INV_Distance_m) / b3)

        ## saves value to a dict so the name of each value is saved, then does basic
        ## operations to find total VRC and where the VRC for a portiun is maximum
        cccdict = {'cc_poa_ccc': cc_poa_ccc, 'poa_mb_ccc': poa_mb_ccc, 'mb_inv_ccc': mb_inv_ccc}
        totalrun = (cc_poa_ccc + poa_mb_ccc + mb_inv_ccc)
        highestccc = max(cccdict.values())
        maxname = (max(cccdict, key=locals().get))

        ##other drawing stuff
        c.drawCentredString(150, 620, '%s' % cable_params.material)
        c.drawCentredString(300, 620, '%s' % cable_params.material)
        c.drawCentredString(450, 620, '%s' % cable_params.material)

        ## changes bottom note on VRC based on whether or not it has passed certain conditions
        if totalrun > 3:
            c.drawCentredString(300, 320, 'Total is greater than 3%, please change something')
        else:
            c.drawCentredString(300, 320, 'Note: no single run is greater than 2%')
        if highestccc > 2:
            c.drawCentredString(300, 300, 'A single run, %s, is greater than 2%% . please change something' % maxname)
        else:
            c.drawCentredString(300, 300, ' and the total is not greater than 3%')

        ##cc to POA drawing

        c.drawCentredString(150, 520, '%dm x %dmm^2' %
                            (cable_params.CC_to_POA_Distance_m, cable_params.CC_to_POA_Cable_Thickness_mm2))
        c.drawCentredString(150, 480, '%dA x %dm' %
                            (a, cable_params.CC_to_POA_Distance_m))
        c.line(100, 475, 200, 475)
        c.drawCentredString(150, 460, '%d' % a)
        c.drawCentredString(150, 430, '= %.3f%% VR' % cc_poa_ccc)

        ##POA to MB drawing
        c.drawCentredString(300, 520, '%dm x %dmm^2' %
                            (cable_params.POA_to_MB_Distance_m, cable_params.POA_to_MB_Cable_Thickness_mm2))
        c.drawCentredString(300, 480, '%dA x %dm' %
                            (a, cable_params.POA_to_MB_Distance_m))
        c.line(250, 475, 350, 475)
        c.drawCentredString(300, 460, '%d' % a)
        c.drawCentredString(300, 430, '= %.3f%% VR' % poa_mb_ccc)

        ##MB to inv drawing
        c.drawCentredString(450, 520, '%dm x %dmm^2' %
                            (cable_params.MB_to_INV_Distance_m, cable_params.MB_to_INV_Cable_Thickness_mm2))
        c.drawCentredString(450, 480, '%dA x %dm' %
                            (a, cable_params.MB_to_INV_Distance_m))
        c.line(400, 475, 500, 475)
        c.drawCentredString(450, 460, '%d' % a)
        c.drawCentredString(450, 430, '= %.3f%% VR' % mb_inv_ccc)
        ##

    def draw_background(name, address):

        ##Title
        c.drawCentredString(300, 750, 'Voltage Rise Calculations for %s - %s' % (name, address))
        c.circle(75, 650, 10, stroke=1, fill=1)
        c.circle(225, 650, 10, stroke=1, fill=1)
        c.circle(375, 650, 10, stroke=1, fill=1)
        c.circle(525, 650, 10, stroke=1, fill=1)

        c.drawCentredString(75, 600, 'CC')
        c.drawCentredString(225, 600, 'P.O.A')
        c.drawCentredString(375, 600, 'M.B')
        c.drawCentredString(525, 600, 'INV')

        c.line(75, 650, 525, 650)
        c.line(225, 575, 225, 400)
        c.line(375, 575, 375, 400)

    draw_background(name, address)
    calcs()
    c.save()
    url = r'file:///C:\Users\Solar4Life\Desktop\solar4life\sld generator files\VRC diagram.pdf'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    # make sure to close connection to database at end of program
    conn.close()


# ----------------------------------------------------------------------
if __name__ == "__main__":
    name = 'Sava Arsenijevic'
    address = '1/56 Heffernan St, Mitchell ACT 2911'
    trianglepath = r"C:\Users\Solar4Life\Desktop\solar4life\sld generator files\sava assets\triangle.png"
    sinepath = r"C:\Users\Solar4Life\Desktop\solar4life\sld generator files\sava assets\sine.png"

    create_VRC("VRC diagram", name, address)
