from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

output = "/Users/durden/.openclaw/workspace/TaiChi_Measurement_Form_v2.pdf"
doc = SimpleDocTemplate(output, pagesize=letter,
                        rightMargin=0.75*inch, leftMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)

styles = getSampleStyleSheet()
title_style = ParagraphStyle('title', fontSize=14, fontName='Helvetica-Bold', alignment=TA_CENTER, spaceAfter=12)
subtitle_style = ParagraphStyle('subtitle', fontSize=11, fontName='Helvetica-Bold', alignment=TA_CENTER, spaceAfter=8)
label_style = ParagraphStyle('label', fontSize=9, fontName='Helvetica-Bold')
normal_style = ParagraphStyle('normal', fontSize=9, fontName='Helvetica')
section_style = ParagraphStyle('section', fontSize=10, fontName='Helvetica-Bold', spaceAfter=4, spaceBefore=8)
instruction_style = ParagraphStyle('instruction', fontSize=9, fontName='Helvetica', leftIndent=12, spaceAfter=3)

elements = []

# ─── PAGE 1: MEASUREMENT FORM ───

elements.append(Paragraph("TAI CHI GARMENT MEASUREMENT FORM", title_style))

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

garment_text = "Garment Type:   ☐  Uniform Set    ☐  Top    ☐  Pants    ☐  Silk    ☐  Cotton"
elements.append(Paragraph(garment_text, normal_style))
elements.append(Spacer(1, 8))

elements.append(Paragraph("Measurements (cm):", label_style))
elements.append(Spacer(1, 4))

measurements = [
    ["Measurement", "How to Measure", "Value (cm)"],
    ["Height", "Without shoes, stand straight against wall", ""],
    ["Weight", "In light clothing", ""],
    ["Neck", "Around base of neck where collar sits", ""],
    ["Shoulder Width", "Shoulder point to shoulder point across back", ""],
    ["Chest / Bust", "Fullest part of chest, arms relaxed", ""],
    ["Waist", "Natural waistline — narrowest part of torso", ""],
    ["Hip", "Fullest part of hips/seat", ""],
    ["Arm Length", "Shoulder point down to wrist bone, arm slightly bent", ""],
    ["Sleeve Length", "Center back neck, across shoulder, to wrist", ""],
    ["Wrist", "Around the wrist bone", ""],
    ["Back Length", "C7 neck bone (nape) straight down to natural waist", ""],
    ["Inseam", "Crotch to ankle bone, inside leg", ""],
    ["Outseam", "Natural waist to ankle, outside leg", ""],
    ["Thigh", "Fullest part of upper thigh", ""],
    ["Calf", "Fullest part of lower leg", ""],
    ["Ankle", "Around the ankle bone", ""],
]

col_widths = [1.5*inch, 3.8*inch, 1.3*inch]
meas_table = Table(measurements, colWidths=col_widths, rowHeights=[20] + [18]*16)
meas_table.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 8),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#d0d0d0')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f5f5f5')]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.black),
    ('ALIGN', (2,0), (2,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('LEFTPADDING', (0,0), (-1,-1), 5),
    ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
]))
elements.append(meas_table)
elements.append(Spacer(1, 10))

elements.append(Paragraph("Notes:", label_style))
notes_table = Table([[""], [""]], colWidths=[6.6*inch], rowHeights=[18, 18])
notes_table.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 0.5, colors.black),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
]))
elements.append(notes_table)
elements.append(Spacer(1, 10))

fit_text = "Fit:   ☐  Loose/Traditional    ☐  Regular    ☐  Form-Fitting          Color: _______________"
elements.append(Paragraph(fit_text, normal_style))
elements.append(Spacer(1, 10))

measured_data = [["Measured by: ________________________________", "Date: _______________"]]
measured_table = Table(measured_data, colWidths=[4.5*inch, 2.1*inch])
measured_table.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
]))
elements.append(measured_table)

# ─── PAGE 2: HOW TO MEASURE GUIDE ───

elements.append(PageBreak())
elements.append(Paragraph("HOW TO TAKE MEASUREMENTS — TAILOR'S GUIDE", title_style))
elements.append(Paragraph("For Tai Chi Garments", subtitle_style))
elements.append(Spacer(1, 4))

instructions = [
    ("BEFORE YOU START", [
        "Use a soft flexible measuring tape — never a rigid ruler.",
        "Have the client stand straight, relaxed, breathing normally.",
        "Measure over light, fitted clothing (not heavy layers).",
        "Keep the tape snug but not tight — you should be able to slide one finger underneath.",
        "For Tai Chi: add 3–5 cm ease to chest, waist, and hips for movement.",
        "Always record in centimeters (cm).",
    ]),
    ("HEIGHT", [
        "Client stands barefoot with back against a wall.",
        "Measure from the floor to the top of the head.",
    ]),
    ("NECK", [
        "Wrap the tape around the base of the neck where a collar would sit.",
        "Keep tape horizontal. Add 1 cm ease.",
    ]),
    ("SHOULDER WIDTH", [
        "Measure across the back from shoulder point to shoulder point.",
        "Shoulder point = where the arm meets the shoulder (the bony tip).",
        "Keep tape flat across the upper back.",
    ]),
    ("CHEST / BUST", [
        "Wrap tape around the fullest part of the chest.",
        "Keep arms relaxed at the sides.",
        "Tape should be level all the way around — check the back isn't drooping.",
    ]),
    ("WAIST", [
        "Find the natural waistline — the narrowest part of the torso.",
        "Tip: Ask the client to bend sideways — the crease that forms IS the natural waist.",
        "Usually 2–3 cm above the navel.",
        "Wrap tape and measure. Do not hold breath.",
    ]),
    ("HIP", [
        "Stand with feet together.",
        "Measure around the fullest part of the hips and seat.",
        "Usually 18–23 cm below the natural waist.",
        "Make sure tape is level all the way around.",
    ]),
    ("ARM LENGTH", [
        "Client stands with arm slightly bent (natural relaxed bend).",
        "Measure from the shoulder point (bony tip) down to the wrist bone.",
    ]),
    ("SLEEVE LENGTH", [
        "Start at the center back of the neck (C7 vertebra — the bump when you tilt your head forward).",
        "Measure across the shoulder and down the arm to the wrist.",
        "Arm should be slightly bent.",
    ]),
    ("WRIST", [
        "Wrap tape around the wrist bone.",
        "Measure snugly — this is for the cuff opening.",
    ]),
    ("BACK LENGTH", [
        "Find C7 — the most prominent vertebra at the back of the neck (client bends head forward).",
        "Measure straight down the spine to the natural waistline.",
    ]),
    ("INSEAM", [
        "Client stands with feet shoulder-width apart.",
        "Measure from the crotch (inside leg top) down to the ankle bone.",
        "Along the inside of the leg.",
    ]),
    ("OUTSEAM", [
        "Measure from the natural waist down the outside of the leg to the ankle bone.",
    ]),
    ("THIGH", [
        "Measure around the fullest part of the upper thigh.",
        "Client should have weight evenly on both feet.",
    ]),
    ("CALF", [
        "Measure around the fullest part of the lower leg.",
    ]),
    ("ANKLE", [
        "Wrap tape around the ankle bone.",
        "This determines the trouser opening width.",
    ]),
    ("FIT GUIDE FOR TAI CHI", [
        "Loose/Traditional: Add 5–8 cm ease to chest, waist, hip. Wide sleeves.",
        "Regular: Add 3–5 cm ease. Comfortable but not billowy.",
        "Form-Fitting: Add 1–2 cm ease only. Follows the body closely.",
        "When in doubt, go looser — Tai Chi requires full range of motion.",
    ]),
]

for section_title, points in instructions:
    elements.append(Paragraph(section_title, section_style))
    for point in points:
        elements.append(Paragraph(f"• {point}", instruction_style))

doc.build(elements)
print("PDF created:", output)
