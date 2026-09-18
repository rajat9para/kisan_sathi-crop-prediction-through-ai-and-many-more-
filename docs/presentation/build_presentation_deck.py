#!/usr/bin/env python3
"""
Kisaan Sathi — SIH 2026 Official Presentation Generator
Problem Statement #26180 · Qualcomm Inc · Hardware Edition · Team TechBuilders
Theme: Disaster Management

Generates an executive-ready 16:9 widescreen presentation deck (PPTX)
with dark high-contrast styling, precise agronomic/hardware metrics,
embedded high-resolution vector diagrams (D1–D4), and the verbatim data honesty statement.
"""

import os
import sys
import shutil
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# Ensure stdout handles UTF-8 safely
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Colors
C_BG = RGBColor(11, 19, 43)          # #0B132B (Deep Midnight Navy)
C_CARD_BG = RGBColor(17, 28, 56)     # #111C38 (Slate Card Navy)
C_CARD_BORDER = RGBColor(45, 59, 98) # #2D3B62 (Card Border)
C_CYAN = RGBColor(56, 189, 248)      # #38BDF8 (Qualcomm Blue / Cyan)
C_GREEN = RGBColor(16, 185, 129)     # #10B981 (Agri Emerald)
C_AMBER = RGBColor(245, 158, 11)     # #F59E0B (Hazard Warning Gold)
C_ORANGE = RGBColor(249, 115, 22)    # #F97316 (Disaster Alert Orange)
C_RED = RGBColor(239, 68, 68)        # #EF4444 (Veto Red)
C_PURPLE = RGBColor(168, 85, 247)    # #A855F7 (Edge AI Violet)
C_TEXT_WHITE = RGBColor(255, 255, 255)
C_TEXT_MUTED = RGBColor(148, 163, 184) # #94A3B8
C_TEXT_LIGHT = RGBColor(226, 232, 240) # #E2E8F0
C_HEADER_BG = RGBColor(15, 23, 42)     # #0F172A

FONT_TITLE = "Calibri"
FONT_BODY = "Calibri"

def apply_background(slide):
    """Draws a full-bleed dark navy background on the slide."""
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = C_BG
    bg.line.color.rgb = C_BG
    return bg

def add_header(slide, title, subtitle=None, category_pill="HARDWARE EDITION", theme="DISASTER MANAGEMENT"):
    """Creates a standardized executive header bar across slides."""
    # Top banner bar
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(0.35), Inches(12.333), Inches(0.85))
    bar.fill.solid()
    bar.fill.fore_color.rgb = C_CARD_BG
    bar.line.color.rgb = C_CARD_BORDER

    # Title text box
    tb = slide.shapes.add_textbox(Inches(0.7), Inches(0.4), Inches(7.8), Inches(0.75))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = FONT_TITLE
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_WHITE

    if subtitle:
        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.name = FONT_BODY
        p2.font.size = Pt(11)
        p2.font.color.rgb = C_TEXT_MUTED

    # Right pills: Theme + Category
    # Theme pill
    tp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.7), Inches(0.52), Inches(2.4), Inches(0.45))
    tp.fill.solid()
    tp.fill.fore_color.rgb = RGBColor(40, 20, 15)
    tp.line.color.rgb = C_ORANGE
    t_tf = tp.text_frame
    t_tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    t_p = t_tf.paragraphs[0]
    t_p.text = f"THEME: {theme}"
    t_p.font.name = FONT_TITLE
    t_p.font.size = Pt(10)
    t_p.font.bold = True
    t_p.font.color.rgb = C_ORANGE
    t_p.alignment = PP_ALIGN.CENTER

    # Category & Org pill
    cp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(11.2), Inches(0.52), Inches(1.5), Inches(0.45))
    cp.fill.solid()
    cp.fill.fore_color.rgb = RGBColor(12, 35, 60)
    cp.line.color.rgb = C_CYAN
    c_tf = cp.text_frame
    c_tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    c_p = c_tf.paragraphs[0]
    c_p.text = "QUALCOMM · PS 26180"
    c_p.font.name = FONT_TITLE
    c_p.font.size = Pt(9.5)
    c_p.font.bold = True
    c_p.font.color.rgb = C_CYAN
    c_p.alignment = PP_ALIGN.CENTER

def add_card(slide, left, top, width, height, bg_color=C_CARD_BG, border_color=C_CARD_BORDER):
    """Creates a rounded container card."""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    return card

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    base_dir = os.path.dirname(os.path.abspath(__file__))
    d1_png = os.path.join(base_dir, "D1_hardware_block_diagram_v2.png")
    d2_png = os.path.join(base_dir, "D2_edge_decision_loop_v2.png")
    d3_png = os.path.join(base_dir, "D3_disaster_resilience_engine_v2.png")
    d4_png = os.path.join(base_dir, "D4_validation_and_capability_panel_v2.png")

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    apply_background(slide1)

    # Top metadata tag
    meta_box = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(0.55), Inches(11.933), Inches(0.65))
    meta_box.fill.solid()
    meta_box.fill.fore_color.rgb = C_CARD_BG
    meta_box.line.color.rgb = C_CARD_BORDER
    m_tf = meta_box.text_frame
    m_tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    m_p = m_tf.paragraphs[0]
    m_p.text = "SMART INDIA HACKATHON 2026  ·  HARDWARE EDITION  ·  PROBLEM STATEMENT #26180  ·  QUALCOMM INC"
    m_p.font.name = FONT_TITLE
    m_p.font.size = Pt(11)
    m_p.font.bold = True
    m_p.font.color.rgb = C_CYAN
    m_p.alignment = PP_ALIGN.CENTER

    # Hero Title Box
    h_box = slide1.shapes.add_textbox(Inches(0.7), Inches(1.35), Inches(11.933), Inches(1.8))
    h_tf = h_box.text_frame
    h_tf.word_wrap = True
    p1 = h_tf.paragraphs[0]
    p1.text = "Kisaan Sathi (किसान साथी)"
    p1.font.name = FONT_TITLE
    p1.font.size = Pt(40)
    p1.font.bold = True
    p1.font.color.rgb = C_TEXT_WHITE

    p2 = h_tf.add_paragraph()
    p2.text = "Field-Deployable Cyber-Physical Node & AI Smart Farming Assistant"
    p2.font.name = FONT_TITLE
    p2.font.size = Pt(19)
    p2.font.color.rgb = C_GREEN

    # Theme Warning/Lens Callout
    theme_box = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(3.1), Inches(11.933), Inches(0.75))
    theme_box.fill.solid()
    theme_box.fill.fore_color.rgb = RGBColor(38, 20, 15)
    theme_box.line.color.rgb = C_ORANGE
    t_tf = theme_box.text_frame
    t_tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tp1 = t_tf.paragraphs[0]
    tp1.text = "OFFICIAL THEME: DISASTER MANAGEMENT"
    tp1.font.name = FONT_TITLE
    tp1.font.size = Pt(13)
    tp1.font.bold = True
    tp1.font.color.rgb = C_ORANGE
    tp2 = t_tf.add_paragraph()
    tp2.text = "Evaluated through the lens of climate hazard resilience: autonomous early detection of drought, flood, heatwave & pest epidemics."
    tp2.font.name = FONT_BODY
    tp2.font.size = Pt(11)
    tp2.font.color.rgb = C_TEXT_LIGHT

    # 10-Second Hook Box
    hook_box = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(3.98), Inches(11.933), Inches(0.85))
    hook_box.fill.solid()
    hook_box.fill.fore_color.rgb = RGBColor(15, 30, 48)
    hook_box.line.color.rgb = C_CYAN
    hk_tf = hook_box.text_frame
    hk_tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    hk_p1 = hk_tf.paragraphs[0]
    hk_p1.text = "THE 10-SECOND EXECUTIVE HOOK:"
    hk_p1.font.name = FONT_TITLE
    hk_p1.font.size = Pt(10)
    hk_p1.font.bold = True
    hk_p1.font.color.rgb = C_CYAN
    hk_p2 = hk_tf.add_paragraph()
    hk_p2.text = '"A ₹9,850 solar-powered field node that detects crop disease, pest, nutrient and water stress on-device in 32 ms — and keeps warning the farmer when the network is gone."'
    hk_p2.font.name = FONT_TITLE
    hk_p2.font.size = Pt(13)
    hk_p2.font.bold = True
    hk_p2.font.color.rgb = C_TEXT_WHITE

    # 4 Pillar Cards at Bottom
    pillars = [
        ("₹9,850 Physical Node", "100% commodity off-the-shelf BOM\n20W PV + 12V 7Ah VRLA Battery\n48-hr zero-sun autonomy · IP65", C_GREEN),
        ("32.4 ms Edge AI", "MobileNetV2 INT8 on Cortex-A72\n7 CNN classes @ 95.87% val acc\n16 ICAR guidance · 5 ETL pests", C_PURPLE),
        ("Disaster Resilience", "Drought, flood & heatwave indices\nFAO-56 Hargreaves ETc water balance\nPre-emptive pump control & alerts", C_ORANGE),
        ("Offline Fail-Safe", "SIM800L Devanagari SMS fallback\nLoRa 868 MHz village mesh\nOpto active-LOW relay + HW watchdog", C_CYAN)
    ]
    card_w = Inches(2.83)
    card_gap = Inches(0.2)
    start_x = Inches(0.7)
    for i, (p_title, p_desc, p_color) in enumerate(pillars):
        px = start_x + i * (card_w + card_gap)
        c = add_card(slide1, px, Inches(4.95), card_w, Inches(1.85), border_color=p_color)
        c_tf = c.text_frame
        c_tf.word_wrap = True
        c_tf.margin_top = Inches(0.12)
        c_tf.margin_left = Inches(0.12)
        cp1 = c_tf.paragraphs[0]
        cp1.text = p_title
        cp1.font.name = FONT_TITLE
        cp1.font.size = Pt(12)
        cp1.font.bold = True
        cp1.font.color.rgb = p_color
        cp2 = c_tf.add_paragraph()
        cp2.text = p_desc
        cp2.font.name = FONT_BODY
        cp2.font.size = Pt(10)
        cp2.font.color.rgb = C_TEXT_LIGHT

    # Team Footer
    tf_box = slide1.shapes.add_textbox(Inches(0.7), Inches(6.92), Inches(11.933), Inches(0.4))
    tf_p = tf_box.text_frame.paragraphs[0]
    tf_p.text = "Team TechBuilders  ·  Autonomous Edge Cyber-Physical System  ·  SIH 2026 Grand Finale Defense"
    tf_p.font.name = FONT_TITLE
    tf_p.font.size = Pt(10)
    tf_p.font.color.rgb = C_TEXT_MUTED
    tf_p.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 2: PROPOSED SOLUTION & PS MAPPING
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    apply_background(slide2)
    add_header(slide2, "Proposed Solution & Problem Statement Alignment", "End-to-End Cyber-Physical Architecture mapped directly to Qualcomm PS #26180 requirements")

    # Left Column: Detailed Explanation + Innovation (Width 5.5 inches)
    left_top_card = add_card(slide2, Inches(0.7), Inches(1.35), Inches(5.6), Inches(3.2))
    lt_tf = left_top_card.text_frame
    lt_tf.word_wrap = True
    lt_tf.margin_top = Inches(0.12)
    lt_tf.margin_left = Inches(0.14)
    lt_p0 = lt_tf.paragraphs[0]
    lt_p0.text = "1. Detailed Solution Architecture"
    lt_p0.font.name = FONT_TITLE
    lt_p0.font.size = Pt(12)
    lt_p0.font.bold = True
    lt_p0.font.color.rgb = C_CYAN

    sol_bullets = [
        ("Edge Sensing:", "Capacitive soil moisture via 16-bit ADS1115 ADC, DHT22 (temp/humidity), FC-37 rain plate, Pi Camera V2. 3-min duty cycle recorded to SQLite."),
        ("Leaf Pathology:", "MobileNetV2 INT8 ONNX (32.4 ms on Cortex-A72). 7 verified CNN classes at 95.87% val acc; 16 unverified crops routed to verified ICAR symptom guidance."),
        ("Nutrient Analysis:", "NPK/pH sensing + Soil Health Card OCR mapped to XGBoost + SHAP explaining nutrient deficiency magnitude in 11 Indian languages."),
        ("Water Balance:", "FAO-56 Hargreaves ET₀ from local Tmax/Tmin, crop Kc curve, soil-water deficit converted to litres and exact pump runtime."),
        ("Disaster Hazards:", "Drought, flood, heatwave & outbreak indices (0–100) combining local telemetry and Open-Meteo ECMWF forecasts."),
        ("Degrading Delivery:", "Web/Flutter Dashboard → SIM800L Devanagari SMS → LoRa 868 MHz village mesh → Local buzzer/pump actuation when isolated.")
    ]
    for b_title, b_body in sol_bullets:
        bp = lt_tf.add_paragraph()
        bp.text = f"• {b_title} {b_body}"
        bp.font.name = FONT_BODY
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = C_TEXT_LIGHT

    # Left Column Bottom: Innovation & Uniqueness
    left_bot_card = add_card(slide2, Inches(0.7), Inches(4.7), Inches(5.6), Inches(2.35))
    lb_tf = left_bot_card.text_frame
    lb_tf.word_wrap = True
    lb_tf.margin_top = Inches(0.12)
    lb_tf.margin_left = Inches(0.14)
    lb_p0 = lb_tf.paragraphs[0]
    lb_p0.text = "2. Innovation & Key Differentiators"
    lb_p0.font.name = FONT_TITLE
    lb_p0.font.size = Pt(12)
    lb_p0.font.bold = True
    lb_p0.font.color.rgb = C_GREEN

    innovations = [
        ("Acts, not just advises:", "Decision terminates at optocoupled relay closing on 12V pump with 15-min HW watchdog and rain lockout."),
        ("Explainability reaches farmer:", "SHAP attribution translated into spoken native audio in 11 languages with local KVK agronomist contact."),
        ("Declared capability boundary:", "Where unverified, returns confidence: null + ICAR guidance instead of fabricated neural hallucination."),
        ("₹9,850 Offline-Native:", "Engineered for marginal smallholders with zero cloud dependence and 48h zero-sun battery autonomy.")
    ]
    for i_title, i_body in innovations:
        ip = lb_tf.add_paragraph()
        ip.text = f"• {i_title} {i_body}"
        ip.font.name = FONT_BODY
        ip.font.size = Pt(9.5)
        ip.font.color.rgb = C_TEXT_LIGHT

    # Right Column: PS Requirement Alignment Table (Width 6.2 inches)
    table_card = add_card(slide2, Inches(6.5), Inches(1.35), Inches(6.133), Inches(5.7))
    t_box = slide2.shapes.add_textbox(Inches(6.6), Inches(1.42), Inches(5.9), Inches(0.4))
    t_tf = t_box.text_frame
    t_p = t_tf.paragraphs[0]
    t_p.text = "Problem Statement Alignment Matrix (PS #26180)"
    t_p.font.name = FONT_TITLE
    t_p.font.size = Pt(12)
    t_p.font.bold = True
    t_p.font.color.rgb = C_AMBER

    # Add Table
    rows = 7
    cols = 3
    t_shape = slide2.shapes.add_table(rows, cols, Inches(6.6), Inches(1.85), Inches(5.933), Inches(5.0))
    table = t_shape.table
    table.columns[0].width = Inches(1.85)
    table.columns[1].width = Inches(2.55)
    table.columns[2].width = Inches(1.533)

    headers = ["PS Requirement", "Implementation Mechanism", "Evidenced Metric"]
    for j, h in enumerate(headers):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(25, 45, 80)
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = FONT_TITLE
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = C_CYAN

    ps_rows = [
        ("Detect crop diseases early", "MobileNetV2 INT8 on leaf imagery on RPi Cortex-A72", "32.4 ms / 95.87% val acc"),
        ("Detect pests early", "ETL-threshold advisory with bio/chemical dosing per ICAR", "5 Major Indian Pests"),
        ("Detect nutrient deficiencies", "NPK/pH sensing + Soil Health Card OCR → XGBoost + SHAP", "7 Features · 11 Languages"),
        ("Detect irrigation needs", "FAO-56 Hargreaves ETc water balance → relay pump control", "Liters/m² → Pump sec"),
        ("Disaster resilience (drought, flood, heatwave)", "4 graded hazard indices (0–100) with pre-emptive actions", "Sensor + ECMWF Forecast"),
        ("Real-time on-device intelligence", "Full closed loop executes on Raspberry Pi with 0 cloud dependency", "100% Offline Autonomous")
    ]
    for i, row in enumerate(ps_rows):
        bg = RGBColor(18, 30, 58) if i % 2 == 0 else RGBColor(14, 24, 48)
        for j, val in enumerate(row):
            cell = table.cell(i + 1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_BODY
            p.font.size = Pt(9.5)
            if j == 2:
                p.font.bold = True
                p.font.color.rgb = C_GREEN
            else:
                p.font.color.rgb = C_TEXT_LIGHT

    # =========================================================================
    # SLIDE 3: TECHNICAL APPROACH & ARCHITECTURE
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    apply_background(slide3)
    add_header(slide3, "Technical Approach & System Architecture", "Hardware wiring, 4 local AI inference engines, cyber-physical actuation, and telemetry fail-safes")

    # 4-Line Technology Strip Card
    tech_card = add_card(slide3, Inches(0.7), Inches(1.35), Inches(11.933), Inches(1.2))
    tc_tf = tech_card.text_frame
    tc_tf.word_wrap = True
    tc_tf.margin_top = Inches(0.08)
    tc_tf.margin_left = Inches(0.12)

    tech_lines = [
        ("Hardware:", "Raspberry Pi 4B (4 GB) · Pi Camera V2 · Capacitive soil probe · ADS1115 16-bit ADC · DHT22 · FC-37 rain plate · 5V opto relay → 12V R385 pump · SIM800L GSM · RYLR896 LoRa 868 MHz · 20W PV + 12V 7Ah VRLA", C_CYAN),
        ("Edge AI:", "PyTorch → ONNX Runtime INT8 · MobileNetV2 (32.4 ms) · OpenCV · XGBoost · SHAP TreeExplainer · scikit-learn", C_PURPLE),
        ("Agronomy:", "FAO-56 Hargreaves ET₀ · crop coefficient Kc · soil-water deficit · ICAR / TNAU / PAU extension guidelines", C_GREEN),
        ("Software & Cloud:", "FastAPI · SQLite (edge) · Supabase PostgreSQL (cloud) · Flutter · PWA · systemd · SoilGrids v2 · Open-Meteo · Sentinel-2 · Agmarknet", C_TEXT_LIGHT)
    ]
    for i, (lbl, desc, col) in enumerate(tech_lines):
        p = tc_tf.paragraphs[0] if i == 0 else tc_tf.add_paragraph()
        p.text = f"{lbl} {desc}"
        p.font.name = FONT_BODY
        p.font.size = Pt(9.2)
        p.font.color.rgb = col

    # Diagrams D1 and D2 side by side
    diag_top = Inches(2.65)
    diag_h = Inches(3.9)
    diag_w = Inches(5.85)

    # D1 (Left)
    if os.path.exists(d1_png):
        slide3.shapes.add_picture(d1_png, Inches(0.7), diag_top, width=diag_w, height=diag_h)
    else:
        d1_box = add_card(slide3, Inches(0.7), diag_top, diag_w, diag_h)
        d1_box.text_frame.text = "D1: Hardware Block Diagram\n(Physical wiring, power buses, sensor pinouts)"

    # D2 (Right)
    if os.path.exists(d2_png):
        slide3.shapes.add_picture(d2_png, Inches(6.78), diag_top, width=diag_w, height=diag_h)
    else:
        d2_box = add_card(slide3, Inches(6.78), diag_top, diag_w, diag_h)
        d2_box.text_frame.text = "D2: Edge Decision Loop\n(Sense → Quality Gate → 4 AI Engines → Actuation Guards)"

    # Caption Strip
    cap_box = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(6.65), Inches(11.933), Inches(0.5))
    cap_box.fill.solid()
    cap_box.fill.fore_color.rgb = RGBColor(15, 23, 42)
    cap_box.line.color.rgb = C_CARD_BORDER
    cp_tf = cap_box.text_frame
    cp_tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    cp_p = cp_tf.paragraphs[0]
    cp_p.text = "TOTAL NODE COST: ₹9,850 (~$118)  ·  POWER DRAW: 59.5 Wh/day  ·  48-HR ZERO-SUN AUTONOMY  ·  IP65 ENCLOSURE (-10°C to +60°C)  ·  GPIO 17 RELAY / GPIO 27 RAIN"
    cp_p.font.name = FONT_TITLE
    cp_p.font.size = Pt(9.5)
    cp_p.font.bold = True
    cp_p.font.color.rgb = C_AMBER
    cp_p.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 4: FEASIBILITY, RISKS & MITIGATION
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    apply_background(slide4)
    add_header(slide4, "Feasibility, Viability & Risk Mitigation", "Demonstrated hardware-software readiness, identified failure modes, and defence-in-depth safeguards")

    col_w = Inches(3.8)
    col_gap = Inches(0.26)
    c1_x = Inches(0.7)
    c2_x = c1_x + col_w + col_gap
    c3_x = c2_x + col_w + col_gap
    card_top = Inches(1.35)
    card_h = Inches(5.75)

    # Col 1: Feasibility
    card1 = add_card(slide4, c1_x, card_top, col_w, card_h, border_color=C_GREEN)
    c1_tf = card1.text_frame
    c1_tf.word_wrap = True
    c1_tf.margin_top = Inches(0.12)
    c1_tf.margin_left = Inches(0.12)
    c1_p0 = c1_tf.paragraphs[0]
    c1_p0.text = "1. Feasibility & Readiness"
    c1_p0.font.name = FONT_TITLE
    c1_p0.font.size = Pt(13)
    c1_p0.font.bold = True
    c1_p0.font.color.rgb = C_GREEN

    feas_items = [
        ("Built, Not Proposed:", "Runs today as an autonomous systemd service (kisan-edge.service); 32.4 ms benchmark, confusion matrices and BOM are committed repository artefacts."),
        ("Commodity Supply Chain:", "All 12 BOM items sourced off-the-shelf from Indian electronics distributors. Zero custom silicon, zero import lead times."),
        ("Power Budget Closes:", "59.5 Wh/day consumption → 74.4 Wh/day with conversion; 4.0 peak-sun hours requires 18.6 W. 20W PV + 12V 7Ah battery provides 48h zero-sun autonomy."),
        ("Latency Closes:", "32.4 ms per frame on Pi's Cortex-A72 CPU — zero GPU required, zero cloud round-trip delay."),
        ("Team Competence:", "Python, PyTorch, FastAPI, Flutter in hand; clean GPIO hardware layer under 1,000 lines.")
    ]
    for t, d in feas_items:
        p = c1_tf.add_paragraph()
        p.text = f"• {t} {d}"
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_LIGHT

    # Col 2: Challenges & Risks
    card2 = add_card(slide4, c2_x, card_top, col_w, card_h, border_color=C_RED)
    c2_tf = card2.text_frame
    c2_tf.word_wrap = True
    c2_tf.margin_top = Inches(0.12)
    c2_tf.margin_left = Inches(0.12)
    c2_p0 = c2_tf.paragraphs[0]
    c2_p0.text = "2. Potential Challenges & Risks"
    c2_p0.font.name = FONT_TITLE
    c2_p0.font.size = Pt(13)
    c2_p0.font.bold = True
    c2_p0.font.color.rgb = C_RED

    risk_items = [
        ("Sensor Drift & Salinity:", "Capacitive probes drift with soil salinity and temperature; uncalibrated probes produce incorrect irrigation."),
        ("Training-Data Gaps:", "No verified public leaf dataset exists for wheat rust, rice blast, or cotton blight at Indian field quality."),
        ("Actuation Hazards:", "A stuck relay floods fields, depletes groundwater, and burns pump motors."),
        ("GSM Network Sunset:", "SIM800L operates on 2G; 2G sunset is an eventual transition risk in some telecom circles."),
        ("Farmer Trust & Literacy:", "Unexplained instructions from an anonymous plastic box in a field will be rejected by farmers."),
        ("Non-Stationary Weather:", "Static models degrade as climate patterns and pest migration windows shift across seasons.")
    ]
    for t, d in risk_items:
        p = c2_tf.add_paragraph()
        p.text = f"• {t} {d}"
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_LIGHT

    # Col 3: Mitigation Strategies
    card3 = add_card(slide4, c3_x, card_top, col_w, card_h, border_color=C_CYAN)
    c3_tf = card3.text_frame
    c3_tf.word_wrap = True
    c3_tf.margin_top = Inches(0.12)
    c3_tf.margin_left = Inches(0.12)
    c3_p0 = c3_tf.paragraphs[0]
    c3_p0.text = "3. Defence-in-Depth Mitigation"
    c3_p0.font.name = FONT_TITLE
    c3_p0.font.size = Pt(13)
    c3_p0.font.bold = True
    c3_p0.font.color.rgb = C_CYAN

    mit_items = [
        ("Two-Point Calibration:", "Air-dry and saturated-wet thresholds stored in SQLite; readings outside 1.2–3.0V rejected automatically."),
        ("Declared Boundary:", "Untrained crops return ICAR symptom guidance with confidence: null; field photos queue for model refresh."),
        ("Triple Actuation Guard:", "Opto-isolated active-LOW relay (GPIO 17) + 15-min HW watchdog cutoff + FC-37 rain plate (GPIO 27) physical veto."),
        ("Three-Tier Comms Fallback:", "GSM SMS (Devanagari) → LoRa 868 MHz → Local buzzer/LED. LTE-CAT1 modem is a drop-in UART replacement."),
        ("Explainable Voice (11 Langs):", "Every alert gives physical reason + confidence + direct verified ICAR-KVK scientist contact phone line."),
        ("Store-and-Forward Sync:", "Zero data lost offline; telemetry and diagnostic outcomes sync when backhaul reconnects.")
    ]
    for t, d in mit_items:
        p = c3_tf.add_paragraph()
        p.text = f"• {t} {d}"
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_LIGHT

    # =========================================================================
    # SLIDE 5: IMPACT, BENEFITS & DISASTER RESILIENCE
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    apply_background(slide5)
    add_header(slide5, "Impact, Benefits & Disaster Resilience Engine", "Quantifiable agronomic, economic, environmental impact backed by multi-hazard early warning")

    # Left Column: Impact & Benefits (Width 5.2 inches)
    impact_card = add_card(slide5, Inches(0.7), Inches(1.35), Inches(5.3), Inches(3.2))
    ic_tf = impact_card.text_frame
    ic_tf.word_wrap = True
    ic_tf.margin_top = Inches(0.12)
    ic_tf.margin_left = Inches(0.12)
    ic_p0 = ic_tf.paragraphs[0]
    ic_p0.text = "1. Target Audience Impact (Marginal Farmers)"
    ic_p0.font.name = FONT_TITLE
    ic_p0.font.size = Pt(12)
    ic_p0.font.bold = True
    ic_p0.font.color.rgb = C_AMBER

    impact_points = [
        ("Earlier Detection (48h):", "Blight and rust are treatable in first 48h. 32 ms on-device diagnosis shifts decision from expert visit to instant triage."),
        ("Water Applied to Demand:", "FAO-56 Hargreaves ETc scheduling cuts wasteful fixed-interval flood irrigation by 25–40%."),
        ("Hazards Seen Before Arrival:", "Drought, flood, heatwave & outbreak indices give lead time for pre-emptive irrigation or early spray windows."),
        ("Survives Network Blackouts:", "GSM SMS and LoRa 868 MHz ensure critical disaster warnings reach farmers when cell towers fail."),
        ("A Reason, Not an Order:", "SHAP attribution in 11 Indian languages plus verified ICAR-KVK contact empowers farmer trust.")
    ]
    for t, d in impact_points:
        p = ic_tf.add_paragraph()
        p.text = f"• {t} {d}"
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_LIGHT

    # Benefits 4-Quadrant Card
    ben_card = add_card(slide5, Inches(0.7), Inches(4.7), Inches(5.3), Inches(2.4))
    bc_tf = ben_card.text_frame
    bc_tf.word_wrap = True
    bc_tf.margin_top = Inches(0.12)
    bc_tf.margin_left = Inches(0.12)
    bc_p0 = bc_tf.paragraphs[0]
    bc_p0.text = "2. Multi-Dimensional Benefits"
    bc_p0.font.name = FONT_TITLE
    bc_p0.font.size = Pt(12)
    bc_p0.font.bold = True
    bc_p0.font.color.rgb = C_GREEN

    benefits = [
        ("Social:", "Voice-first advisory in 11 languages; reaches marginal farmers without smartphones or data connectivity."),
        ("Economic:", "Reduces chemical & diesel pump costs; prevents crop loss; ₹9,850 node accessible to FPOs without subsidies."),
        ("Environmental:", "Rain-aware pump scheduling preserves groundwater; targeted spray windows reduce aquifer runoff."),
        ("Technological:", "Proves quantized CNNs + explainable agronomy run on a ₹4,200 SBC; direct migration path to Qualcomm NPU.")
    ]
    for t, d in benefits:
        p = bc_tf.add_paragraph()
        p.text = f"• {t} {d}"
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_LIGHT

    # Right Column: Diagram D3 (Multi-Hazard Resilience Engine)
    d3_w = Inches(6.45)
    d3_h = Inches(5.75)
    if os.path.exists(d3_png):
        slide5.shapes.add_picture(d3_png, Inches(6.2), Inches(1.35), width=d3_w, height=d3_h)
    else:
        d3_box = add_card(slide5, Inches(6.2), Inches(1.35), d3_w, d3_h)
        d3_box.text_frame.text = "D3: Multi-Hazard Disaster Resilience Engine\n(Drought, Flood, Heatwave, Outbreak Indices)"

    # =========================================================================
    # SLIDE 6: RESEARCH, EVIDENCE & DEFENSE
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    apply_background(slide6)
    add_header(slide6, "Research, Empirical Evidence & Defense Dossier", "Scientific citations, capability boundary, benchmark rigor, and verbatim data honesty commitment")

    # Upper Area: Diagram D4 (Evidence Panel)
    d4_w = Inches(11.933)
    d4_h = Inches(3.55)
    if os.path.exists(d4_png):
        slide6.shapes.add_picture(d4_png, Inches(0.7), Inches(1.35), width=d4_w, height=d4_h)
    else:
        d4_box = add_card(slide6, Inches(0.7), Inches(1.35), d4_w, d4_h)
        d4_box.text_frame.text = "D4: Validation & Capability Panel (Capability boundary, 5-Fold CV, Edge profiling)"

    # Bottom Area: Left = Citations, Right = Data Honesty Statement
    bot_top = Inches(5.02)
    bot_h = Inches(2.15)

    # Left: Citations Card (Width 6.4 inches)
    cit_card = add_card(slide6, Inches(0.7), bot_top, Inches(6.6), bot_h)
    cc_tf = cit_card.text_frame
    cc_tf.word_wrap = True
    cc_tf.margin_top = Inches(0.1)
    cc_tf.margin_left = Inches(0.12)
    cc_p0 = cc_tf.paragraphs[0]
    cc_p0.text = "Peer-Reviewed Agronomic & Machine Learning Foundations"
    cc_p0.font.name = FONT_TITLE
    cc_p0.font.size = Pt(11)
    cc_p0.font.bold = True
    cc_p0.font.color.rgb = C_CYAN

    citations = [
        "• FAO Irrigation & Drainage Paper 56 — Allen et al. (1998) [Hargreaves ET₀, Kc water balance]",
        "• PlantVillage — Hughes & Salathé (CC-BY-SA) [4,200 verified images across 7 CNN classes]",
        "• MobileNetV2 — Sandler et al., CVPR 2018 [Inverted Residuals & Linear Bottlenecks]",
        "• SHAP — Lundberg & Lee, NeurIPS 2017 [A Unified Approach to Interpreting Model Predictions]",
        "• ISRIC SoilGrids v2.0 (250m global layers) · Open-Meteo ECMWF (7-day forecast)",
        "• ICAR / TNAU / PAU Extension Guidelines [Symptom triage, ETL thresholds, bio/chemical dosing]"
    ]
    for c_text in citations:
        p = cc_tf.add_paragraph()
        p.text = c_text
        p.font.name = FONT_BODY
        p.font.size = Pt(8.8)
        p.font.color.rgb = C_TEXT_LIGHT

    # Right: Data Honesty Statement Card (Width 5.1 inches)
    hon_card = add_card(slide6, Inches(7.5), bot_top, Inches(5.133), bot_h, border_color=C_GREEN)
    hc_tf = hon_card.text_frame
    hc_tf.word_wrap = True
    hc_tf.margin_top = Inches(0.1)
    hc_tf.margin_left = Inches(0.12)
    hc_p0 = hc_tf.paragraphs[0]
    hc_p0.text = "VERBATIM DATA HONESTY STATEMENT"
    hc_p0.font.name = FONT_TITLE
    hc_p0.font.size = Pt(11)
    hc_p0.font.bold = True
    hc_p0.font.color.rgb = C_GREEN

    hc_p1 = hc_tf.add_paragraph()
    hc_p1.text = '"Every API response carries an explicit source field. Where a live feed is unavailable the system degrades to a clearly-labelled cached or estimated value. It never presents simulated data as verified data. Confidence scores are raw softmax outputs — never floored, clamped, or invented."'
    hc_p1.font.name = FONT_BODY
    hc_p1.font.size = Pt(9.5)
    hc_p1.font.italic = True
    hc_p1.font.color.rgb = C_TEXT_WHITE

    hc_p2 = hc_tf.add_paragraph()
    hc_p2.text = "Core DNA: edge-first (32.4 ms) · offline-first (GSM → LoRa) · closed-loop (sense → decide → pump) · explainable (11 langs) · bounded (declared boundary)."
    hc_p2.font.name = FONT_BODY
    hc_p2.font.size = Pt(9)
    hc_p2.font.bold = True
    hc_p2.font.color.rgb = C_AMBER

    # =========================================================================
    # SAVE PPTX
    # =========================================================================
    output_path = os.path.join(base_dir, "Kisaan_Sathi_SIH2026_Official_Presentation.pptx")
    prs.save(output_path)
    print(f"[OK] Generated PPTX at: {output_path}")

    # Copy to user Downloads folder if accessible
    downloads_dir = os.path.expanduser(r"~\Downloads")
    if os.path.exists(downloads_dir):
        dl_target = os.path.join(downloads_dir, "Kisaan_Sathi_SIH2026_Official_Presentation.pptx")
        try:
            shutil.copy2(output_path, dl_target)
            print(f"[OK] Copied PPTX to Downloads: {dl_target}")
        except Exception as e:
            print(f"[WARN] Could not copy to Downloads: {e}")

if __name__ == "__main__":
    build_presentation()
