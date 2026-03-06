from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

output = "/Users/durden/.openclaw/workspace/TaiChi_Measurement_Form.pdf"
doc = SimpleDocTemplate(output, pagesize=letter,
                        rightMargin=0.75*inch, leftMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)

styles = getSampleStyleSheet()
title_style = ParagraphStyle('title', fontSize=14, fontName='Helvetica-Bold', alignment=TA_CENTER, spaceAfter=12)
label_style = ParagraphStyle('label', fontSize=9, fontName='Helvetica-Bold')
normal_style = ParagraphStyle('normal', fontSize=9, fontName='Helvetica')

elements = []

# Title
elements.append(Paragraph("TAI CHI GARMENT MEASUREMENT FORM", title_style))

# Client info table
client_data = [
    ["Client Name:", "", "Date:", ""],
    ["Phone:", "", "Email:", ""],
]
client_table = Table(client_data, colWidths=[1.2*inch, 2.3*inch, 0.8*inch, 2.3*inch])
client_table.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
    ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
    ('FONTNAME', (2,0), (2,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('BOX', (1,0), (1,0), 0.5, colors.black),
    ('BOX', (3,0), (3,0), 0.5, colors.black),
    ('BOX', (1,1), (1,1), 0.5, colors.black),
    ('BOX', (3,1), (3,1), 0.5, colors.black),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('TOPPADDING', (0,0), (-1,-1), 4),
]))
elements.append(client_table)
elements.append(Spacer(1, 8))

# Garment type
garment_text = "Garment Type:   ☐  Uniform Set    ☐  Top    ☐  Pants    ☐  Silk    ☐  Cotton"
elements.append(Paragraph(garment_text, normal_style))
elements.append(Spacer(1, 8))

elements.append(Paragraph("Measurements (cm):", label_style))
elements.append(Spacer(1, 4))

# Measurements table
measurements = [
    ["Measurement", "How to Measure", "Value (cm)"],
    ["Height", "Without shoes", ""],
    ["Weight", "", ""],
    ["Neck", "Base of neck", ""],
    ["Shoulder Width", "Shoulder to shoulder across back", ""],
    ["Chest/Bust", "Fullest part", ""],
    ["Waist", "Natural waistline", ""],
    ["Hip", "Fullest part", ""],
    ["Arm Length", "Shoulder to wrist", ""],
    ["Sleeve Length", "Center back neck to wrist", ""],
    ["Wrist", "Around wrist bone", ""],
    ["Back Length", "Neck to waist", ""],
    ["Inseam", "Crotch to ankle", ""],
    ["Outseam", "Waist to ankle", ""],
    ["Thigh", "Fullest part", ""],
    ["Calf", "Fullest part", ""],
    ["Ankle", "Around ankle bone", ""],
]

col_widths = [1.8*inch, 3.5*inch, 1.3*inch]
meas_table = Table(measurements, colWidths=col_widths, rowHeights=[20] + [18]*16)
meas_table.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#d0d0d0')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f5f5f5')]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.black),
    ('ALIGN', (2,0), (2,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
]))
elements.append(meas_table)
elements.append(Spacer(1, 10))

# Notes
elements.append(Paragraph("Notes:", label_style))
notes_table = Table([[""], [""]], colWidths=[6.6*inch], rowHeights=[18, 18])
notes_table.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 0.5, colors.black),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
]))
elements.append(notes_table)
elements.append(Spacer(1, 10))

# Fit and color
fit_text = "Fit:   ☐  Loose/Traditional    ☐  Regular    ☐  Form-Fitting          Color: _______________"
elements.append(Paragraph(fit_text, normal_style))
elements.append(Spacer(1, 10))

# Measured by
measured_data = [["Measured by: ________________________________", "Date: _______________"]]
measured_table = Table(measured_data, colWidths=[4.5*inch, 2.1*inch])
measured_table.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
]))
elements.append(measured_table)

doc.build(elements)
print("PDF created:", output)
