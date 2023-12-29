import requests
from datetime import *
from settings import *
import os
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def tests_pdf_test_report_maker():
    pdf_report = canvas.Canvas(os.path.abspath("logs/pdf_files/test_report.pdf"))
    pdfmetrics.registerFont(TTFont('Arial_Bold', os.path.abspath('logs/pdf_files/Arial_Bold.ttf')))
    pdfmetrics.registerFont(TTFont('Arial_Cyr', os.path.abspath('logs/pdf_files/Arial_Cyr.ttf')))
    pdf_report.setFillColor('SteelBlue')
    pdf_report.roundRect(x=5, y=5, width=585, height=831, radius=12, stroke=0, fill=1)
    pdf_report.setFillColor('White')
    pdf_report.roundRect(x=10, y=10, width=575, height=821, radius=10, stroke=0, fill=1)
    pdf_report.drawImage(os.path.abspath("logs/pdf_files/Python_logo.jpg"), x=20, y=740, width=77, height=80)
    pdf_report.drawImage(os.path.abspath("logs/pdf_files/Pytest_logo.jpg"), x=120, y=730, width=97, height=100)
    # Generate test name:
    pdf_report.setFillColor('Black')
    pdf_report.setFont('Arial_Bold', 16)
    pdf_report.drawString(40, 700, f"Тест: <ИМЯ ТЕСТА>")
    # Generate test result:
    pdf_report.setFillColor('Gainsboro')
    pdf_report.roundRect(x=20, y=630, width=555, height=40, radius=18, stroke=0, fill=1)
    pdf_report.setFillColor('YellowGreen')
    pdf_report.circle(40, 650, 15, fill=1, stroke=0)
    pdf_report.setFillColor('Black')
    pdf_report.setFont('Arial_Cyr', 12)
    pdf_report.drawString(60, 645, "PASSED   [100%]")
    pdf_report.setFillColor('Gainsboro')
    pdf_report.roundRect(x=20, y=600, width=555, height=200, radius=18, stroke=0, fill=1)
    pdf_report.setFont('Arial_Cyr', 12)
    pdf_report.drawString(40, 700, f"""Идея:\n'<ОПИСАНИЕ ТЕСТА>'""")
    pdf_report.save()