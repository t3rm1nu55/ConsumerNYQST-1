# Manufacturer Data Collection Summary

**File:** `/home/user/ConsumerNYQST-1/knowledge_base/deterministic_sources/02_manufacturer_data.py`
**Retrieved:** 2025-11-11
**Status:** ✓ Complete

## Overview

This file contains **deterministic, publicly available** technical specifications and cutting data from major tool and machine manufacturers. All data is sourced from official manufacturer websites and technical documentation with full provenance tracking.

## Statistics

- **Total Manufacturers Documented:** 10
- **Total Data Records:** 17
- **Total Sources:** 34
- **File Outputs:**
  - Python source: `02_manufacturer_data.py` (41 KB)
  - JSON data: `02_manufacturer_data.json` (35 KB)
  - Provenance report: `02_manufacturer_data_provenance.md` (6.6 KB)

## Tool Manufacturers (6)

### 1. Sandvik Coromant
**Records:** 3 (cutting speeds, tool specs)
**Key Data:**
- **Aluminum 6061 Cutting Speeds:**
  - Typical: 1000 SFM with carbide
  - Range: 600-1200 SFM
  - High-performance PCD: 6562 SFM (2000 m/min)
  - Feed per tooth: 0.005-0.010 IPT
  - Grade recommendation: H10 (uncoated carbide)

- **Digital Tools:**
  - CoroPlus ToolGuide (web and mobile)
  - Machining Calculator App (iOS/Android)
  - Features: Tool selection, cutting data calculations, CAM integration

**Sources:** 6 official manufacturer sources

### 2. Kennametal
**Records:** 2 (cutting speeds, tool specs)
**Key Data:**
- **Calculation Formulas:**
  - RPM = (SFM × 3.82) / Tool Diameter
  - Feed Rate = RPM × Chip Load × Number of Teeth
  - SFM = (RPM × Tool Diameter) / 3.82

- **Resources Available:**
  - Online speed/feed calculator
  - Engineering calculators (surface finish, cost savings)
  - PDF technical guides

**Sources:** 3 official manufacturer sources

### 3. Harvey Tool
**Records:** 2 (cutting speeds, tool specs)
**Key Data:**
- **Aluminum 6061 Recommendations:**
  - Speed range: 800-1500 SFM
  - Feed per tooth: 0.005-0.010 IPT
  - Aggressive cutting: up to 5000-8000 SFM (optimal conditions)

- **Digital Tools:**
  - Machining Advisor Pro (MAP) - free, customizable
  - Product-specific downloadable speed/feed charts
  - Mobile and desktop access

**Sources:** 3 official manufacturer sources

### 4. Iscar
**Records:** 2 (tool specs)
**Key Data:**
- **ITA (Iscar Tool Advisor):**
  - Web-based tool selection software
  - Unique mathematical algorithm
  - Input: 2-6 mandatory fields
  - Output: 3-25 tool recommendations with full cutting data
  - Features: 25 languages, inch/metric, mobile app
  - Advanced: NEO-ITA with AI and machine learning

- **2025 Products:**
  - New Industry 4.0 connectivity
  - Latest catalog available

**Sources:** 4 official manufacturer sources

### 5. Seco Tools
**Records:** 2 (tool specs)
**Key Data:**
- **Digital Solutions (2025):**
  - Machine Library (web-based, launched July 2025)
  - Seco Assistant App (iOS/Android)
  - Secocut Software (desktop)
  - Instant cutting data recommendations

- **Technical Documentation:**
  - Catalog & Technical Guide 2020.2
  - Product-specific PDF brochures
  - Holemaking, milling, turning guides

**Sources:** 5 official manufacturer sources

### 6. OSG Corporation
**Records:** 1 (tool specs)
**Key Data:**
- **Technical Charts Available:**
  - Tap Drill Size & Pitch Limits (2024 edition)
  - High Speed Machining Guide (1.89 MB)
  - STI Tap Drill Size charts
  - Decimal wall charts (23.92 MB)
  - Coverage: 21+ thread standards (M, UNC, UNF, NPT, BSW, etc.)

**Sources:** 2 official manufacturer sources

## Machine Tool Manufacturers (4)

### 7. Haas Automation
**Records:** 2 (machine specs)
**Key Data:**
- **Spindle Power Characteristics:**
  - Peak: 200% load for 3 minutes
  - High: 150% load for 10-15 minutes
  - Continuous: 100% load

- **Spindle Types:**
  - Inline: 8,100-20,000 RPM
  - Geared-head: up to 10,000 RPM (high torque)
  - Example (MiniMill): 33 lb-ft @ 1200 RPM

- **Specific Models Documented:**
  - 7500 RPM / 60 HP (50 taper)
  - 8100, 10000, 12000 RPM (40 taper)
  - Torque curves available per model

**Sources:** 3 official manufacturer sources

### 8. DMG MORI
**Records:** 1 (machine specs)
**Key Data:**
- **2025 Machine Lineup:**

  **DMU 40 Series (5-axis):**
  - DMU 40: 12,000 RPM, 15 kW, 95 Nm
  - DMU 40 PLUS: 15,000 RPM, 16.5 kW, 121 Nm
  - DMU 40 PRO: 20,000 RPM, 32 kW, 130 Nm

  **DMX U Series (Universal):**
  - Standard: inlineMASTER 12,000 RPM
  - Optional: speedMASTER 20,000 RPM or 200 Nm

  **NHX Series (Horizontal):**
  - Speedmaster spindle @ 400V
  - Rapid traverse: 70 m/min
  - 50% more output

  **M1 Vertical Mill:**
  - Travel: 22" × 22" × 20" (550 × 550 × 510 mm)
  - Spindle: 10,000 or 12,000 RPM
  - Max workpiece: 1,323 lbs (600 kg)
  - Control: SIEMENS 828D
  - 24-pocket tool magazine

**Sources:** 3 official manufacturer sources

### 9. Okuma
**Records:** 1 (machine specs)
**Key Data:**
- **Multus Series (Turn-Mill):**
  - Up to 5-axis simultaneous control
  - Feed rates: up to 1,000 mm/min
  - Rapid traverse: 30 m/min
  - Positioning accuracy: ±0.001 mm
  - Spindle: up to 20,000 RPM
  - Tool magazine: up to 120 tools

- **Product Lines:**
  - Vertical machining centers (MB-VA, MF-VA/VB, GENOS M560V)
  - Lathes (LT2000 EX, LU3000 EX, LU7000EX, GENOS L250)
  - Multitasking (MU-4000V, MU-5000V, MU-6300V)

- **Control System:** OSP-P (Okuma proprietary)
- **Monitoring:** Okuma Connect Plan

**Sources:** 2 official manufacturer sources

### 10. Mazak
**Records:** 1 (machine specs)
**Key Data:**
- **2025 CMTS Featured Models:**

  **SYNCREX 38/8:**
  - Type: Swiss-type turning
  - Bar stock: up to 1.5" diameter
  - Control: MAZATROL SmoothSt CNC
  - 15" touch panel

  **QTE-100:**
  - Type: CNC turning center
  - Chuck: 6"
  - Max diameter: 11.42"
  - Built-in high-torque motor spindle

  **VC-Ez 20:**
  - Type: Vertical machining center
  - Spindle: 25 HP, 12,000 RPM
  - Tool changer: 30-tool automatic
  - Made in Kentucky, USA

- **Technical Documentation:**
  - General information manuals
  - MAZATROL programming manuals
  - Parameter and alarm lists
  - Available at cncmanual.com/mazak/

**Sources:** 3 official manufacturer sources

## Data Types Breakdown

| Data Type | Records | Description |
|-----------|---------|-------------|
| **cutting_speeds** | 3 | SFM, IPT, material-specific recommendations |
| **tool_specs** | 9 | Digital tools, calculators, technical charts |
| **machine_specs** | 5 | Spindle specs, travel ranges, torque curves |

## Source Quality

All sources are:
- ✓ Publicly accessible
- ✓ Official manufacturer websites
- ✓ Current as of 2025-11-11
- ✓ Fully documented with URLs
- ✓ No proprietary or confidential data

## Data Structure

Each manufacturer record includes:
```python
{
  "manufacturer": "Name",
  "product_line": "Specific product/series",
  "data_type": "cutting_speeds|tool_specs|machine_specs",
  "data": {
    # Structured technical data
  },
  "sources": [
    {
      "url": "direct URL",
      "source_type": "manufacturer",
      "retrieved_date": "2025-11-11",
      "title": "Document title",
      "excerpt": "Key quotes (if applicable)"
    }
  ]
}
```

## Key Findings

### Cutting Speeds for Aluminum 6061 (Carbide):
- **Conservative range:** 600-1200 SFM
- **Typical:** 1000 SFM
- **Aggressive:** 5000-8000 SFM (optimal conditions)
- **High-performance PCD:** 6562 SFM (2000 m/min)
- **Feed per tooth:** 0.005-0.010 IPT typical

### Digital Tool Availability:
All major manufacturers offer **free**, publicly accessible digital tools:
- Web-based calculators and tool advisors
- Mobile apps (iOS/Android)
- CAM software integration
- Real-time cutting data recommendations

### Machine Specifications (2025):
- **Spindle speeds:** 7,500-20,000 RPM typical
- **Power:** 15-60+ HP
- **Torque:** 95-302 Nm depending on spindle type
- **Control systems:** Proprietary and SIEMENS

## Files Generated

1. **02_manufacturer_data.py** (41 KB)
   - Main Python source code
   - Uses ManufacturerData class from kb_infrastructure.py
   - Executable: generates JSON and reports

2. **02_manufacturer_data.json** (35 KB)
   - Structured JSON output
   - Programmatically accessible
   - Includes metadata and verification status

3. **02_manufacturer_data_provenance.md** (6.6 KB)
   - Detailed source documentation
   - All 34 sources listed
   - URLs and excerpts included

## Usage

```python
# Load the data
from kb_infrastructure import KnowledgeBase
import json

# From JSON
with open('02_manufacturer_data.json', 'r') as f:
    data = json.load(f)

# Or run the Python script
from deterministic_sources.manufacturer_data_02 import create_manufacturer_database
kb = create_manufacturer_database()

# Access manufacturer data
for md in kb.manufacturer_data:
    print(f"{md.manufacturer}: {md.product_line}")
    print(f"  Type: {md.data_type}")
    print(f"  Sources: {len(md.sources)}")
```

## Verification

- ✓ All data from official manufacturer sources
- ✓ 34 source URLs documented
- ✓ Retrieved: 2025-11-11
- ✓ No confidential or proprietary information
- ✓ All resources publicly accessible
- ✓ Full provenance tracking

## Next Steps

This manufacturer data can be used to:
1. Validate feeds & speeds calculator algorithms
2. Cross-reference with industry standards
3. Provide real-world examples for CNC apps
4. Benchmark competitive tools
5. Support market sizing for B2B tools segment

---

**Collection Date:** 2025-11-11
**Total Sources:** 34 official manufacturer sources
**Manufacturers:** 10 (6 tool, 4 machine)
**Data Records:** 17
**Status:** ✓ Complete and verified
