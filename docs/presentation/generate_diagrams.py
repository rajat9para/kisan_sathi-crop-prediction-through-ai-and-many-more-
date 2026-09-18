"""
Generates the 4 Official High-Resolution Vector Diagrams for Kisaan Sathi (SIH 2026):
- D1_hardware_block_diagram_v2.svg
- D2_edge_decision_loop_v2.svg
- D3_disaster_resilience_engine_v2.svg
- D4_validation_and_capability_panel_v2.svg
"""

import os
import sys
import shutil

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

OUTPUT_DIRS = [
    os.path.join("docs", "presentation"),
    os.path.join("docs", "assets"),
    "."
]

def save_svg(filename: str, content: str):
    for d in OUTPUT_DIRS:
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"[OK] Saved: {path}")

# ==============================================================================
# D1: HARDWARE BLOCK DIAGRAM v2
# ==============================================================================
D1_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 820" width="100%" height="100%" style="background:#0F172A; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <linearGradient id="gradPrimary" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="gradGreen" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <linearGradient id="gradBlue" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#0284C7"/>
    </linearGradient>
    <linearGradient id="gradAmber" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#D97706"/>
    </linearGradient>
    <linearGradient id="gradPurple" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#A855F7"/>
      <stop offset="100%" stop-color="#7E22CE"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Title Header Banner -->
  <rect x="30" y="25" width="1220" height="75" rx="12" fill="#1E293B" stroke="#334155" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="60" y="60" font-size="22" font-weight="700" fill="#F8FAFC">D1: Kisaan Sathi Edge Node — Hardware Architecture &amp; Subsystem Interconnect</text>
  <text x="60" y="84" font-size="13" fill="#94A3B8">SIH 2026 · PS #26180 (Disaster Management) · Hardware Edition · Sponsoring Org: Qualcomm Inc · Total Node BOM: ₹9,850</text>
  <rect x="1100" y="42" width="130" height="32" rx="6" fill="#10B981" fill-opacity="0.2" stroke="#10B981" stroke-width="1.5"/>
  <text x="1165" y="63" font-size="12" font-weight="700" fill="#34D399" text-anchor="middle">PHYSICAL BUILD</text>

  <!-- 1. COMPUTE SBC CORE (CENTER LEFT) -->
  <rect x="420" y="125" width="440" height="370" rx="14" fill="#1E293B" stroke="#38BDF8" stroke-width="2" filter="url(#shadow)"/>
  <rect x="420" y="125" width="440" height="42" rx="14" fill="#0284C7" fill-opacity="0.2"/>
  <text x="445" y="152" font-size="16" font-weight="700" fill="#38BDF8">COMPUTE ENGINE: RASPBERRY PI 4 MODEL B (4GB)</text>
  <text x="445" y="190" font-size="13" fill="#CBD5E1">Quad-core Arm Cortex-A72 @ 1.5 GHz · 4GB LPDDR4</text>
  <text x="445" y="212" font-size="13" fill="#CBD5E1">Operating System: Linux (Debian 12 Bookworm, 64-bit)</text>
  <text x="445" y="234" font-size="13" fill="#CBD5E1">Edge Runtime: ONNX Runtime INT8 (32.4 ms / frame)</text>
  <text x="445" y="256" font-size="13" fill="#CBD5E1">Execution: Autonomous systemd daemon (<tspan fill="#38BDF8">kisan-edge.service</tspan>)</text>

  <!-- Pi Internal Interfaces Sub-Box -->
  <rect x="440" y="275" width="400" height="200" rx="8" fill="#0F172A" stroke="#334155" stroke-width="1"/>
  <text x="455" y="298" font-size="12" font-weight="700" fill="#94A3B8">40-PIN EXPANSION HEADER &amp; CSI INTERCONNECT</text>
  
  <text x="455" y="325" font-size="12" fill="#E2E8F0"><tspan font-weight="700" fill="#34D399">I2C Bus 1</tspan> (Pins 3 &amp; 5 · GPIO 2/3) ──► ADS1115 16-bit ADC (Addr 0x48)</text>
  <text x="455" y="352" font-size="12" fill="#E2E8F0"><tspan font-weight="700" fill="#FBBF24">1-Wire Bus</tspan> (Pin 7 · GPIO 4) ────────► DHT22 Temp &amp; Humidity</text>
  <text x="455" y="380" font-size="12" fill="#E2E8F0"><tspan font-weight="700" fill="#F87171">Rain Int</tspan> (Pin 13 · GPIO 27) ────────► FC-37 Rain Plate (Active-LOW)</text>
  <text x="455" y="407" font-size="12" fill="#E2E8F0"><tspan font-weight="700" fill="#60A5FA">Relay Veto</tspan> (Pin 11 · GPIO 17) ──────► 5V Opto Relay (Active-LOW)</text>
  <text x="455" y="435" font-size="12" fill="#E2E8F0"><tspan font-weight="700" fill="#C084FC">UART0</tspan> (Pins 8 &amp; 10 · GPIO 14/15) ────► SIM800L GSM (9600 baud)</text>
  <text x="455" y="462" font-size="12" fill="#E2E8F0"><tspan font-weight="700" fill="#A78BFA">SPI0 Bus</tspan> (Pins 19, 21, 23, 24) ──────► Reyax RYLR896 LoRa 868MHz</text>

  <!-- 2. SENSING ARRAY (LEFT COLUMN) -->
  <rect x="30" y="125" width="360" height="370" rx="14" fill="#1E293B" stroke="#10B981" stroke-width="2" filter="url(#shadow)"/>
  <rect x="30" y="125" width="360" height="42" rx="14" fill="#059669" fill-opacity="0.2"/>
  <text x="50" y="152" font-size="16" font-weight="700" fill="#34D399">PHYSICAL SENSING ARRAY</text>

  <!-- Soil Sensor & ADC -->
  <rect x="48" y="180" width="324" height="68" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="62" y="202" font-size="13" font-weight="700" fill="#F1F5F9">Capacitive Soil Moisture Probe v1.2</text>
  <text x="62" y="222" font-size="11" fill="#94A3B8">Corrosion-resistant analog output (1.2V wet – 3.0V dry)</text>
  <text x="62" y="238" font-size="11" fill="#34D399">Interfaced via ADS1115 16-Bit I2C ADC (0.125 mV/LSB)</text>

  <!-- DHT22 Sensor -->
  <rect x="48" y="258" width="324" height="64" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="62" y="280" font-size="13" font-weight="700" fill="#F1F5F9">DHT22 Ambient Microclimate</text>
  <text x="62" y="300" font-size="11" fill="#94A3B8">Temp: -40 to +80°C (±0.5°C) · RH: 0–100% (±2%)</text>
  <text x="62" y="314" font-size="11" fill="#FBBF24">Feeds FAO-56 Hargreaves ET₀ &amp; Heatwave Index</text>

  <!-- FC-37 Rain Sensor -->
  <rect x="48" y="332" width="324" height="64" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="62" y="354" font-size="13" font-weight="700" fill="#F1F5F9">FC-37 Rain Conduction Sensor Plate</text>
  <text x="62" y="374" font-size="11" fill="#94A3B8">LM393 comparator · Digital DO to GPIO 27</text>
  <text x="62" y="388" font-size="11" fill="#F87171">Hardware lockout veto (overrides software irrigation)</text>

  <!-- Pi Camera V2 -->
  <rect x="48" y="406" width="324" height="74" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="62" y="428" font-size="13" font-weight="700" fill="#F1F5F9">Raspberry Pi Camera Module V2</text>
  <text x="62" y="448" font-size="11" fill="#94A3B8">8MP Sony IMX219 via dedicated 2-Lane MIPI CSI-2</text>
  <text x="62" y="462" font-size="11" fill="#38BDF8">Laplacian Blur &amp; Green Chroma Quality Gating</text>

  <!-- 3. ACTUATION & POWER (RIGHT COLUMN) -->
  <rect x="890" y="125" width="360" height="370" rx="14" fill="#1E293B" stroke="#F59E0B" stroke-width="2" filter="url(#shadow)"/>
  <rect x="890" y="125" width="360" height="42" rx="14" fill="#D97706" fill-opacity="0.2"/>
  <text x="910" y="152" font-size="16" font-weight="700" fill="#FBBF24">ACTUATION &amp; POWER SUBSYSTEM</text>

  <!-- Relay & Pump -->
  <rect x="908" y="180" width="324" height="88" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="922" y="202" font-size="13" font-weight="700" fill="#F1F5F9">Opto-Isolated 5V Relay ──► 12V DC Pump</text>
  <text x="922" y="222" font-size="11" fill="#94A3B8">Active-LOW trigger on GPIO 17 (no boot transients)</text>
  <text x="922" y="238" font-size="11" fill="#FBBF24">Actuates 12V R385 Diaphragm Micro-Pump (1.8 L/min)</text>
  <text x="922" y="254" font-size="11" fill="#F87171">Hard 15-Minute Watchdog Cutoff (firmware safe)</text>

  <!-- Solar PV & Battery -->
  <rect x="908" y="278" width="324" height="96" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="922" y="300" font-size="13" font-weight="700" fill="#F1F5F9">Off-Grid Solar Energy Harvesting</text>
  <text x="922" y="320" font-size="11" fill="#94A3B8">20W Monocrystalline PV Panel (18V Voc)</text>
  <text x="922" y="336" font-size="11" fill="#94A3B8">10A PWM Solar Charge Controller + 12V 7Ah VRLA</text>
  <text x="922" y="352" font-size="11" fill="#34D399">Dual LM2596 Buck Converters (5V 3A &amp; 4.2V 2A)</text>
  <text x="922" y="366" font-size="11" fill="#38BDF8">Daily consumption: 59.5 Wh/day · 48h zero-sun reserve</text>

  <!-- Enclosure & Protection -->
  <rect x="908" y="384" width="324" height="96" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="922" y="406" font-size="13" font-weight="700" fill="#F1F5F9">IP65 Rugged Industrial Enclosure</text>
  <text x="922" y="426" font-size="11" fill="#94A3B8">ABS Weatherproof junction housing with cable glands</text>
  <text x="922" y="442" font-size="11" fill="#94A3B8">Operating range: -10°C to +60°C ambient field temp</text>
  <text x="922" y="458" font-size="11" fill="#A855F7">Surge suppression &amp; flyback diode on inductive pump</text>

  <!-- 4. ZERO-INTERNET RESILIENT COMMUNICATIONS (BOTTOM HALF) -->
  <rect x="30" y="515" width="1220" height="180" rx="14" fill="#1E293B" stroke="#A855F7" stroke-width="2" filter="url(#shadow)"/>
  <rect x="30" y="515" width="1220" height="38" rx="14" fill="#7E22CE" fill-opacity="0.2"/>
  <text x="50" y="540" font-size="15" font-weight="700" fill="#C084FC">THREE-TIER GRACEFUL DEGRADATION COMMUNICATIONS SUBSYSTEM (SURVIVES COMPLETE NETWORK BLACKOUT)</text>

  <!-- Comms Tier 1: Cloud/Web -->
  <rect x="50" y="565" width="370" height="115" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="70" y="590" font-size="13" font-weight="700" fill="#38BDF8">TIER 1: HIGH-SPEED CLOUD / DASHBOARD</text>
  <text x="70" y="612" font-size="12" fill="#CBD5E1">Wi-Fi (802.11ac) / 4G Cellular Backhaul</text>
  <text x="70" y="632" font-size="11" fill="#94A3B8">Syncs full NDVI, SoilGrids, APMC Mandi modal prices</text>
  <text x="70" y="650" font-size="11" fill="#94A3B8">Delivers PWA portal &amp; Flutter multi-lingual dashboard</text>
  <text x="70" y="668" font-size="11" fill="#10B981">Active when full Internet connectivity is present</text>

  <!-- Comms Tier 2: Cellular SMS -->
  <rect x="455" y="565" width="370" height="115" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="475" y="590" font-size="13" font-weight="700" fill="#FBBF24">TIER 2: 2G CELLULAR SMS (SIM800L)</text>
  <text x="475" y="612" font-size="12" fill="#CBD5E1">Quad-band GSM/GPRS via UART0 AT-Commands</text>
  <text x="475" y="632" font-size="11" fill="#94A3B8">Pushes Devanagari Hindi / Regional language SMS</text>
  <text x="475" y="650" font-size="11" fill="#94A3B8">Emergency drought, flood, and heatwave micro-alerts</text>
  <text x="475" y="668" font-size="11" fill="#FBBF24">Active when mobile internet fails but 2G signal exists</text>

  <!-- Comms Tier 3: LoRa Mesh + Local -->
  <rect x="860" y="565" width="370" height="115" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="880" y="590" font-size="13" font-weight="700" fill="#A855F7">TIER 3: LONG-RANGE LORA MESH (RYLR896)</text>
  <text x="880" y="612" font-size="12" fill="#CBD5E1">Semtech SX1278 @ 868 MHz (Sub-GHz, SPI0)</text>
  <text x="880" y="632" font-size="11" fill="#94A3B8">14-Byte binary packets with CRC-16-CCITT protection</text>
  <text x="880" y="650" font-size="11" fill="#94A3B8">Meshes 2–5 km to Village Panchayat Gateway or KVK Hub</text>
  <text x="880" y="668" font-size="11" fill="#A855F7">Zero network needed · Fallback to local LED/Buzzer</text>

  <!-- 5. ENGINEERING METRICS FOOTER STRIP -->
  <rect x="30" y="715" width="1220" height="80" rx="10" fill="#0B1329" stroke="#1E293B" stroke-width="1.5"/>
  <text x="60" y="745" font-size="13" font-weight="700" fill="#F8FAFC">ENGINEERING SPECIFICATIONS VERIFIED ON HARDWARE PROTOTYPE:</text>
  <text x="60" y="772" font-size="13" fill="#94A3B8">Total Node Build Cost: <tspan font-weight="700" fill="#34D399">₹9,850 INR (~$118 USD)</tspan>  │  Daily Power Draw: <tspan font-weight="700" fill="#38BDF8">59.5 Wh/day</tspan> (74.4 Wh with conv.)  │  PV Autonomy: <tspan font-weight="700" fill="#FBBF24">48 Hours Zero-Sun</tspan>  │  Measured Inference: <tspan font-weight="700" fill="#A78BFA">32.4 ms</tspan> (Arm Cortex-A72 INT8)</text>
</svg>"""

# ==============================================================================
# D2: EDGE DECISION LOOP v2
# ==============================================================================
D2_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 820" width="100%" height="100%" style="background:#0F172A; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <linearGradient id="gradCard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <filter id="shadowD2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Header -->
  <rect x="30" y="25" width="1220" height="75" rx="12" fill="#1E293B" stroke="#334155" stroke-width="1.5" filter="url(#shadowD2)"/>
  <text x="60" y="60" font-size="22" font-weight="700" fill="#F8FAFC">D2: Closed-Loop Edge Decision Engine &amp; Autonomous Control Flow</text>
  <text x="60" y="84" font-size="13" fill="#94A3B8">Sense ──► Quality Gate ──► 4 Edge AI Engines ──► Safety Guards ──► Actuate Pump &amp; Resilient Alerting</text>
  <rect x="1100" y="42" width="130" height="32" rx="6" fill="#0284C7" fill-opacity="0.2" stroke="#38BDF8" stroke-width="1.5"/>
  <text x="1165" y="63" font-size="12" font-weight="700" fill="#38BDF8" text-anchor="middle">DECISION ENGINE</text>

  <!-- STEP 1: WAKEUP & SENSE -->
  <rect x="30" y="125" width="220" height="420" rx="12" fill="#1E293B" stroke="#34D399" stroke-width="1.5" filter="url(#shadowD2)"/>
  <rect x="30" y="125" width="220" height="38" rx="12" fill="#059669" fill-opacity="0.25"/>
  <text x="45" y="150" font-size="14" font-weight="700" fill="#34D399">1. ACQUISITION</text>
  
  <rect x="42" y="180" width="196" height="58" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="52" y="202" font-size="12" font-weight="700" fill="#F8FAFC">3-Minute Duty Cycle</text>
  <text x="52" y="222" font-size="11" fill="#94A3B8">Low-power edge wakeup</text>

  <rect x="42" y="248" width="196" height="68" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="52" y="270" font-size="12" font-weight="700" fill="#F8FAFC">Capacitive Moisture</text>
  <text x="52" y="290" font-size="11" fill="#94A3B8">ADS1115 16-bit ADC</text>
  <text x="52" y="306" font-size="11" fill="#34D399">VWC%: 1.2V to 3.0V</text>

  <rect x="42" y="326" width="196" height="68" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="52" y="348" font-size="12" font-weight="700" fill="#F8FAFC">DHT22 Microclimate</text>
  <text x="52" y="368" font-size="11" fill="#94A3B8">Ambient Temp &amp; RH</text>
  <text x="52" y="384" font-size="11" fill="#FBBF24">Tmax / Tmin tracking</text>

  <rect x="42" y="404" width="196" height="58" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="52" y="426" font-size="12" font-weight="700" fill="#F8FAFC">FC-37 Rain &amp; Camera</text>
  <text x="52" y="446" font-size="11" fill="#94A3B8">Pin 27 Rain + Pi Cam V2</text>

  <rect x="42" y="472" width="196" height="58" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="52" y="494" font-size="12" font-weight="700" fill="#F8FAFC">Local SQLite Sync</text>
  <text x="52" y="514" font-size="11" fill="#38BDF8">Zero data loss buffer</text>

  <!-- STEP 2: QUALITY GATE -->
  <rect x="275" y="125" width="200" height="420" rx="12" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5" filter="url(#shadowD2)"/>
  <rect x="275" y="125" width="200" height="38" rx="12" fill="#D97706" fill-opacity="0.25"/>
  <text x="290" y="150" font-size="14" font-weight="700" fill="#FBBF24">2. QUALITY GATE</text>

  <rect x="287" y="180" width="176" height="100" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="297" y="202" font-size="12" font-weight="700" fill="#F8FAFC">Laplacian Blur Filter</text>
  <text x="297" y="222" font-size="11" fill="#94A3B8">cv2.Laplacian() variance</text>
  <text x="297" y="242" font-size="11" fill="#F87171">σ² &lt; 100 ──► Blur Reject</text>
  <text x="297" y="262" font-size="11" fill="#34D399">σ² ≥ 100 ──► Frame Pass</text>

  <rect x="287" y="295" width="176" height="100" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="297" y="317" font-size="12" font-weight="700" fill="#F8FAFC">Foliage Chroma Gate</text>
  <text x="297" y="337" font-size="11" fill="#94A3B8">Excess Green: 2G - R - B</text>
  <text x="297" y="357" font-size="11" fill="#F87171">&lt; 12% ──► Non-crop Veto</text>
  <text x="297" y="377" font-size="11" fill="#34D399">≥ 12% ──► Leaf Verified</text>

  <rect x="287" y="410" width="176" height="120" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="297" y="432" font-size="12" font-weight="700" fill="#F8FAFC">Sensor Range Audit</text>
  <text x="297" y="452" font-size="11" fill="#94A3B8">ADC: 1.2V to 3.0V limits</text>
  <text x="297" y="472" font-size="11" fill="#94A3B8">DHT22: -10 to 55°C</text>
  <text x="297" y="492" font-size="11" fill="#F87171">Out-of-range discarded</text>
  <text x="297" y="512" font-size="11" fill="#34D399">Prevents bad actuation</text>

  <!-- STEP 3: 4 ON-DEVICE AI ENGINES -->
  <rect x="500" y="125" width="300" height="420" rx="12" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5" filter="url(#shadowD2)"/>
  <rect x="500" y="125" width="300" height="38" rx="12" fill="#0284C7" fill-opacity="0.25"/>
  <text x="515" y="150" font-size="14" font-weight="700" fill="#38BDF8">3. FOUR EDGE AI ENGINES</text>

  <rect x="512" y="180" width="276" height="78" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="522" y="200" font-size="12" font-weight="700" fill="#38BDF8">A. Leaf Pathology (MobileNetV2 INT8)</text>
  <text x="522" y="218" font-size="11" fill="#CBD5E1">7 Verified classes: 95.87% val accuracy</text>
  <text x="522" y="234" font-size="11" fill="#94A3B8">16 Crops: ICAR symptoms (conf: null)</text>
  <text x="522" y="248" font-size="11" fill="#34D399">Inference: 32.4 ms on Arm CPU</text>

  <rect x="512" y="268" width="276" height="78" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="522" y="288" font-size="12" font-weight="700" fill="#34D399">B. Nutrient Deficiency (XGBoost + SHAP)</text>
  <text x="522" y="306" font-size="11" fill="#CBD5E1">Soil Health Card OCR + Sensor NPK/pH</text>
  <text x="522" y="322" font-size="11" fill="#94A3B8">SHAP log-odds feature attributions</text>
  <text x="522" y="336" font-size="11" fill="#38BDF8">Spoken rationale in 11 languages</text>

  <rect x="512" y="356" width="276" height="78" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="522" y="376" font-size="12" font-weight="700" fill="#FBBF24">C. Water Budget (FAO-56 Hargreaves)</text>
  <text x="522" y="394" font-size="11" fill="#CBD5E1">ET₀ = 0.0023(T+17.8)√(Tmax-Tmin)Ra</text>
  <text x="522" y="410" font-size="11" fill="#94A3B8">ETc = Kc × ET₀ · Soil Deficit (Dsoil)</text>
  <text x="522" y="424" font-size="11" fill="#FBBF24">Converts deficit liters to pump seconds</text>

  <rect x="512" y="444" width="276" height="88" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="522" y="464" font-size="12" font-weight="700" fill="#F87171">D. Environmental Hazard Indices (0–100)</text>
  <text x="522" y="482" font-size="11" fill="#CBD5E1">Drought Risk · Flood Risk</text>
  <text x="522" y="498" font-size="11" fill="#94A3B8">Canopy Heat Stress · Pathogen Outbreak</text>
  <text x="522" y="514" font-size="11" fill="#F87171">Fused with Open-Meteo 7-day forecast</text>

  <!-- STEP 4: PHYSICAL ACTUATION & GUARDS -->
  <rect x="825" y="125" width="210" height="420" rx="12" fill="#1E293B" stroke="#F87171" stroke-width="1.5" filter="url(#shadowD2)"/>
  <rect x="825" y="125" width="210" height="38" rx="12" fill="#DC2626" fill-opacity="0.25"/>
  <text x="840" y="150" font-size="14" font-weight="700" fill="#F87171">4. ACTUATION GUARDS</text>

  <rect x="837" y="180" width="186" height="100" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="847" y="202" font-size="12" font-weight="700" fill="#F87171">Rain Veto (Guard 1)</text>
  <text x="847" y="222" font-size="11" fill="#94A3B8">FC-37 Pin 27 active?</text>
  <text x="847" y="242" font-size="11" fill="#F87171">YES ──► HARD PUMP LOCK</text>
  <text x="847" y="262" font-size="11" fill="#34D399">NO  ──► Check Moisture</text>

  <rect x="837" y="295" width="186" height="100" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="847" y="317" font-size="12" font-weight="700" fill="#38BDF8">Relay Firing (Guard 2)</text>
  <text x="847" y="337" font-size="11" fill="#94A3B8">VWC &lt; 22% threshold?</text>
  <text x="847" y="357" font-size="11" fill="#34D399">YES ──► GPIO 17 Active-LOW</text>
  <text x="847" y="377" font-size="11" fill="#94A3B8">12V R385 Pump Starts</text>

  <rect x="837" y="410" width="186" height="120" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="847" y="432" font-size="12" font-weight="700" fill="#FBBF24">Watchdog (Guard 3)</text>
  <text x="847" y="452" font-size="11" fill="#94A3B8">Continuous run time</text>
  <text x="847" y="472" font-size="11" fill="#F87171">t ≥ 15 min ──► SAFETY TRIP</text>
  <text x="847" y="492" font-size="11" fill="#CBD5E1">Prevents motor burnout</text>
  <text x="847" y="512" font-size="11" fill="#34D399">Prevents root hypoxia</text>

  <!-- STEP 5: DEGRADED COMMS OUTPUT -->
  <rect x="1060" y="125" width="190" height="420" rx="12" fill="#1E293B" stroke="#A855F7" stroke-width="1.5" filter="url(#shadowD2)"/>
  <rect x="1060" y="125" width="190" height="38" rx="12" fill="#7E22CE" fill-opacity="0.25"/>
  <text x="1075" y="150" font-size="14" font-weight="700" fill="#C084FC">5. DELIVERY</text>

  <rect x="1072" y="180" width="166" height="75" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="1082" y="202" font-size="12" font-weight="700" fill="#38BDF8">Cloud / Web</text>
  <text x="1082" y="222" font-size="11" fill="#94A3B8">PWA &amp; Flutter App</text>
  <text x="1082" y="240" font-size="11" fill="#34D399">If 4G/Wi-Fi active</text>

  <rect x="1072" y="268" width="166" height="75" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="1082" y="290" font-size="12" font-weight="700" fill="#FBBF24">Cellular SMS</text>
  <text x="1082" y="310" font-size="11" fill="#94A3B8">SIM800L Hindi SMS</text>
  <text x="1082" y="328" font-size="11" fill="#FBBF24">Feature phone direct</text>

  <rect x="1072" y="356" width="166" height="75" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="1082" y="378" font-size="12" font-weight="700" fill="#A855F7">LoRa 868 MHz</text>
  <text x="1082" y="398" font-size="11" fill="#94A3B8">RYLR896 Mesh</text>
  <text x="1082" y="416" font-size="11" fill="#A855F7">To Village Gateway</text>

  <rect x="1072" y="444" width="166" height="88" rx="6" fill="#0F172A" stroke="#334155"/>
  <text x="1082" y="466" font-size="12" font-weight="700" fill="#34D399">Autonomous</text>
  <text x="1082" y="486" font-size="11" fill="#94A3B8">Local Pump Action</text>
  <text x="1082" y="504" font-size="11" fill="#CBD5E1">Heartbeat Buzzer</text>
  <text x="1082" y="520" font-size="11" fill="#34D399">Zero-network survival</text>

  <!-- Connective Arrows & Dataflow Strip across bottom -->
  <rect x="30" y="565" width="1220" height="225" rx="12" fill="#1E293B" stroke="#334155" stroke-width="1.5" filter="url(#shadowD2)"/>
  <text x="60" y="595" font-size="15" font-weight="700" fill="#F8FAFC">CRITICAL ARCHITECTURAL SAFEGUARDS BUILT INTO THE CONTROL LOOP:</text>

  <!-- Box 1 -->
  <rect x="50" y="615" width="370" height="155" rx="8" fill="#0F172A" stroke="#10B981"/>
  <text x="70" y="640" font-size="13" font-weight="700" fill="#34D399">1. PHYSICAL CONSEQUENCE CONTROL</text>
  <text x="70" y="662" font-size="12" fill="#CBD5E1">• Galvanic Opto-Isolation prevents MCU latchup.</text>
  <text x="70" y="684" font-size="12" fill="#CBD5E1">• Active-LOW relay logic eliminates startup glitches.</text>
  <text x="70" y="706" font-size="12" fill="#CBD5E1">• Hard 15-minute watchdog cannot be overridden by software.</text>
  <text x="70" y="728" font-size="12" fill="#CBD5E1">• Rain sensor hardware veto stops pumping regardless of soil state.</text>

  <!-- Box 2 -->
  <rect x="455" y="615" width="370" height="155" rx="8" fill="#0F172A" stroke="#38BDF8"/>
  <text x="475" y="640" font-size="13" font-weight="700" fill="#38BDF8">2. DECLARED CAPABILITY BOUNDARY</text>
  <text x="475" y="662" font-size="12" fill="#CBD5E1">• 7 CNN classes diagnosed with 95.87% validated accuracy.</text>
  <text x="475" y="684" font-size="12" fill="#CBD5E1">• 16 further crops served by ICAR/TNAU symptom guidance.</text>
  <text x="475" y="706" font-size="12" fill="#CBD5E1">• Confidence returned as NULL when no verified neural model exists.</text>
  <text x="475" y="728" font-size="12" fill="#CBD5E1">• We never fabricate confidence scores or fake bounding boxes.</text>

  <!-- Box 3 -->
  <rect x="860" y="615" width="370" height="155" rx="8" fill="#0F172A" stroke="#A855F7"/>
  <text x="880" y="640" font-size="13" font-weight="700" fill="#C084FC">3. ZERO-INTERNET SURVIVABILITY</text>
  <text x="880" y="662" font-size="12" fill="#CBD5E1">• Full sensing, inference, and pump control runs locally on Pi 4.</text>
  <text x="880" y="684" font-size="12" fill="#CBD5E1">• Devanagari Hindi SMS works over basic 2G voice channel.</text>
  <text x="880" y="706" font-size="12" fill="#CBD5E1">• LoRa 868 MHz transmits 14-byte CRC16 packets across 5 km.</text>
  <text x="880" y="728" font-size="12" fill="#CBD5E1">• System never hangs or stalls waiting for cloud APIs.</text>
</svg>"""

# ==============================================================================
# D3: DISASTER RESILIENCE ENGINE v2
# ==============================================================================
D3_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 850" width="100%" height="100%" style="background:#0F172A; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <linearGradient id="gradD3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <filter id="shadowD3" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Title Header Banner -->
  <rect x="30" y="25" width="1220" height="85" rx="12" fill="#1E293B" stroke="#334155" stroke-width="1.5" filter="url(#shadowD3)"/>
  <text x="60" y="60" font-size="22" font-weight="700" fill="#F8FAFC">D3: Disaster Management &amp; Agro-Climatic Resilience Engine</text>
  <text x="60" y="85" font-size="13" fill="#94A3B8">SIH 2026 Theme: Disaster Management · Four Graded Early-Warning Risk Indices (0–100) with Autonomous Field Interventions</text>
  <rect x="1080" y="42" width="150" height="32" rx="6" fill="#DC2626" fill-opacity="0.2" stroke="#EF4444" stroke-width="1.5"/>
  <text x="1155" y="63" font-size="12" font-weight="700" fill="#F87171" text-anchor="middle">DISASTER THEME</text>

  <!-- 4 HAZARD INDEX CARDS (2x2 GRID) -->

  <!-- 1. DROUGHT RISK -->
  <rect x="30" y="135" width="595" height="260" rx="12" fill="#1E293B" stroke="#F59E0B" stroke-width="2" filter="url(#shadowD3)"/>
  <rect x="30" y="135" width="595" height="42" rx="12" fill="#D97706" fill-opacity="0.25"/>
  <text x="55" y="162" font-size="16" font-weight="700" fill="#FBBF24">1. DROUGHT DEFICIT INDEX (0–100)</text>
  <rect x="490" y="142" width="120" height="26" rx="4" fill="#F59E0B" fill-opacity="0.2"/>
  <text x="550" y="160" font-size="11" font-weight="700" fill="#FBBF24" text-anchor="middle">SOIL &amp; RAIN DEFICIT</text>

  <text x="55" y="202" font-size="13" font-weight="700" fill="#CBD5E1">Mathematical Formulation &amp; Input Telemetry:</text>
  <text x="55" y="224" font-size="12" fill="#94A3B8">• Capacitive Soil VWC (%) trajectory over 72 hours</text>
  <text x="55" y="244" font-size="12" fill="#94A3B8">• Open-Meteo 7-day cumulative precipitation forecast vs. historical ETc</text>
  <text x="55" y="264" font-size="12" fill="#94A3B8">• Soil texture water retention capacity from ISRIC SoilGrids v2.0</text>

  <rect x="50" y="280" width="555" height="100" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="65" y="304" font-size="12" font-weight="700" fill="#FBBF24">Autonomous Edge Interventions &amp; Farmer Action:</text>
  <text x="65" y="324" font-size="12" fill="#E2E8F0">1. Pre-emptive Irrigation Pulse: Triggers deep root-zone wetting before canal shutdown.</text>
  <text x="65" y="344" font-size="12" fill="#E2E8F0">2. Mulching Alert: Dispatches Hindi SMS advising organic mulch to cut soil evaporation.</text>
  <text x="65" y="364" font-size="12" fill="#E2E8F0">3. Anti-Transpirant Advisory: Recommends 2% Kaolin spray to conserve canopy moisture.</text>

  <!-- 2. FLOOD & WATERLOGGING RISK -->
  <rect x="655" y="135" width="595" height="260" rx="12" fill="#1E293B" stroke="#38BDF8" stroke-width="2" filter="url(#shadowD3)"/>
  <rect x="655" y="135" width="595" height="42" rx="12" fill="#0284C7" fill-opacity="0.25"/>
  <text x="680" y="162" font-size="16" font-weight="700" fill="#38BDF8">2. FLOOD &amp; WATERLOGGING RISK (0–100)</text>
  <rect x="1115" y="142" width="120" height="26" rx="4" fill="#38BDF8" fill-opacity="0.2"/>
  <text x="1175" y="160" font-size="11" font-weight="700" fill="#38BDF8" text-anchor="middle">DELUGE &amp; HYPOXIA</text>

  <text x="680" y="202" font-size="13" font-weight="700" fill="#CBD5E1">Mathematical Formulation &amp; Input Telemetry:</text>
  <text x="680" y="224" font-size="12" fill="#94A3B8">• FC-37 Rain sensor state fused with high-rate rainfall forecasts (&gt;50mm/24h)</text>
  <text x="680" y="244" font-size="12" fill="#94A3B8">• Capacitive sensor voltage &lt; 1.30V (indicates complete soil saturation / pooling)</text>
  <text x="680" y="264" font-size="12" fill="#94A3B8">• Topographic parcel drainage factor from Digital Elevation Models (DEM)</text>

  <rect x="675" y="280" width="555" height="100" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="690" y="304" font-size="12" font-weight="700" fill="#38BDF8">Autonomous Edge Interventions &amp; Farmer Action:</text>
  <text x="690" y="324" font-size="12" fill="#E2E8F0">1. Instant Pump Hardware Lockout: Software and hardware inhibit relay closure.</text>
  <text x="690" y="344" font-size="12" fill="#E2E8F0">2. Trench Drainage Alert: Audio alarm and SMS to clear field discharge channels.</text>
  <text x="690" y="364" font-size="12" fill="#E2E8F0">3. Root Hypoxia Guard: Nitrogen top-dress postponement to prevent nitrate leaching.</text>

  <!-- 3. CANOPY HEATWAVE STRESS -->
  <rect x="30" y="415" width="595" height="260" rx="12" fill="#1E293B" stroke="#EF4444" stroke-width="2" filter="url(#shadowD3)"/>
  <rect x="30" y="415" width="595" height="42" rx="12" fill="#B91C1C" fill-opacity="0.25"/>
  <text x="55" y="442" font-size="16" font-weight="700" fill="#F87171">3. CANOPY HEATWAVE STRESS (0–100)</text>
  <rect x="490" y="422" width="120" height="26" rx="4" fill="#EF4444" fill-opacity="0.2"/>
  <text x="550" y="440" font-size="11" font-weight="700" fill="#F87171" text-anchor="middle">THERMAL ANOMALY</text>

  <text x="55" y="482" font-size="13" font-weight="700" fill="#CBD5E1">Mathematical Formulation &amp; Input Telemetry:</text>
  <text x="55" y="504" font-size="12" fill="#94A3B8">• DHT22 dry-bulb temperature sustained &gt; 38°C for &gt; 3 consecutive hours</text>
  <text x="55" y="524" font-size="12" fill="#94A3B8">• Atmospheric Vapor Pressure Deficit (VPD = es - ea &gt; 2.5 kPa)</text>
  <text x="55" y="544" font-size="12" fill="#94A3B8">• Crop phenology stage sensitivity (flowering / grain-filling critical threshold)</text>

  <rect x="50" y="560" width="555" height="100" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="65" y="584" font-size="12" font-weight="700" fill="#F87171">Autonomous Edge Interventions &amp; Farmer Action:</text>
  <text x="65" y="604" font-size="12" fill="#E2E8F0">1. Schedule Shifting: Inhibits midday watering; schedules irrigation at 04:00 AM.</text>
  <text x="65" y="624" font-size="12" fill="#E2E8F0">2. Canopy Cooling Pulse: Triggers short 3-minute overhead micro-sprinkler misting.</text>
  <text x="65" y="644" font-size="12" fill="#E2E8F0">3. Flower Abortion Warning: Warns tomato/cotton growers of pollen sterility risks.</text>

  <!-- 4. PATHOGEN & EPIDEMIC OUTBREAK -->
  <rect x="655" y="415" width="595" height="260" rx="12" fill="#1E293B" stroke="#A855F7" stroke-width="2" filter="url(#shadowD3)"/>
  <rect x="655" y="415" width="595" height="42" rx="12" fill="#7E22CE" fill-opacity="0.25"/>
  <text x="680" y="442" font-size="16" font-weight="700" fill="#C084FC">4. DISEASE OUTBREAK EPIDEMIC INDEX (0–100)</text>
  <rect x="1115" y="422" width="120" height="26" rx="4" fill="#A855F7" fill-opacity="0.2"/>
  <text x="1175" y="440" font-size="11" font-weight="700" fill="#C084FC" text-anchor="middle">EPIDEMIC TRIAGE</text>

  <text x="680" y="482" font-size="13" font-weight="700" fill="#CBD5E1">Mathematical Formulation &amp; Input Telemetry:</text>
  <text x="680" y="504" font-size="12" fill="#94A3B8">• Sustained Relative Humidity (RH &gt; 85%) for &gt; 12 hours (leaf-wetness proxy)</text>
  <text x="680" y="524" font-size="12" fill="#94A3B8">• Temperature trapezoid matching ICAR pathogen spore sporulation ranges</text>
  <text x="680" y="544" font-size="12" fill="#94A3B8">• Targets: Wheat Yellow Rust (10-18°C), Rice Blast (20-28°C), Late Blight (12-22°C)</text>

  <rect x="675" y="560" width="555" height="100" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="690" y="584" font-size="12" font-weight="700" fill="#C084FC">Autonomous Edge Interventions &amp; Farmer Action:</text>
  <text x="690" y="604" font-size="12" fill="#E2E8F0">1. Pre-Spore Spray Window: Identifies optimal 4-hour window before rain spreads spores.</text>
  <text x="690" y="624" font-size="12" fill="#E2E8F0">2. Prophylactic Biopesticide: Advises Trichoderma / Neem spray before visible lesions.</text>
  <text x="690" y="644" font-size="12" fill="#E2E8F0">3. KVK Escalation: Auto-packages temperature/RH history for district KVK scientist.</text>

  <!-- BOTTOM ESCALATION STRIP -->
  <rect x="30" y="695" width="1220" height="135" rx="12" fill="#0B1329" stroke="#334155" stroke-width="1.5"/>
  <text x="60" y="725" font-size="14" font-weight="700" fill="#F8FAFC">DISASTER ESCALATION ARCHITECTURE — GUARANTEED WARNING DELIVERY WITHOUT INTERNET</text>
  
  <rect x="50" y="740" width="370" height="75" rx="6" fill="#1E293B" stroke="#334155"/>
  <text x="65" y="762" font-size="12" font-weight="700" fill="#FBBF24">LEVEL 1: LOCAL FIELD ACTUATION</text>
  <text x="65" y="782" font-size="11" fill="#CBD5E1">Autonomous pump veto, LED warning strobe, buzzer.</text>
  <text x="65" y="798" font-size="11" fill="#34D399">Requires zero connectivity · Runs on internal battery.</text>

  <rect x="455" y="740" width="370" height="75" rx="6" fill="#1E293B" stroke="#334155"/>
  <text x="470" y="762" font-size="12" font-weight="700" fill="#38BDF8">LEVEL 2: FARMER TELEPHONY (SMS)</text>
  <text x="470" y="782" font-size="11" fill="#CBD5E1">SIM800L sends Devanagari Hindi SMS to registered phone.</text>
  <text x="470" y="798" font-size="11" fill="#38BDF8">Operates over 2G voice channel during 4G data blackouts.</text>

  <rect x="860" y="740" width="370" height="75" rx="6" fill="#1E293B" stroke="#334155"/>
  <text x="875" y="762" font-size="12" font-weight="700" fill="#C084FC">LEVEL 3: PANCHAYAT &amp; KVK DISPATCH</text>
  <text x="875" y="782" font-size="11" fill="#CBD5E1">LoRa 868MHz packet relays hazard code to Village Gateway.</text>
  <text x="875" y="798" font-size="11" fill="#C084FC">Escalates severe outbreaks to 18-Hub ICAR-KVK network.</text>
</svg>"""

# ==============================================================================
# D4: VALIDATION & CAPABILITY PANEL v2
# ==============================================================================
D4_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1350 900" width="100%" height="100%" style="background:#0F172A; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <linearGradient id="gradD4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <filter id="shadowD4" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Title Header Banner -->
  <rect x="30" y="25" width="1290" height="80" rx="12" fill="#1E293B" stroke="#334155" stroke-width="1.5" filter="url(#shadowD4)"/>
  <text x="60" y="60" font-size="22" font-weight="700" fill="#F8FAFC">D4: Empirical Validation, Benchmark Rigor &amp; Capability Boundary</text>
  <text x="60" y="85" font-size="13" fill="#94A3B8">Honest Verification Metrics · MobileNetV2 INT8 on Arm Cortex-A72 · XGBoost 5-Fold Cross-Validation · Zero Invented Scores</text>
  <rect x="1150" y="42" width="140" height="32" rx="6" fill="#10B981" fill-opacity="0.2" stroke="#10B981" stroke-width="1.5"/>
  <text x="1220" y="63" font-size="12" font-weight="700" fill="#34D399" text-anchor="middle">EVIDENCE PANEL</text>

  <!-- SECTION A: VISION CAPABILITY BOUNDARY (LEFT HALF) -->
  <rect x="30" y="125" width="630" height="420" rx="12" fill="#1E293B" stroke="#38BDF8" stroke-width="2" filter="url(#shadowD4)"/>
  <rect x="30" y="125" width="630" height="42" rx="12" fill="#0284C7" fill-opacity="0.25"/>
  <text x="50" y="152" font-size="15" font-weight="700" fill="#38BDF8">A. COMPUTER VISION: DECLARED CAPABILITY BOUNDARY</text>

  <!-- Capability Sub-Cards -->
  <!-- 7 CNN Classes -->
  <rect x="50" y="180" width="590" height="96" rx="8" fill="#0F172A" stroke="#10B981" stroke-width="1.5"/>
  <text x="65" y="204" font-size="13" font-weight="700" fill="#34D399">7 CLASSES CNN-DIAGNOSED (95.87% VALIDATION ACCURACY)</text>
  <text x="65" y="224" font-size="11" fill="#CBD5E1">Dataset: PlantVillage (spMohanty, CC-BY-SA) · 4,200 verified images (3,570 train / 630 val)</text>
  <text x="65" y="240" font-size="11" fill="#94A3B8">Trained: Apple Scab (0.98 F1), Grape Black Rot (0.99 F1), Healthy Leaf (0.97 F1),</text>
  <text x="65" y="256" font-size="11" fill="#94A3B8">Potato Early/Late Blight (0.96/0.94 F1), Tomato Early/Late Blight (0.93/0.92 F1).</text>
  <text x="65" y="270" font-size="11" fill="#38BDF8">Inference: 32.4 ms per frame on Raspberry Pi 4 Arm Cortex-A72 (INT8 ONNX).</text>

  <!-- 16 Untrained Classes -->
  <rect x="50" y="288" width="590" height="96" rx="8" fill="#0F172A" stroke="#F59E0B" stroke-width="1.5"/>
  <text x="65" y="312" font-size="13" font-weight="700" fill="#FBBF24">16 UNVERIFIED CROPS SERVED BY ICAR SYMPTOM GUIDELINES</text>
  <text x="65" y="332" font-size="11" fill="#CBD5E1">Crops: Wheat Rusts, Rice Blast/Blight, Cotton Blight, Chilli Anthracnose, Mustard Rust...</text>
  <text x="65" y="348" font-size="11" fill="#FBBF24">Boundary Principle: No verified public leaf dataset exists at Indian field quality.</text>
  <text x="65" y="364" font-size="11" fill="#CBD5E1">Returned with <tspan font-weight="700" fill="#F87171">confidence: null</tspan> and labelled as "ICAR Symptom Guidance" in the UI.</text>
  <text x="65" y="378" font-size="11" fill="#34D399"><tspan font-weight="700">"We do not claim neural coverage we cannot evidence."</tspan></text>

  <!-- 5 Major Insect Pests -->
  <rect x="50" y="396" width="590" height="88" rx="8" fill="#0F172A" stroke="#A855F7" stroke-width="1.5"/>
  <text x="65" y="420" font-size="13" font-weight="700" fill="#C084FC">5 MAJOR INDIAN PESTS VIA ICAR ECONOMIC THRESHOLDS (ETL)</text>
  <text x="65" y="440" font-size="11" fill="#CBD5E1">Pests: Fall Armyworm, Cotton Aphid, Whitefly Vector, Stem Borer, Cotton Bollworm.</text>
  <text x="65" y="456" font-size="11" fill="#94A3B8">Mechanism: Diagnostic symptom keyword matching + ICAR ETL threshold assessment.</text>
  <text x="65" y="472" font-size="11" fill="#A855F7">Delivers biological parasites (Trichogramma) + targeted chemical remedies.</text>

  <rect x="50" y="494" width="590" height="40" rx="6" fill="#0B1329" stroke="#334155"/>
  <text x="65" y="518" font-size="11" fill="#94A3B8">Honest Code: Hardcoded bounding boxes and +32.5 ms latency fudges deleted from edge repo.</text>

  <!-- SECTION B: ML STATISTICAL RIGOR (RIGHT HALF) -->
  <rect x="680" y="125" width="640" height="420" rx="12" fill="#1E293B" stroke="#10B981" stroke-width="2" filter="url(#shadowD4)"/>
  <rect x="680" y="125" width="640" height="42" rx="12" fill="#059669" fill-opacity="0.25"/>
  <text x="700" y="152" font-size="15" font-weight="700" fill="#34D399">B. AGRONOMIC ML: STATISTICAL EVALUATION (22 CROPS)</text>

  <!-- 5-Fold CV Table -->
  <rect x="700" y="180" width="600" height="150" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="715" y="204" font-size="13" font-weight="700" fill="#34D399">5-FOLD STRATIFIED CROSS-VALIDATION (2,200 BENCHMARK VECTORS)</text>
  
  <text x="715" y="230" font-size="12" fill="#CBD5E1">Fold 1: <tspan font-weight="700" fill="#38BDF8">99.09%</tspan>   │   Fold 2: <tspan font-weight="700" fill="#38BDF8">98.64%</tspan>   │   Fold 3: <tspan font-weight="700" fill="#38BDF8">98.41%</tspan></text>
  <text x="715" y="254" font-size="12" fill="#CBD5E1">Fold 4: <tspan font-weight="700" fill="#38BDF8">98.41%</tspan>   │   Fold 5: <tspan font-weight="700" fill="#38BDF8">98.64%</tspan></text>
  <line x1="715" y1="268" x2="1285" y2="268" stroke="#334155" stroke-width="1"/>
  <text x="715" y="290" font-size="13" font-weight="700" fill="#FBBF24">Mean CV Accuracy: 98.64% (± 0.25% variance) · Held-Out Test Set: 99.09%</text>
  <text x="715" y="312" font-size="11" fill="#94A3B8">Weighted Precision: 99.12% · Weighted Recall: 99.09% · Weighted F1-Score: 99.08%</text>

  <!-- Re-Ranking & Explainability -->
  <rect x="700" y="342" width="600" height="192" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="715" y="366" font-size="13" font-weight="700" fill="#38BDF8">BEYOND ACCURACY: EXPLAINABLE MULTI-PILLAR RE-RANKING</text>
  <text x="715" y="390" font-size="11" fill="#CBD5E1">• Raw XGBoost prediction is NOT treated as final; it is a strong agro-climatic prior.</text>
  <text x="715" y="410" font-size="11" fill="#CBD5E1">• Re-ranked against live SoilGrids NPK/pH, Open-Meteo 7-day weather, and APMC Mandi trends.</text>
  <text x="715" y="430" font-size="11" fill="#CBD5E1">• <tspan font-weight="700" fill="#34D399">SHAP TreeExplainer</tspan> computes exact log-odds attributions for all 7 input features.</text>
  <text x="715" y="450" font-size="11" fill="#CBD5E1">• Translated into spoken vernacular explanations in 11 Indian languages (Groq LLM engine).</text>
  <text x="715" y="470" font-size="11" fill="#CBD5E1">• Includes dynamic net profit margin (₹/acre) and 4-pillar quantitative sustainability score.</text>
  <text x="715" y="492" font-size="11" fill="#FBBF24">• Farmers receive actionable explanations they can verify with local KVK agronomists.</text>
  <text x="715" y="512" font-size="11" fill="#38BDF8">• 18-Hub ICAR-KVK directory embedded with one-tap scientist WhatsApp escalation.</text>

  <!-- SECTION C & D: LOWER HALF (DATA HONESTY & SILICON ROADMAP) -->
  <rect x="30" y="565" width="1290" height="305" rx="12" fill="#1E293B" stroke="#A855F7" stroke-width="2" filter="url(#shadowD4)"/>
  <rect x="30" y="565" width="1290" height="40" rx="12" fill="#7E22CE" fill-opacity="0.25"/>
  <text x="50" y="591" font-size="15" font-weight="700" fill="#C084FC">C. DATA HONESTY CONTRACT, SILICON BENCHMARK &amp; SCIENTIFIC CITATIONS</text>

  <!-- Column 1: Data Honesty Statement -->
  <rect x="50" y="618" width="410" height="235" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="68" y="642" font-size="13" font-weight="700" fill="#34D399">DATA HONESTY STATEMENT</text>
  <text x="68" y="666" font-size="12" fill="#CBD5E1" font-style="italic">"Every API response carries an explicit"</text>
  <text x="68" y="686" font-size="12" fill="#CBD5E1" font-style="italic"><tspan fill="#38BDF8">source</tspan> field. Where a live feed is</text>
  <text x="68" y="706" font-size="12" fill="#CBD5E1" font-style="italic">unavailable the system degrades to a</text>
  <text x="68" y="726" font-size="12" fill="#CBD5E1" font-style="italic">clearly-labelled cached or estimated</text>
  <text x="68" y="746" font-size="12" fill="#CBD5E1" font-style="italic">value. It never presents simulated data</text>
  <text x="68" y="766" font-size="12" fill="#CBD5E1" font-style="italic">as verified data. Confidence scores are</text>
  <text x="68" y="786" font-size="12" fill="#CBD5E1" font-style="italic">raw softmax outputs — never floored,</text>
  <text x="68" y="806" font-size="12" fill="#CBD5E1" font-style="italic">clamped, or invented."</text>
  <text x="68" y="834" font-size="11" font-weight="700" fill="#34D399">Verified by automated CI test suite (18/18 passing)</text>

  <!-- Column 2: Qualcomm Silicon Roadmap -->
  <rect x="480" y="618" width="410" height="235" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="498" y="642" font-size="13" font-weight="700" fill="#38BDF8">QUALCOMM SILICON &amp; NPU ROADMAP</text>
  <text x="498" y="668" font-size="12" fill="#CBD5E1">• <tspan font-weight="700" fill="#FBBF24">Measured Prototype Baseline:</tspan></text>
  <text x="498" y="688" font-size="12" fill="#94A3B8">  Raspberry Pi 4 Model B (Arm Cortex-A72 CPU)</text>
  <text x="498" y="706" font-size="12" fill="#94A3B8">  INT8 ONNX Runtime latency: <tspan font-weight="700" fill="#34D399">32.4 ms / frame</tspan></text>
  <text x="498" y="724" font-size="12" fill="#94A3B8">  Throughput: 30.8 FPS @ 160x160 RGB resolution</text>
  
  <text x="498" y="750" font-size="12" fill="#CBD5E1">• <tspan font-weight="700" fill="#38BDF8">Qualcomm Build-Phase Target:</tspan></text>
  <text x="498" y="770" font-size="12" fill="#94A3B8">  Porting the same validated ONNX graph to</text>
  <text x="498" y="788" font-size="12" fill="#94A3B8">  Qualcomm Dragonwing / QCS-class NPU via</text>
  <text x="498" y="806" font-size="12" fill="#94A3B8">  Qualcomm Neural Network (QNN) SDK / LiteRT.</text>
  <text x="498" y="830" font-size="11" font-style="italic" fill="#FBBF24">Honest roadmap beats unverified simulated claims.</text>

  <!-- Column 3: Peer-Reviewed Scientific Foundations -->
  <rect x="910" y="618" width="390" height="235" rx="8" fill="#0F172A" stroke="#334155"/>
  <text x="928" y="642" font-size="13" font-weight="700" fill="#C084FC">PEER-REVIEWED SCIENTIFIC FOUNDATIONS</text>
  <text x="928" y="666" font-size="11" fill="#CBD5E1"><tspan font-weight="700" fill="#38BDF8">FAO-56 Hargreaves (1998):</tspan> Crop Evapotranspiration</text>
  <text x="928" y="682" font-size="10" fill="#94A3B8">Allen et al. — Reduced-data irrigation scheduling</text>

  <text x="928" y="704" font-size="11" fill="#CBD5E1"><tspan font-weight="700" fill="#34D399">PlantVillage Dataset:</tspan> Hughes &amp; Salathé</text>
  <text x="928" y="720" font-size="10" fill="#94A3B8">4,200 verified images across 7 foliar classes</text>

  <text x="928" y="742" font-size="11" fill="#CBD5E1"><tspan font-weight="700" fill="#FBBF24">MobileNetV2 (CVPR 2018):</tspan> Sandler et al.</text>
  <text x="928" y="758" font-size="10" fill="#94A3B8">Inverted Residuals and Linear Bottlenecks</text>

  <text x="928" y="780" font-size="11" fill="#CBD5E1"><tspan font-weight="700" fill="#F87171">SHAP (NeurIPS 2017):</tspan> Lundberg &amp; Lee</text>
  <text x="928" y="796" font-size="10" fill="#94A3B8">Unified Approach to Interpreting Model Predictions</text>

  <text x="928" y="818" font-size="11" fill="#CBD5E1"><tspan font-weight="700" fill="#A855F7">ISRIC SoilGrids v2.0 &amp; Open-Meteo ECMWF</tspan></text>
  <text x="928" y="834" font-size="10" fill="#94A3B8">250m global soil property layers &amp; 7-day forecasts</text>
</svg>"""

if __name__ == "__main__":
    print("Generating official vector diagrams for Kisaan Sathi...")
    save_svg("D1_hardware_block_diagram_v2.svg", D1_SVG)
    save_svg("D2_edge_decision_loop_v2.svg", D2_SVG)
    save_svg("D3_disaster_resilience_engine_v2.svg", D3_SVG)
    save_svg("D4_validation_and_capability_panel_v2.svg", D4_SVG)
    print("\n[✓] All 4 vector diagrams successfully generated in all target directories!")
