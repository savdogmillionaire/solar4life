######
#
# creates job sheet based on CA TEST
# look to transition from importing CA TEST
# into importing from main tool
#
######


from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
##from justeverything import name
from CATEST import *

template = "JOB SHEET TEMPLATE.docx"

document = MailMerge(template)
print(document.get_merge_fields())


document.merge(
    STATE='%s' % State,
    UNIT='%s' % Unit,
    STREETNAME='%s' % Streetname,
    STREETNUMBER='%s' % StreetNumber,
    SUBURB='%s' % Suburb,
    NAME='%s' % CustomerorBusinessName,
    DATE='{:%d/%m/%Y}'.format(date.today()),
    BLOCK='%s' % BlockNumber,
    SECTION='%s' % SectionNumber,
    INVERTER='%s' % Inverter,
    PANEL='%s' % Panel,
    LOT='%s' % Lot,
    DP='%s' % Dp,
    NMI='%s' % NMI,
    PANELNUMBER='%s' % NumberofPanels,
    COMPANY='%s' % Company,
    POSTCODE='%s' % Postcode,
    PHONE='%s' % Phone,
    EMAIL='%s' % Email
)

document.write('%s JOB SHEET.docx' % CustomerorBusinessName)
