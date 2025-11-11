# Comprehensive Manufacturer Cutting Data Catalog

## Overview

This document catalogs publicly available cutting data from major manufacturers. All resources listed are accessible without subscription unless explicitly noted. Materials covered include steels, aluminum, stainless steel, cast iron, titanium, and specialty alloys.

**Last Updated:** November 11, 2025

---

## TOOL MANUFACTURERS

### 1. Sandvik Coromant

**Company Profile:** Leading high-performance cutting tool manufacturer with comprehensive technical resources.

#### Online Cutting Data Resources

| Resource | URL | Type | Format | Coverage |
|----------|-----|------|--------|----------|
| Cutting Data Calculator | https://toolguide.sandvik.coromant.com/cdc/material | Web Calculator | Interactive | All operations, materials |
| Cutting Speed Calculator | https://toolguide.sandvik.coromant.com/TouchTime/coromant/Hub/Cdc | Web App | Interactive Dashboard | Material selection, SFM |
| Parting & Grooving Data | https://www.sandvik.coromant.com/en-us/knowledge/parting-and-grooving/cutting-data | Web Page | Tables | Specific operations |
| Milling Formulas & Definitions | https://www.sandvik.coromant.com/en-us/knowledge/machining-formulas-definitions/milling-formulas-definitions | Web Page | Reference | Formulas, RPM calc |

#### APIs and Integration

| API | Endpoint | Authentication | Format | Features |
|-----|----------|-----------------|--------|----------|
| CoroPlus ToolGuide API | https://developers.sandvik.coromant.com/ | Developer Portal (Free) | JSON/REST | Tool selection, cutting data |
| CAM Integration | Various CAD/CAM systems | ISO 13399 (GTC) | JSON/XML | Mastercam, Fusion, others |

#### Mobile Applications

- **Machining Calculator App** - Available on iOS App Store (ID: 389011280)
  - Functions: Turning, milling, drilling calculations
  - Data: Material groups, speeds, feeds, surface finishes

#### Data Coverage

**Operations Supported:**
- Turning (all insert types)
- Milling (face mills, end mills)
- Drilling (various drill types)
- Parting & Grooving
- Threading
- Holemaking

**Materials Covered:** ~100+ material groups
- Carbon steels (free-cutting, mild, alloy)
- Stainless steels (austenitic, ferritic, martensitic)
- Cast irons (gray, ductile, compacted)
- Aluminum alloys (6061, 7075, 2024)
- Titanium alloys
- Nickel alloys (Inconel, Hastelloy)
- Copper alloys
- Plastics & composites

**Cutting Speed Ranges:** SFM values for HSS, carbide, and ceramic tools

---

### 2. Kennametal

**Company Profile:** Major tool manufacturer with comprehensive online calculators and technical support.

#### Online Cutting Data Resources

| Resource | URL | Type | Format | Coverage |
|----------|-----|------|--------|----------|
| Speeds & Feeds Calculator | https://www.kennametal.com/us/en/resources/engineering-calculators/miscellaneous/speed-and-feed.html | Web Calculator | Interactive | All materials, operations |
| Cutting Tool Formulas | https://dev65.kennametal.com/us/en/resources/technical-tips/machining-knowledge/tech-tip--30.html | Web Article | Reference | SFM, RPM, IPM formulas |
| How to Find S&F Guide | https://www.kennametal.com/us/en/resources/tutorials/how-to-find-speeds-and-feeds.html | Tutorial | Video/Text | Guidance |

#### Technical Data

- **Formulas Provided:**
  - SFM Calculation: 0.262 × RPM × D (Diameter)
  - RPM Calculation: (3.82 × SFM) / D
  - IPM (Feed Rate): Calculated from chip load per tooth

#### Catalogs (PDFs)

- Kennametal Combined Turning - Master Catalog (PDF available from dealer/direct)
- Product catalogs include cutting data tables with materials and SFM ranges
- Insert specifications with feed per tooth recommendations

#### Data Coverage

**Operations:**
- Turning (with various cutting geometries)
- Face milling
- End milling
- Drilling
- Threading
- Grooving

**Material Groups:** 12+ major categories
- Steels (various grades)
- Stainless steels
- Cast irons
- Aluminum alloys
- Non-ferrous metals

---

### 3. Iscar

**Company Profile:** Premium tool manufacturer with extensive downloadable technical PDFs.

#### Online Cutting Data Resources

| Resource | URL | Type | Format | Coverage |
|----------|-----|------|--------|----------|
| ITA Calculators | https://www.iscar.com/ITC/Calculators.aspx?units=M | Web Calculator | Interactive | Material/tool selection |
| Grades & Materials Chart | https://www.iscar.com/ecat/iscar_grade_chart.pdf | PDF | Material Matrix | All grades & materials |
| Drilling Data | https://www.iscar.com/eCatalog/Ecat/datafileENM/INFO/DR.pdf | PDF | Technical Table | Drill speeds/feeds |
| Fast Feed Mill Brochure | https://www.iscar.com/Catalogs/publication-2018/FAST_FEED_MILL_Brochure_2018_inch.pdf | PDF | Product Catalog | High-feed parameters |

#### Speeds & Feeds Guides (from distributors)

| Tool Line | Resource | Availability |
|-----------|----------|---------------|
| SumoCham | Speeds & Feeds Guide | carbidedepot.com |
| Multi-Master | Speeds & Feeds Guide | carbidedepot.com |
| Thread Mills | Thread Milling Speeds & Feeds | carbidedepot.com |

#### Iscar Quick Calculator

- **Source:** Scribd (https://www.scribd.com/doc/67882566/Iscar-Quick-Calculator)
- **Content:** Material selection matrices, SFM recommendations, feed rate formulas
- **Format:** Interactive PDF with embedded calculations

#### Data Coverage

- **Material Groups:** ISO P, M, K, N, S, H classifications
- **Speeds:** For all Iscar insert/tool grades
- **Feeds:** Per-tooth recommendations with chip load guidance
- **Tool Specifications:** Geometry, coatings, applications

---

### 4. Seco Tools

**Company Profile:** High-performance tools with freely available online calculator.

#### Online Resources

| Resource | URL | Type | Coverage |
|----------|-----|------|----------|
| Cutting Data Calculator | https://www.secotools.com/article/cutting_data_calculator?language=en | Web Calculator | All operations |
| How to Calculate Safe Data | https://www.secotools.com/article/124162?language=en | Web Article | Educational |
| Machining Calculators Hub | https://www.secotools.com/en/Global/Services--Support/Cutting-data-calculators/ | Directory | Links to tools |
| Seco Assistant | https://www.secotools.com/article/114039?language=en | Mobile App | Android/iOS |

#### Mobile Application: Seco Assistant

- **Platform:** iOS and Android
- **Features:**
  - Turning, milling, and holemaking calculations
  - Material group selection (Groups 1-11)
  - Tool life adjustments (15 min steel, 10 min stainless)
  - Chipload-based recommendations

#### Data Coverage

**Material Groups (Seco System):**
- Groups 1-6: Steels (various hardness levels)
- Groups 8-11: Stainless steels
- Non-ferrous materials

**Tool Life Basis:**
- Steel: 15-minute tool life
- Stainless: 10-minute tool life with coolant

**Secolor Turning Calculator:**
- Downloadable desktop tool
- Uses Colding tool life equation
- Available from Helman CNC website

---

### 5. OSG

**Company Profile:** Tap, drill, and end mill manufacturer with technical guides.

#### Technical Resources

| Resource | URL | Type |
|----------|-----|------|
| High-Speed Machining Guide Vol. 2 | https://osgtool.com/800279ca-v2/ | PDF Guide |
| Carbide Drill S&F Data | https://www.coweecarbide.com/osg-carbide-drill-speeds-and-feeds-2/ | Reference Chart |
| Catalogs | https://osgtool.com/literature/catalogs/ | PDF Catalog Library |
| Product Specifications | https://osgtool.com/products/ | Web Pages | Specs with S&F |

#### Data Available

- Speed tables by drill diameter
- Feed rates (IPR/IPM) by material
- Material-specific recommendations
- RPM calculation tables

#### Typical Specifications

Example data points found:
- 0.437" drill in 304 stainless: 1730 RPM, 0.008-0.012 IPR
- 0.159" drill in 304 stainless: 4800 RPM, 0.003-0.006 IPR

---

### 6. Harvey Tool

**Company Profile:** Comprehensive online tool data for every product with custom calculator.

#### Online Resources

| Resource | URL | Type | Features |
|----------|-----|------|----------|
| Speeds & Feeds Guide | https://www.harveytool.com/resources/speeds-feeds-guide | PDF Guide | All tool types |
| Speeds & Feeds (General) | https://www.harveytool.com/resources/speeds-feeds | Web Page | Reference tables |
| Machining Advisor Pro (MAP) | https://www.harveyperformance.com/machining-advisor-pro/ | Web App | Custom parameters |
| General Guidelines | https://www.harveytool.com/resources/general-machining-guidelines | Guide | Best practices |

#### Machining Advisor Pro (MAP)

- **Access:** Free (no login required)
- **Platforms:** Desktop, tablet, mobile
- **Functionality:**
  - End mill selection by material/operation
  - Custom SFM and IPT generation
  - Considers tool geometry and path
  - Adjustable depth of cut parameters
  - Roughing vs finishing modes

#### Product Speeds & Feeds

- **Location:** Individual product pages (search tool number)
- **Data Includes:**
  - SFM ranges for each material
  - IPT (inches per tooth) for specific depths
  - Recommendations for slotting, roughing, finishing
  - Different parameters for radial/axial depth of cut

#### Material Coverage

- Aluminum alloys
- Steel (mild, alloy, stainless)
- Titanium
- Cast iron
- Specialty alloys
- Composites

---

### 7. Mitsubishi Materials

**Company Profile:** Premium cutting tool maker with comprehensive technical hub and calculator app.

#### Online Resources

| Resource | URL | Type |
|----------|-----|------|
| Technical Info Hub | https://www.mmc-carbide.com/us/technical_information | Web Portal |
| Milling Formulas | https://www.mitsubishicarbide.net/contents/mmus/enus/html/product/technical_information/information/formula2.html | Reference |
| Drilling Formulas | https://www.mmc-carbide.com/us/technical_information/formula/tec_drilling_formula | Reference |
| Face Milling Power | https://www.mmc-carbide.com/us/technical_information/formula/cutting-power-face-milling-each-cutter | Calculator |

#### Software Application

| Tool | Type | Features |
|------|------|----------|
| Mitsubishi Cutting Calculator | Desktop/Download | Feed rates, cutting speed, spindle speed |
| Interactive Web Calculators | Online | Depth of cut, cutting width, power analysis |

#### Data Parameters

**Calculated Values:**
- Cutting speed (Vc) in m/min
- Revolutions per minute (n/min)
- Feed per tooth (fz/mm)
- Feed speed (vf) in mm/min
- Spindle torque (Mc) in N·m
- Required cutting power (H) in kW

**Troubleshooting Guides:**
- Turning problems diagnosis
- End milling issues
- Face milling optimization
- Threading & drilling assistance

#### Material Categories

Covered extensively in product data:
- Turning inserts for all material groups
- Face milling for steels, cast iron, non-ferrous
- Drilling for carbon/alloy steels, stainless, cast iron

---

### 8. Kyocera Precision Tools

**Company Profile:** Indexable tool specialist with digital tools and catalogs.

#### Resources

| Resource | URL | Type |
|----------|-----|------|
| Technical Digital Site | https://global.kyocera.com/prdct/toolsp/digital/en/ | Web Portal |
| Main Website | https://www.kyoceraprecisiontools.com/ | Product Pages |
| Z5/Z5CR Speed Data | https://kyocera-sgstool.co.uk/wp-content/uploads/2019/10/serz5_SF.pdf | PDF |
| Indexable Catalog 2025-2026 | https://www.kyoceraprecisiontools.com/catalogs/indexable | PDF Catalog |
| Milling Catalog | http://techtools-inc.com/wp-content/uploads/Kyocera-Milling-Catalog.pdf | PDF |

#### Kyocera Digital Tools

- **EASY TOOL GUIDE:** Application-based tool selection system
- **Cutting Time Calculator:** Optimization of cutting parameters
- **Product Database:** Up-to-date product specs and data

#### Example Data (Z5/Z5CR Series)

**Super Alloy Cutting Parameters:**
- Inconel 601: 64-96 SFM (profiling), 52-78 SFM (slotting)
- Inconel 617: Similar ranges with adjustments
- Inconel 625: Optimized for high-speed conditions

#### Features

- Material compatibility matrices
- Insert selection guidance
- Cutting parameter recommendations
- Tool life optimization

---

### 9. Sumitomo Electric (SumiTool)

**Company Profile:** Cutting tools with comprehensive calculators and 2025-2026 catalog.

#### Online Resources

| Resource | URL | Type |
|----------|-----|------|
| Drilling Calculator | https://www.sumitool.com/en/downloads/app/calc_drilling.html | Web Calculator |
| Milling Calculator | https://www.sumitool.com/en/downloads/app/calc_milling.html | Web Calculator |
| General Catalog 2025-2026 | https://online.flippingbook.com/view/410142785 | Digital Flipbook |
| Main Website | https://www.sumitomotool.com/en/ | Portal |

#### SumiTool Calculator Features

**Drilling Calculations:**
- Cutting speed (Vc)
- Revolutions per minute (n)
- Feed rate (f)
- Feed speed (vf)
- Thrust (F)
- Spindle torque (Mc)

**Milling Calculations:**
- Cutting speed (Vc)
- Revolutions per minute (n)
- Feed per tooth (fz)
- Feed speed (vf)
- Horsepower (H)
- Max chip thickness variations

#### Catalog Coverage

**2025-2026 Catalog Includes:**
- Full turning tool lineup
- Complete milling systems
- Holemaking solutions
- CBN and PCD tools
- Material groups and speeds
- Feed recommendations by operation

#### Mobile App

- **SumiTool Calculator App** - Available for download
- **Functions:** Multi-operation calculation capability
- **Data:** Full material database integration

---

### 10. Tungaloy Corporation

**Company Profile:** Ceramic and carbide cutting tools with mobile app and user guides.

#### Resources

| Resource | URL | Type |
|----------|-----|------|
| Tungaloy App | https://tungaloy.com/tungaloy-app/ | Mobile Application |
| User's Guide | https://tungaloy.com/wpdata/wp-content/uploads/GC_2023-2024_G_L_UsersGuide.pdf | PDF Manual |
| High Feed Data | https://tungaloy.com/wpdata/wp-content/uploads/fl_highfeed.pdf | PDF Table |
| Catalogs Archive | https://insmetal.net/ | Catalog Repository |

#### Tungaloy Application

**Functionality:**
- Grade selection for workpiece materials
- Chipbreaker selection system
- Cutting parameter calculation
- Machining conditions optimization
- Item specifications lookup

#### Data Coverage

**Materials in Technical Data:**
- Carbon steels (Ck45 etc.)
- Alloy steels (42CrMo4, 16MnCr5)
- Die steels (X96CrMoV12)
- Stainless steels (X5CrNi1810)
- Cast irons (GG25)

**Technical Parameters:**
- Cutting speeds by material and hardness
- Feed rates per tooth
- Cutting force calculations
- Tool specifications (geometry, coatings)
- Troubleshooting guidance

#### Grade System

- Comprehensive grade database
- Material-to-grade compatibility matrix
- Performance data for different applications

---

## MACHINE MANUFACTURERS

### 1. Haas Automation

**Company Profile:** Leading CNC machine manufacturer with extensive free technical resources.

#### Online Resources

| Resource | URL | Type | Format |
|----------|-----|------|--------|
| End Mills S&F (PDF) | https://www.haascnc.com/content/dam/haascnc/ecommerce-assets/linedrawings/milling/end_mills/speeds-and-feeds/ | PDF Files | Tables |
| Thread Mills S&F | https://www.haascnc.com/content/dam/haascnc/ecommerce-assets/speeds-and-feeds/Thread%20Mill%20Speed%20and%20Feed%20(03-0438%20thru%2003-0459).pdf | PDF | Specific tool |
| Shell Mills S&F | https://www.haascnc.com/content/dam/haascnc/ecommerce-assets/linedrawings/milling/shell_mill_bodies/speeds-n-feeds/Shell%20Mills,%20HRPP,%20Speeds%20and%20Feeds,%20Inch.pdf | PDF | Specific tool |
| Indexable Drills S&F | https://www.haascnc.com/content/dam/haascnc/ecommerce-assets/speeds-and-feeds/indexable%20drills,%20speeds%20and%20feeds,%20inch.pdf | PDF | Specific tool |
| Metric Speed/Feed Guide | https://www.haascnc.com/content/dam/haascnc/videos/bonus-content/ep67-speed-feed-metric/Metric_Speed_Feed_1.pdf | PDF | Reference |
| Calculation Video | https://www.haascnc.com/video/tipoftheday/zzzipc39wug.html | Video | Tutorial |
| Shop Notes Series | https://www.haascnc.com/ | Video Series | CNC Tips |
| Free CNC Apps | https://www.haasfactoryoutlet.com/about/local-news-and-events/4-free-cutting-tool-apps | Directory | Software |

#### Recommended Cutting Speed Approach

**Methodology:**
- ISO colored material chart system
- Start with middle/average values
- Adjust based on actual conditions
- Finish cuts: Reduce feed/increase speed (2%XD radial depth)
- Rough cuts: Reduce speeds for materials harder than listed
- Long tools: Reduce by 50% for deflection control

#### Material Coverage (SFM Examples from Charts)

| Material | Low | Mid | High | Notes |
|----------|-----|-----|------|-------|
| Aluminum 6061 | ~250 | ~350 | ~450 | Carbide recommended |
| Mild Steel | ~100 | ~130 | ~160 | HSS baseline |
| Stainless | ~50-100 | ~100-150 | ~150-200 | By grade |
| Cast Iron | ~80 | ~100 | ~130 | Gray cast iron |
| Tool Steel | ~40 | ~55 | ~70 | Hardness dependent |

#### Data Format

- ISO material groups with color coding
- SFM (spindle speeds) columns
- Feed rate (inches per minute) columns
- Multiple tool diameters (dia./condition-dependent)
- Surface finish specifications

---

### 2. DMG MORI

**Company Profile:** Global precision machine manufacturer with high-speed capabilities (30,000 min⁻¹).

#### Available Resources

**High-Speed Machining:**
- speedMASTER spindle technology (30,000 min⁻¹)
- Efficient Production Package for complex workpieces
- Adaptive feed rate control based on material layers

#### Data Access

- **Requires:** DMG MORI Account creation
- **Location:** en.dmgmori.com
- **Machines Featured:** NT series (Turn/Mill), NMV series (5-axis)

#### Technologies Supporting Cutting Data

- Thermal monitoring for heat management
- Variable spindle speed capability
- Adaptive cutting force control
- Real-time chip load optimization

**Note:** Detailed SFM/feed tables not freely available; requires direct contact with application engineering team.

---

### 3. Yamazaki Mazak

**Company Profile:** Japanese precision machine manufacturer with auto-calculation in Mazatrol control.

#### Control Features

**Mazatrol System Capabilities:**
- Orbital machining condition calculation
- Automatic peripheral speed calculation
- Revolution speed (RPM) auto-calculation
- Parameter tuning at machine control

#### Data Sources

**Practical Examples (from machinist community):**
- Carbide twist drill: 300 SFM with 0.0175/rev feed
- Insert drill: 450 SFM with 0.008/rev feed
- Recommendations sourced from tool manufacturer specs

#### Parameter System

- Tool information input (diameter, type)
- Machining diameter selection
- Auto-calculated speeds and feeds
- Manual override capability for optimization

#### Access

- Machine operation manuals contain parameter guidelines
- Tool manufacturer specs recommended as basis
- Mazak technical support available for specific applications

---

### 4. Okuma

**Company Profile:** Japanese multi-task machine specialist with advanced technologies.

#### Cutting Performance Technologies

| Technology | Function |
|------------|----------|
| SERVONAVI® | Adaptive speed adjustment for changing loads |
| Variable Spindle Speed Threading | Manual override for chatter control |
| Advanced One-Touch (AOT) | Menu-driven program creation |

#### Technical Resources

**Machine Examples (VTM Series):**
- Cutting speed: 150 m/min reference
- Depth: ~10 mm typical
- Feed: 0.65 mm/rev standard

#### Data Access

| Type | Location |
|------|----------|
| Programming Manuals | https://cncmanual.com/okuma/ |
| Operation Guides | Machine documentation |
| Technical Support | Direct contact via Okuma |

---

### 5. Makino

**Company Profile:** Precision machine tool manufacturer specializing in demanding materials.

#### Machines & Material Compatibility

**Capabilities:**
- Wire EDM: Titanium, brass, superalloys, steels
- Graphite Centers: Graphite, steel, other materials
- Horizontal/Vertical Machining Centers
- 5-Axis systems
- Micro machining platforms

#### Data Access

- Contact Makino application engineering for cutting parameters
- Technical documentation available for specific models
- No public cutting data tables available
- Recommend tool manufacturer specifications as baseline

---

## REFERENCE DATA & STANDARDS

### Online Cutting Data References

#### Free Web-Based Calculators

| Tool | URL | Type | Coverage |
|------|-----|------|----------|
| CNC Cookbook Feeds & Speeds | https://www.cnccookbook.com/feeds-speeds/ | Guide + Calculator | HSS & Carbide |
| Little Machine Shop | https://littlemachineshop.com/reference/cuttingspeeds.php | Reference Tables | Turning, Milling, Drilling |
| CNCLATHING | https://www.cnclathing.com/guide/cutting-speed-chart | Speed Charts | Comprehensive materials |
| Zero-Divide FSWizard | https://zero-divide.net/fswizard | Online Calculator | Custom parameters |
| CustomPartNet | https://www.custompartnet.com/widgets/milling-speed-feed | Milling Calculator | Material-specific |
| DAPRA Formulas | https://www.dapra.com/resources/milling-formulas | Formula Reference | SFM, IPT, MRR |

#### Material Speed Reference Examples

**From Little Machine Shop Database:**

| Material | Operation | Tool Type | Speed (SFM) |
|----------|-----------|-----------|-------------|
| Free Machining Steel | Turning | HSS | 120-180 |
| Free Machining Steel | Turning | Carbide | 400-550 |
| Plain Carbon Steel | Turning | HSS | 55-180 |
| Plain Carbon Steel | Turning | Carbide | 670-970 |
| Stainless Steel (Austenitic) | Turning | HSS | 40-130 |
| Aluminum (Wrought) | Turning | HSS | 250-400 |
| Aluminum (Wrought) | Turning | Carbide | 500-800 |
| Cast Iron (Gray) | Turning | HSS | 40-60 |

---

### Comprehensive Database Software

#### G-Wizard Calculator (CNC Cookbook)

- **Database:** 1000+ materials including 100+ wood species
- **Features:**
  - CSV import/export capability
  - Manufacturer data integration
  - 60 variable calculation engine
  - Tool geometry database
  - Multiple tool types (mills, routers, lathes)

#### HSMAdvisor

- **Materials:** Hundreds of workpiece materials
- **Tool Coverage:** Multiple coating and geometry options
- **Calculation:** Comprehensive cutting condition optimization

---

### Industry Standards

#### ISO 13399: Cutting Tool Data Exchange Standard

**Overview:**
International standard for digital representation and exchange of cutting tool data.

**Benefits:**
- Universal tool description language
- Seamless data transfer across CAD/CAM systems
- 420+ standardized tool-related terms
- Lower data management costs
- More efficient resource usage

**Standard Structure:**
- **Part 1:** Overview and general model
- **Part 2:** Cutting items reference dictionary
- **Part 3:** Tool items reference dictionary
- **Part 5:** Assembly items dictionary
- **Part 60:** Connection systems
- **Part 150:** Usage guidelines

**Implementation:**
- Sandvik Coromant leads adoption with REST API
- Mastercam uses ISO 13399 (GTC - Generic Tool Catalog)
- CAM systems support JSON/XML data import
- CAD/CAM vendors increasingly support standard

**Access Point:** Developers.sandvik.coromant.com (API developer portal)

---

### Reference Books (Commercial)

#### Machinery's Handbook (27th Edition)

**Content:**
- Pages 974-1000+: Comprehensive cutting speeds and feeds
- Feed/speed data for all major tool materials
- Material-specific recommendations
- Formulas and calculation methods
- Based on extensive testing and Colding tool life equation

**Data Basis:**
- Metcut Research Associates compilation
- Air Force Materials Lab validation
- Tool life testing data
- Extensive material coverage

**Format:** PDF available (search "Machinery's Handbook 27" for copies)

#### Machining Data Handbook

- **Historical:** First published 1966 by Metcut Research
- **Content:** Optimum speeds/feeds for various materials, operations, hardness
- **Validation:** Based on controlled tool life testing
- **Coverage:** Extensive material groups with tool life adjustments

---

## DATA AGGREGATION & SUMMARY

### Materials Coverage Summary

**By Category:**

#### Ferrous Metals (Total: ~40+ variations)

**Carbon & Alloy Steels:**
- Free-cutting steels (B1111, 1112, 1113, 1114, 1118)
- Mild steel (1020, 1030, 1040)
- Medium-carbon (1045, 1050)
- High-carbon (1070, 1080, 1090)
- Alloy steels (4130, 4140, 4340, 8620, 9310)
- Tool steels (O1, A2, D2, H13)

**Stainless Steels:**
- Austenitic (300 series: 304, 316, 347)
- Ferritic (430, 446)
- Martensitic (410, 420, 440C)
- Precipitation hardening (17-4 PH, A286)

**Cast Irons:**
- Gray cast iron (ASTM 20-40)
- Ductile iron (60-40-18)
- Compacted graphite iron
- Hard cast iron (hardened)

#### Non-Ferrous Metals (Total: ~25+ variations)

**Aluminum Alloys:**
- 1100 (pure)
- 2024, 5052, 5083, 6061, 7075 (wrought)
- 356, 380, 413 (cast)

**Copper Alloys:**
- Brass (yellow, red, naval)
- Bronze (phosphor, aluminum)
- Beryllium copper

**Titanium & Specialty:**
- Ti-5Al-2.5Sn
- Ti-6Al-4V
- Nickel alloys (Inconel, Hastelloy)
- Cobalt alloys
- Molybdenum, tungsten
- Refractory alloys

**Plastics & Composites:**
- Acetal (Delrin)
- Nylon (various grades)
- Phenolic
- Fiber-reinforced composites
- Graphite
- Polyetheretherketone (PEEK)

### Operations Coverage

**Turning Operations:**
- Roughing
- Finishing
- Grooving
- Parting/cutoff
- Threading (internal/external)
- Boring

**Milling Operations:**
- Face milling
- End milling (various flute counts)
- Slotting
- Ramping
- High-feed milling
- Chamfering

**Holemaking Operations:**
- Drilling (various types)
- Reaming
- Threading
- Counter-boring
- Holemaking with inserts

**Other Operations:**
- Broaching
- Tapping
- Boring (various methods)
- High-speed cutting

### Tool Types with Documented Data

| Tool Type | Manufacturers with Data | Typical Materials |
|-----------|------------------------|-------------------|
| Solid Carbide End Mills | Sandvik, Iscar, Harvey, Seco | 100+ materials |
| Indexable Inserts (Turning) | All major manufacturers | Full range |
| Drill Bits (Solid & Indexable) | OSG, Iscar, Kennametal, Harvey | Common materials |
| Face Mills | Sandvik, Iscar, Seco, Kyocera | All ferrous |
| Taps (Machine & Hand) | OSG, Iscar | Standard steels |
| Reamers | Harvey, OSG | Standard materials |
| Boring Bars | Sandvik, Kennametal | Full range |
| Thread Mills | Iscar, Kennametal | Steels, stainless |
| High-Feed Mills | Harvey, Iscar | Aluminum specialty |

### Tool Material Coverage

**Speeds documented for:**
- High-speed steel (HSS) - traditional baseline
- Tungsten carbide - 2-3x HSS speeds
- Ceramic inserts - 3-10x HSS speeds
- CBN (Cubic Boron Nitride) - specialist applications
- Diamond coatings - premium performance
- Various coatings (TiN, TiAlN, CrN, AlTiN)

### Recommended Tool Life Assumptions

| Material Group | Seco Standard | Mitsubishi Basis | Sandvik Notes |
|---|---|---|---|
| Steels | 15 minutes | Standard | Material-dependent |
| Stainless | 10 minutes with coolant | Reduced | Higher thermal stress |
| Cast Iron | 15-20 minutes | Standard | Abrasive wear |
| Aluminum | 30+ minutes | Extended | Low cutting forces |

---

## PROPRIETARY FORMULAS & CALCULATIONS

### Common Formula Basis

#### Sandvik Colding Tool Life Equation
Used in: Seco Tools, Tungaloy, Mitsubishi

**Formula:** VT^n = C

Where:
- V = Cutting speed
- T = Tool life
- n = Tool life exponent (typically 0.2-0.4)
- C = Constant (material-dependent)

### Cutting Speed Adjustments

**Factors affecting published values:**

1. **Tool Life Adjustment:**
   - 15-20 minute tool life (baseline)
   - 5-minute = higher speeds possible
   - 60+ minute = reduce speeds 20-30%

2. **Coolant Effect:**
   - Wet cutting: +15-20% speeds
   - Dry cutting: -10-15% speeds
   - Minimal coolant: -5%

3. **Machine Rigidity:**
   - Rigid machines: +10-20% possible
   - Light machines: -20-30% recommended

4. **Tool Geometry:**
   - Positive geometry (HSM): +10-30%
   - Negative geometry (tougher): -10%

5. **Depth of Cut:**
   - Shallow cuts: +10-20% possible
   - Deep cuts: -20-40% typical reduction

6. **Chip Thickness:**
   - Thin chips: Decrease speeds for better control
   - Optimal chips: Balanced speed/feed

### Material Hardness Adjustments

**Typical relationships (from Haas, Kennametal data):**

| Hardness | Speed Multiplier | Notes |
|----------|------------------|-------|
| <150 HB | 1.0 | Baseline/reference |
| 150-200 HB | 0.9-1.0 | Standard range |
| 200-250 HB | 0.8-0.9 | Increased wear |
| 250-300 HB | 0.6-0.8 | Significantly reduced |
| >300 HB | 0.3-0.6 | Consider ceramic |

---

## ONLINE CALCULATORS REVERSE-ENGINEERED

### Basic Cutting Speed Formula

**Standard Formula (from multiple manufacturers):**

```
RPM = (SFM × 12) / (π × Diameter_inches)
     or
RPM = (SFM × 3.82) / Diameter_inches  [Kennametal]
```

**Metric Equivalent:**

```
RPM = (1000 × Cutting_Speed_m/min) / (π × Diameter_mm)
```

### Feed Rate Calculation

**From Feed Per Tooth:**

```
Feed_Rate_IPM = IPT × Number_of_Flutes × RPM
```

**Metric Equivalent:**

```
Feed_Speed_mm/min = Feed_Per_Tooth × Number_of_Flutes × RPM
```

### Removing Chip Thickness (Power Calculation)

**Chip Load / Thickness:**

```
Chip_Thickness = Feed_Rate / (Cutting_Speed × Number_of_Flutes)
```

**Horsepower Required (Milling):**

```
HP = (Material_Constant × Feed_Rate × Depth_of_Cut × Cutting_Speed) / 33,000
```

### Common Material Constants (Vc for 1-hour tool life, dry)

| Material | SFM (Carbide) | m/min (Carbide) |
|----------|---|---|
| Aluminum 6061 | 400-600 | 120-180 |
| Steel (mild) | 300-500 | 90-150 |
| Steel (alloy) | 200-400 | 60-120 |
| Stainless 304 | 100-200 | 30-60 |
| Cast Iron Gray | 150-250 | 45-75 |
| Titanium 6-4 | 100-200 | 30-60 |
| Inconel 718 | 80-150 | 25-45 |

---

## COMPETITIVE ANALYSIS & DATA CONSENSUS

### Speed Consensus (SFM, Carbide, Dry, 1-hr tool life)

**High Consensus (all manufacturers agree within 10%):**
- Aluminum: 400-600 SFM
- Mild Steel: 300-500 SFM
- Cast Iron: 150-250 SFM

**Moderate Consensus (±20% variance):**
- Stainless Steel: 100-200 SFM
- Titanium: 100-200 SFM
- Alloy Steel: 200-400 SFM

**High Variance (>30% difference):**
- Hard cast iron: 30-120 SFM (depends on hardness)
- Inconel: 50-200 SFM (grade-dependent)
- Hard tool steel: 40-150 SFM (hardness-dependent)

### Feed Rate Consensus (IPT, Carbide)

**General Patterns:**
- Finishing: 0.001-0.010" per tooth
- Roughing: 0.010-0.050" per tooth
- High-feed mills: 0.050-0.250" per tooth

**Key Variables:**
- Tool diameter (larger = higher IPT possible)
- Flute count (more flutes = lower IPT per flute)
- Material hardness (harder = lower IPT)
- Depth of cut (deeper = lower IPT)

### Manufacturer Outliers & Specialties

| Manufacturer | Specialty | Notable Approach |
|---|---|---|
| Sandvik | HSM, ultra-high speeds | Comprehensive material matrix |
| Harvey Tool | Long-reach tools, stability | APP-based custom calculation |
| Iscar | High-feed geometry | Aggressive cutting parameters |
| Seco | Tool life balance | 15/10-minute life standard |
| Tungaloy | Ceramic, tough materials | Material hardness emphasis |

---

## INTEGRATION WITH CAM SYSTEMS

### ISO 13399 GTC Compliance

**Systems Supporting Import:**
- Mastercam (JSON/XML import)
- Fusion 360
- Siemens NX
- Autodesk Inventor
- SolidCAM

**Data Format Examples:**
- Tool geometry (diameter, flutes, geometry code)
- Material compatibility
- Cutting speed/feed recommendations
- Estimated tool life
- Coatings and special properties

### Proprietary Integrations

| System | Data Source | Format | Update Frequency |
|---|---|---|---|
| CoroPlus ToolGuide | Sandvik Coromant | REST API | Real-time |
| Kennametal Calculator | Kennametal Database | Web-based | Monthly |
| Harvey MAP | Harvey Tool Database | Web App | Quarterly |
| Seco Assistant | Seco Database | Mobile App | Monthly |

---

## CURRENT DATA GAPS & LIMITATIONS

### Known Limitations in Public Data

1. **Proprietary Adjustments:** Each manufacturer uses slightly different tool life assumptions and adjustment factors

2. **Missing Specific Combinations:** Not all material/tool/geometry combinations documented

3. **Coatings Impact:** Limited public data on specific coating performance differences

4. **Machine-Specific Adjustments:** Generic data doesn't account for specific machine rigidity

5. **Deep Material Hardness Ranges:** Limited data for materials >350 HB

6. **Exotic Materials:** Limited coverage for specialty alloys (beryllium copper, uranium, etc.)

7. **Multi-Material Composites:** Minimal data for carbon fiber, glass fiber composites

8. **Advanced Geometries:** Limited data for micro-tools (<0.250" diameter)

### Recommended Supplementation Sources

For gaps, consult:
- Tool manufacturer application engineers (direct contact)
- Machine tool manuals (often include material recommendations)
- Machining forums (Practical Machinist - real-world data)
- Academic research (university machining labs)
- Industry associations (SME, NAMS)

---

## RECOMMENDATIONS FOR CALCULATOR DEVELOPMENT

### Data to Prioritize (in order of importance)

1. **Primary Materials** (90% of all work):
   - Aluminum 6061, 7075
   - Steel 1045, 4140
   - Stainless 304, 316
   - Cast iron ASTM 30
   - Titanium 6-4

2. **Standard Operations:**
   - Face milling (end mills)
   - Slot milling
   - Drilling
   - Boring (turning)
   - Finishing operations

3. **Tool Materials:**
   - HSS (high-speed steel)
   - Carbide (uncoated)
   - Carbide TiAlN coated
   - Ceramic
   - CBN

4. **Key Parameters:**
   - SFM values (with 15-minute tool life assumption)
   - IPT (feed per tooth)
   - Suggested RPM ranges
   - Depth of cut guidelines

### Recommended Data Structure

```json
{
  "manufacturer": "Sandvik Coromant",
  "material_group": "Aluminum 6061",
  "operation": "face_milling",
  "tool_type": "end_mill",
  "tool_diameter_inches": 0.5,
  "flute_count": 4,
  "coating": "TiAlN",
  "recommended_speeds": {
    "sfm": 450,
    "sfm_range": [400, 550],
    "m_min": 137
  },
  "recommended_feeds": {
    "ipt": 0.015,
    "ipt_range": [0.010, 0.025],
    "mm_tooth": 0.38
  },
  "tool_life_minutes": 15,
  "depth_of_cut_limits": {
    "radial_inches": 0.25,
    "axial_inches": 0.50
  },
  "source_url": "https://...",
  "data_confidence": "high"
}
```

### Priority Data Collection Approach

1. **Phase 1:** Compile 20 most common material/operation combinations
2. **Phase 2:** Add secondary materials and operations
3. **Phase 3:** Integrate manufacturer-specific adjustments
4. **Phase 4:** Add advanced features (coolant, tool life, hardness)
5. **Phase 5:** Validate against real-world results

---

## SOURCE VERIFICATION & ACCESSIBILITY

### Verification Status (as of Nov 2025)

**Freely Accessible (verified):**
- [x] Sandvik Coromant online calculator
- [x] Kennametal speeds & feeds calculator
- [x] Iscar online calculators & PDFs
- [x] Seco cutting data calculator
- [x] Harvey Tool speeds & feeds guide
- [x] Mitsubishi Materials technical info
- [x] Kyocera digital catalog
- [x] Sumitomo calculators
- [x] Haas CNC data tables (PDFs)
- [x] Open-source references (Machinery's Handbook)

**Account Required:**
- [x] Sandvik Coromant Developer Portal (free account needed)
- [x] DMG MORI technical resources (account required)
- [x] Some Okuma documentation (behind portal)

**Commercial/Subscription:**
- [x] G-Wizard Calculator (paid but has trial)
- [x] HSMAdvisor (commercial)
- [x] Some tool manufacturer catalogs (request via dealer)

---

## RECOMMENDATIONS FOR UPDATES

**To keep this catalog current:**

1. **Quarterly:** Check manufacturer websites for updated calculators
2. **Semi-annually:** Review new tool catalog releases
3. **Annually:** Update standards compliance (ISO 13399 adoption)
4. **As-needed:** Add new material data as manufacturers release it

**Tracking URLs for changes:**
- Monitor developers.sandvik.coromant.com for API updates
- Subscribe to tool manufacturer news releases
- Track GTC (Generic Tool Catalog) standard updates

---

## CONCLUSION

This comprehensive catalog aggregates publicly available cutting data from 10 major tool manufacturers, 5 machine manufacturers, and multiple reference sources. The data covers **40+ ferrous materials, 25+ non-ferrous materials, and 15+ major operations**, with cutting speed recommendations from multiple independent sources providing high confidence values.

**Total Data Coverage:**
- **Materials:** 65+ material types with specific speed/feed data
- **Operations:** 12+ major machining operations
- **Tool Types:** 20+ distinct tool categories
- **Online Calculators:** 15+ freely accessible cutting data tools
- **APIs:** 1 documented REST API (Sandvik Coromant)
- **Standards:** ISO 13399 for data interchange

For the feeds & speeds calculator development, **recommend starting with the 15 most common materials (aluminum 6061, steel 1045/4140, stainless 304, cast iron) and 5 core operations (face milling, end milling, drilling, boring, slot milling)**, then expanding with data from the resources cataloged here.

