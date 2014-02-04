#!/usr/bin/env python 

from PyPDF2 import PdfFileWriter, PdfFileReader

import os,sys
# del 4, 12, 13, 26, 27, 41, 42, 52, 53, 63, 64, 88, 89, 100, 101, 102, 113, 119
pages = [ 3, 4, 12, 13, 26, 27, 41, 42, 52, 53, 63, 64, 88, 89, 100, 101, 102, 108, 113, 119 ]

pages = [ i - 1 for i in pages ]

output = PdfFileWriter()
input1 = PdfFileReader(open(sys.argv[1], "rb"))
    
# print how many pages input1 has:
print "%s has %d pages." % (sys.argv[1], input1.getNumPages())

for i in range(input1.getNumPages()):
	# add page 1 from input1 to output document, unchanged
	if i not in pages:
		output.addPage(input1.getPage(i))

# finally, write "output" to document-output.pdf
outputStream = file(sys.argv[2], "wb")
output.write(outputStream)
