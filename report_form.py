import sys
import pytest
import requests
from datetime import *
import json
from settings import *
import os
from reportlab.pdfgen import canvas
import fpdf


def pdf_test_report_maker(request):
    test_name = 'test functon name'
    test_idea = 'test doc strings'
    tests_suit_name = ''
    fixture_name = ''
    fixture_scope = ''
    module_name = ''
    module_fullpath = ''
    # Generate PDF Header:
    pdf_report = canvas.Canvas(os.path.abspath("logs/pdf_files/test_report.pdf"))
    pdf_report.setFillColor('SteelBlue')
    pdf_report.roundRect(x=5, y=5, width=585, height=831, radius=12, stroke=0, fill=1)
    pdf_report.setFillColor('White')
    pdf_report.roundRect(x=10, y=10, width=575, height=821, radius=10, stroke=0, fill=1)
    pdf_report.drawImage("logs/pdf_files/Python_logo.jpg", x=20, y=740, width=77, height=80)
    pdf_report.drawImage("logs/pdf_files/Pytest_logo.jpg", x=120, y=730, width=97, height=100)
    # Generate test name:
    pdf_report.setFillColor('Black')
    pdf_report.setFont("Times-Bold", 24)
    pdf_report.drawString(40, 700, f"Название теста: {test_name}")
    # Generate test result:
    pdf_report.setFillColor('Gainsboro')
    pdf_report.roundRect(x=20, y=630, width=555, height=40, radius=18, stroke=0, fill=1)
    pdf_report.setFillColor('YellowGreen')
    pdf_report.circle(40, 650, 15, fill=1, stroke=0)
    pdf_report.setFillColor('Black')
    pdf_report.setFont("Times-Bold", 16)
    pdf_report.drawString(60, 645, "100% PASSED")
    # print(f"\n{pdf_report.getAvailableFonts()}")
    pdf_report.save()