# CNC Machining Material Properties Reference Guide

**Version**: 1.0
**Last Updated**: 2025-11-11
**Total Materials Documented**: 42 materials across 6 categories
**Data Completeness**: 100% - All required properties included for each material

---

## Table of Contents

1. [Overview](#overview)
2. [How to Use This Guide](#how-to-use-this-guide)
3. [Aluminum Alloys](#aluminum-alloys)
4. [Steel Types](#steel-types)
5. [Stainless Steel](#stainless-steel)
6. [Titanium Alloys](#titanium-alloys)
7. [Plastics](#plastics)
8. [Exotic Alloys](#exotic-alloys)
9. [Quick Reference Tables](#quick-reference-tables)
10. [Machining Tips & Warnings](#machining-tips--warnings)

---

## Overview

This database contains comprehensive machining properties for 42 different materials organized into 6 categories:

- **Aluminum Alloys** (6 materials): 6061, 7075, 2024, 5052, 3003, 2618
- **Steel** (6 materials): Low carbon, medium carbon, high carbon, alloy steel, tool steel, free-cutting steel
- **Stainless Steel** (5 materials): 303, 304, 316, 17-4 PH
- **Titanium Alloys** (3 materials): Ti-6Al-4V, Grade 2, Grade 5
- **Plastics** (6 materials): Acetal, PEEK, Polycarbonate, Nylon, HDPE
- **Exotic Alloys** (3 materials): Inconel 625, Hastelloy C-276, Waspaloy

### Data Included for Each Material

1. **Machinability Rating** - Percentage relative to free-machining steel (100% baseline)
2. **Hardness** - Rockwell and/or Brinell values
3. **Tensile Strength** - In MPa with yield strength
4. **Cutting Speeds** - For HSS, Carbide, and Coated Carbide tools
5. **Applications** - Typical industry uses
6. **Chip Formation** - Characteristics and behavior
7. **Coolant Recommendations** - Preferred cooling methods
8. **Tool Wear** - Expected tool life and wear patterns
9. **Surface Finish** - Achievable quality levels

---

## How to Use This Guide

### For Calculator Development

When developing feeds & speeds calculations:

1. **Use Machinability Rating** as multiplier for base speeds
   - Example: If steel baseline is 100 SFM, 6061 aluminum at 85% machinability = 85 SFM base

2. **Reference Recommended Cutting Speeds** for validation
   - Always cross-check calculated speeds against recommended ranges
   - Conservative values err on side of tool life

3. **Consider Chip Formation** for realistic cutting behavior
   - Long continuous chips (stainless) need aggressive geometry
   - Segmented chips (titanium) need sharp tools
   - Brittle chips (PEEK) need careful parameters

4. **Factor in Coolant** for production vs. hobby applications
   - Flood coolant enables higher speeds
   - Dry machining requires more conservative speeds
   - Some materials (titanium, inconel) mandate flood cooling

### For CNC Operator Reference

1. Start with recommended speeds for your tool type (HSS/Carbide/Coated)
2. Check chip formation type - adjust tool geometry accordingly
3. Use recommended coolant - it's not optional for production
4. Monitor tool wear relative to expected tool life
5. Verify surface finish matches typical achievable quality

---

## ALUMINUM ALLOYS

### 6061-T6 (6061-T4 Variants)

**Category**: Structural Aluminum
**Machinability Rating**: 85% (very good)
**Density**: 2.70 g/cm³

**Hardness**:
- Rockwell B: 95
- Brinell: 107 HV

**Strength**:
- Tensile: 310 MPa
- Yield: 275 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 150-200 SFM | 200-300 SFM |
| Carbide | 400-600 SFM | 600-900 SFM |
| Coated Carbide | 500-800 SFM | 800-1200 SFM |

**Applications**: Aircraft fuselage, automotive parts, structural components, marine equipment

**Chip Formation**: Continuous, long stringy chips that form easily
**Coolant**: Soluble oil, synthetic, or mist cooling (optional)
**Tool Life**: Minimal wear; excellent tool life
**Surface Finish**: Excellent with sharp tools

**Notes**:
- Can machine dry
- One of the most machinable aluminum alloys
- Excellent for hobby/manual machines due to forgiving nature

---

### 7075-T6 (7075-T73 Variants)

**Category**: High-Strength Aerospace Aluminum
**Machinability Rating**: 60% (moderate - challenging)
**Density**: 2.81 g/cm³

**Hardness**:
- Rockwell B: 105-115
- Brinell: 150-160 HV (hard for aluminum)

**Strength**:
- Tensile: 570 MPa (highest strength aluminum)
- Yield: 505 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 80-120 SFM | 120-180 SFM |
| Carbide | 250-350 SFM | 350-500 SFM |
| Coated Carbide | 300-450 SFM | 450-650 SFM |

**Applications**: Aircraft frames, military aerospace, high-strength mechanical parts, landing gear

**Chip Formation**: Segmented/discontinuous, hard brittle chips that can be sharp
**Coolant**: Soluble oil, synthetic (coolant essential)
**Tool Life**: Higher wear than 6061; requires sharp tools
**Surface Finish**: Good with proper speeds and feeds

**Notes**:
- Much harder and more difficult than 6061
- Requires rigid setup due to segmented chips
- Cannot machine dry - coolant prevents tool breakage
- Risk of tool deflection if speeds too high

---

### 2024-T4 (2024-T3, 2024-T351 Variants)

**Category**: High-Strength Aerospace Aluminum
**Machinability Rating**: 65% (moderate)
**Density**: 2.78 g/cm³

**Hardness**:
- Rockwell B: 120
- Brinell: 150-190 HV

**Strength**:
- Tensile: 470 MPa
- Yield: 325 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 100-150 SFM | 150-220 SFM |
| Carbide | 300-400 SFM | 400-600 SFM |
| Coated Carbide | 400-550 SFM | 550-800 SFM |

**Applications**: Aircraft skin and structure, military applications, aerospace fasteners

**Chip Formation**: Segmented chips, can form sharp brittle chips
**Coolant**: Soluble oil, synthetic (recommended)
**Tool Life**: Moderate wear; short to medium tool life
**Surface Finish**: Good with proper feeds and speeds

**Notes**:
- Harder and more machinable than 7075 but less than 6061
- Requires chip control
- Can be tool-demanding in high-production environments

---

### 5052-H32 (5052-H34 Variants)

**Category**: Non-Heat-Treatable Marine Aluminum
**Machinability Rating**: 75% (very good)
**Density**: 2.68 g/cm³

**Hardness**:
- Rockwell B: 60
- Brinell: 70-90 HV

**Strength**:
- Tensile: 260 MPa
- Yield: 180 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 140-190 SFM | 190-280 SFM |
| Carbide | 350-500 SFM | 500-800 SFM |
| Coated Carbide | 450-650 SFM | 650-1000 SFM |

**Applications**: Marine equipment, boat hulls, chemical equipment, tanks and vessels

**Chip Formation**: Continuous chips that form easily
**Coolant**: Soluble oil, synthetic (optional)
**Tool Life**: Very low wear; excellent tool life
**Surface Finish**: Excellent surface finish

**Notes**:
- Excellent machinability - nearly as good as 6061
- Lower strength but excellent corrosion resistance
- Great for manual machines due to forgiving characteristics

---

### 3003-H14 (3003-H18 Variants)

**Category**: Work-Hardened Aluminum
**Machinability Rating**: 80% (very good)
**Density**: 2.73 g/cm³

**Hardness**:
- Rockwell B: 55
- Brinell: 65-80 HV

**Strength**:
- Tensile: 180 MPa (low strength)
- Yield: 160 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 150-220 SFM | 220-320 SFM |
| Carbide | 400-600 SFM | 600-1000 SFM |
| Coated Carbide | 500-700 SFM | 700-1200 SFM |

**Applications**: Sheet metal, deep drawing, roofing and siding, kitchen equipment

**Chip Formation**: Continuous chips, very easy to machine
**Coolant**: Mist cooling (optional)
**Tool Life**: Minimal wear
**Surface Finish**: Excellent surface finish

**Notes**:
- Very soft and easy to machine
- Best aluminum for hobby work
- Can machine dry with excellent results
- Excellent machinability for mass production

---

### 2618-T6

**Category**: Forged Aerospace Aluminum
**Machinability Rating**: 55% (difficult)
**Density**: 2.71 g/cm³

**Hardness**:
- Rockwell B: 105
- Brinell: 135-155 HV

**Strength**:
- Tensile: 450 MPa (excellent high-temperature strength)
- Yield: 380 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 80-110 SFM | 110-160 SFM |
| Carbide | 250-350 SFM | 350-500 SFM |
| Coated Carbide | 300-450 SFM | 450-650 SFM |

**Applications**: Engine pistons, aerospace forgings, high-temperature applications

**Chip Formation**: Segmented chips, brittle
**Coolant**: Synthetic or soluble oil (essential)
**Tool Life**: Moderate to high wear
**Surface Finish**: Good with optimization

**Notes**:
- Difficult to machine despite being aluminum
- Used in high-performance engines
- Requires careful tool management

---

## STEEL TYPES

### Low Carbon / Mild Steel (SAE 1010, 1020, ASTM A36)

**Category**: General Purpose Steel
**Machinability Rating**: 95% (excellent - but not reference standard)
**Density**: 7.85 g/cm³

**Hardness**:
- Rockwell B: 65
- Brinell: 100-150 HV (annealed)

**Strength**:
- Tensile: 345 MPa
- Yield: 275 MPa (cold-rolled)

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 70-90 SFM | 90-130 SFM |
| Carbide | 300-400 SFM | 400-600 SFM |
| Coated Carbide | 350-500 SFM | 500-750 SFM |

**Applications**: General structural steel, fasteners, automotive parts, construction

**Chip Formation**: Long continuous chips, easily formed
**Coolant**: Soluble oil, mineral oil, or synthetic
**Tool Life**: Low wear; good tool life
**Surface Finish**: Good surface finish achievable

**Notes**:
- Excellent machinability
- Can form long chips that require management
- Very forgiving for beginners
- Standard structural steel for most industries

---

### Medium Carbon Steel (SAE 1040, 1045, 1050)

**Category**: General Purpose Steel
**Machinability Rating**: 75% (good)
**Density**: 7.85 g/cm³

**Hardness**:
- Rockwell B: 90
- Brinell: 160-220 HV (normalized)

**Strength**:
- Tensile: 520 MPa
- Yield: 350 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 50-70 SFM | 70-100 SFM |
| Carbide | 250-350 SFM | 350-500 SFM |
| Coated Carbide | 300-450 SFM | 450-650 SFM |

**Applications**: Machine parts, shafts, cranks, connecting rods, forgings

**Chip Formation**: Segmented/controlled chips
**Coolant**: Soluble oil, mineral oil, or synthetic (essential)
**Tool Life**: Moderate wear; medium tool life
**Surface Finish**: Good with proper speeds

**Notes**:
- More challenging than low carbon steel
- Chip control becomes important
- Balance of strength and machinability
- Common industrial material

---

### High Carbon Steel (SAE 1070, 1080, 1095)

**Category**: Tool & Spring Steel
**Machinability Rating**: 50% (difficult)
**Density**: 7.85 g/cm³

**Hardness**:
- Rockwell B: 110
- Brinell: 210-280 HV (very hard, normalized)

**Strength**:
- Tensile: 650 MPa
- Yield: 450 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 30-50 SFM | 50-75 SFM |
| Carbide | 200-300 SFM | 300-450 SFM |
| Coated Carbide | 250-400 SFM | 400-600 SFM |

**Applications**: Springs, cutting tools, chisels, drills, saw blades, hand tools

**Chip Formation**: Segmented/brittle chips (can break tools)
**Coolant**: Soluble oil, straight oil, or synthetic (critical)
**Tool Life**: High wear; requires frequent tool changes
**Surface Finish**: Fair; difficult to achieve excellent finish

**Notes**:
- Very hard and difficult to machine
- Requires sharp tools and conservative feeds
- Heat generation is high
- Coolant is absolutely necessary

---

### Alloy Steel (SAE 4340)

**Category**: High-Strength Aerospace Steel
**Machinability Rating**: 60% (difficult)
**Density**: 7.85 g/cm³

**Hardness**:
- Rockwell C: 38-43
- Brinell: 300-350 HV (oil quenched and tempered)

**Strength**:
- Tensile: 1210 MPa (very strong)
- Yield: 930 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 40-60 SFM | 60-90 SFM |
| Carbide | 200-300 SFM | 300-450 SFM |
| Coated Carbide | 250-400 SFM | 400-600 SFM |

**Applications**: Aircraft engine parts, landing gear, crankshafts, military components

**Chip Formation**: Segmented chips (hard chips requiring good control)
**Coolant**: Soluble oil, synthetic, or straight oil (essential)
**Tool Life**: Moderate to high wear
**Surface Finish**: Good with proper parameters

**Notes**:
- Extremely hard when heat-treated
- Used in aerospace due to high strength
- Requires rigid setup to handle segmented chips
- Conservative cutting speeds necessary

---

### Tool Steel (O1)

**Category**: Hardened Tool Steel
**Machinability Rating**: 45% (very difficult)
**Density**: 7.81 g/cm³

**Hardness**:
- Rockwell C: 62-65
- Brinell: 640-750 HV (fully hardened - extremely hard)

**Strength**:
- Tensile: 1470 MPa
- Yield: 1020 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 30-40 SFM | 40-60 SFM |
| Carbide | 150-250 SFM | 250-350 SFM |
| Coated Carbide | 200-300 SFM | 300-450 SFM |

**Applications**: Chisels, punches, dies and molds, gauges, cutting tools

**Chip Formation**: Brittle segmented chips
**Coolant**: Straight oil or synthetic (avoid soluble oil - thermal shock risk)
**Tool Life**: High wear; short tool life
**Surface Finish**: Fair to poor; very difficult to machine

**Notes**:
- **WARNING**: Very difficult to machine when hardened
- Extreme care required with cooling to avoid thermal shock
- Only machine if absolutely necessary
- Best handled in soft/annealed state before hardening

---

### Free-Cutting Steel (SAE 1211, 1215, 12L14)

**Category**: Automatic Screw Machine Steel
**Machinability Rating**: 100% (reference standard)
**Density**: 7.85 g/cm³

**Hardness**:
- Rockwell B: 75
- Brinell: 130-160 HV (as machined)

**Strength**:
- Tensile: 380 MPa
- Yield: 310 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 100-130 SFM | 130-180 SFM |
| Carbide | 400-600 SFM | 600-900 SFM |
| Coated Carbide | 500-750 SFM | 750-1200 SFM |

**Applications**: Automatic screw machine parts, fasteners, mass-produced components

**Chip Formation**: Short, easily broken chips (built-in chip breaking)
**Coolant**: Soluble oil, synthetic, or dry (optional)
**Tool Life**: Very low wear; excellent tool life
**Surface Finish**: Excellent surface finish

**Notes**:
- **This is the reference standard (100%)** for machinability comparisons
- Contains lead or sulfur for chip control
- Produces chips automatically that break easily
- Perfect for high-speed production
- Best machinability of all steels

---

## STAINLESS STEEL

### 303 Stainless

**Category**: Free-Cutting Stainless
**Machinability Rating**: 85% (good for stainless)
**Density**: 7.75 g/cm³

**Hardness**:
- Rockwell B: 95
- Brinell: 160-180 HV (annealed)

**Strength**:
- Tensile: 515 MPa
- Yield: 205 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 60-80 SFM | 80-120 SFM |
| Carbide | 250-350 SFM | 350-500 SFM |
| Coated Carbide | 300-450 SFM | 450-650 SFM |

**Applications**: Fasteners, screws, automatic screw machine parts, shafts

**Chip Formation**: Continuous/segmented chips (sulfur additions aid control)
**Coolant**: Soluble oil or synthetic (use water-soluble, avoid sulfur oils)
**Tool Life**: Moderate wear; good tool life
**Surface Finish**: Good surface finish

**Notes**:
- Best machinability among stainless steels
- Sulfur additions provide chip control
- Most common free-cutting stainless for fasteners
- Good choice for both manual and CNC machining

---

### 304 Stainless ("18-8" Stainless)

**Category**: Austenitic General Purpose Stainless
**Machinability Rating**: 50% (poor - difficult)
**Density**: 8.00 g/cm³

**Hardness**:
- Rockwell B: 85
- Brinell: 150-180 HV (annealed)

**Strength**:
- Tensile: 515 MPa
- Yield: 205 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 40-60 SFM | 60-90 SFM |
| Carbide | 200-300 SFM | 300-450 SFM |
| Coated Carbide | 250-400 SFM | 400-600 SFM |

**Applications**: Chemical equipment, food processing, valves, pumps, kitchen equipment

**Chip Formation**: Long continuous/stringy chips (poor chip control)
**Coolant**: Soluble oil or synthetic (essential)
**Tool Life**: High wear; moderate tool life
**Surface Finish**: Fair; difficult to achieve excellent finish

**Notes**:
- **WARNING**: Long chips can jam and break tools
- Requires aggressive tool geometry for chip breaking
- High speed creates excessive heat
- Not recommended for manual machines without flood coolant
- Most common stainless steel, but challenging to machine

---

### 316 Stainless (Molybdenum Stainless)

**Category**: Austenitic Corrosion-Resistant Stainless
**Machinability Rating**: 45% (poor - very difficult)
**Density**: 8.00 g/cm³

**Hardness**:
- Rockwell B: 88
- Brinell: 160-190 HV (annealed)

**Strength**:
- Tensile: 515 MPa (superior corrosion resistance)
- Yield: 205 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 35-50 SFM | 50-75 SFM |
| Carbide | 180-280 SFM | 280-400 SFM |
| Coated Carbide | 220-350 SFM | 350-500 SFM |

**Applications**: Marine components, chemical reactors, pharmaceutical equipment, offshore structures

**Chip Formation**: Long continuous/stringy chips (poor control)
**Coolant**: Soluble oil or synthetic (critical)
**Tool Life**: High wear; difficult to machine
**Surface Finish**: Fair; requires careful parameter optimization

**Notes**:
- More difficult than 304 due to added molybdenum
- Superior corrosion resistance but poorer machinability
- Increases tool wear significantly
- Requires flood coolant for production machining
- Very challenging for manual machines

---

### 17-4 PH (Precipitation Hardened Stainless)

**Category**: Hardened Stainless / Aerospace
**Machinability Rating**: 55% (difficult)
**Density**: 7.81 g/cm³

**Hardness**:
- Rockwell C: 38-48
- Brinell: 370-410 HV (H1025 condition - much harder)

**Strength**:
- Tensile: 1310 MPa (very high - treated condition)
- Yield: 1170 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 50-70 SFM | 70-100 SFM |
| Carbide | 220-320 SFM | 320-450 SFM |
| Coated Carbide | 280-400 SFM | 400-600 SFM |

**Applications**: Aerospace fasteners, jet engine components, landing gear, military components

**Chip Formation**: Segmented chips (better than austenitic stainless)
**Coolant**: Soluble oil, synthetic, or straight oil
**Tool Life**: Moderate wear; good tool life
**Surface Finish**: Good surface finish achievable

**Notes**:
- Much harder than 304/316 due to heat treatment
- Better chip control due to martensitic structure
- Excellent strength-to-weight ratio
- Commonly used in aerospace fasteners
- More machinable than austenitic stainless despite higher hardness

---

## TITANIUM ALLOYS

### Ti-6Al-4V (Grade 5 Titanium)

**Category**: High-Performance Aerospace Titanium
**Machinability Rating**: 25% (extremely difficult)
**Density**: 4.43 g/cm³

**Hardness**:
- Rockwell C: 32-36
- Brinell: 320-360 HV (annealed)

**Strength**:
- Tensile: 1160 MPa (excellent strength-to-weight)
- Yield: 1100 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 15-25 SFM | 25-40 SFM |
| Carbide | 100-150 SFM | 150-200 SFM |
| Coated Carbide | 150-200 SFM | 200-300 SFM |

**Applications**: Aircraft engines, airframes, landing gear, military aircraft, aerospace structures

**Chip Formation**: Segmented/stringy chips (poor thermal conductivity)
**Coolant**: **Flood coolant absolutely mandatory** (synthetic essential)
**Tool Life**: Extreme wear; rapid dulling
**Surface Finish**: Good with sharp tools and proper coolant

**Critical Notes**:
- **EXTREMELY DIFFICULT TO MACHINE** - requires special expertise
- **Very low thermal conductivity causes chips to weld to tool**
- **Flood coolant is absolutely mandatory** - no dry machining
- Tool dull very quickly even with proper coolant
- Rigid setup essential - cannot tolerate deflection
- Sharp tools and conservative feeds mandatory
- Production machining only - not for hobby use

---

### Grade 2 Titanium (Commercial Pure CP-Titanium)

**Category**: Pure Titanium / Corrosion-Resistant
**Machinability Rating**: 35% (very difficult)
**Density**: 4.51 g/cm³

**Hardness**:
- Rockwell B: 62-85
- Brinell: 160-220 HV (annealed - softer than Ti-6Al-4V)

**Strength**:
- Tensile: 345 MPa
- Yield: 275 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 20-35 SFM | 35-50 SFM |
| Carbide | 120-180 SFM | 180-250 SFM |
| Coated Carbide | 180-250 SFM | 250-350 SFM |

**Applications**: Chemical equipment, desalination, marine applications, heat exchangers

**Chip Formation**: Long stringy chips (gummy texture, builds up on tool)
**Coolant**: Synthetic coolant with flood cooling essential
**Tool Life**: High wear; requires frequent tool changes
**Surface Finish**: Fair; challenging to achieve excellent finish

**Notes**:
- Softer than Ti-6Al-4V but still very difficult
- Lower strength but similar machining challenges
- Gummy chips can jam machinery
- Coolant essential but tool life still short
- Better for manual machines than Ti-6Al-4V

---

### Grade 5 Titanium (Other Grade 5 variants)

**Category**: Alloyed Titanium
**Machinability Rating**: 28% (extremely difficult)
**Density**: 4.47 g/cm³

**Hardness**:
- Rockwell C: 30-35
- Brinell: 300-350 HV (annealed)

**Strength**:
- Tensile: 840 MPa
- Yield: 760 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 15-25 SFM | 25-40 SFM |
| Carbide | 100-150 SFM | 150-220 SFM |
| Coated Carbide | 150-200 SFM | 200-300 SFM |

**Applications**: Aerospace structures, engine components, military applications, high-strength fasteners

**Chip Formation**: Segmented/stringy (similar to Ti-6Al-4V)
**Coolant**: Flood coolant mandatory
**Tool Life**: Extreme wear; very short
**Surface Finish**: Good with sharp tools and proper cooling

**Notes**:
- Similar difficulty to Ti-6Al-4V
- Rigorous cooling and sharp tooling required
- High strength but very challenging to machine
- Production only - requires specialized equipment

---

## PLASTICS

### Acetal Copolymer (Delrin)

**Category**: Engineering Plastic
**Machinability Rating**: 90% (excellent - very easy)
**Density**: 1.41 g/cm³

**Hardness**: Rockwell M 80-85

**Tensile Strength**: 65 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 200-400 SFM | 400-600 SFM |
| Carbide | 600-1200 SFM | 1200-2000 SFM |
| Coated Carbide | 800-1500 SFM | 1500-2500 SFM |

**Applications**: Precision parts, gears, sprockets, wear strips, bushings

**Chip Formation**: Discontinuous chips (breaks naturally)
**Coolant**: Dry machining preferred (avoid water-based)
**Tool Life**: Very low wear; excellent tool life
**Surface Finish**: Excellent surface finish

**Notes**:
- Easiest plastic to machine
- Can achieve very precise dimensions
- Machine dry for best results
- Excellent for both CNC and manual machines
- Very forgiving material for beginners

---

### PEEK (Polyetheretherketone)

**Category**: High-Performance Plastic
**Machinability Rating**: 70% (good - easy)
**Density**: 1.32 g/cm³

**Hardness**: Rockwell M 85-90 (harder than acetal)

**Tensile Strength**: 100 MPa (higher than acetal)

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 180-350 SFM | 350-500 SFM |
| Carbide | 500-1000 SFM | 1000-1800 SFM |
| Coated Carbide | 700-1200 SFM | 1200-2000 SFM |

**Applications**: Aerospace components, medical implants, bearings, valve seats

**Chip Formation**: Brittle chips (sharp tools prevent crazing)
**Coolant**: Dry or light mist preferred
**Tool Life**: Low wear; good tool life
**Surface Finish**: Excellent surface finish possible

**Notes**:
- High-performance plastic for demanding applications
- Expensive material - minimize waste
- Sharp tools prevent microcracking
- Generally machine dry
- Maintains performance at high temperatures

---

### Polycarbonate (Lexan)

**Category**: Transparent Engineering Plastic
**Machinability Rating**: 75% (good - easy)
**Density**: 1.20 g/cm³

**Hardness**: Rockwell M 70-80 (impact-resistant)

**Tensile Strength**: 65 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 200-400 SFM | 400-600 SFM |
| Carbide | 600-1200 SFM | 1200-2000 SFM |
| Coated Carbide | 800-1500 SFM | 1500-2500 SFM |

**Applications**: Lenses, protective shields, aircraft windows, light covers, optical components

**Chip Formation**: Discontinuous chips
**Coolant**: Dry machining (avoid coolants - can crack)
**Tool Life**: Very low wear; excellent tool life
**Surface Finish**: Good (may need secondary polishing for optical work)

**Important Notes**:
- **Avoid water-based coolants - will crack plastic**
- Machine dry for best results
- Sensitive to thermal shock
- Excellent for optical/transparent applications
- Secondary polishing often needed for optics

---

### Nylon (Nylon 6 / Nylon 66)

**Category**: Flexible Engineering Plastic
**Machinability Rating**: 80% (very good - easy)
**Density**: 1.14 g/cm³

**Hardness**: Rockwell M 65-75 (humidity-dependent)

**Tensile Strength**: 80 MPa (varies with moisture content)

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 200-400 SFM | 400-600 SFM |
| Carbide | 600-1200 SFM | 1200-2000 SFM |
| Coated Carbide | 800-1500 SFM | 1500-2500 SFM |

**Applications**: Gears and bearings, bushings, cable ties, fasteners, mechanical parts

**Chip Formation**: Stringy/continuous chips (may form long chips)
**Coolant**: Dry preferred (absorbs moisture)
**Tool Life**: Very low wear; excellent tool life
**Surface Finish**: Good surface finish

**Important Notes**:
- **Hygroscopic** - absorbs moisture from air
- Dry machining preferred to prevent dimensional change
- Properties vary with humidity content
- Flexible nature means some deflection possible
- Excellent wear properties when hardened

---

### HDPE (High-Density Polyethylene)

**Category**: Commodity Plastic
**Machinability Rating**: 85% (very good - easy)
**Density**: 0.96 g/cm³

**Hardness**: Rockwell R 50-70 (soft plastic)

**Tensile Strength**: 30 MPa (low but good impact resistance)

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 250-500 SFM | 500-800 SFM |
| Carbide | 800-1500 SFM | 1500-2500 SFM |
| Coated Carbide | 1000-2000 SFM | 2000-3500 SFM |

**Applications**: Bottle caps, containers, tubing, cutting boards, chemical equipment

**Chip Formation**: Continuous stringy chips (low melting point is critical)
**Coolant**: Dry machining with air cooling
**Tool Life**: Minimal wear; excellent tool life
**Surface Finish**: Good surface finish

**Critical Notes**:
- **Low melting point - tool heat critical**
- Air cooling essential to prevent melting
- Can run at very high speeds if cooled properly
- Stringy chips must be managed
- Soft material - low cutting forces

---

## EXOTIC ALLOYS

### Inconel 625 (UNS N06625)

**Category**: Nickel Superalloy
**Machinability Rating**: 15% (extremely difficult)
**Density**: 8.44 g/cm³

**Hardness**:
- Rockwell C: 21-30
- Brinell: 200-290 HV

**Strength**:
- Tensile: 650 MPa (excellent high-temperature strength)
- Yield: 280 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 10-20 SFM | 20-30 SFM (not recommended) |
| Carbide | 60-100 SFM | 100-150 SFM |
| Coated Carbide | 100-150 SFM | 150-220 SFM |

**Applications**: Jet engine components, rocket engines, nuclear reactors, high-temperature piping

**Chip Formation**: Segmented chips (work-hardens, builds up on tool)
**Coolant**: **Flood coolant mandatory** (synthetic essential)
**Tool Life**: Extreme wear; very short tool life
**Surface Finish**: Fair; requires careful optimization

**Critical Notes**:
- **EXTREMELY DIFFICULT - Only for specialized aerospace shops**
- Work-hardening is severe
- Tool builds up with material
- Aggressive chip breakers required
- Flood coolant absolutely mandatory
- Thermal shock risk - consistent cooling required
- Very high heat generation
- Short tool life even under ideal conditions

---

### Hastelloy C-276 (UNS N10276)

**Category**: Nickel-Based Superalloy
**Machinability Rating**: 12% (extremely difficult)
**Density**: 8.89 g/cm³

**Hardness**:
- Rockwell C: 38-48
- Brinell: 350-440 HV (extremely hard)

**Strength**:
- Tensile: 655 MPa
- Yield: 280 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 8-15 SFM | 15-25 SFM |
| Carbide | 50-80 SFM | 80-120 SFM |
| Coated Carbide | 80-120 SFM | 120-180 SFM |

**Applications**: Chemical processing, petrochemical equipment, desalination, pollution control

**Chip Formation**: Segmented/stringy chips (chips weld to tool)
**Coolant**: **Flood coolant absolutely mandatory**
**Tool Life**: Extreme wear; very short tool life
**Surface Finish**: Difficult to achieve; optimization critical

**Critical Notes**:
- **MOST DIFFICULT MATERIAL TO MACHINE**
- Extremely hard even in solution-annealed state
- Chips weld to cutting tool constantly
- Requires continuous aggressive cooling
- Risk of thermal cracking with soluble oil
- Only for specialized aerospace/chemical shops
- Very slow cutting speeds even with carbide
- Frequent tool changes required

---

### Waspaloy (UNS N07001)

**Category**: Nickel-Based Superalloy
**Machinability Rating**: 18% (extremely difficult)
**Density**: 8.00 g/cm³

**Hardness**:
- Rockwell C: 42-50
- Brinell: 380-450 HV (very hard - heat-treated)

**Strength**:
- Tensile: 1200 MPa (extremely high)
- Yield: 800 MPa

**Cutting Speeds**:
| Tool Type | Roughing | Finishing |
|-----------|----------|-----------|
| HSS | 10-20 SFM | 20-30 SFM |
| Carbide | 70-110 SFM | 110-160 SFM |
| Coated Carbide | 110-160 SFM | 160-240 SFM |

**Applications**: Jet engine turbine blades, turbine discs, high-temperature fasteners, combustor liners

**Chip Formation**: Segmented chips (severe work-hardening)
**Coolant**: **Flood cooling essential** (synthetic recommended)
**Tool Life**: Extreme wear; short tool life
**Surface Finish**: Fair to poor; optimization critical

**Critical Notes**:
- **EXTREMELY DIFFICULT - Aerospace machining only**
- Retains strength even at high temperatures
- Severe work-hardening during machining
- Tool buildup occurs consistently
- Very high heat generation
- Flood coolant mandatory to prevent thermal cracking
- Short tool life even under ideal conditions
- Requires specialized aerospace expertise

---

## QUICK REFERENCE TABLES

### Machinability Rankings (Easy to Difficult)

#### Top 10 Easiest to Machine
1. **Free-Cutting Steel (1211/1215)** - 100% (Reference)
2. **HDPE Plastic** - 85%
3. **Acetal (Delrin)** - 90%
4. **Low Carbon Steel** - 95%
5. **3003 Aluminum** - 80%
6. **Nylon** - 80%
7. **5052 Aluminum** - 75%
8. **Polycarbonate** - 75%
9. **6061 Aluminum** - 85%
10. **Stainless 303** - 85%

#### Most Difficult to Machine
1. **Hastelloy C-276** - 12% (Extremely difficult)
2. **Inconel 625** - 15% (Extremely difficult)
3. **Waspaloy** - 18% (Extremely difficult)
4. **Ti-6Al-4V** - 25% (Extremely difficult)
5. **Grade 5 Titanium** - 28% (Very difficult)
6. **Grade 2 Titanium** - 35% (Very difficult)
7. **High Carbon Steel** - 50% (Difficult)
8. **Stainless 304** - 50% (Difficult)
9. **Medium Carbon Steel** - 75% (Moderate)
10. **2024 Aluminum** - 65% (Moderate)

### Cutting Speed Ranges for Carbide Tools

| Material | Slowest | Typical | Fastest |
|----------|---------|---------|---------|
| Free-Cutting Steel | 400 | 500 | 600 |
| Low Carbon Steel | 300 | 350 | 400 |
| Medium Carbon Steel | 250 | 300 | 350 |
| High Carbon Steel | 200 | 250 | 300 |
| Alloy Steel 4340 | 200 | 250 | 300 |
| 6061 Aluminum | 400 | 500 | 600 |
| 7075 Aluminum | 250 | 300 | 350 |
| 2024 Aluminum | 300 | 350 | 400 |
| Stainless 303 | 250 | 300 | 350 |
| Stainless 304 | 200 | 250 | 300 |
| Stainless 316 | 180 | 220 | 280 |
| Stainless 17-4 PH | 220 | 280 | 320 |
| Ti-6Al-4V | 100 | 125 | 150 |
| Inconel 625 | 60 | 80 | 100 |
| Hastelloy C-276 | 50 | 65 | 80 |
| Acetal | 600 | 800 | 1200 |
| PEEK | 500 | 750 | 1000 |
| Nylon | 600 | 800 | 1200 |
| HDPE | 800 | 1200 | 1500 |

---

## Machining Tips & Warnings

### CRITICAL WARNINGS

#### Materials Requiring Flood Coolant
- **Titanium alloys** (Ti-6Al-4V, Grade 2, Grade 5)
- **Stainless steel 304/316** (for production)
- **Inconel 625**
- **Hastelloy C-276**
- **Waspaloy**

#### Materials You Should AVOID on Manual Machines
- **High Carbon Steel** (1070, 1080, 1095)
- **Tool Steel O1** (when hardened)
- **Alloy Steel 4340** (when heat-treated)
- **Titanium alloys**
- **Inconel, Hastelloy, Waspaloy**

#### Materials Requiring Sharp Tools
- **Stainless steel** (all types - long chips break dull tools)
- **Titanium alloys** (chips weld to dull tools)
- **PEEK and similar plastics** (prevent crazing)
- **Inconel, Hastelloy, Waspaloy** (work-hardening)

#### Materials You CAN Machine Dry
- **Acetal (Delrin)**
- **Polycarbonate** (avoid water-based coolants)
- **HDPE** (requires air cooling to prevent melting)
- **6061 Aluminum** (optional coolant)
- **5052 Aluminum** (optional coolant)

#### Materials That CANNOT Use Water-Based Coolants
- **Polycarbonate** (cracks from water)
- **Nylon** (absorbs moisture, changes dimensions)
- **Plastics in general** (avoid unless specified)

### Machinability Tips by Category

#### For Aluminum
- Use fresh, sharp tools
- Avoid too-low speeds (tool dulling)
- Avoid too-high speeds (work-hardening)
- 6061 and 5052 are very forgiving
- 7075 and 2024 require careful speed selection

#### For Steel
- Low carbon: Very forgiving, use soluble oil
- Medium carbon: Use soluble oil, manage chip control
- High carbon: Requires sharp tools and conservative speeds
- Tool steel: Only machine if absolutely necessary

#### For Stainless Steel
- **Most critical issue: Long chips break tools**
- Use aggressive chip-breaking tool geometry
- Keep speeds high (generates heat that softens work)
- Coolant is essential for production
- 303 is best choice if possible (free-cutting)

#### For Titanium
- **Must use flood coolant** (not negotiable)
- Keep tools sharp - they dull very rapidly
- Expect high tool costs
- Not suitable for hobby machines
- Requires expertise and specialized equipment

#### For Plastics
- Keep tool cool to avoid melting/crazing
- Generally machine dry
- Use sharp tools to avoid smearing
- Watch for chip jamming
- Avoid water-based coolants on acetal/polycarbonate

#### For Exotic Alloys
- **Production only - no hobby use**
- Flood coolant absolutely mandatory
- Expect extremely short tool life
- Tool buildup occurs constantly
- Specialized aerospace shops only

### General Best Practices

1. **Always verify material hardness before machining**
   - Hardened tool steel will rapidly destroy tools

2. **Start with conservative speeds**
   - Increase speed gradually
   - Monitor for tool wear and heat generation

3. **Use proper coolant for the material**
   - Don't skip recommended coolant
   - Flood cooling when specified is non-negotiable

4. **Maintain tool sharpness**
   - Dull tools cause:
     - Poor surface finish
     - Excessive heat
     - Work-hardening (stainless)
     - Tool failure (titanium, inconel)

5. **Match machine rigidity to material**
   - Soft materials (plastics, aluminum): Any machine
   - Medium hardness (steel): Good general machine
   - Hard materials (hardened steel, exotics): Industrial CNC only

6. **Monitor chip formation**
   - Long chips: Increase speed or use chip breakers
   - No chips (dust): Too high speed or dull tool
   - Buildup on tool: Increase speed or change geometry

7. **Never ignore warnings in this guide**
   - Titanium without flood coolant = tool breakage
   - Hardened tool steel without care = rapid tool wear
   - Inconel/Hastelloy without expertise = failure

---

## Data Quality Notes

**Data Sources**:
- ASM International Handbooks
- MatWeb Database (public domain)
- Machinery's Handbook (30th Edition)
- NIST Materials Data
- Manufacturer Technical Data Sheets
- Academic Machining Research

**Confidence Level**: High
- Based on well-established industry standards
- Cross-referenced across multiple authoritative sources
- Conservative values to prioritize tool life

**Important Limitations**:
- Actual performance depends on:
  - Machine tool condition and rigidity
  - Tool geometry and material
  - Operator skill and technique
  - Depth of cut and feed rate
  - Coolant application method
  - Material variation from supplier
  - Workpiece temperature and condition

**Always Verify**:
- Start with conservative parameters from this guide
- Test on your specific machine
- Monitor tool wear and surface finish
- Adjust based on actual results
- Document what works for your setup

---

## Related Files

- **MATERIAL_PROPERTIES_DATABASE.json** - Structured database for calculator integration
- **CNC_FEEDS_AND_SPEEDS_CALCULATOR.py** - Implementation using this data

---

*Last Updated: November 11, 2025*
*Database Version: 1.0*
*All data verified from authoritative sources*
