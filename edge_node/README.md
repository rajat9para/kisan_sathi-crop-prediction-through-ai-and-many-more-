# Kisan Sathi 2.0 — Edge Node Hardware Specification & Wiring Guide

**Targeting Qualcomm Problem Statement #26180 (Agriculture, FoodTech & Rural Development)**

---

## 1. Hardware Architecture (Dual-Track)

Kisan Sathi 2.0 supports a dual-track deployment strategy:
- **Track A (Field-Deployable Build - Implemented & Tested)**: Built with off-the-shelf components designed for rugged field deployment and local maintainability.
- **Track B (High-Throughput Edge AI Reference Platform)**: Qualcomm Dragonwing RB3 Gen 2 Development Kit with Qualcomm QCS6490 Octa-Core SoC and Hexagon NPU (12 TOPS).

---

## 2. Track A Bill of Materials (BOM) & Specifications

| Component | Specification / Part | Interface | Functional Responsibility |
| :--- | :--- | :--- | :--- |
| **Compute SBC** | Raspberry Pi 4 Model B (4GB / 8GB) | 40-Pin GPIO, CSI, USB | Edge inference, decision state machine, local API |
| **Camera Module** | Raspberry Pi Camera V2 (8MP Sony IMX219) | 2-Lane MIPI CSI-2 | Optical capture of leaf pathology & insect pests |
| **Soil Moisture** | Capacitive Soil Moisture Sensor v1.2 | Analog (1.2V–3.0V) | Corrosion-resistant volumetric soil water fraction |
| **ADC Converter** | ADS1115 16-Bit 4-Channel I2C ADC | I2C (Address `0x48`) | High-resolution digitization of analog moisture signal |
| **Air Temp / Humidity** | DHT22 / AM2302 Sensor | Single-bus digital (1-Wire)| Ambient dry-bulb $T$ and $RH$ for $ET_0$ water budgeting |
| **Rain Inhibitor** | FC-37 / YL-83 Raindrop Sensor Module | Digital Comparator (LM393) | Hardware pump inhibition during rainfall events |
| **Relay Actuator** | 5V 1-Channel Relay Module (Optocoupler) | Active-LOW GPIO input | Galvanically isolated switching of 12V DC water pump |
| **Pump Actuator** | 12V R385 Mini Diaphragm DC Water Pump | Switched 12V DC leads | Pressurizes demonstration drip irrigation distribution |
| **Offline GSM/SMS** | SIM800L GPRS / GSM Module | UART0 @ 9600 baud, 8N1 | Regional language SMS dispatch without 4G/Wi-Fi |
| **Long-Range RF** | Reyax RYLR896 LoRa SX1278 (868 MHz) | SPI0 Bus (`/dev/spidev0.0`)| Sub-GHz mesh telemetry packets across farm plots |
| **Power Regulation**| Dual-Rail LM2596 Buck Step-Down | DC Rails | Dual 5V 3A and 4.2V 2A rails from 12V 2A supply |

---

## 3. Raspberry Pi 4 GPIO Pinout Table

```
      3.3V Power [01] [02] 5.0V Power (Relay VCC, LM2596)
   I2C1 SDA (03) [03] [04] 5.0V Power
   I2C1 SCL (05) [05] [06] Ground (GND)
   GPIO 4 (DHT22)[07] [08] UART TX (GPIO 14 -> SIM800L RX)
          Ground [09] [10] UART RX (GPIO 15 <- SIM800L TX)
         GPIO 17 [11] [12] GPIO 18 (Status LED)
         GPIO 27 [13] [14] Ground
         GPIO 22 [15] [16] GPIO 23 (5V Relay Pump Control)
       3.3V Pwr  [17] [18] GPIO 24 (FC-37 Rain Detector)
 SPI0 MOSI (10)  [19] [20] Ground
 SPI0 MISO (09)  [21] [22] GPIO 25 (LoRa Reset)
  SPI0 SCLK (11) [23] [24] SPI0 CE0 (LoRa NSS)
          Ground [25] [26] SPI0 CE1
```

---

## 4. Actuation Safety Protocol

1. **Hardware Inversion Protection**: Relay control pin uses active-LOW logic with optocoupler isolation to prevent transient relay firing during bootloader startup.
2. **15-Minute Hardware Watchdog**: The `SmartIrrigationController` enforces an autonomous hard cutoff at 15 minutes continuous runtime to prevent field waterlogging, root asphyxiation, or motor burnout.
3. **Rain Invalidation Guard**: Digital rain sensor overrides irrigation schedule even if soil moisture is below the 22% threshold.
4. **Offline Resilience**:
   - If Wi-Fi/Internet drops: The edge daemon continues operating autonomously, switching to SIM800L GSM SMS for alerting.
   - If sensors disconnect: System falls back to Hargreaves climatological averages.

---

## 5. How to Run

### Standalone Edge Daemon
```bash
cd edge_node
python edge_daemon.py --crop tomato --interval 3 --phone +919876543210
```

### Run Single Evaluation Test
```bash
python edge_daemon.py --crop tomato --once
```
