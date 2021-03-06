## This Program creates the sLD
##

##
##
import os
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.colors import yellow, red, black, white
import sqlite3

##must run this import pytohn file to get inputs from calculations.
# from designgui import array_1_model_input,array_1_length,array_1_strings,array_2_length,array_2_strings,inverter_1_input
from input_from_main import *


# from SLDGUI import inverterno, battery, arrays, phase, current, reposit

def create_SLD(fname, inverterno, battery, array, phase, customer_ID, current, reposit):
    """"""

    # establish connecttion to database
    conn = sqlite3.connect('VRCtable.db')
    cur = conn.cursor()

    ##accessing databse to find customer details based on a unique customer ID
    cur.execute('SELECT Name FROM customer_details WHERE CustomerID =?', customer_ID)
    name = cur.fetchone()[0]
    cur.execute('SELECT Street FROM customer_details WHERE CustomerID =?', customer_ID)
    street = cur.fetchone()[0]
    cur.execute('SELECT Suburb FROM customer_details WHERE CustomerID =?', customer_ID)
    suburb = cur.fetchone()[0]
    cur.execute('SELECT State FROM customer_details WHERE CustomerID =?', customer_ID)
    state = cur.fetchone()[0]
    cur.execute('SELECT Postcode FROM customer_details WHERE CustomerID =?', customer_ID)
    postoode = cur.fetchone()[0]
    ## string concatenation to create title.
    address = street + ', ' + suburb + ' ' + state + ' ' + str(postoode)

    arrayisc = system_1.array_Isc()[0]
    arrayvoc = system_1.array_Voc()[0]
    arrayvocminus10 = system_1.array_Voc_minus_10()[0]

    ## these values should be taken from the design tool. for now they will be entered manually.
    # inverterno = 1
    # battery = 0
    # arrays = 1
    # phase = 1
    # current = 'DC'
    # reposit = 1
    # customer_ID = (123456,)

    ## where images of some shapes in the program used. cahgne if required.
    trianglepath = r"C:\Users\Solar4Life\Desktop\solar4life\sld generator files\sava assets\triangle.png"
    sinepath = r"C:\Users\Solar4Life\Desktop\solar4life\sld generator files\sava assets\sine.png"

    panelspec = ('%s' % array_1_model_input,)
    batteryl = ('SolaX 3.3kWh Battery',)
    battery2 = ('BYD Battery Box H 6.4',)
    inverter1 = ('%s' % inverter_1_input,)
    inverter2 = ('',)
    meter1 = ('LG Meter',)
    meter2 = ('',)

    Inverter1ACIsolator = ('250V 1P 32A 6kA Suntree SUKF',)
    Inverter2ACIsolator = ('1P 10A 6kA NHP mod6 AC Breaker',)
    SolarSupplyMainSwitch = ('250V 1P 25A 6kA Suntree SL7-63',)
    BatteryACIsolator = ('1P 25A 6kA NHP mod6 AC Breaker',)
    BatteryDCIsolator = ('1P 25A 6kA NHP mod6 AC Breaker',)
    EPSACIsolator = ('3P 32A 6kA NHP mod6 AC Breaker',)

    filename = os.path.join(fname + ".pdf")
    c = canvas.Canvas(filename)
    c.setLineWidth(.3)
    c.setFont('Helvetica', 12)

    ##Title
    c.drawCentredString(300, 820, 'Single Line Diagram for %s - %s' % (name, address))

    def draw_arc(x, y):
        x += -7.5
        y += 7
        c.arc(x, y, x + 15, y - 15, extent=180)

    ## draws meter based on how many meters ther are an layout of wiring
    def draw_reposit():
        if reposit > 0:
            if phase == 1 and battery == 1:
                ##reposit
                c.setFont('Helvetica', 7)
                c.rect(250, 50, 50, 30)

                cur.execute('SELECT Model FROM Meterspecifications where Meter=?', meter1)
                model = cur.fetchone()[0]
                c.drawRightString(300, 40, 'Model Number: %s ' % model)
                cur.execute('SELECT Make FROM Meterspecifications where Meter=?', meter1)
                make = cur.fetchone()[0]
                c.drawRightString(300, 30, "Make: %s " % make)

                if reposit >= 2:
                    cur.execute('SELECT Model FROM Meterspecifications where Meter=?', meter2)
                    model = cur.fetchone()[0]
                    c.drawRightString(300, 20, 'Model Number: %s ' % model)
                    cur.execute('SELECT Make FROM Meterspecifications where Meter=?', meter2)
                    make = cur.fetchone()[0]
                    c.drawRightString(300, 10, "Make: %s " % make)

                c.drawString(255, 60, "Reposit")
                c.circle(200, 185, 7)
                c.line(200, 177, 200, 65)
                c.line(200, 65, 250, 65)
                c.line(300, 65, 340, 65)
                c.line(340, 65, 340, 93.5)
                c.rect(333.5, 93.5, 13, 13)
                c.drawCentredString(340, 122, 'Voltage')
                c.drawCentredString(340, 112, 'Reference')

            if phase == 1 and battery == 0:
                c.setFont('Helvetica', 7)
                c.rect(250, 50, 50, 30)
                c.drawString(255, 60, "Reposit")
                cur.execute('SELECT Model FROM Meterspecifications where Meter=?', meter1)
                model = cur.fetchone()[0]
                c.drawRightString(300, 40, 'Model Number: %s ' % model)
                cur.execute('SELECT Make FROM Meterspecifications where Meter=?', meter1)
                if reposit >= 2:
                    make = cur.fetchone()[0]
                    c.drawRightString(300, 30, "Make: %s " % make)
                    cur.execute('SELECT Model FROM Meterspecifications where Meter=?', meter2)
                    model = cur.fetchone()[0]
                    c.drawRightString(300, 20, 'Model Number: %s ' % model)
                    cur.execute('SELECT Make FROM Meterspecifications where Meter=?', meter2)
                    make = cur.fetchone()[0]
                    c.drawRightString(300, 10, "Make: %s " % make)

                c.circle(230, 185, 7)
                c.line(230, 177, 230, 65)
                c.line(230, 65, 250, 65)
                c.line(300, 65, 340, 65)
                c.line(340, 65, 340, 93.5)
                c.rect(333.5, 93.5, 13, 13)
                c.drawCentredString(340, 122, 'Voltage')
                c.drawCentredString(340, 112, 'Reference')

            if phase == 3:
                ##reposit
                c.circle(225, 195, 5)
                c.circle(205, 182.5, 5)
                c.circle(185, 170, 5)
                draw_arc(205, 170)
                draw_arc(225, 182.5)
                draw_arc(225, 170)

                c.setFont('Helvetica', 7)
                c.rect(300, 25, 50, 30)

                cur.execute('SELECT Model FROM Meterspecifications where Meter=?', meter1)
                model = cur.fetchone()[0]
                c.drawString(255, 17, 'Model Number: %s ' % model)
                cur.execute('SELECT Make FROM Meterspecifications where Meter=?', meter1)
                make = cur.fetchone()[0]
                c.drawString(255, 8, "Make: %s " % make)

                c.drawString(305, 30, "Reposit")
                c.rect(363.5, 113.5, 13, 13)
                c.rect(393.5, 128.5, 13, 13)
                c.rect(423.5, 143.5, 13, 13)
                draw_arc(370, 135)
                draw_arc(370, 150)
                draw_arc(400, 150)
                c.drawString(440, 122, 'Voltage')
                c.drawString(440, 112, 'Reference')

    ##switch function. draws based on x and y coordinates, and rotation
    def draw_switch(x, y, rot):
        if rot == 0:
            c.circle(x, y, 2, stroke=1, fill=0)
            c.circle(x, y + 15, 2, stroke=1, fill=0)
            c.line(x, y + 2, x - 7, y + 15)

        if rot == 90:
            c.circle(x, y, 2, stroke=1, fill=0)
            c.circle(x + 15, y, 2, stroke=1, fill=0)
            c.line(x + 2, y, x + 15, y - 7)

        if rot == 180:
            c.circle(x, y, 2, stroke=1, fill=0)
            c.circle(x, y - 15, 2, stroke=1, fill=0)
            c.line(x, y - 2, x + 7, y - 15)

        if rot == 270:
            c.circle(x, y, 2, stroke=1, fill=0)
            c.circle(x + 15, y, 2, stroke=1, fill=0)
            c.line(x + 2, y, x + 15, y + 7)

    ##draw battery function. needs x and y coordinates
    def draw_battery(x, y, battery):

        c.line(x + 10, y - 10, x + 10, y)
        c.line(x + 10, y, x - 35, y)
        c.line(x - 35, y, x - 35, y + 35)
        c.line(x - 35, y + 35, x - 20, y + 35)
        c.line(x - 20, y + 25, x - 20, y + 45)
        c.line(x - 10, y + 15, x - 10, y + 55)
        c.line(x, y + 25, x, y + 45)
        c.line(x + 10, y + 15, x + 10, y + 55)
        c.line(x + 20, y + 25, x + 20, y + 45)
        c.line(x + 30, y + 15, x + 30, y + 55)
        c.line(x + 40, y + 25, x + 40, y + 45)
        c.line(x + 50, y + 15, x + 50, y + 55)
        c.line(x + 60, y + 25, x + 60, y + 45)
        c.line(x + 70, y + 15, x + 70, y + 55)
        c.line(x + 70, y + 35, x + 85, y + 35)
        c.line(x + 85, y + 35, x + 85, y)
        c.line(x + 85, y, x + 40, y)
        c.line(x + 40, y, x + 40, y - 10)
        x += 100
        y += 40
        c.setFont('Helvetica', 14)
        c.drawString(x - 120, y + 70, "1 x Battery")
        c.setFont('Helvetica', 10)

        cur.execute('SELECT make FROM Batteryspecifications where Battery=?', battery)
        bmake = cur.fetchone()[0]
        c.drawString(x - 120, y + 55, "Make: %s" % bmake)

        cur.execute('SELECT model FROM Batteryspecifications where Battery=?', battery)
        bmodel = cur.fetchone()[0]
        c.drawString(x - 120, y + 40, "Model: %s" % bmodel)

        cur.execute('SELECT CapacityatDoDkWh FROM Batteryspecifications where Battery=?', battery)
        bcap = cur.fetchone()[0]
        c.drawString(x - 120, y + 25, "Capacity: %s kWh" % bcap)

    ## draw array and associated switches
    def draw_array(x, y, arrayno, arraymodules, panelspec, strings):

        c.rect(x, y, 150, 170)
        c.line(x + 35, y + 125, x + 35, y + 160)
        c.line(x + 45, y + 130, x + 45, y + 155)
        c.line(x + 35, y + 142.5, x + 5, y + 142.5)
        c.line(x + 45, y + 142.5, x + 75, y + 142.5)

        c.drawString(x + 80, array_height + 145, 'Array %d' % arrayno)
        c.setFont('Helvetica', 7)

        ##c.drawString(x + 5, y + 5, 'w/ Built-In Optimisers')
        c.drawString(x + 5, y + 20, 'Isc')

        c.drawString(x + 60, y + 20, '=  %.2fA' % arrayisc)
        c.drawString(x + 5, y + 35, 'Voc')
        c.drawString(x + 60, y + 35, '=  %.2fV' % arrayvoc)
        c.drawString(x + 5, y + 50, 'Voc(-10C)')
        c.drawString(x + 60, y + 50, '=  %.2fV' % arrayvocminus10)

        cur.execute('SELECT PmaxW FROM Panelspecifications where Panel=?', panelspec)
        arraymodulerating = cur.fetchone()[0]
        c.drawString(x + 5, y + 65, '%d x %dW modules' % (arraymodules, arraymodulerating))

        cur.execute('SELECT Model FROM Panelspecifications where Panel=?', panelspec)
        arraymodelnumber = cur.fetchone()[0]
        c.drawString(x + 5, y + 80, '%s' % arraymodelnumber)

        cur.execute('SELECT Manufacturer FROM Panelspecifications where Panel=?', panelspec)
        arraymanufacturer = cur.fetchone()[0]
        c.drawString(x + 5, y + 95, '%d/ String/s of %s' % (strings, arraymanufacturer))

        draw_switch(x + 65, array_height - 50, 180)
        draw_switch(x + 95, array_height - 50, 180)
        draw_switch(x + 65, array_height - 100, 180)
        draw_switch(x + 95, array_height - 100, 180)
        c.setDash(array=[3], phase=13)
        c.line(x + 65, array_height - 107, x + 95, array_height - 107)
        c.line(x + 65, array_height - 57, x + 95, array_height - 57)
        c.setDash(array=[], phase=0)
        if arrayno == 1:
            x += 120
            c.drawString(x - 15, array_height - 50, 'Rooftop DC Isolator')
            c.drawString(x - 15, array_height - 65, '1200V 32A')
            c.drawString(x - 15, array_height - 100, 'Inverter DC Isolator')
            c.drawString(x - 15, array_height - 115, '1200V 32A')
            x += -120
        else:

            c.drawString(x - 5, array_height - 50, 'Rooftop DC Isolator')
            c.drawString(x - 5, array_height - 65, '1200V 32A')
            c.drawString(x - 5, array_height - 100, 'Inverter DC Isolator')
            c.drawString(x - 5, array_height - 115, '1200V 32A')
        c.circle(x + 65, array_height, 2, stroke=1, fill=0)
        c.circle(x + 95, array_height, 2, stroke=1, fill=0)
        c.setFont('Helvetica', 12)

    ## draw arrays and wires when there are 4 arrays required
    def draw_small_array(x, y, arrayno, arraymodules1, arraymodules2, panelspec, strings1, strings2):

        c.setFont('Helvetica', 12)
        c.rect(x, y, 120, 140)
        c.line(x + 30, y + 105, x + 30, y + 135)
        c.line(x + 37, y + 110, x + 37, y + 130)
        c.line(x + 30, y + 120, x + 10, y + 120)
        c.line(x + 37, y + 120, x + 55, y + 120)
        c.drawString(x + 70, y + 115, 'Array %d' % arrayno)
        c.setFont('Helvetica', 7)
        ##c.drawString(x + 5, y + 5, 'w/ Built-In Optimisers')

        c.drawString(x + 5, y + 20, 'Isc')
        cur.execute('SELECT IscA FROM Panelspecifications where Panel=?', panelspec)
        arrayisc = cur.fetchone()[0]
        c.drawString(x + 60, y + 20, '=  %.2fA' % arrayisc)

        c.drawString(x + 5, y + 35, 'Voc')
        cur.execute('SELECT VocV FROM Panelspecifications where Panel=?', panelspec)
        arrayvoc = cur.fetchone()[0]
        c.drawString(x + 60, y + 35, '=  %.2fV' % arrayvoc)

        c.drawString(x + 5, y + 50, 'Voc(-10C)')
        cur.execute('SELECT Voctemperaturecoeffcient_pc_per_C FROM Panelspecifications where Panel=?', panelspec)
        arrayvocminus10 = cur.fetchone()[0]
        c.drawString(x + 60, y + 50, '=  %.2fV' % arrayvocminus10)

        cur.execute('SELECT PmaxW FROM Panelspecifications where Panel=?', panelspec)
        arraymodulerating = cur.fetchone()[0]
        c.drawString(x + 5, y + 65, '%d x %dW modules' % (arraymodules1, arraymodulerating))

        cur.execute('SELECT Model FROM Panelspecifications where Panel=?', panelspec)
        arraymodelnumber = cur.fetchone()[0]
        c.drawString(x + 5, y + 80, '%s' % arraymodelnumber)

        cur.execute('SELECT Manufacturer FROM Panelspecifications where Panel=?', panelspec)
        arraymanufacturer = cur.fetchone()[0]
        c.drawString(x + 5, y + 95, '%d/ String/s of %s' % (strings1, arraymanufacturer))

        draw_switch(x + 35, y - 40, 180)
        draw_switch(x + 65, y - 40, 180)
        draw_switch(x + 35, y - 90, 180)
        draw_switch(x + 65, y - 90, 180)
        c.setDash(array=[3], phase=13)
        c.line(x + 35, y - 97, x + 65, y - 97)
        c.line(x + 35, y - 47, x + 65, y - 47)
        c.setDash(array=[], phase=0)
        c.drawString(x + 90, y - 40, 'Rooftop DC Isolator')
        c.drawString(x + 90, y - 55, '1200V 32A')
        c.drawString(x + 90, y - 90, 'Inverter DC Isolator')
        c.drawString(x + 90, y - 105, '1200V 32A')
        c.circle(x + 35, y, 2, stroke=1, fill=0)
        c.circle(x + 65, y, 2, stroke=1, fill=0)
        c.setFont('Helvetica', 12)

        c.line(x + 35, y - 2, x + 35, y - 38)
        c.line(x + 35, y - 57, x + 35, y - 88)
        c.line(x + 35, y - 107, x + 35, y - 170)
        c.line(x + 35, y - 170, x + 70, y - 170)
        c.line(x + 70, y - 170, x + 70, y - 185)

        c.line(x + 65, y - 2, x + 65, y - 38)
        c.line(x + 65, y - 57, x + 65, y - 88)
        c.line(x + 65, y - 107, x + 65, y - 157.5)
        c.line(x + 65, y - 157.5, x + 82.5, y - 157.5)
        c.line(x + 82.5, y - 157.5, x + 82.5, y - 185)

        x += 130
        arrayno += 1
        c.setFont('Helvetica', 12)
        c.circle(x + 35, y, 2, stroke=1, fill=0)
        c.circle(x + 65, y, 2, stroke=1, fill=0)
        c.rect(x, y, 120, 140)
        c.line(x + 30, y + 105, x + 30, y + 135)
        c.line(x + 37, y + 110, x + 37, y + 130)
        c.line(x + 30, y + 120, x + 10, y + 120)
        c.line(x + 37, y + 120, x + 55, y + 120)
        c.drawString(x + 70, y + 115, 'Array %d' % arrayno)
        c.setFont('Helvetica', 7)
        ##c.drawString(x + 5, y + 5, 'w/ Built-In Optimisers')

        c.drawString(x + 5, y + 20, 'Isc')
        cur.execute('SELECT IscA FROM Panelspecifications where Panel=?', panelspec)
        arrayisc = cur.fetchone()[0]
        c.drawString(x + 60, y + 20, '=  %.2fA' % arrayisc)

        c.drawString(x + 5, y + 35, 'Voc')
        cur.execute('SELECT VocV FROM Panelspecifications where Panel=?', panelspec)
        arrayvoc = cur.fetchone()[0]
        c.drawString(x + 60, y + 35, '=  %.2fV' % arrayvoc)

        c.drawString(x + 5, y + 50, 'Voc(-10C)')
        cur.execute('SELECT Voctemperaturecoeffcient_pc_per_C FROM Panelspecifications where Panel=?', panelspec)
        arrayvocminus10 = cur.fetchone()[0]
        c.drawString(x + 60, y + 50, '=  %.2fV' % arrayvocminus10)

        cur.execute('SELECT PmaxW FROM Panelspecifications where Panel=?', panelspec)
        arraymodulerating = cur.fetchone()[0]
        c.drawString(x + 5, y + 65, '%d x %dW modules' % (arraymodules2, arraymodulerating))

        cur.execute('SELECT Model FROM Panelspecifications where Panel=?', panelspec)
        arraymodelnumber = cur.fetchone()[0]
        c.drawString(x + 5, y + 80, '%s' % arraymodelnumber)

        cur.execute('SELECT Manufacturer FROM Panelspecifications where Panel=?', panelspec)
        arraymanufacturer = cur.fetchone()[0]
        c.drawString(x + 5, y + 95, '%d/ String/s of %s' % (strings2, arraymanufacturer))

        draw_switch(x + 35, y - 40, 180)
        draw_switch(x + 65, y - 40, 180)
        draw_switch(x + 35, y - 90, 180)
        draw_switch(x + 65, y - 90, 180)
        c.setDash(array=[3], phase=13)
        c.line(x + 35, y - 97, x + 65, y - 97)
        c.line(x + 35, y - 47, x + 65, y - 47)
        c.setDash(array=[], phase=0)

        c.line(x + 35, y - 2, x + 35, y - 38)
        c.line(x + 35, y - 57, x + 35, y - 88)
        c.line(x + 35, y - 107, x + 35, y - 120)
        c.line(x + 35, y - 120, x - 35, y - 120)
        c.line(x - 35, y - 120, x - 35, y - 185)

        c.line(x + 65, y - 2, x + 65, y - 38)
        c.line(x + 65, y - 57, x + 65, y - 88)
        c.line(x + 65, y - 107, x + 65, y - 132.5)
        c.line(x + 65, y - 132.5, x - 22.5, y - 132.5)
        c.line(x - 22.5, y - 132.5, x - 22.5, y - 185)

    ##draw inverter function
    def draw_inverter(x, y, inverter, inverterno, batt):

        c.rect(x, y, 75, 75)
        c.line(x, y, x + 75, y + 75)
        c.drawImage(sinepath, x + 45, y + 5, width=25, height=25)
        c.line(x + 5, y + 55, x + 35, y + 55)
        c.line(x + 5, y + 45, x + 15, y + 45)
        c.line(x + 25, y + 45, x + 35, y + 45)
        ##label
        x += 200
        y += -15
        if batt == 'N':
            c.setFont('Helvetica', 14)
            c.drawString(x - 120, y + 80, "1 x Inverter")
            c.setFont('Helvetica', 7)

            cur.execute('SELECT Make FROM Inverterspecifications where Inverter =?', inverter)
            imake = cur.fetchone()[0]
            c.drawString(x - 120, y + 65, "Make: %s" % imake)

            cur.execute('SELECT Series FROM Inverterspecifications where Inverter =?', inverter)
            iseries = cur.fetchone()[0]
            c.drawString(x - 120, y + 50, "Series: %s" % iseries)

            c.drawString(x - 120, y + 35, "Model:")
            cur.execute('SELECT Model FROM Inverterspecifications where Inverter =?', inverter)
            imodel = cur.fetchone()[0]
            c.setFont('Helvetica', 6)
            c.drawString(x - 120, y + 23, "%s" % imodel)

            c.setFont('Times-Italic', 6)
            if inverterno == 1 and current == 'DC' and battery > 0:
                c.drawString(x - 45, y + 80, "When network is down inverter")
                c.drawString(x - 45, y + 72, "isolates from the grid and")
                c.drawString(x - 45, y + 64, "can only power essential loads")
            if inverterno == 1 and current == 'AC' and battery > 0:
                c.drawString(x - 45, y + 80, "*Inverter isolates in ")
                c.drawString(x - 45, y + 72, "the event of blackout")

    ## draw most of the wriing and components that are common to all systems
    def basic_wiring(x, y):

        ##earth-CN
        c.line(530, 70, 570, 70)
        c.line(550, 70, 550, 210)
        c.line(535, 65, 565, 65)
        c.line(540, 60, 560, 60)
        c.line(550, 210, 480, 210)
        c.circle(480, 210, 2, stroke=1, fill=1)

        ## customer neutral link
        c.setFont('Helvetica', 8)
        c.drawString(420, 230, 'Customer Neutral')
        c.circle(430, 210, 2, stroke=1, fill=1)
        c.rect(430, 200, 50, 20)

        ##neutrallink/servicefuse
        c.rect(85, 40, 20, 40)
        c.rect(115, 40, 20, 40)
        c.setFont('Helvetica', 7)
        c.drawRightString(75, 60, 'Neutral Link')
        c.drawString(140, 60, 'Service')
        c.drawString(140, 45, 'Fuse')

        ##NDS
        c.setFillColor(black)
        c.setFont('Helvetica', 8)
        c.drawString(45, 15, 'Normal Distribution Supply')

        ## always there wiring
        # circle to NL / SF
        c.line(95, 80, 95, 110)
        c.line(125, 80, 125, 110)
        # NL / SF to nds
        c.line(95, 40, 95, 30)
        c.line(125, 40, 125, 30)
        c.circle(95, 30, 2)
        c.circle(125, 30, 2)

        ##main circle
        c.circle(110, 130, 25, stroke=1, fill=0)
        c.setFont('Helvetica', 18)
        c.drawString(103, 122, "M")

        ##customers final subcircuits
        c.line(370, 100, 370, 50)
        c.circle(370, 100, 2, stroke=1, fill=1)
        c.drawImage(trianglepath, 367, 44, width=7, height=7)
        c.line(400, 100, 400, 50)
        c.circle(400, 100, 2, stroke=1, fill=1)
        c.drawImage(trianglepath, 397, 44, width=7, height=7)
        c.line(430, 100, 430, 50)
        c.circle(430, 100, 2, stroke=1, fill=1)
        c.drawImage(trianglepath, 427, 44, width=7, height=7)
        c.setFillColor(black)
        c.setFont('Helvetica', 8)
        c.drawCentredString(400, 25, "Customer's Final")
        c.drawCentredString(400, 15, 'Subcircuits')
        c.setFont('Helvetica', 12)

        draw_reposit()

    ## main meat of the wiring. depends on variables taken from main design tool.
    def complex_wiring(phase, array, battery, inverterno, array_height, current):

        if phase == 1:
            if array == 1:
                draw_array(25, array_height, 1, array_1_length, panelspec, array_1_strings)
                if battery == 0:
                    ##wiring
                    x = 25
                    c.circle(x + 65, array_height - 180, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, array_height - 180, 2, stroke=1, fill=1)
                    c.line(x + 65, array_height - 2, x + 65, array_height - 48)
                    c.line(x + 95, array_height - 2, x + 95, array_height - 48)
                    c.line(x + 65, array_height - 67, x + 65, array_height - 98)
                    c.line(x + 95, array_height - 67, x + 95, array_height - 98)
                    c.line(x + 65, array_height - 117, x + 65, array_height - 178)
                    c.line(x + 77.5, array_height - 129.5, x + 77.5, array_height - 178)
                    c.line(x + 77.5, array_height - 129.5, x + 95, array_height - 129.5)
                    c.line(x + 95, array_height - 129.5, x + 95, array_height - 117)
                    draw_inverter(75, 375, inverter1, inverterno, 'N')

                    ##BOTTOM
                    draw_switch(250, 310, 0)
                    draw_switch(250, 250, 0)
                    c.setFont('Helvetica', 7)
                    c.drawString(260, 320, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(260, 305, "%s" % i1iso)

                    c.drawString(260, 260, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(260, 245, "%s" % SSiso)

                    draw_arc(250, 210)
                    draw_switch(180, 185, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(187.5, 170, 'Main Switch')
                    c.circle(250, 185, 2, stroke=1, fill=1)
                    c.circle(225, 210, 2, stroke=1, fill=1)

                    c.line(250, 185, 250, 248)
                    c.line(250, 266, 250, 308)
                    c.line(250, 327, 250, 360)
                    c.line(250, 360, 130, 360)
                    c.line(130, 360, 130, 375)

                    c.line(225, 210, 225, 340)
                    c.line(225, 340, 110, 340)
                    c.line(110, 340, 110, 375)

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 242.5, 210)
                    c.line(257.5, 210, 430, 210)

                    c.line(125, 150, 125, 185)
                    c.line(125, 185, 177.5, 185)
                    c.line(197.5, 185, 300, 185)
                    c.line(300, 185, 300, 100)
                    c.line(300, 100, 430, 100)

                if battery == 1 and current == 'DC':
                    x = 25
                    c.circle(x + 65, array_height - 180, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, array_height - 180, 2, stroke=1, fill=1)
                    c.line(x + 65, array_height - 2, x + 65, array_height - 48)
                    c.line(x + 95, array_height - 2, x + 95, array_height - 48)
                    c.line(x + 65, array_height - 67, x + 65, array_height - 98)
                    c.line(x + 95, array_height - 67, x + 95, array_height - 98)
                    c.line(x + 65, array_height - 117, x + 65, array_height - 178)
                    c.line(x + 77.5, array_height - 129.5, x + 77.5, array_height - 178)
                    c.line(x + 77.5, array_height - 129.5, x + 95, array_height - 129.5)
                    c.line(x + 95, array_height - 129.5, x + 95, array_height - 117)
                    draw_battery(400, 550, batteryl)

                    c.line(410, array_height - 90, 410, array_height - 145)
                    c.line(410, array_height - 145, x + 280, array_height - 145)
                    c.line(x + 261, array_height - 145, x + 95, array_height - 145)
                    c.line(x + 95, array_height - 145, x + 95, array_height - 178)
                    draw_switch(x + 263, array_height - 145, 270)

                    c.circle(x + 95, array_height - 180, 2, stroke=1, fill=1)

                    draw_inverter(75, 375, inverter1, inverterno, 'N')
                    c.circle(x + 105, array_height - 180, 2, stroke=1, fill=1)
                    c.line(x + 415, array_height - 90, x + 415, array_height - 165)
                    c.line(x + 415, array_height - 165, x + 280, array_height - 165)
                    c.line(x + 261, array_height - 165, x + 105, array_height - 165)
                    c.line(x + 105, array_height - 165, x + 105, array_height - 180)
                    draw_switch(x + 263, array_height - 165, 270)
                    c.setFont('Helvetica', 7)
                    c.drawString(x + 240, array_height - 110, 'Battery DC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', BatteryDCIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(x + 240, array_height - 125, '1200V 32A')
                    c.setFont('Helvetica', 12)
                    c.setDash(array=[3], phase=13)
                    c.line(x + 270, array_height - 145, x + 270, array_height - 165)
                    c.setDash(array=[], phase=0)

                    ##BOTTOM
                    draw_switch(225, 310, 0)
                    draw_switch(225, 250, 0)
                    c.setFont('Helvetica', 7)
                    c.drawString(235, 320, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(235, 305, '%s' % i1iso)

                    c.drawString(235, 260, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(235, 245, '%s' % SSiso)

                    draw_arc(225, 210)
                    draw_switch(155, 185, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(162.5, 170, 'Main Switch')
                    c.circle(225, 185, 2, stroke=1, fill=1)
                    c.circle(200, 210, 2, stroke=1, fill=1)

                    ##inv switch line
                    c.line(225, 185, 225, 248)
                    c.line(225, 266, 225, 308)
                    c.line(225, 327, 225, 340)
                    c.line(225, 340, 110, 340)
                    c.line(110, 340, 110, 375)

                    ##main line
                    c.line(200, 210, 200, 320)
                    c.line(200, 320, 90, 320)
                    c.line(90, 320, 90, 375)

                    ##out of m into CN
                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 217.5, 210)
                    c.line(232.5, 210, 372.5, 210)
                    draw_arc(380, 210)
                    c.line(387.5, 210, 430, 210)

                    ##into CFS
                    c.line(125, 150, 125, 185)
                    c.line(125, 185, 152.5, 185)
                    c.line(172.5, 185, 275, 185)
                    c.line(275, 185, 275, 100)
                    c.line(275, 100, 430, 100)

                    ##L1 P1 Line
                    c.line(130, 375, 130, 360)
                    c.line(130, 360, 380, 360)
                    c.line(380, 360, 380, 327.5)
                    draw_switch(380, 310, 0)

                    c.setFont('Helvetica', 6)
                    c.drawString(390, 320, 'EPS AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', EPSACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(390, 305, '%s' % i1iso)
                    c.setFont('Helvetica', 7)

                    c.line(380, 307.5, 380, 278)
                    draw_switch(380, 260, 0)
                    c.line(380, 258, 380, 190)
                    c.line(380, 190, 450, 190)
                    c.line(450, 190, 450, 100)
                    c.line(450, 100, 500, 100)

                    c.line(470, 100, 470, 50)
                    c.circle(470, 100, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 467, 44, width=7, height=7)
                    c.line(500, 100, 500, 50)
                    c.circle(500, 100, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 497, 44, width=7, height=7)
                    c.drawCentredString(470, 110, 'L1')
                    c.drawCentredString(500, 110, 'L1')

                if battery == 1 and current == 'AC':
                    x = 25
                    c.circle(x + 65, array_height - 180, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, array_height - 180, 2, stroke=1, fill=1)
                    c.line(x + 65, array_height - 2, x + 65, array_height - 48)
                    c.line(x + 95, array_height - 2, x + 95, array_height - 48)
                    c.line(x + 65, array_height - 67, x + 65, array_height - 98)
                    c.line(x + 95, array_height - 67, x + 95, array_height - 98)
                    c.line(x + 65, array_height - 117, x + 65, array_height - 178)
                    c.line(x + 77.5, array_height - 129.5, x + 77.5, array_height - 178)
                    c.line(x + 77.5, array_height - 129.5, x + 95, array_height - 129.5)
                    c.line(x + 95, array_height - 129.5, x + 95, array_height - 117)
                    draw_inverter(75, 375, inverter1, inverterno, 'N')

                    draw_battery(430, 540, batteryl)
                    draw_inverter(420, 455, inverter2, inverterno, 'Y')

                    ##BOTTOM
                    draw_switch(225, 310, 0)
                    draw_switch(225, 250, 0)
                    c.setFont('Helvetica', 7)
                    c.drawString(235, 320, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(235, 305, '%s' % i1iso)

                    c.drawString(235, 260, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(235, 245, '%s' % SSiso)

                    draw_arc(225, 210)
                    draw_switch(155, 185, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(162.5, 170, 'Main Switch')
                    c.circle(225, 185, 2, stroke=1, fill=1)
                    c.circle(200, 210, 2, stroke=1, fill=1)

                    ##inv switch line
                    c.line(225, 185, 225, 248)
                    c.line(225, 266, 225, 308)
                    c.line(225, 327, 225, 340)
                    c.line(225, 340, 110, 340)
                    c.line(110, 340, 110, 375)

                    ##main line
                    c.line(200, 210, 200, 320)
                    c.line(200, 320, 90, 320)
                    c.line(90, 320, 90, 375)

                    ##out of m into CN
                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 217.5, 210)
                    c.line(232.5, 210, 372.5, 210)
                    draw_arc(380, 210)
                    c.line(387.5, 210, 430, 210)

                    ##into CFS
                    c.line(125, 150, 125, 185)
                    c.line(125, 185, 152.5, 185)
                    c.line(172.5, 185, 275, 185)
                    c.line(275, 185, 275, 100)
                    c.line(275, 100, 430, 100)

                    ##reposit

                    ##battery inverter wiring
                    c.circle(275, 185, 2, stroke=1, fill=1)
                    c.line(275, 185, 380, 185)
                    c.line(380, 185, 380, 307.5)
                    c.line(380, 326.5, 380, 380)
                    c.line(380, 380, 470, 380)
                    c.line(470, 380, 470, 455)

                    draw_switch(380, 310, 0)
                    c.drawString(390, 320, 'Battery AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', BatteryACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(390, 305, '%s' % i1iso)

                    c.circle(355, 210, 2, stroke=1, fill=1)
                    c.line(355, 210, 355, 400)
                    c.line(355, 400, 450, 400)
                    c.line(450, 400, 450, 455)

            if array == 2:
                if battery == 0:
                    draw_array(20, array_height, 1, array_1_length, panelspec, array_1_strings)
                    draw_array(320, array_height, 2, array_2_length, panelspec, array_2_strings)

                    # inverter circles
                    x = 20
                    y = array_height
                    c.circle(x + 65, y - 180, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 180, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 180, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 180, 2, stroke=1, fill=1)

                    ##jagged wiring
                    c.line(x + 77.5, y - 178, x + 77.5, y - 140)
                    c.line(x + 77.5, y - 140, x + 95, y - 140)
                    c.line(x + 95, y - 140, x + 95, y - 117)

                    c.line(x + 90, y - 178, x + 90, y - 152.5)
                    c.line(x + 90, y - 152.5, x + 365, y - 152.5)
                    c.line(x + 365, y - 152.5, x + 365, y - 117)

                    c.line(x + 102.5, y - 178, x + 102.5, y - 165)
                    c.line(x + 102.5, y - 165, x + 395, y - 165)
                    c.line(x + 395, y - 165, x + 395, y - 117)

                    c.circle(x + 65, y, 2, stroke=1, fill=0)
                    c.circle(x + 95, y, 2, stroke=1, fill=0)
                    c.line(x + 65, y - 2, x + 65, y - 48)
                    c.line(x + 95, y - 2, x + 95, y - 48)
                    c.line(x + 65, y - 67, x + 65, y - 98)
                    c.line(x + 95, y - 67, x + 95, y - 98)
                    c.line(x + 65, y - 117, x + 65, y - 178)

                    ##wiring
                    c.line(x + 65, y, x + 65, y - 48)
                    c.line(x + 95, y, x + 95, y - 48)
                    c.line(x + 65, y - 67, x + 65, y - 98)
                    c.line(x + 95, y - 67, x + 95, y - 98)
                    c.line(x + 365, y - 98, x + 365, y - 67)
                    c.line(x + 395, y - 98, x + 395, y - 67)

                    c.line(x + 365, y - 48, x + 365, y - 2)
                    c.line(x + 395, y - 48, x + 395, y - 2)
                    draw_inverter(75, 375, inverter1, inverterno, 'N')

                    ##BOTTOM
                    draw_switch(250, 310, 0)
                    draw_switch(250, 250, 0)
                    c.setFont('Helvetica', 7)
                    c.drawString(260, 320, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(260, 305, '%s' % i1iso)

                    c.drawString(260, 260, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(260, 245, '%s' % SSiso)

                    draw_arc(250, 210)
                    draw_switch(180, 185, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(187.5, 170, 'Main Switch')
                    c.circle(250, 185, 2, stroke=1, fill=1)
                    c.circle(225, 210, 2, stroke=1, fill=1)

                    c.line(250, 185, 250, 248)
                    c.line(250, 266, 250, 308)
                    c.line(250, 327, 250, 360)
                    c.line(250, 360, 130, 360)
                    c.line(130, 360, 130, 375)

                    c.line(225, 210, 225, 340)
                    c.line(225, 340, 110, 340)
                    c.line(110, 340, 110, 375)

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 242.5, 210)
                    c.line(257.5, 210, 430, 210)

                    c.line(125, 150, 125, 185)
                    c.line(125, 185, 177.5, 185)
                    c.line(197.5, 185, 300, 185)
                    c.line(300, 185, 300, 100)
                    c.line(300, 100, 430, 100)

                if battery == 1 and current == 'DC':
                    x = 20
                    y = array_height
                    draw_array(x, array_height, 1, array_1_length, panelspec, array_1_strings)
                    draw_array(x + 200, array_height, 2, array_2_length, panelspec, array_2_strings)
                    draw_battery(x + 430, 550, batteryl)
                    draw_inverter(x + 60, 350, inverter1, inverterno, 'N')
                    c.circle(x + 65, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 115, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 127.5, y - 205, 2, stroke=1, fill=1)

                    c.line(490, array_height - 90, 490, 450)
                    c.line(490, 450, x + 367, 450)

                    c.line(x + 440, array_height - 90, x + 440, array_height - 165)
                    c.line(x + 440, array_height - 165, x + 367, array_height - 165)
                    c.line(x + 348, array_height - 165, x + 115, array_height - 165)
                    c.line(x + 115, array_height - 165, x + 115, 427)

                    c.line(x + 65, array_height - 2, x + 65, array_height - 48)
                    c.line(x + 95, array_height - 2, x + 95, array_height - 48)
                    c.line(x + 65, array_height - 67, x + 65, array_height - 98)
                    c.line(x + 95, array_height - 67, x + 95, array_height - 98)

                    c.line(x + 65, array_height - 117, x + 65, array_height - 205)
                    c.line(x + 77.5, array_height - 125, x + 77.5, array_height - 205)
                    c.line(x + 77.5, array_height - 125, x + 95, array_height - 125)
                    c.line(x + 95, array_height - 125, x + 95, array_height - 117)

                    c.line(x + 102.5, y - 205, x + 102.5, y - 150)
                    c.line(x + 102.5, y - 150, x + 295, y - 150)
                    c.line(x + 295, y - 150, x + 295, y - 117)

                    c.line(x + 265, y - 2, x + 265, y - 48)
                    c.line(x + 295, y - 2, x + 295, y - 48)
                    c.line(x + 265, y - 67, x + 265, y - 98)
                    c.line(x + 295, y - 67, x + 295, y - 98)
                    c.line(x + 265, y - 117, x + 265, y - 137.5)

                    c.line(x + 90, y - 205, x + 90, y - 137.5)
                    c.line(x + 90, y - 137.5, x + 265, y - 137.5)
                    c.line(x + 265, y - 137.5, x + 265, y - 117)

                    draw_switch(x + 350, y - 165, 270)
                    draw_switch(x + 350, y - 180, 270)

                    c.line(x + 127.5, 450, x + 127.5, 427)
                    c.line(x + 127.5, 450, x + 348, 450)

                    c.line(x + 127.5, 450, x + 127.5, 427)
                    c.line(x + 127.5, 450, x + 348, 450)

                    c.setFont('Helvetica', 7)
                    c.drawString(x + 330, array_height - 125, 'Battery DC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', BatteryDCIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(x + 330, array_height - 140, '1200V 32A')
                    c.setFont('Helvetica', 12)
                    c.setDash(array=[3], phase=13)
                    c.line(x + 357, array_height - 165, x + 357, array_height - 180)
                    c.setDash(array=[], phase=0)

                    ##BOTTOM

                    ##inv switch line
                    draw_switch(225, 280, 0)
                    draw_switch(225, 240, 0)
                    c.setFont('Helvetica', 7)
                    c.drawString(235, 290, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(235, 275, '%s' % i1iso)

                    c.drawString(235, 250, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(235, 235, '%s' % SSiso)

                    draw_arc(225, 210)
                    draw_switch(155, 185, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(162.5, 170, 'Main Switch')
                    c.circle(225, 185, 2, stroke=1, fill=1)
                    c.circle(200, 210, 2, stroke=1, fill=1)

                    c.line(225, 185, 225, 238)
                    c.line(225, 256, 225, 278)
                    c.line(225, 297, 225, 290)
                    c.line(225, 290, 110, 290)
                    c.line(110, 290, 110, 350)

                    ##main line
                    c.line(200, 210, 200, 280)
                    c.line(200, 280, 90, 280)
                    c.line(90, 280, 90, 350)

                    ##out of m into CN
                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 217.5, 210)
                    c.line(232.5, 210, 372.5, 210)
                    draw_arc(380, 210)
                    c.line(387.5, 210, 430, 210)

                    ##into CFS
                    c.line(125, 150, 125, 185)
                    c.line(125, 185, 152.5, 185)
                    c.line(172.5, 185, 275, 185)
                    c.line(275, 185, 275, 100)
                    c.line(275, 100, 430, 100)

                    ##L1 P1 Line
                    c.line(130, 350, 130, 335)
                    c.line(130, 335, 380, 335)
                    c.line(380, 335, 380, 313)
                    draw_switch(380, 295, 0)
                    c.setFont('Helvetica', 6)
                    c.drawString(390, 305, 'EPS AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', EPSACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(390, 290, '%s' % i1iso)
                    c.setFont('Helvetica', 7)

                    c.line(380, 292, 380, 262)
                    draw_switch(380, 245, 0)
                    c.line(380, 243, 380, 160)
                    c.line(380, 160, 450, 160)
                    c.line(450, 160, 450, 100)
                    c.line(450, 100, 500, 100)

                    c.line(470, 100, 470, 50)
                    c.circle(470, 100, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 467, 44, width=7, height=7)
                    c.line(500, 100, 500, 50)
                    c.circle(500, 100, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 497, 44, width=7, height=7)
                    c.drawCentredString(470, 110, 'L1')
                    c.drawCentredString(500, 110, 'L1')

                    ##reposit

                if battery == 1 and current == 'AC':
                    x = 20
                    y = array_height
                    draw_array(x, array_height, 1, array_1_length, panelspec, array_1_strings)
                    draw_array(x + 200, array_height, 2, array_2_length, panelspec, array_2_strings)
                    draw_inverter(x + 60, 350, inverter1, inverterno, 'N')
                    draw_battery(430, 540, batteryl)
                    draw_inverter(420, 455, inverter2, inverterno, 'Y')

                    c.circle(x + 65, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 205, 2, stroke=1, fill=1)

                    c.line(x + 65, array_height - 2, x + 65, array_height - 48)
                    c.line(x + 95, array_height - 2, x + 95, array_height - 48)
                    c.line(x + 65, array_height - 67, x + 65, array_height - 98)
                    c.line(x + 95, array_height - 67, x + 95, array_height - 98)

                    c.line(x + 65, array_height - 117, x + 65, array_height - 205)
                    c.line(x + 77.5, array_height - 125, x + 77.5, array_height - 205)
                    c.line(x + 77.5, array_height - 125, x + 95, array_height - 125)
                    c.line(x + 95, array_height - 125, x + 95, array_height - 117)

                    c.line(x + 102.5, y - 205, x + 102.5, y - 150)
                    c.line(x + 102.5, y - 150, x + 295, y - 150)
                    c.line(x + 295, y - 150, x + 295, y - 117)

                    c.line(x + 265, y - 2, x + 265, y - 48)
                    c.line(x + 295, y - 2, x + 295, y - 48)
                    c.line(x + 265, y - 67, x + 265, y - 98)
                    c.line(x + 295, y - 67, x + 295, y - 98)
                    c.line(x + 265, y - 117, x + 265, y - 137.5)

                    c.line(x + 90, y - 205, x + 90, y - 137.5)
                    c.line(x + 90, y - 137.5, x + 265, y - 137.5)
                    c.line(x + 265, y - 137.5, x + 265, y - 117)

                    ##BOTTOM
                    draw_switch(225, 310, 0)
                    draw_switch(225, 250, 0)
                    c.setFont('Helvetica', 7)
                    c.drawString(235, 320, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(235, 305, '%s' % i1iso)

                    c.drawString(235, 260, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(235, 245, '%s' % SSiso)

                    draw_arc(225, 210)
                    draw_switch(155, 185, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(162.5, 170, 'Main Switch')
                    c.circle(225, 185, 2, stroke=1, fill=1)
                    c.circle(200, 210, 2, stroke=1, fill=1)

                    ##inv switch line
                    c.line(225, 185, 225, 248)
                    c.line(225, 266, 225, 308)
                    c.line(225, 327, 225, 340)
                    c.line(225, 340, 110, 340)
                    c.line(110, 340, 110, 350)

                    ##main line
                    c.line(200, 210, 200, 320)
                    c.line(200, 320, 90, 320)
                    c.line(90, 320, 90, 350)

                    ##out of m into CN
                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 217.5, 210)
                    c.line(232.5, 210, 372.5, 210)
                    draw_arc(380, 210)
                    c.line(387.5, 210, 430, 210)

                    ##into CFS
                    c.line(125, 150, 125, 185)
                    c.line(125, 185, 152.5, 185)
                    c.line(172.5, 185, 275, 185)
                    c.line(275, 185, 275, 100)
                    c.line(275, 100, 430, 100)

                    ##battery inverter wiring
                    c.circle(275, 185, 2, stroke=1, fill=1)
                    c.line(275, 185, 380, 185)
                    c.line(380, 185, 380, 307.5)
                    c.line(380, 326.5, 380, 380)
                    c.line(380, 380, 470, 380)
                    c.line(470, 380, 470, 455)

                    draw_switch(380, 310, 0)
                    c.drawString(390, 320, 'Battery AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', BatteryACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(390, 305, '%s' % i1iso)

                    c.circle(355, 210, 2, stroke=1, fill=1)
                    c.line(355, 210, 355, 400)
                    c.line(355, 400, 450, 400)
                    c.line(450, 400, 450, 455)

        if phase == 3:
            if array == 1:
                draw_array(25, array_height, 1, array_1_length, panelspec, array_1_strings)
                if battery == 0:
                    ##top
                    x = 25
                    c.circle(x + 65, array_height - 180, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, array_height - 180, 2, stroke=1, fill=1)
                    c.line(x + 65, array_height - 2, x + 65, array_height - 48)
                    c.line(x + 95, array_height - 2, x + 95, array_height - 48)
                    c.line(x + 65, array_height - 67, x + 65, array_height - 98)
                    c.line(x + 95, array_height - 67, x + 95, array_height - 98)
                    c.line(x + 65, array_height - 117, x + 65, array_height - 178)
                    c.line(x + 77.5, array_height - 129.5, x + 77.5, array_height - 178)
                    c.line(x + 77.5, array_height - 129.5, x + 95, array_height - 129.5)
                    c.line(x + 95, array_height - 129.5, x + 95, array_height - 117)
                    draw_inverter(75, 375, inverter1, inverterno, 'N')

                    ##BOTTOM
                    draw_switch(145, 195, 270)
                    draw_switch(145, 182.5, 270)
                    draw_switch(145, 170, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(152.5, 155, 'Main')
                    c.drawCentredString(152.5, 145, 'Switch')
                    c.circle(245, 210, 2, stroke=1, fill=1)

                    ##main line
                    c.line(245, 210, 245, 310)
                    c.line(245, 310, 85, 310)
                    c.line(85, 310, 85, 375)
                    ##inv switch line

                    c.setFont('Helvetica', 7)
                    c.drawRightString(230, 290, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawRightString(230, 275, '%s' % i1iso)

                    c.drawRightString(230, 245, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawRightString(230, 230, '%s' % SSiso)
                    draw_switch(265, 290, 0)
                    draw_switch(265, 230, 0)
                    c.line(265, 195, 265, 228)
                    c.line(265, 246, 265, 288)
                    c.line(265, 307, 265, 325)
                    c.line(265, 325, 100, 325)
                    c.line(100, 325, 100, 375)

                    draw_switch(285, 290, 0)
                    draw_switch(285, 230, 0)
                    c.line(285, 182.5, 285, 228)
                    c.line(285, 246, 285, 288)
                    c.line(285, 307, 285, 335)
                    c.line(285, 335, 110, 335)
                    c.line(110, 335, 110, 375)

                    draw_switch(305, 290, 0)
                    draw_switch(305, 230, 0)
                    c.line(305, 170, 305, 228)
                    c.line(305, 246, 305, 288)
                    c.line(305, 307, 305, 345)
                    c.line(305, 345, 120, 345)
                    c.line(120, 345, 120, 375)

                    c.setDash(array=[3], phase=13)
                    c.line(265, 297.5, 305, 297.5)
                    c.line(265, 237.5, 305, 237.5)
                    c.setDash(array=[], phase=0)

                    ##out of m into CN
                    ##ac inv arcs
                    draw_arc(265, 210)
                    c.circle(265, 195, 2, stroke=1, fill=1)
                    draw_arc(285, 210)
                    draw_arc(285, 195)
                    c.circle(285, 182.5, 2, stroke=1, fill=1)
                    draw_arc(305, 210)
                    draw_arc(305, 195)
                    draw_arc(305, 182.5)
                    c.circle(305, 170, 2, stroke=1, fill=1)
                    # dc inv arcs
                    # draw_arc(325, 210)
                    # draw_arc(325, 195)
                    # draw_arc(325, 182.5)
                    # draw_arc(325, 170)
                    # c.line(312.5, 210, 317.5, 210)
                    # c.line(312.5, 195, 317.5, 195)
                    # c.line(312.5, 182.5, 317.5, 182.5)
                    # c.line(332.5, 170, 370, 170)

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 257.5, 210)
                    c.line(272.5, 210, 277.5, 210)
                    c.line(292.5, 210, 297.5, 210)
                    c.line(312.5, 210, 430, 210)

                    c.line(105, 150, 105, 195)
                    c.line(105, 195, 144, 195)
                    c.line(162, 195, 277.5, 195)
                    c.line(292.5, 195, 297.5, 195)
                    c.line(312.5, 195, 430, 195)
                    c.line(430, 195, 430, 100)

                    c.line(115, 150, 115, 182.5)
                    c.line(115, 182.5, 144, 182.5)
                    c.line(162, 182.5, 217.5, 182.5)
                    c.line(232.5, 182.5, 297.5, 182.5)
                    c.line(312.5, 182.5, 400, 182.5)
                    c.line(400, 182.5, 400, 100)

                    c.line(125, 150, 125, 170)
                    c.line(125, 170, 144, 170)
                    c.line(162, 170, 197.5, 170)
                    c.line(212.5, 170, 217.5, 170)
                    c.line(232.5, 170, 370, 170)
                    c.line(370, 170, 370, 100)

                    # ball to repo
                    c.line(185, 167.5, 185, 30)
                    c.line(205, 177.5, 205, 40)
                    c.line(225, 187.5, 225, 50)
                    c.line(185, 30, 300, 30)
                    c.line(205, 40, 300, 40)
                    c.line(225, 50, 300, 50)

                    # repo to VR
                    c.line(335, 55, 335, 150)
                    c.line(335, 150, 363.5, 150)
                    c.line(378.5, 150, 392.5, 150)
                    c.line(407.5, 150, 423.5, 150)

                    c.line(340, 55, 340, 135)
                    c.line(340, 135, 363.5, 135)
                    c.line(378.5, 135, 393.5, 135)

                    c.line(345, 55, 345, 120)
                    c.line(345, 120, 363.5, 120)

                if battery == 1 and current == 'DC':
                    x = 25
                    c.circle(x + 65, array_height - 180, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, array_height - 180, 2, stroke=1, fill=1)
                    c.line(x + 65, array_height - 2, x + 65, array_height - 48)
                    c.line(x + 95, array_height - 2, x + 95, array_height - 48)
                    c.line(x + 65, array_height - 67, x + 65, array_height - 98)
                    c.line(x + 95, array_height - 67, x + 95, array_height - 98)
                    c.line(x + 65, array_height - 117, x + 65, array_height - 178)
                    c.line(x + 77.5, array_height - 129.5, x + 77.5, array_height - 178)
                    c.line(x + 77.5, array_height - 129.5, x + 95, array_height - 129.5)
                    c.line(x + 95, array_height - 129.5, x + 95, array_height - 117)
                    draw_battery(400, 550, batteryl)

                    c.line(410, array_height - 90, 410, array_height - 145)
                    c.line(410, array_height - 145, x + 280, array_height - 145)
                    c.line(x + 261, array_height - 145, x + 95, array_height - 145)
                    c.line(x + 95, array_height - 145, x + 95, array_height - 178)
                    draw_switch(x + 263, array_height - 145, 270)

                    c.circle(x + 95, array_height - 180, 2, stroke=1, fill=1)

                    draw_inverter(75, 375, inverter1, inverterno, 'N')
                    c.circle(x + 105, array_height - 180, 2, stroke=1, fill=1)
                    c.line(x + 415, array_height - 90, x + 415, array_height - 165)
                    c.line(x + 415, array_height - 165, x + 280, array_height - 165)
                    c.line(x + 261, array_height - 165, x + 105, array_height - 165)
                    c.line(x + 105, array_height - 165, x + 105, array_height - 180)
                    draw_switch(x + 263, array_height - 165, 270)
                    c.setFont('Helvetica', 7)
                    c.drawString(x + 240, array_height - 110, 'Battery DC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', BatteryDCIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(x + 240, array_height - 125, '1200V 32A')
                    c.setFont('Helvetica', 12)
                    c.setDash(array=[3], phase=13)
                    c.line(x + 270, array_height - 145, x + 270, array_height - 165)
                    c.setDash(array=[], phase=0)

                    ##BOTTOM
                    draw_switch(145, 195, 270)
                    draw_switch(145, 182.5, 270)
                    draw_switch(145, 170, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(152.5, 155, 'Main')
                    c.drawCentredString(152.5, 145, 'Switch')
                    c.circle(245, 210, 2, stroke=1, fill=1)

                    ##main line
                    c.line(245, 210, 245, 310)
                    c.line(245, 310, 85, 310)
                    c.line(85, 310, 85, 375)
                    ##inv switch line

                    c.setFont('Helvetica', 7)
                    c.drawRightString(230, 290, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawRightString(230, 275, '%s' % i1iso)

                    c.drawRightString(230, 245, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawRightString(230, 230, '%s' % SSiso)
                    draw_switch(265, 290, 0)
                    draw_switch(265, 230, 0)
                    c.line(265, 195, 265, 228)
                    c.line(265, 246, 265, 288)
                    c.line(265, 307, 265, 325)
                    c.line(265, 325, 100, 325)
                    c.line(100, 325, 100, 375)

                    draw_switch(285, 290, 0)
                    draw_switch(285, 230, 0)
                    c.line(285, 182.5, 285, 228)
                    c.line(285, 246, 285, 288)
                    c.line(285, 307, 285, 335)
                    c.line(285, 335, 110, 335)
                    c.line(110, 335, 110, 375)

                    draw_switch(305, 290, 0)
                    draw_switch(305, 230, 0)
                    c.line(305, 170, 305, 228)
                    c.line(305, 246, 305, 288)
                    c.line(305, 307, 305, 345)
                    c.line(305, 345, 120, 345)
                    c.line(120, 345, 120, 375)

                    c.setDash(array=[3], phase=13)
                    c.line(265, 297.5, 305, 297.5)
                    c.line(265, 237.5, 305, 237.5)
                    c.setDash(array=[], phase=0)

                    ##out of m into CN
                    ##ac inv arcs
                    draw_arc(265, 210)
                    c.circle(265, 195, 2, stroke=1, fill=1)
                    draw_arc(285, 210)
                    draw_arc(285, 195)
                    c.circle(285, 182.5, 2, stroke=1, fill=1)
                    draw_arc(305, 210)
                    draw_arc(305, 195)
                    draw_arc(305, 182.5)
                    c.circle(305, 170, 2, stroke=1, fill=1)

                    draw_arc(325, 210)
                    draw_arc(325, 195)
                    draw_arc(325, 182.5)
                    draw_arc(325, 170)
                    c.line(312.5, 210, 317.5, 210)
                    c.line(312.5, 195, 317.5, 195)
                    c.line(312.5, 182.5, 317.5, 182.5)
                    c.line(332.5, 170, 370, 170)

                    ##L1 P1 Line
                    c.line(130, 375, 130, 360)
                    c.line(130, 360, 325, 360)
                    c.line(325, 360, 325, 327.5)
                    draw_switch(325, 310, 0)
                    c.setFont('Helvetica', 6)
                    c.drawString(335, 305, 'EPS AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', EPSACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(335, 290, '%s' % i1iso)
                    c.setFont('Helvetica', 7)

                    c.line(325, 307.5, 325, 278)
                    draw_switch(325, 260, 0)
                    c.line(325, 258, 325, 125)
                    c.line(325, 125, 250, 125)

                    c.line(250, 125, 250, 75)
                    c.circle(250, 125, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 247, 70, width=7, height=7)
                    c.line(280, 125, 280, 75)
                    c.circle(280, 125, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 277, 70, width=7, height=7)
                    c.drawCentredString(250, 135, 'L1')
                    c.drawCentredString(280, 135, 'P1')

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 257.5, 210)
                    c.line(272.5, 210, 277.5, 210)
                    c.line(292.5, 210, 297.5, 210)
                    c.line(312.5, 210, 317.5, 210)
                    c.line(332.5, 210, 430, 210)

                    c.line(105, 150, 105, 195)
                    c.line(105, 195, 144, 195)
                    c.line(162, 195, 277.5, 195)
                    c.line(292.5, 195, 297.5, 195)
                    c.line(312.5, 195, 317.5, 195)
                    c.line(332.5, 195, 430, 195)
                    c.line(430, 195, 430, 100)

                    c.line(115, 150, 115, 182.5)
                    c.line(115, 182.5, 144, 182.5)
                    c.line(162, 182.5, 217.5, 182.5)
                    c.line(232.5, 182.5, 297.5, 182.5)
                    c.line(312.5, 182.5, 317.5, 182.5)
                    c.line(332.5, 182.5, 400, 182.5)
                    c.line(400, 182.5, 400, 100)

                    c.line(125, 150, 125, 170)
                    c.line(125, 170, 144, 170)
                    c.line(162, 170, 197.5, 170)
                    c.line(212.5, 170, 217.5, 170)
                    c.line(232.5, 170, 317.5, 170)
                    c.line(332.5, 170, 370, 170)
                    c.line(370, 170, 370, 100)

                    ##reposit

                    # ball to repo
                    c.line(185, 167.5, 185, 30)
                    c.line(205, 177.5, 205, 40)
                    c.line(225, 187.5, 225, 50)
                    c.line(185, 30, 300, 30)
                    c.line(205, 40, 300, 40)
                    c.line(225, 50, 300, 50)

                    # repo to VR
                    c.line(335, 55, 335, 150)
                    c.line(335, 150, 363.5, 150)
                    c.line(378.5, 150, 392.5, 150)
                    c.line(407.5, 150, 423.5, 150)

                    c.line(340, 55, 340, 135)
                    c.line(340, 135, 363.5, 135)
                    c.line(378.5, 135, 393.5, 135)

                    c.line(345, 55, 345, 120)
                    c.line(345, 120, 363.5, 120)

                if battery == 1 and current == 'AC':
                    x = 25
                    c.circle(x + 65, array_height - 180, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, array_height - 180, 2, stroke=1, fill=1)
                    c.line(x + 65, array_height - 2, x + 65, array_height - 48)
                    c.line(x + 95, array_height - 2, x + 95, array_height - 48)
                    c.line(x + 65, array_height - 67, x + 65, array_height - 98)
                    c.line(x + 95, array_height - 67, x + 95, array_height - 98)
                    c.line(x + 65, array_height - 117, x + 65, array_height - 178)
                    c.line(x + 77.5, array_height - 129.5, x + 77.5, array_height - 178)
                    c.line(x + 77.5, array_height - 129.5, x + 95, array_height - 129.5)
                    c.line(x + 95, array_height - 129.5, x + 95, array_height - 117)
                    draw_inverter(75, 375, inverter1, inverterno, 'N')

                    draw_battery(430, 540, batteryl)
                    draw_inverter(420, 455, inverter2, inverterno, 'Y')

                    ##BOTTOM
                    draw_switch(145, 195, 270)
                    draw_switch(145, 182.5, 270)
                    draw_switch(145, 170, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(152.5, 155, 'Main')
                    c.drawCentredString(152.5, 145, 'Switch')
                    c.circle(245, 210, 2, stroke=1, fill=1)

                    ##main line
                    c.line(245, 210, 245, 310)
                    c.line(245, 310, 85, 310)
                    c.line(85, 310, 85, 375)
                    ##inv switch line

                    c.setFont('Helvetica', 7)
                    c.drawRightString(230, 290, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawRightString(230, 275, '%s' % i1iso)

                    c.drawRightString(230, 245, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawRightString(230, 230, '%s' % SSiso)
                    draw_switch(265, 290, 0)
                    draw_switch(265, 230, 0)
                    c.line(265, 195, 265, 228)
                    c.line(265, 246, 265, 288)
                    c.line(265, 307, 265, 325)
                    c.line(265, 325, 100, 325)
                    c.line(100, 325, 100, 375)

                    draw_switch(285, 290, 0)
                    draw_switch(285, 230, 0)
                    c.line(285, 182.5, 285, 228)
                    c.line(285, 246, 285, 288)
                    c.line(285, 307, 285, 335)
                    c.line(285, 335, 110, 335)
                    c.line(110, 335, 110, 375)

                    draw_switch(305, 290, 0)
                    draw_switch(305, 230, 0)
                    c.line(305, 170, 305, 228)
                    c.line(305, 246, 305, 288)
                    c.line(305, 307, 305, 345)
                    c.line(305, 345, 120, 345)
                    c.line(120, 345, 120, 375)

                    c.setDash(array=[3], phase=13)
                    c.line(265, 297.5, 305, 297.5)
                    c.line(265, 237.5, 305, 237.5)
                    c.setDash(array=[], phase=0)

                    ##out of m into CN
                    ##ac inv arcs
                    draw_arc(265, 210)
                    c.circle(265, 195, 2, stroke=1, fill=1)
                    draw_arc(285, 210)
                    draw_arc(285, 195)
                    c.circle(285, 182.5, 2, stroke=1, fill=1)
                    draw_arc(305, 210)
                    draw_arc(305, 195)
                    draw_arc(305, 182.5)
                    c.circle(305, 170, 2, stroke=1, fill=1)
                    # dc inv arcs
                    # draw_arc(325, 210)
                    # draw_arc(325, 195)
                    # draw_arc(325, 182.5)
                    # draw_arc(325, 170)
                    # c.line(312.5, 210, 317.5, 210)
                    # c.line(312.5, 195, 317.5, 195)
                    # c.line(312.5, 182.5, 317.5, 182.5)
                    # c.line(332.5, 170, 370, 170)

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 257.5, 210)
                    c.line(272.5, 210, 277.5, 210)
                    c.line(292.5, 210, 297.5, 210)
                    c.line(312.5, 210, 372.5, 210)
                    c.line(387.5, 210, 430, 210)

                    c.line(105, 150, 105, 195)
                    c.line(105, 195, 144, 195)
                    c.line(162, 195, 277.5, 195)
                    c.line(292.5, 195, 297.5, 195)
                    c.line(312.5, 195, 430, 195)
                    c.line(430, 195, 430, 100)

                    c.line(115, 150, 115, 182.5)
                    c.line(115, 182.5, 144, 182.5)
                    c.line(162, 182.5, 217.5, 182.5)
                    c.line(232.5, 182.5, 297.5, 182.5)
                    c.line(312.5, 182.5, 400, 182.5)
                    c.line(400, 182.5, 400, 100)

                    c.line(125, 150, 125, 170)
                    c.line(125, 170, 144, 170)
                    c.line(162, 170, 197.5, 170)
                    c.line(212.5, 170, 217.5, 170)
                    c.line(232.5, 170, 370, 170)
                    c.line(370, 170, 370, 100)

                    ##reposit

                    # ball to repo
                    c.line(185, 167.5, 185, 30)
                    c.line(205, 177.5, 205, 40)
                    c.line(225, 187.5, 225, 50)
                    c.line(185, 30, 300, 30)
                    c.line(205, 40, 300, 40)
                    c.line(225, 50, 300, 50)

                    # repo to VR
                    c.line(335, 55, 335, 150)
                    c.line(335, 150, 363.5, 150)
                    c.line(378.5, 150, 392.5, 150)
                    c.line(407.5, 150, 423.5, 150)

                    c.line(340, 55, 340, 135)
                    c.line(340, 135, 363.5, 135)
                    c.line(378.5, 135, 393.5, 135)

                    c.line(345, 55, 345, 120)
                    c.line(345, 120, 363.5, 120)

                    ##battery inverter wiring
                    c.circle(380, 195, 2, stroke=1, fill=1)
                    c.line(380, 195, 380, 307.5)
                    c.line(380, 326.5, 380, 380)
                    c.line(380, 380, 470, 380)
                    c.line(470, 380, 470, 455)
                    draw_switch(380, 310, 0)
                    c.drawString(390, 320, 'Battery AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', BatteryACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(390, 305, '%s' % i1iso)
                    c.circle(355, 210, 2, stroke=1, fill=1)
                    c.line(355, 210, 355, 400)
                    c.line(355, 400, 450, 400)
                    c.line(450, 400, 450, 455)
                    draw_arc(380, 210)

            if array == 2:
                if battery == 0:
                    # top
                    draw_array(20, array_height, 1, array_1_length, panelspec, array_1_strings)
                    draw_array(320, array_height, 2, array_2_length, panelspec, array_2_strings)
                    # inverter circles
                    x = 20
                    y = array_height
                    c.circle(x + 65, y - 180, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 180, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 180, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 180, 2, stroke=1, fill=1)

                    ##jagged wiring
                    c.line(x + 77.5, y - 178, x + 77.5, y - 140)
                    c.line(x + 77.5, y - 140, x + 95, y - 140)
                    c.line(x + 95, y - 140, x + 95, y - 117)

                    c.line(x + 90, y - 178, x + 90, y - 152.5)
                    c.line(x + 90, y - 152.5, x + 365, y - 152.5)
                    c.line(x + 365, y - 152.5, x + 365, y - 117)

                    c.line(x + 102.5, y - 178, x + 102.5, y - 165)
                    c.line(x + 102.5, y - 165, x + 395, y - 165)
                    c.line(x + 395, y - 165, x + 395, y - 117)

                    c.circle(x + 65, y, 2, stroke=1, fill=0)
                    c.circle(x + 95, y, 2, stroke=1, fill=0)
                    c.line(x + 65, y - 2, x + 65, y - 48)
                    c.line(x + 95, y - 2, x + 95, y - 48)
                    c.line(x + 65, y - 67, x + 65, y - 98)
                    c.line(x + 95, y - 67, x + 95, y - 98)
                    c.line(x + 65, y - 117, x + 65, y - 178)

                    ##wiring
                    c.line(x + 65, y, x + 65, y - 48)
                    c.line(x + 95, y, x + 95, y - 48)
                    c.line(x + 65, y - 67, x + 65, y - 98)
                    c.line(x + 95, y - 67, x + 95, y - 98)
                    c.line(x + 365, y - 98, x + 365, y - 67)
                    c.line(x + 395, y - 98, x + 395, y - 67)

                    c.line(x + 365, y - 48, x + 365, y - 2)
                    c.line(x + 395, y - 48, x + 395, y - 2)
                    draw_inverter(75, 375, inverter1, inverterno, 'N')

                    ##BOTTOM
                    draw_switch(145, 195, 270)
                    draw_switch(145, 182.5, 270)
                    draw_switch(145, 170, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(152.5, 155, 'Main')
                    c.drawCentredString(152.5, 145, 'Switch')
                    c.circle(245, 210, 2, stroke=1, fill=1)

                    ##main line
                    c.line(245, 210, 245, 310)
                    c.line(245, 310, 85, 310)
                    c.line(85, 310, 85, 375)
                    ##inv switch line

                    c.setFont('Helvetica', 7)
                    c.drawRightString(230, 290, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawRightString(230, 275, '%s' % i1iso)

                    c.drawRightString(230, 245, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawRightString(230, 230, '%s' % SSiso)
                    draw_switch(265, 290, 0)
                    draw_switch(265, 230, 0)
                    c.line(265, 195, 265, 228)
                    c.line(265, 246, 265, 288)
                    c.line(265, 307, 265, 325)
                    c.line(265, 325, 100, 325)
                    c.line(100, 325, 100, 375)

                    draw_switch(285, 290, 0)
                    draw_switch(285, 230, 0)
                    c.line(285, 182.5, 285, 228)
                    c.line(285, 246, 285, 288)
                    c.line(285, 307, 285, 335)
                    c.line(285, 335, 110, 335)
                    c.line(110, 335, 110, 375)

                    draw_switch(305, 290, 0)
                    draw_switch(305, 230, 0)
                    c.line(305, 170, 305, 228)
                    c.line(305, 246, 305, 288)
                    c.line(305, 307, 305, 345)
                    c.line(305, 345, 120, 345)
                    c.line(120, 345, 120, 375)

                    c.setDash(array=[3], phase=13)
                    c.line(265, 297.5, 305, 297.5)
                    c.line(265, 237.5, 305, 237.5)
                    c.setDash(array=[], phase=0)

                    ##out of m into CN
                    ##ac inv arcs
                    draw_arc(265, 210)
                    c.circle(265, 195, 2, stroke=1, fill=1)
                    draw_arc(285, 210)
                    draw_arc(285, 195)
                    c.circle(285, 182.5, 2, stroke=1, fill=1)
                    draw_arc(305, 210)
                    draw_arc(305, 195)
                    draw_arc(305, 182.5)
                    c.circle(305, 170, 2, stroke=1, fill=1)
                    # dc inv arcs
                    # draw_arc(325, 210)
                    # draw_arc(325, 195)
                    # draw_arc(325, 182.5)
                    # draw_arc(325, 170)
                    # c.line(312.5, 210, 317.5, 210)
                    # c.line(312.5, 195, 317.5, 195)
                    # c.line(312.5, 182.5, 317.5, 182.5)
                    # c.line(332.5, 170, 370, 170)

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 257.5, 210)
                    c.line(272.5, 210, 277.5, 210)
                    c.line(292.5, 210, 297.5, 210)
                    c.line(312.5, 210, 430, 210)

                    c.line(105, 150, 105, 195)
                    c.line(105, 195, 144, 195)
                    c.line(162, 195, 277.5, 195)
                    c.line(292.5, 195, 297.5, 195)
                    c.line(312.5, 195, 430, 195)
                    c.line(430, 195, 430, 100)

                    c.line(115, 150, 115, 182.5)
                    c.line(115, 182.5, 144, 182.5)
                    c.line(162, 182.5, 217.5, 182.5)
                    c.line(232.5, 182.5, 297.5, 182.5)
                    c.line(312.5, 182.5, 400, 182.5)
                    c.line(400, 182.5, 400, 100)

                    c.line(125, 150, 125, 170)
                    c.line(125, 170, 144, 170)
                    c.line(162, 170, 197.5, 170)
                    c.line(212.5, 170, 217.5, 170)
                    c.line(232.5, 170, 370, 170)
                    c.line(370, 170, 370, 100)

                    ##reposit

                    # ball to repo
                    c.line(185, 167.5, 185, 30)
                    c.line(205, 177.5, 205, 40)
                    c.line(225, 187.5, 225, 50)
                    c.line(185, 30, 300, 30)
                    c.line(205, 40, 300, 40)
                    c.line(225, 50, 300, 50)

                    # repo to VR
                    c.line(335, 55, 335, 150)
                    c.line(335, 150, 363.5, 150)
                    c.line(378.5, 150, 392.5, 150)
                    c.line(407.5, 150, 423.5, 150)

                    c.line(340, 55, 340, 135)
                    c.line(340, 135, 363.5, 135)
                    c.line(378.5, 135, 393.5, 135)

                    c.line(345, 55, 345, 120)
                    c.line(345, 120, 363.5, 120)

                if battery == 1 and current == 'DC':
                    x = 20
                    y = array_height
                    draw_array(x, array_height, 1, array_1_length, panelspec, array_1_strings)
                    draw_array(x + 200, array_height, 2, array_2_length, panelspec, array_2_strings)
                    draw_battery(x + 430, 550, batteryl)
                    draw_inverter(x + 60, 350, inverter1, inverterno, 'N')
                    c.circle(x + 65, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 115, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 127.5, y - 205, 2, stroke=1, fill=1)

                    c.line(490, array_height - 90, 490, 450)
                    c.line(490, 450, x + 367, 450)

                    c.line(x + 440, array_height - 90, x + 440, array_height - 165)
                    c.line(x + 440, array_height - 165, x + 367, array_height - 165)
                    c.line(x + 348, array_height - 165, x + 115, array_height - 165)
                    c.line(x + 115, array_height - 165, x + 115, 427)

                    c.line(x + 65, array_height - 2, x + 65, array_height - 48)
                    c.line(x + 95, array_height - 2, x + 95, array_height - 48)
                    c.line(x + 65, array_height - 67, x + 65, array_height - 98)
                    c.line(x + 95, array_height - 67, x + 95, array_height - 98)

                    c.line(x + 65, array_height - 117, x + 65, array_height - 205)
                    c.line(x + 77.5, array_height - 125, x + 77.5, array_height - 205)
                    c.line(x + 77.5, array_height - 125, x + 95, array_height - 125)
                    c.line(x + 95, array_height - 125, x + 95, array_height - 117)

                    c.line(x + 102.5, y - 205, x + 102.5, y - 150)
                    c.line(x + 102.5, y - 150, x + 295, y - 150)
                    c.line(x + 295, y - 150, x + 295, y - 117)

                    c.line(x + 265, y - 2, x + 265, y - 48)
                    c.line(x + 295, y - 2, x + 295, y - 48)
                    c.line(x + 265, y - 67, x + 265, y - 98)
                    c.line(x + 295, y - 67, x + 295, y - 98)
                    c.line(x + 265, y - 117, x + 265, y - 137.5)

                    c.line(x + 90, y - 205, x + 90, y - 137.5)
                    c.line(x + 90, y - 137.5, x + 265, y - 137.5)
                    c.line(x + 265, y - 137.5, x + 265, y - 117)

                    draw_switch(x + 350, y - 165, 270)
                    draw_switch(x + 350, y - 180, 270)

                    c.line(x + 127.5, 450, x + 127.5, 427)
                    c.line(x + 127.5, 450, x + 348, 450)

                    c.line(x + 127.5, 450, x + 127.5, 427)
                    c.line(x + 127.5, 450, x + 348, 450)

                    c.setFont('Helvetica', 7)
                    c.drawString(x + 330, array_height - 125, 'Battery DC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', BatteryDCIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(x + 330, array_height - 140, '1200V 32A')
                    c.setFont('Helvetica', 12)
                    c.setDash(array=[3], phase=13)
                    c.line(x + 357, array_height - 165, x + 357, array_height - 180)
                    c.setDash(array=[], phase=0)

                    ##BOTTOM
                    draw_switch(145, 195, 270)
                    draw_switch(145, 182.5, 270)
                    draw_switch(145, 170, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(152.5, 155, 'Main')
                    c.drawCentredString(152.5, 145, 'Switch')
                    c.circle(245, 210, 2, stroke=1, fill=1)

                    ##main line
                    c.line(245, 210, 245, 290)
                    c.line(245, 290, 85, 290)
                    c.line(85, 290, 85, 350)
                    ##inv switch line

                    c.setFont('Helvetica', 7)
                    c.drawRightString(230, 275, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawRightString(230, 260, '%s' % i1iso)

                    c.drawRightString(230, 240, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawRightString(230, 225, '%s' % SSiso)
                    draw_switch(265, 275, 0)
                    draw_switch(265, 230, 0)
                    c.line(265, 195, 265, 228)
                    c.line(265, 246, 265, 273)
                    c.line(265, 292, 265, 310)
                    c.line(265, 310, 100, 310)
                    c.line(100, 310, 100, 350)

                    draw_switch(285, 275, 0)
                    draw_switch(285, 230, 0)
                    c.line(285, 182.5, 285, 228)
                    c.line(285, 246, 285, 273)
                    c.line(285, 292, 285, 320)
                    c.line(285, 320, 110, 320)
                    c.line(110, 320, 110, 350)

                    draw_switch(305, 275, 0)
                    draw_switch(305, 230, 0)
                    c.line(305, 170, 305, 228)
                    c.line(305, 246, 305, 273)
                    c.line(305, 292, 305, 330)
                    c.line(305, 330, 120, 330)
                    c.line(120, 330, 120, 350)

                    c.setDash(array=[3], phase=13)
                    c.line(265, 282.5, 305, 282.5)
                    c.line(265, 237.5, 305, 237.5)
                    c.setDash(array=[], phase=0)

                    ##out of m into CN
                    ##ac inv arcs
                    draw_arc(265, 210)
                    c.circle(265, 195, 2, stroke=1, fill=1)
                    draw_arc(285, 210)
                    draw_arc(285, 195)
                    c.circle(285, 182.5, 2, stroke=1, fill=1)
                    draw_arc(305, 210)
                    draw_arc(305, 195)
                    draw_arc(305, 182.5)
                    c.circle(305, 170, 2, stroke=1, fill=1)

                    draw_arc(325, 210)
                    draw_arc(325, 195)
                    draw_arc(325, 182.5)
                    draw_arc(325, 170)
                    c.line(312.5, 210, 317.5, 210)
                    c.line(312.5, 195, 317.5, 195)
                    c.line(312.5, 182.5, 317.5, 182.5)
                    c.line(332.5, 170, 370, 170)

                    ##L1 P1 Line
                    c.line(130, 350, 130, 340)
                    c.line(130, 340, 325, 340)
                    c.line(325, 340, 325, 312.5)
                    draw_switch(325, 295, 0)
                    c.setFont('Helvetica', 6)
                    c.drawString(335, 280, 'EPS AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', EPSACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(335, 265, '%s' % i1iso)
                    c.setFont('Helvetica', 7)

                    c.line(325, 292.5, 325, 263)
                    draw_switch(325, 245, 0)
                    c.line(325, 243, 325, 125)
                    c.line(325, 125, 250, 125)

                    c.line(250, 125, 250, 75)
                    c.circle(250, 125, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 247, 70, width=7, height=7)
                    c.line(280, 125, 280, 75)
                    c.circle(280, 125, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 277, 70, width=7, height=7)
                    c.drawCentredString(250, 135, 'L1')
                    c.drawCentredString(280, 135, 'P1')

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 257.5, 210)
                    c.line(272.5, 210, 277.5, 210)
                    c.line(292.5, 210, 297.5, 210)
                    c.line(312.5, 210, 317.5, 210)
                    c.line(332.5, 210, 430, 210)

                    c.line(105, 150, 105, 195)
                    c.line(105, 195, 144, 195)
                    c.line(162, 195, 277.5, 195)
                    c.line(292.5, 195, 297.5, 195)
                    c.line(312.5, 195, 317.5, 195)
                    c.line(332.5, 195, 430, 195)
                    c.line(430, 195, 430, 100)

                    c.line(115, 150, 115, 182.5)
                    c.line(115, 182.5, 144, 182.5)
                    c.line(162, 182.5, 217.5, 182.5)
                    c.line(232.5, 182.5, 297.5, 182.5)
                    c.line(312.5, 182.5, 317.5, 182.5)
                    c.line(332.5, 182.5, 400, 182.5)
                    c.line(400, 182.5, 400, 100)

                    c.line(125, 150, 125, 170)
                    c.line(125, 170, 144, 170)
                    c.line(162, 170, 197.5, 170)
                    c.line(212.5, 170, 217.5, 170)
                    c.line(232.5, 170, 317.5, 170)
                    c.line(332.5, 170, 370, 170)
                    c.line(370, 170, 370, 100)

                    ##reposit

                    # ball to repo
                    c.line(185, 167.5, 185, 30)
                    c.line(205, 177.5, 205, 40)
                    c.line(225, 187.5, 225, 50)
                    c.line(185, 30, 300, 30)
                    c.line(205, 40, 300, 40)
                    c.line(225, 50, 300, 50)

                    # repo to VR
                    c.line(335, 55, 335, 150)
                    c.line(335, 150, 363.5, 150)
                    c.line(378.5, 150, 392.5, 150)
                    c.line(407.5, 150, 423.5, 150)

                    c.line(340, 55, 340, 135)
                    c.line(340, 135, 363.5, 135)
                    c.line(378.5, 135, 393.5, 135)

                    c.line(345, 55, 345, 120)
                    c.line(345, 120, 363.5, 120)

                if battery == 1 and current == 'AC':
                    x = 20
                    y = array_height
                    draw_array(x, array_height, 1, array_1_length, panelspec, array_1_strings)
                    draw_array(x + 200, array_height, 2, array_2_length, panelspec, array_2_strings)
                    draw_inverter(x + 60, 350, inverter1, inverterno, 'N')

                    draw_battery(430, 540, batteryl)
                    draw_inverter(420, 455, inverter2, inverterno, 'Y')
                    c.circle(x + 65, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 205, 2, stroke=1, fill=1)

                    c.line(x + 65, array_height - 2, x + 65, array_height - 48)
                    c.line(x + 95, array_height - 2, x + 95, array_height - 48)
                    c.line(x + 65, array_height - 67, x + 65, array_height - 98)
                    c.line(x + 95, array_height - 67, x + 95, array_height - 98)

                    c.line(x + 65, array_height - 117, x + 65, array_height - 205)
                    c.line(x + 77.5, array_height - 125, x + 77.5, array_height - 205)
                    c.line(x + 77.5, array_height - 125, x + 95, array_height - 125)
                    c.line(x + 95, array_height - 125, x + 95, array_height - 117)

                    c.line(x + 102.5, y - 205, x + 102.5, y - 150)
                    c.line(x + 102.5, y - 150, x + 295, y - 150)
                    c.line(x + 295, y - 150, x + 295, y - 117)

                    c.line(x + 265, y - 2, x + 265, y - 48)
                    c.line(x + 295, y - 2, x + 295, y - 48)
                    c.line(x + 265, y - 67, x + 265, y - 98)
                    c.line(x + 295, y - 67, x + 295, y - 98)
                    c.line(x + 265, y - 117, x + 265, y - 137.5)

                    c.line(x + 90, y - 205, x + 90, y - 137.5)
                    c.line(x + 90, y - 137.5, x + 265, y - 137.5)
                    c.line(x + 265, y - 137.5, x + 265, y - 117)

                    ##BOTTOM
                    draw_switch(145, 195, 270)
                    draw_switch(145, 182.5, 270)
                    draw_switch(145, 170, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(152.5, 155, 'Main')
                    c.drawCentredString(152.5, 145, 'Switch')
                    c.circle(245, 210, 2, stroke=1, fill=1)

                    ##main line
                    c.line(245, 210, 245, 310)
                    c.line(245, 310, 85, 310)
                    c.line(85, 310, 85, 350)
                    ##inv switch line

                    c.setFont('Helvetica', 7)
                    c.drawRightString(230, 290, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawRightString(230, 275, '%s' % i1iso)

                    c.drawRightString(230, 245, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawRightString(230, 230, '%s' % SSiso)
                    draw_switch(265, 290, 0)
                    draw_switch(265, 230, 0)
                    c.line(265, 195, 265, 228)
                    c.line(265, 246, 265, 288)
                    c.line(265, 307, 265, 325)
                    c.line(265, 325, 100, 325)
                    c.line(100, 325, 100, 350)

                    draw_switch(285, 290, 0)
                    draw_switch(285, 230, 0)
                    c.line(285, 182.5, 285, 228)
                    c.line(285, 246, 285, 288)
                    c.line(285, 307, 285, 335)
                    c.line(285, 335, 110, 335)
                    c.line(110, 335, 110, 350)

                    draw_switch(305, 290, 0)
                    draw_switch(305, 230, 0)
                    c.line(305, 170, 305, 228)
                    c.line(305, 246, 305, 288)
                    c.line(305, 307, 305, 345)
                    c.line(305, 345, 120, 345)
                    c.line(120, 345, 120, 350)

                    c.setDash(array=[3], phase=13)
                    c.line(265, 297.5, 305, 297.5)
                    c.line(265, 237.5, 305, 237.5)
                    c.setDash(array=[], phase=0)

                    ##out of m into CN
                    ##ac inv arcs
                    draw_arc(265, 210)
                    c.circle(265, 195, 2, stroke=1, fill=1)
                    draw_arc(285, 210)
                    draw_arc(285, 195)
                    c.circle(285, 182.5, 2, stroke=1, fill=1)
                    draw_arc(305, 210)
                    draw_arc(305, 195)
                    draw_arc(305, 182.5)
                    c.circle(305, 170, 2, stroke=1, fill=1)

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 257.5, 210)
                    c.line(272.5, 210, 277.5, 210)
                    c.line(292.5, 210, 297.5, 210)
                    c.line(312.5, 210, 372.5, 210)
                    c.line(387.5, 210, 430, 210)

                    c.line(105, 150, 105, 195)
                    c.line(105, 195, 144, 195)
                    c.line(162, 195, 277.5, 195)
                    c.line(292.5, 195, 297.5, 195)
                    c.line(312.5, 195, 430, 195)
                    c.line(430, 195, 430, 100)

                    c.line(115, 150, 115, 182.5)
                    c.line(115, 182.5, 144, 182.5)
                    c.line(162, 182.5, 217.5, 182.5)
                    c.line(232.5, 182.5, 297.5, 182.5)
                    c.line(312.5, 182.5, 400, 182.5)
                    c.line(400, 182.5, 400, 100)

                    c.line(125, 150, 125, 170)
                    c.line(125, 170, 144, 170)
                    c.line(162, 170, 197.5, 170)
                    c.line(212.5, 170, 217.5, 170)
                    c.line(232.5, 170, 370, 170)
                    c.line(370, 170, 370, 100)

                    ##reposit

                    # ball to repo
                    c.line(185, 167.5, 185, 30)
                    c.line(205, 177.5, 205, 40)
                    c.line(225, 187.5, 225, 50)
                    c.line(185, 30, 300, 30)
                    c.line(205, 40, 300, 40)
                    c.line(225, 50, 300, 50)

                    # repo to VR
                    c.line(335, 55, 335, 150)
                    c.line(335, 150, 363.5, 150)
                    c.line(378.5, 150, 392.5, 150)
                    c.line(407.5, 150, 423.5, 150)

                    c.line(340, 55, 340, 135)
                    c.line(340, 135, 363.5, 135)
                    c.line(378.5, 135, 393.5, 135)

                    c.line(345, 55, 345, 120)
                    c.line(345, 120, 363.5, 120)

                    ##battery inverter wiring
                    c.circle(380, 195, 2, stroke=1, fill=1)
                    c.line(380, 195, 380, 307.5)
                    c.line(380, 326.5, 380, 380)
                    c.line(380, 380, 470, 380)
                    c.line(470, 380, 470, 455)
                    draw_switch(380, 310, 0)
                    c.drawString(390, 320, 'Battery AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', BatteryACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(390, 305, '%s' % i1iso)
                    c.circle(355, 210, 2, stroke=1, fill=1)
                    c.line(355, 210, 355, 400)
                    c.line(355, 400, 450, 400)
                    c.line(450, 400, 450, 455)
                    draw_arc(380, 210)

            if array == 4:
                draw_small_array(10, 660, 1, array_1_length, array_2_length, panelspec, array_1_strings,
                                 array_2_strings)
                draw_small_array(335, 660, 3, array_3_length, array_4_length, panelspec, array_3_strings,
                                 array_4_strings)
                draw_inverter(75, 400, inverter1, inverterno, 'N')
                draw_inverter(400, 400, inverter2, inverterno, 'N')
                if battery == 1 and current == 'DC':
                    draw_battery(270, 520, batteryl)

                    ##topdots
                    x = 15
                    y = 680
                    c.circle(x + 65, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 115, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 127.5, y - 205, 2, stroke=1, fill=1)

                    ##top battery to inverter
                    c.line(x + 115, y - 205, x + 115, y - 175)
                    c.line(x + 115, y - 175, x + 208, y - 175)
                    draw_switch(x + 210, y - 175, 270)
                    c.line(x + 227, y - 175, x + 265, y - 175)
                    c.line(x + 265, y - 175, x + 265, y - 170)

                    c.line(x + 127.5, y - 205, x + 127.5, y - 190)
                    c.line(x + 127.5, y - 190, x + 208, y - 190)
                    draw_switch(x + 210, y - 190, 270)
                    c.line(x + 227, y - 190, x + 295, y - 190)
                    c.line(x + 295, y - 190, x + 295, y - 170)

                    c.setDash(array=[3], phase=13)
                    c.line(x + 219, y - 190, x + 219, y - 170)
                    c.setDash(array=[], phase=0)
                    c.setFont('Helvetica', 7)
                    c.drawString(x + 227, y - 205, 'Battery DC Isolator')

                    x += 325
                    c.circle(x + 65, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 205, 2, stroke=1, fill=1)

                    ##BOTTOM
                    draw_switch(145, 195, 270)
                    draw_switch(145, 182.5, 270)
                    draw_switch(145, 170, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(152.5, 155, 'Main')
                    c.drawCentredString(152.5, 145, 'Switch')
                    c.circle(245, 210, 2, stroke=1, fill=1)

                    ##main line
                    c.line(245, 210, 245, 230)
                    c.line(245, 230, 100, 230)
                    c.line(100, 230, 100, 400)
                    ##inv switch line

                    c.setFont('Helvetica', 7)
                    c.drawString(135, 340, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(135, 325, '%s' % i1iso)

                    c.drawString(135, 295, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(135, 280, '%s' % SSiso)
                    draw_switch(125, 327, 0)
                    draw_switch(125, 282, 0)
                    c.line(265, 195, 265, 245)
                    c.line(265, 245, 125, 245)
                    c.line(125, 245, 125, 280)
                    c.line(125, 300, 125, 325)
                    c.line(125, 345, 125, 400)

                    ##out of m into CN
                    ##ac inv arcs
                    draw_arc(265, 210)
                    c.circle(265, 195, 2, stroke=1, fill=1)
                    draw_arc(325, 210)
                    draw_arc(325, 195)
                    draw_arc(325, 182.5)
                    draw_arc(325, 170)

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 257.5, 210)
                    c.line(272.5, 210, 317.5, 210)
                    c.line(332.5, 210, 372.5, 210)
                    c.line(387.5, 210, 430, 210)

                    c.line(105, 150, 105, 195)
                    c.line(105, 195, 144, 195)
                    c.line(162, 195, 317.5, 195)
                    c.line(332.5, 195, 430, 195)
                    c.line(430, 195, 430, 100)

                    c.line(115, 150, 115, 182.5)
                    c.line(115, 182.5, 144, 182.5)
                    c.line(162, 182.5, 217.5, 182.5)
                    c.line(232.5, 182.5, 317.5, 182.5)
                    c.line(332.5, 182.5, 400, 182.5)
                    c.line(400, 182.5, 400, 100)

                    c.line(125, 150, 125, 170)
                    c.line(125, 170, 144, 170)
                    c.line(162, 170, 197.5, 170)
                    c.line(212.5, 170, 217.5, 170)
                    c.line(232.5, 170, 317.5, 170)
                    c.line(332.5, 170, 370, 170)
                    c.line(370, 170, 370, 100)

                    ##reposit

                    # ball to repo
                    c.line(185, 167.5, 185, 30)
                    c.line(205, 177.5, 205, 40)
                    c.line(225, 187.5, 225, 50)
                    c.line(185, 30, 300, 30)
                    c.line(205, 40, 300, 40)
                    c.line(225, 50, 300, 50)

                    # repo to VR
                    c.line(335, 55, 335, 150)
                    c.line(335, 150, 363.5, 150)
                    c.line(378.5, 150, 392.5, 150)
                    c.line(407.5, 150, 423.5, 150)

                    c.line(340, 55, 340, 135)
                    c.line(340, 135, 363.5, 135)
                    c.line(378.5, 135, 393.5, 135)

                    c.line(345, 55, 345, 120)
                    c.line(345, 120, 363.5, 120)

                    ##battery inverter wiring
                    c.circle(380, 195, 2, stroke=1, fill=1)
                    c.line(380, 195, 380, 250)
                    c.line(380, 250, 460, 250)
                    c.line(460, 250, 460, 278)
                    c.line(460, 297, 460, 318)
                    c.line(460, 340, 460, 400)
                    draw_switch(460, 320, 0)
                    c.drawString(470, 330, 'Inverter 2 AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', Inverter2ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(470, 315, '%s' % i1iso)
                    draw_switch(460, 280, 0)

                    c.drawString(470, 290, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(470, 275, '%s' % SSiso)
                    c.circle(355, 210, 2, stroke=1, fill=1)
                    c.line(355, 210, 355, 265)
                    c.line(355, 265, 440, 265)
                    c.line(440, 265, 440, 400)
                    draw_arc(380, 210)

                    ##L1 P1 Line
                    c.line(140, 400, 140, 370)
                    c.line(140, 370, 325, 370)
                    c.line(325, 370, 325, 312.5)
                    draw_switch(325, 295, 0)
                    c.setFont('Helvetica', 6)
                    c.drawString(330, 310, 'EPS AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', EPSACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(330, 295, '%s' % i1iso)
                    c.setFont('Helvetica', 7)

                    c.line(325, 292.5, 325, 263)
                    draw_switch(325, 245, 0)
                    c.line(325, 243, 325, 125)
                    c.line(325, 125, 250, 125)

                    c.line(250, 125, 250, 75)
                    c.circle(250, 125, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 247, 70, width=7, height=7)
                    c.line(280, 125, 280, 75)
                    c.circle(280, 125, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 277, 70, width=7, height=7)
                    c.drawCentredString(250, 135, 'L1')
                    c.drawCentredString(280, 135, 'P1')

                    ##backfeed
                    c.setFont('Times-Italic', 6)
                    c.drawString(312, 510, '* In case of blackout, ')
                    c.drawString(312, 503, ' blackout backfeed')
                    c.drawString(312, 496, ' is impossible')
                    c.drawString(10, 390, '* Inverter isolates in ')
                    c.drawString(10, 383, 'the event of a blackout')
                    c.drawString(340, 390, '* Inverter isolates ')
                    c.drawString(340, 383, 'in the event of a blackout')

                if battery == 1 and current == 'AC':
                    draw_battery(270, 400, batteryl)
                    draw_inverter(250, 315, inverter1, inverterno, 'Y')
                    x = 15
                    y = 680
                    c.circle(x + 65, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 205, 2, stroke=1, fill=1)

                    x += 325
                    c.circle(x + 65, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 205, 2, stroke=1, fill=1)

                    ##BOTTOM
                    draw_switch(145, 195, 270)
                    draw_switch(145, 182.5, 270)
                    draw_switch(145, 170, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(152.5, 155, 'Main')
                    c.drawCentredString(152.5, 145, 'Switch')
                    c.circle(245, 210, 2, stroke=1, fill=1)

                    ##main line
                    c.line(245, 210, 245, 230)
                    c.line(245, 230, 100, 230)
                    c.line(100, 230, 100, 400)
                    ##inv switch line

                    c.setFont('Helvetica', 7)
                    c.drawString(135, 340, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(135, 325, '%s' % i1iso)

                    c.drawString(135, 295, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(135, 280, '%s' % SSiso)
                    draw_switch(125, 327, 0)
                    draw_switch(125, 282, 0)
                    c.line(265, 195, 265, 245)
                    c.line(265, 245, 125, 245)
                    c.line(125, 245, 125, 280)
                    c.line(125, 300, 125, 325)
                    c.line(125, 345, 125, 400)

                    c.circle(285, 210, 2, stroke=1, fill=1)
                    c.line(285, 210, 285, 315)

                    c.circle(305, 195, 2, stroke=1, fill=1)
                    draw_switch(305, 270, 0)
                    c.drawString(315, 290, 'Battery AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', BatteryACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(315, 275, '%s' % i1iso)
                    c.line(305, 195, 305, 268)
                    c.line(305, 287, 305, 315)

                    ##out of m into CN
                    ##ac inv arcs
                    draw_arc(265, 210)
                    c.circle(265, 195, 2, stroke=1, fill=1)
                    draw_arc(305, 210)

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 257.5, 210)
                    c.line(272.5, 210, 292.5, 210)
                    c.line(292.5, 210, 297.5, 210)
                    c.line(312.5, 210, 372.5, 210)
                    c.line(387.5, 210, 430, 210)

                    c.line(105, 150, 105, 195)
                    c.line(105, 195, 144, 195)
                    c.line(162, 195, 312.5, 195)
                    c.line(312.5, 195, 430, 195)
                    c.line(430, 195, 430, 100)

                    c.line(115, 150, 115, 182.5)
                    c.line(115, 182.5, 144, 182.5)
                    c.line(162, 182.5, 217.5, 182.5)
                    c.line(232.5, 182.5, 312.5, 182.5)
                    c.line(312.5, 182.5, 400, 182.5)
                    c.line(400, 182.5, 400, 100)

                    c.line(125, 150, 125, 170)
                    c.line(125, 170, 144, 170)
                    c.line(162, 170, 197.5, 170)
                    c.line(212.5, 170, 217.5, 170)
                    c.line(232.5, 170, 370, 170)
                    c.line(370, 170, 370, 100)

                    ##reposit

                    # ball to repo
                    c.line(185, 167.5, 185, 30)
                    c.line(205, 177.5, 205, 40)
                    c.line(225, 187.5, 225, 50)
                    c.line(185, 30, 300, 30)
                    c.line(205, 40, 300, 40)
                    c.line(225, 50, 300, 50)

                    # repo to VR
                    c.line(335, 55, 335, 150)
                    c.line(335, 150, 363.5, 150)
                    c.line(378.5, 150, 392.5, 150)
                    c.line(407.5, 150, 423.5, 150)

                    c.line(340, 55, 340, 135)
                    c.line(340, 135, 363.5, 135)
                    c.line(378.5, 135, 393.5, 135)

                    c.line(345, 55, 345, 120)
                    c.line(345, 120, 363.5, 120)

                    ##battery inverter wiring
                    c.circle(380, 195, 2, stroke=1, fill=1)
                    c.line(380, 195, 380, 250)
                    c.line(380, 250, 460, 250)
                    c.line(460, 250, 460, 278)
                    c.line(460, 297, 460, 318)
                    c.line(460, 340, 460, 400)
                    draw_switch(460, 320, 0)
                    c.drawString(470, 330, 'Inverter 2 AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', Inverter2ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(470, 315, '%s' % i1iso)
                    draw_switch(460, 280, 0)
                    c.drawString(470, 290, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(470, 275, '%s' % SSiso)
                    c.circle(355, 210, 2, stroke=1, fill=1)
                    c.line(355, 210, 355, 265)
                    c.line(355, 265, 440, 265)
                    c.line(440, 265, 440, 400)
                    draw_arc(380, 210)

                    ##backfeed
                    c.setFont('Times-Italic', 7)
                    c.drawString(302, 540, '* In case of blackout, ')
                    c.drawString(302, 533, ' backfeed is ')
                    c.drawString(302, 526, 'impossible')
                    c.drawString(10, 390, '* Inverter isolates in ')
                    c.drawString(10, 383, 'the event of a blackout')
                    c.drawString(470, 390, '* Inverter isolates ')
                    c.drawString(470, 383, 'in the event of a blackout')

    array_height = 630
    basic_wiring(25, 100)
    complex_wiring(phase, array, battery, inverterno, array_height, current)
    c.save()
    url = r'file:///C:\Users\Solar4Life\Desktop\solar4life\sld generator files\SLD.pdf'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    # make sure to close connection to database at end of program
    conn.close()

# create_SLD('SLD', name, address, inverterno, battery, arrays, phase,current,reposit,customer_ID)
