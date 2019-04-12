from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
##from justeverything import name
from CATEST import *

template = "JOB SHEET TEMPLATE.docx"

document = MailMerge(template)
print(document.get_merge_fields())

document.merge(
    POSTCODE='%s' % Postcode,
    STATE='%s' % State,
    UNIT='%s' % Unit,
    STREETNAME='%s' % Streetname,
    STREETNUMBER='%s' % StreetNumber,
    SUBURB='%s' % Suburb,
    NAME='%s' % CustomerorBusinessName,
    DATE='{:%d/%m/%Y}'.format(date.today()),
    BLOCK='%s' % BlockNumber,
    SECTION='%s' % SectionNumber,
)

document.write('%s JOB SHEET.docx' % CustomerorBusinessName)
