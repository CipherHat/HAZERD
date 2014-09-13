from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from pdfminer import pdfparser, pdfdocument

# Create your views here.

def index(request):
    # return HttpResponse("Hello World")
    return render(request, "index.html")

def parseHTML(request):
    parser = pdfparser("https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/353962/Tiers_2__5_Register_of_Sponsors_2014-09-12.pdf")
    doc = pdfdocument()
    doc.set_parser(parser)
    return HttpResponse(doc)