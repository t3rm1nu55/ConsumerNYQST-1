# Comprehensive ISO and ANSI Standards Reference for CNC Machining, Feeds, Speeds, and Tooling

**Document Version:** 1.0
**Last Updated:** November 2025
**Purpose:** Complete reference guide for all relevant ISO and ANSI standards applicable to CNC machining, feeds and speeds calculations, tool life testing, and cutting tool designations.

---

## Table of Contents

1. [Tool Life Testing Standards](#tool-life-testing-standards)
2. [Cutting Tool Designation Standards](#cutting-tool-designation-standards)
3. [Tool Material Classification Standards](#tool-material-classification-standards)
4. [Surface Texture and Roughness Standards](#surface-texture-and-roughness-standards)
5. [Tool Dimension and Geometry Standards](#tool-dimension-and-geometry-standards)
6. [CNC Programming Standards](#cnc-programming-standards)
7. [Related Standards](#related-standards)
8. [Free Resources and Alternatives](#free-resources-and-alternatives)
9. [Implementation Guide for Feeds & Speeds Calculator](#implementation-guide-for-feeds--speeds-calculator)

---

## Tool Life Testing Standards

### ISO 3685:1993 - Tool-Life Testing with Single-Point Turning Tools

**Official Title:** Tool-life testing with single-point turning tools (Second Edition)

**What It Covers:**
- Establishes standardized procedures for testing tool life with high-speed steel (HSS), cemented carbide, and ceramic single-point turning tools
- Covers testing on steel and cast iron workpieces
- Specifies workpiece characteristics, tool specifications, cutting fluid requirements, cutting conditions, equipment, and assessment of tool deterioration
- Applies to both laboratory testing and production practice
- Focuses on tool wear deterioration (not edge fracture or plastic deformation)

**Key Testing Parameters:**
- Tool life criteria: average flank wear < 0.3 mm, maximum flank wear < 0.6 mm, crater depth < 0.14 mm
- Requires constant cutting speed testing until complete tool wear
- Defines procedures for recording and evaluating results

**Relevance to Feeds & Speeds Calculator:**
- Provides the foundation for understanding tool life relationships with cutting speed
- Essential for calculating optimal speeds based on desired tool life (e.g., 15-minute, 30-minute, 60-minute tool life)
- Enables correlation between cutting parameters and actual tool performance
- Supports development of cutting speed recommendations for different materials

**Public Availability:**
- **NOT free** - Must be purchased from ISO, ANSI, or other standards organizations
- Available through: ANSI Webstore (webstore.ansi.org), ISO Store, IHS Global
- Price typically $80-150 USD

**Alternative Free Resources:**
- Academic papers on ResearchGate that cite and explain ISO 3685 methodology
- Michigan State University cutting tool technology resources (egr.msu.edu)
- Machinery's Handbook sections on tool life principles
- Academic textbooks: "Metal Cutting Theory and Practice" by Stephenson and Agapiou
- SME (Society of Manufacturing Engineers) educational guides

---

### ISO 8688-1:1989 and ISO 8688-2:1989 - Tool Life Testing in Milling

**Official Titles:**
- Part 1: Face milling
- Part 2: End milling

**What It Covers:**
- Specifies recommended procedures for tool-life testing with cemented carbide tools (Part 1: face milling)
- Covers high-speed steel tools for end milling operations (Part 2: end milling)
- Testing on steel and cast iron workpieces
- Establishes specifications for: workpiece, tool, cutting fluid, cutting conditions, equipment, assessment of tool deterioration
- Applicable to laboratory and production practice
- Focuses on wear-dominated tool deterioration

**Relevance to Feeds & Speeds Calculator:**
- Extends tool life testing methodology to milling operations (beyond turning)
- Provides foundation for milling speed recommendations
- Enables comparison between face milling and end milling performance
- Last reviewed and confirmed in 2022 (still current standard)

**Public Availability:**
- **NOT free** - Requires purchase
- Available through standards organizations (ISO, ANSI, CSA Group, etc.)

**Alternative Free Resources:**
- Manufacturing textbooks covering milling tool life
- Tool manufacturer technical documentation
- Academic research papers on milling tool life

---

## Cutting Tool Designation Standards

### ISO 1832:2017 - Indexable Inserts for Cutting Tools — Designation

**Official Title:** Indexable inserts for cutting tools — Designation (updated 2017, replaces 2012 and 1991 editions)

**What It Covers:**
- Establishes universal code system for designating indexable carbide, ceramic, and other hard material inserts
- Provides 13-character designation system describing:
  - **Design Group (4 symbols):** Shape, relief angle, tolerance class, chipbreaker/fixing method
  - **Dimensions Group (3 symbols):** Size, thickness, corner radius
  - Plus additional optional symbols for edge condition, cutting direction, and manufacturer identification
- Covers turning inserts, milling inserts, threading inserts, and specialty applications
- Specifies inserts for cubic boron nitride (BL, BH, BC) and polycrystalline diamond (DP)
- Does NOT specify grades, coatings, or chipbreaker geometries (these vary by manufacturer)

**Designation System Example:**
```
C N M G 1 2 0 4 08-T308
│ │ │ │ │ │ │ │ │
│ │ │ │ │ │ │ │ └─ Manufacturer symbol
│ │ │ │ │ │ │ └───── Wiper/tipped length code
│ │ │ │ │ │ └─────── Nose radius (0.8 mm)
│ │ │ │ │ └───────── Thickness (3.18 mm)
│ │ │ │ └─────────── Size/inscribed circle (12.7 mm)
│ │ │ └───────────── Chipbreaker/fixing method
│ │ └─────────────── Tolerance class
│ └───────────────── Relief angle (5°)
└─────────────────── Shape (Rhombus 80°)
```

**Relevance to Feeds & Speeds Calculator:**
- Critical for identifying what insert geometry is being used in calculations
- Shape code determines effective feed per tooth values
- Relief and nose angle affect cutting forces and speed capabilities
- Size code correlates to insert capacity for different material removal rates
- Thickness impacts rigidity and maximum speeds

**Public Availability:**
- **NOT free** - Requires purchase from ISO or ANSI
- Available through: ANSI Webstore, ISO Store

**Alternative Free Resources:**
- **Walter Tools PDF:** Free designation key chart (walter-tools.com)
- **Carbide Depot:** Free insert designation chart (carbidedepot.com)
- **Seco Tools:** Free ISO insert designation explanation (secotools.com)
- **LittleMachineShop.com:** Free ANSI/ISO insert charts
- **Cutwel Ltd:** Free complete guide to ISO code system (cutwel.co.uk)
- **Travers Tool:** Free insert identification chart (travers.com)
- Manufacturer datasheets (Iscar, Mitsubishi, Sandvik Coromant, etc.)

---

## Tool Material Classification Standards

### ISO 513:2012 - Classification and Application of Hard Cutting Materials

**Official Title:** Classification and application of hard cutting materials for metal removal with defined cutting edges — Designation of the main groups and groups of application (Fourth Edition, 2012; replaces 2004 edition)

**What It Covers:**
- Specifies classification system for all hard cutting materials used in machining:
  - Hardmetals (Tungsten Carbide)
  - Ceramics
  - Diamond
  - Cubic Boron Nitride (CBN)
- Establishes six main application groups based on workpiece material being machined
- Each main group divided into sub-application groups with specific wear resistance/toughness tradeoffs
- Color coding system for quick identification (see below)
- Based on application and performance characteristics, not specific manufacturers' grades

**Main Material Groups and Color Codes:**

| Code | Color  | Workpiece Material | Characteristics |
|------|--------|-------------------|-----------------|
| **P** | Blue   | Steel | Largest group; unalloyed to high-alloyed steels, steel castings, ferritic/martensitic stainless steels. Long chip materials with moderate wear. |
| **M** | Yellow | Stainless Steel (Austenitic) | 12%+ chromium stainless steels. Sticky materials that create built-up edge and work-hardening. Require balanced toughness/wear resistance. |
| **K** | Red    | Cast Iron | Gray, malleable, nodular, and austempered cast irons. Abrasive due to SiC content. Generate short chips. Hard materials. |
| **N** | Green  | Non-Ferrous | Aluminum, copper, brass, etc. Soft, non-ferrous metals. Generally easy to machine, allow high speeds and long tool life. |
| **S** | Brown  | Superalloys & Heat-Resistant | Nickel, cobalt, and titanium-based alloys. Very difficult to machine; sticky, work-harden, generate extreme heat. |
| **H** | White  | Hardened Materials | Hardened steels (45-65 HRC) and chilled cast iron (400-600 HB). Extremely abrasive, generate intense heat. |

**Subdivision System:**
- Each main group (P, M, K, N, S, H) is subdivided into application groups (e.g., P01, P10, P20, P25, etc.)
- Numbers indicate relative wear resistance and toughness:
  - Lower numbers (01, 10, 20): Higher wear resistance, lower toughness (finishing)
  - Higher numbers (30, 40, 50): Lower wear resistance, higher toughness (roughing)

**Relevance to Feeds & Speeds Calculator:**
- **CRITICAL for speed selection:** Different material groups require different cutting speeds
- Steel (P) typically allows moderate speeds with emphasis on tool life
- Non-ferrous (N) allows much higher speeds
- Superalloys (S) and hardened materials (H) require very conservative speeds
- Sub-group classification affects optimal feed and speed selection
- Understanding workpiece machinability rating depends on ISO material group

**Public Availability:**
- **NOT free** - Requires purchase
- Available through: ISO Store, ANSI Webstore, DIN Media
- Current version is ISO 513:2012

**Alternative Free Resources:**
- **ISO 513:2004 PDF sample** available at cdn.standards.iteh.ai (older edition, but content similar)
- **FM Carbide:** Free ISO material group page (fmcarbide.com)
- **Machining Doctor:** Free machinability and material groups guide (machiningdoctor.com)
- **Sandvik Coromant:** Free workpiece materials guide (sandvik.coromant.com)
- **Mitsubishi Materials:** Free material classification guides (mmc-carbide.com)
- **Iscar:** Free material grades table (iscar.com)
- **CNC Lathing:** Free workpiece material guide and ISO classification chart (cnclathing.com)
- Coban Engineering: Material groups and machinability info (cobanengineering.com)

---

### Machinability Index and Material Classification Concepts (Not a single standard)

**Key Concept:**
Machinability index uses B1112 free-cutting steel as reference (100% rating) and rates all materials relative to it.

**Index Formula:**
```
Machinability Index = (Vt / Vs) × 100
where:
  Vt = cutting speed of subject material for 1-minute tool life
  Vs = cutting speed of B1112 steel for 1-minute tool life (reference)
```

**Material Machinability Ranges:**
- Superalloys (Waspalloy, Inconel 718): 8-15% (extremely difficult)
- Hardened steels (45-65 HRC): 15-25% (very difficult)
- Stainless steels: 20-50% (difficult)
- Steel castings: 30-60% (difficult)
- Plain carbon steels: 40-100% (easy to moderate)
- Aluminum alloys: 200-400% (very easy)

**Application to Feeds & Speeds:**
- If material has 70% machinability, reduce standard speeds by 30%
- Used to scale cutting speeds from reference material recommendations
- Particularly useful for materials without direct ISO 513 sub-group data

---

## Surface Texture and Roughness Standards

### ISO 4287:1997 and ISO 4288:1996 - Surface Texture Measurement

**Official Titles:**
- ISO 4287:1997 - Surface texture: Profile method — Terms, definitions and surface texture parameters
- ISO 4288:1996 - Surface texture: Profile method — Rules and procedures for the assessment of surface texture

**What They Cover:**

**ISO 4287:**
- Defines terminology and parameters for surface roughness and texture
- Establishes measurement methodology using stylus instruments
- Defines "R" parameters (roughness parameters):
  - **Ra:** Arithmetic mean roughness (average deviation)
  - **Rq:** Root mean square roughness
  - **Rz:** Maximum height (peak to valley)
  - **Rt:** Total height
  - And many others (Rp, Rv, Rc, etc.)
- Specifies primary profile and roughness profile measurement

**ISO 4288:**
- Specifies rules for comparison of measured values with tolerance limits
- Defines default rules for cut-off wavelength (λc) selection based on surface texture
- Specifies evaluation length and calculation procedures
- Default calculation number: 5 (evaluates over 5 sampling lengths)
- Establishes roughness profile parameter ranges

**Current Status:**
- **IMPORTANT:** ISO 1302, 4287, 4288, 12085, 13565-2, and 13565-3 have been **withdrawn**
- **Replaced by:** ISO 21920 series standards (newer specification)
- Some calculation changes for key parameters in ISO 21920
- However, ISO 4287/4288 still widely used in manufacturing practice

**Relevance to Feeds & Speeds Calculator:**
- Determines acceptable surface finishes achievable with different feeds/speeds
- Higher speeds with lower feeds → finer finishes (lower Ra)
- Lower speeds with higher feeds → rougher finishes (higher Ra)
- Tool geometry and edge condition directly affect achievable roughness
- Material and insert coating affect achievable surface finish
- Can estimate roughness based on feed rate and nose radius: Ra ≈ (Feed²)/(8 × Nose Radius)

**Public Availability:**
- **NOT free** - Requires purchase from ISO
- Available through: ISO Store, ANSI Webstore
- Note: Older editions may be available through universities or technical libraries

**Alternative Free Resources:**
- **NPL (National Physical Laboratory) UK:** Free PDF specification (resource.npl.co.uk)
- **Digital Surf:** Free ISO 4287 parameters guide (guide.digitalsurf.com)
- **Engineers Edge:** Free ISO surface roughness symbols and terminology (engineersedge.com)
- **Polytec:** Free surface parameter fundamentals guide (polytec.com)
- **Willrich:** Free surface roughness parameters PDF (willrich.com)
- Machinery's Handbook sections on surface finish
- Manufacturer cutting data sheets (commonly list achievable Ra values)

---

## Tool Dimension and Geometry Standards

### ANSI/ASME B94.11M-1993 - Twist Drills (Jobber Length)

**Official Title:** Twist Drills — Nomenclature, Definitions, Sizes and Tolerances

**What It Covers:**
- Specifies dimensions and tolerances for straight and taper shank jobber-length twist drills
- Covers high-speed steel (HSS) drill bit sizing from 1/64" through 1" in 1/64" increments
- Establishes standard drill flute lengths, overall lengths, and point geometry
- Specifies drill point angles (typically 118° included angle)
- Defines clearance angles, helix angles, and margin specifications
- Includes standard drill sizes in fractional and metric dimensions

**Key Drill Geometry Features:**
- **Point Angle:** 118° for general-purpose drilling
- **Helix Angle:** ~30° (varies slightly by manufacturer)
- **Relief/Clearance Angle:** 6-15° (primary relief)
- **Margin:** Provides guidance on cutting surface

**Relevance to Feeds & Speeds Calculator:**
- Drill size directly affects maximum speed and feed recommendations
- Smaller drills (<1/8") require higher RPMs but lower feeds
- Larger drills require lower RPMs but higher feed rates
- Point geometry affects feed rate recommendations
- Different drill types (split point, parabolic) modify speed/feed recommendations

**Public Availability:**
- **NOT free** - Must be purchased from ASME/ANSI Webstore
- Current version: ASME B94.11M-1993

**Alternative Free Resources:**
- **CustomPartNet:** Free drill size reference chart (custompartnet.com)
- **Engineers Edge:** Free machinist drill bit size tables (engineersedge.com)
- **Mechanical Engineering:** Free inch and metric drill size charts (mechanical-engineering.com)
- **CNC Lathing:** Free drill bit and tap size lists (cnclathing.com)
- **Wikipedia:** Drill bit sizes article (en.wikipedia.org/wiki/Drill_bit_sizes)
- Drill manufacturer specification sheets (widely available)
- Machinery's Handbook drill tables

---

### ASME B94.19-1997 (R2019) - Milling Cutters and End Mills

**Official Title:** Milling Cutters and End Mills — Nomenclature, Definitions, Sizes and Tolerances

**What It Covers:**
- Establishes dimensions and tolerances for high-speed steel end mills and milling cutters
- Covers one-piece construction cutters (not cartridge inserts)
- Specifies:
  - Overall length and flute length
  - Cutting diameter
  - Shank size and type (straight, taper, etc.)
  - Number of flutes
  - Helix angle specifications
  - Tolerance classes

**Relevance to Feeds & Speeds Calculator:**
- Establishes standard dimensions for end mill selection
- Flute count affects feed rate recommendations (feeds per tooth × number of flutes = feed per revolution)
- Cutter diameter affects maximum speed recommendations
- Helix angle influences chip evacuation and feed capability
- Larger diameter cutters generally require lower RPMs
- More flutes allow higher feed rates at same surface speed

**Public Availability:**
- **NOT free** - Must be purchased from ASME Webstore
- Current version: ASME B94.19-1997 (R2019)

**Alternative Free Resources:**
- Tool manufacturer catalogs and spec sheets (readily available)
- Machinery's Handbook end mill tables
- CNC reference materials
- Tool distributor specification sheets

---

### ANSI B94.50-1975 (R2003) - Basic Nomenclature for Single-Point Cutting Tools

**Official Title:** Basic Nomenclature and Definitions for Single-Point Cutting Tools

**What It Covers:**
- Establishes standardized terminology for single-point tool geometry
- Defines cutting edges, faces, flanks, and their reference systems
- Specifies tool angles and their measurement procedures:
  - **Back rake angle (γb):** Angle from horizontal
  - **Side rake angle (γs):** Angle from horizontal on side
  - **Back clearance angle (αb):** Relief angle at back
  - **Side clearance angle (αs):** Relief angle on side
  - **End cutting edge angle (ψe):** Lead angle
  - **Side cutting edge angle (λs):** Approach angle
- Applies to HSS turning tools, boring bars, and single-point tools

**Relevance to Feeds & Speeds Calculator:**
- Establishes standard angle references used in tool geometry specification
- Positive vs. negative rake angles significantly affect cutting forces and speeds
- Tool holders and inserts reference these standardized angles
- Crater angle and nose radius are key to surface finish prediction
- Tool angles determine chip formation and cutting temperatures

**Public Availability:**
- **NOT free** - Requires purchase from ASME Webstore
- Currently ANSI/ASME B94.50-1975 (R2003 reaffirmed)

**Alternative Free Resources:**
- **SpringerLink:** Free chapter "Basic Definitions and Cutting Tool Geometry" from academic text
- CSME technical documents
- Academic textbooks on cutting tool design
- Tool manufacturer specification sheets

---

## CNC Programming Standards

### ISO 6983-1 (RS-274D) - G-Code Programming for CNC Machines

**Official Title:** Numerical control of machines — Program format and definition of address words (Also known as RS-274D or G-Code)

**What It Covers:**
- Establishes standardized G-code format for programming CNC machines
- Defines G-codes (preparatory functions) and M-codes (miscellaneous functions)
- Specifies block structure with words containing address and numeric values
- Examples of key codes:
  - **G00:** Rapid positioning (traverse)
  - **G01:** Linear interpolation (cutting feed)
  - **G02/G03:** Circular interpolation (arc milling)
  - **G21/G20:** Metric/Inch mode selection
  - **M03/M05:** Spindle on/off
  - **M08/M09:** Coolant on/off
  - **F:** Feed rate in units/minute
  - **S:** Spindle speed (RPM)
- Originally developed by EIA in 1960s, standardized as ISO 6983 in 1982

**Current Status:**
- Still the dominant standard for CNC programming
- Most machines programmed in ISO 6983 format
- Limitations: focuses on tool center path rather than machining process description
- Low-level "how-to" instructions rather than process definition

**Relevance to Feeds & Speeds Calculator:**
- Speeds and feeds entered directly into G-code as S (spindle speed) and F (feed rate) values
- F values can be per-minute (inches/minute or mm/minute) or per-tooth (chip load)
- Must account for number of flutes to convert between per-minute and per-tooth rates
- Tool offsets in ISO 6983 enable compensation for different tool dimensions
- CNC machine must execute calculated speed/feed values accurately

**Public Availability:**
- **NOT free officially** - ISO standard requires purchase
- **However:** G-code reference widely available in practice through:
  - CNC machine manuals (provide subset relevant to specific machine)
  - Open source implementations
  - Educational materials

**Alternative Free Resources:**
- **Wikipedia:** Comprehensive G-code article (en.wikipedia.org/wiki/G-code)
- **GCode Tutor:** RS-274 G-code reference and history (gcodetutor.com)
- **CNC Machine Python:** Comprehensive G-code reference documentation
- CNC machine manuals (manufacturer-provided)
- CAM software documentation
- Online CNC forums and communities

---

## Related Standards

### ISO 4957:2018 - Tool Steels

**Official Title:** Tool Steels — Types and Classification

**What It Covers:**
- Classification of tool steel grades (H13, A2, D2, O1, etc.)
- Properties including hardness, toughness, wear resistance
- Heat treatment specifications
- Thermal fatigue resistance for hot-work applications
- Tool life characteristics for different steel grades

**Relevance to Feeds & Speeds Calculator:**
- Identifies material properties of tool steel used in tool construction
- H13 commonly used in hot-work applications
- Affects tool capability and maximum recommended speeds
- Tool steel hardness determines cutting forces and thermal stress

**Public Availability:**
- NOT free - Available from ISO Store

**Alternative Free Resources:**
- Tool steel manufacturers' datasheets
- Wikipedia tool steel article
- ASTM equivalent specifications (A681 for tool steels)

---

### ISO 9013:2017 - Thermal Cutting

**Official Title:** Thermal cutting — Classification of thermal cuts — Geometrical product specification and quality tolerances

**What It Covers:**
- Specifications for oxyfuel flame cutting, plasma cutting, and laser cutting
- Quality tolerances and edge condition classifications
- Surface roughness specifications from thermal cutting

**Relevance to Feeds & Speeds Calculator:**
- Provides context for edge finish specifications after machining
- Thermal cutting often precedes CNC finishing operations
- Relevant for understanding post-cutting surface quality targets

---

### ISO 230-3:2007 - Machine Tool Testing

**Official Title:** Test code for machine tools — Part 3: Determination of thermal effects

**What It Covers:**
- Testing procedures for thermal effects on machine tools
- Machine spindle thermal distortion
- Linear axis thermal effects
- Rotary component thermal effects
- Environmental temperature variation effects

**Relevance to Feeds & Speeds Calculator:**
- High spindle speeds generate heat affecting tool accuracy
- Machine thermal growth affects dimensional accuracy
- Cutting temperature affects workpiece dimensional stability
- Important for high-precision finishing operations

---

## Free Resources and Alternatives

### High-Quality Free References for Feeds and Speeds

#### 1. **Machinery's Handbook (31st Edition)**

**What It Is:** Comprehensive manufacturing reference with extensive feeds and speeds tables

**Coverage:**
- Chapters 111-120 cover speeds, feeds, and machining power
- Tables for turning, milling, drilling, threading
- Data for ferrous and non-ferrous materials
- Organized by material type and tool material
- Based on lab testing and shop experience

**Availability:**
- Full handbook available for purchase (~$100)
- Some sections available as free PDF samples online
- Companion guide available (31st Edition Guide, ~$50)
- Digital version with interactive links available

**Strengths:**
- Authoritative, widely respected
- Practical data from actual production experience
- Comprehensive material coverage
- Multiple operation types covered

**Limitations:**
- Dated in some areas (CNC-specific recommendations limited)
- Requires purchase for full access
- Heavier on traditional machining than CNC-specific

**Free Access Method:**
- University library access (if available)
- Some sections posted online legally
- 27th edition samples available at theswissbay.ch

---

#### 2. **CNC Cookbook Free Resources**

**What It Is:** Online CNC machining education platform with free tutorials

**Coverage:**
- "CNC Feeds and Speeds Cookbook" - comprehensive PDF tutorial
- Feeds and speeds calculation formulas
- Material-specific recommendations
- Practical examples and scenarios
- Updated for 2024

**Availability:**
- Free PDF download at cnccookbook.com
- Website articles on feeds and speeds theory
- Speed and feed calculator tools (web-based)
- Feeds and speeds guide (The Ultimate Guide, Updated for 2024)

**Strengths:**
- CNC-focused (more relevant than traditional references)
- Free and regularly updated
- Practical examples
- Online tools for quick calculations

---

#### 3. **Manufacturer Technical Documentation**

**Free Sources:**
- **Haas CNC:** Comprehensive feeds and speeds documentation for all operations (haascnc.com)
  - End mills, drills, threading tools
  - Both metric and imperial units
  - Material-specific recommendations
  - Free PDF downloads

- **Sandvik Coromant:** Extensive cutting data and formulas (sandvik.coromant.com)
  - Milling formulas and definitions
  - Workpiece material guides
  - Cutting speed recommendations
  - Free web-based tools

- **Iscar:** Grade charts and material classification tables (iscar.com)
  - Free ISO 513 material group charts
  - Grade selection guides
  - Recommended cutting data by material

- **Mitsubishi Materials:** Cutting data and insert selection guides (mmc-carbide.com)
  - Material classification courses
  - Insert geometry information
  - Recommended speeds and feeds

- **Dormer Pramet:** Cutting data selection guidance (dormerpramet.com)
  - How to find and use cutting data
  - Material group recommendations
  - Free technical guides

- **Seco Tools:** ISO insert designation system information (secotools.com)
  - Insert code explanations
  - Material group classification

- **Carbide Depot:** Free insert designation charts (carbidedepot.com)
  - ISO and ANSI designation systems
  - PMK grade range charts
  - Convert between systems

---

#### 4. **Academic Resources**

**Free University Resources:**

- **Michigan State University:** Cutting Tool Technology course materials (egr.msu.edu)
  - Comprehensive PDF on tool life, materials, geometry
  - Lab testing data
  - Academic treatment of standards

- **University of Florida:** Manufacturing speeds and feeds (mae.ufl.edu)
  - Academic treatment of feed rate and speed selection
  - Material recommendations
  - Machining formulas and theory

- **Open Oregon:** Manufacturing Processes 4-5 textbook (openoregon.pressbooks.pub)
  - Free educational content
  - Feed rate specifications
  - Cutting speed recommendations
  - Material recommendations by type

- **SME (Society of Manufacturing Engineers):** Educational guides
  - "Cutting Tool Design Fundamentals" study guide (PDF available)
  - Standards references and explanations

- **ResearchGate:** Academic papers on tool life and cutting parameters
  - Direct access to cutting tool research
  - Tool life equation explanations
  - Material-specific cutting data studies

---

#### 5. **Wikipedia and Free Encyclopedic References**

- **Speeds and Feeds:** en.wikipedia.org/wiki/Speeds_and_feeds
  - Comprehensive explanation of concepts
  - Historical context
  - Material recommendations
  - Calculation methods

- **Machinability:** en.wikipedia.org/wiki/Machinability
  - Machinability index definition and use
  - Material ratings
  - Factors affecting machinability

- **Drill Bit Sizes:** en.wikipedia.org/wiki/Drill_bit_sizes
  - Standard drill sizes
  - ANSI and ISO specifications
  - Tolerance information

- **G-code:** en.wikipedia.org/wiki/G-code
  - G-code history and development
  - G-code and M-code references
  - Standard format information

---

#### 6. **Government and Standards Body Resources**

- **Indian DVET:** "Specification for Cutting Tools" document
  - Free PDF available from Indian government education
  - Comprehensive cutting tool specifications
  - References to ANSI and ISO standards

- **Internet Archive (archive.org):** ISO Standards Collection
  - Some older ISO standards available
  - Uncertain completeness of collection

- **ITEH Standards Database (cdn.standards.iteh.ai):** Sample PDFs
  - Free sample pages from various ISO and ISO-equivalent standards
  - Not complete standards, but useful summaries
  - Examples: ISO 513 samples, ISO 4288 samples available

---

### Materials and Machinability Information

**Free Online Tools and References:**

- **Machining Doctor** (machiningdoctor.com)
  - ISO material classification guide
  - Machinability ratings by material
  - Material-specific cutting data
  - Grade selection tools

- **CNC Lathing** (cnclathing.com)
  - Workpiece material guide with ISO classifications
  - Machinability charts
  - Drill and tap size lists
  - Material recommendations

- **Engineers Edge** (engineersedge.com)
  - Extensive manufacturing reference database
  - Drill sizes and tolerances
  - Tap drill charts
  - Screw thread information
  - Surface roughness symbols

- **Practical Machinist Forums** (practicalmachinist.com)
  - Community knowledge and experience
  - Material-specific cutting data from practitioners
  - Problem-solving discussions

- **The Hobby Machinist Forums** (hobby-machinist.com)
  - Practical speeds and feeds discussions
  - Real-world machining experience
  - Material recommendations

---

## Implementation Guide for Feeds & Speeds Calculator

### Data Points From Standards to Include

#### From ISO 3685 (Tool Life Testing):
1. **Tool life reference speed** - Cutting speed for specific tool life (e.g., 15, 30, 60-minute life)
2. **Taylor's exponent (n)** - How tool life varies with speed:
   - HSS: n = 0.08 to 0.2
   - Cemented carbide (uncoated): n = 0.2 to 0.4
   - Coated carbide: n = 0.35 to 0.4
   - Ceramics: n = 0.5 to 0.7

3. **Tool life criterion** - Flank wear limits and crater depth limits
4. **Speed adjustment factors** - For different tool materials and conditions

#### From ISO 513 (Material Classification):
1. **Material group** (P, M, K, N, S, H)
2. **Workpiece material specific speed adjustment** - Speed modifications within same group
3. **Machinability index** - For speed scaling across materials
4. **Material hardness ranges** - HRC or HB values affecting speed selection

#### From ISO 1832 (Insert Designation):
1. **Insert shape code** - Determines cutting edges and load distribution
2. **Nose radius** - Affects surface finish: Ra ≈ (Feed²)/(8 × R)
3. **Clearance angle** - Affects tool performance and speed limits
4. **Edge condition** - Sharp vs. honed vs. rounded affects speeds/feeds

#### From Machining Handbooks:
1. **Base cutting speeds** for standard operations:
   - Turning: speeds by material group
   - Milling: speeds by tool type (end mills, face mills, slot drills)
   - Drilling: speeds by drill size and material

2. **Feed rate recommendations**:
   - Per tooth (chip load) for each operation type
   - Per revolution guidelines
   - Per minute guidelines for manual machines

3. **Adjustment factors for:**
   - Tool material (HSS vs carbide)
   - Coating presence and type
   - Tool condition (new vs dull)
   - Coolant effectiveness
   - Machine rigidity
   - Surface finish requirements

#### From ISO 4287/4288 (Surface Texture):
1. **Surface roughness (Ra)** achievable with different feeds
2. **Relationship:** Ra ≈ (Feed per tooth²)/(8 × Nose radius)
3. **Finish thresholds** for different applications

### Key Calculation Formulas to Implement

**1. Spindle Speed (RPM) from Cutting Speed:**
```
RPM = (Cutting Speed in SFM × 12) / (π × Diameter in inches)
or
RPM = (Cutting Speed in m/min × 1000) / (π × Diameter in mm)
```

**2. Feed Rate from Feed per Tooth (Chip Load):**
```
Feed Rate (IPM) = Feed per Tooth × Number of Teeth × RPM
or
Feed Rate (mm/min) = Feed per Tooth × Number of Teeth × RPM
```

**3. Tool Life Adjustment with Taylor's Equation:**
```
V1 × T1^n = V2 × T2^n
where:
  V = cutting speed
  T = tool life
  n = Taylor's exponent (material dependent)

Solving for V2 (new speed for different tool life):
V2 = V1 × (T1/T2)^(n)
```

**4. Estimated Surface Roughness (Ra) from Feed:**
```
Ra (µin) = (Feed per tooth)² / (8 × Nose radius)
Convert: 1 µm = 0.0394 µin
```

**5. Machinability-based Speed Adjustment:**
```
Adjusted Speed = Reference Speed × (Material Machinability % / 100)
```

**6. Material-Specific Speed Modification:**
```
Final Speed = Base Speed × (Material Group Factor) × (Hardness Factor) × (Condition Factor)
```

### Reference Data Tables to Build

**Table 1: Base Cutting Speeds by Material Group (ISO 513)**
- Speeds in SFM and m/min
- By tool material (HSS, Carbide-Uncoated, Carbide-Coated, Ceramic)
- By operation (Turning, Face Milling, End Milling, Drilling)

**Table 2: Feed per Tooth (Chip Load) by Operation**
- End Mills: 0.001-0.010 IPT (inches per tooth) typical
- Face Mills: 0.003-0.015 IPT
- Drills: 0.002-0.008 IPT
- Single-point tools: 0.005-0.015 IPR (inches per revolution)

**Table 3: Material Machinability Index**
- Reference materials (B1112 steel = 100%)
- Common materials with index values
- Speed adjustment multipliers

**Table 4: Tool Coating Performance Factors**
- Uncoated carbide baseline
- TiN coating factor (typically 1.2-1.5×)
- TiAlN coating factor (typically 1.5-2.0×)
- Multi-layer coatings

**Table 5: Surface Finish Achievable (Ra in µm)**
- By operation
- By feed rate
- By tool geometry
- By material group

### Standards Compliance Checklist

For calculator to be compliant with referenced standards:

**ISO 3685 Compliance:**
- [ ] Include tool life selection (e.g., 15, 30, 60-minute options)
- [ ] Apply Taylor's equation exponent appropriate to tool material
- [ ] Show speed adjustment for different tool life targets
- [ ] Include tool wear criteria reference

**ISO 513 Compliance:**
- [ ] Identify workpiece material group (P, M, K, N, S, H)
- [ ] Apply group-specific speed adjustment factors
- [ ] Display selected material group with color code
- [ ] Note speed reduction for harder materials within group

**ISO 1832 Compliance:**
- [ ] Allow insert designation input (or simplified form)
- [ ] Use nose radius from insert code for finish prediction
- [ ] Account for edge condition (sharp, honed, etc.)
- [ ] Consider insert shape for optimal feed rates

**ISO 4287/4288 Compliance:**
- [ ] Predict achievable surface roughness (Ra) from feeds
- [ ] Show relationship between feed and finish
- [ ] Provide roughness recommendations by application
- [ ] Reference cutting speed impact on finish

**ANSI B94.11M and ASME B94.19 Compliance:**
- [ ] Support standard tool sizes (drills, end mills)
- [ ] Account for flute count in feed calculations
- [ ] Include standard drill and tool dimensions
- [ ] Apply size-appropriate speed limits

---

## Summary: Critical Standards for Feeds & Speeds Calculator

### Top 5 Priority Standards

**1. ISO 3685 (Tool-Life Testing with Single-Point Turning Tools)** ⭐⭐⭐
- **Why:** Foundation for understanding cutting speed relationships
- **Impact:** Enables tool life-based speed calculations
- **Use:** Taylor's equation coefficients, tool life criteria
- **Alternative:** Academic papers on tool life, Machinery's Handbook

**2. ISO 513 (Classification of Hard Cutting Materials)** ⭐⭐⭐
- **Why:** Establishes material classification framework (P, M, K, N, S, H)
- **Impact:** Drives speed selection by workpiece material group
- **Use:** Material group identification, speed adjustment factors
- **Alternative:** Manufacturer datasheet materials guide (Haas, Iscar, Sandvik)

**3. ISO 1832 (Indexable Insert Designation)** ⭐⭐⭐
- **Why:** Defines insert geometry and capabilities
- **Impact:** Determines feed per tooth, surface finish capability
- **Use:** Insert shape, nose radius, edge condition
- **Alternative:** Carbide Depot, Walter Tools, Seco Tools free charts

**4. ISO 4287/4288 (Surface Texture)** ⭐⭐
- **Why:** Relates feeds to achievable surface finish
- **Impact:** Enables surface finish predictions
- **Use:** Feed-to-roughness conversion formulas
- **Alternative:** NPL free specification, manufacturer data

**5. ANSI/ASME B94.11M & B94.19 (Tool Dimensions)** ⭐⭐
- **Why:** Establishes standard tool sizes and limits
- **Impact:** Size-dependent speed and feed recommendations
- **Use:** Drill and end mill size databases
- **Alternative:** Manufacturer catalogs, CustomPartNet, Engineers Edge

### Critical Data Points by Standard

| Standard | Key Data | Calculator Use | Fallback Resource |
|----------|----------|-----------------|-------------------|
| ISO 3685 | Taylor coefficients (n, C) | Speed adjustment for tool life | Academic papers, handbooks |
| ISO 513 | Material groups (P,M,K,N,S,H) | Base speed selection | Manufacturer guides |
| ISO 1832 | Insert geometry, nose radius | Feed/finish calculation | Free download charts |
| ISO 4287/4288 | Ra vs feed relationship | Surface finish prediction | NPL free spec |
| B94.11M/B94.19 | Tool dimensions & limits | Size-based adjustments | Manufacturer specs |
| ISO 8688 | Milling tool life procedures | Milling speed validation | Academic references |
| Handbooks | Empirical speed/feed tables | Base values by material | Web references listed |

### Building Without Paid Standards (Fully Feasible)

**Good News:** A fully functional feeds & speeds calculator can be built using only free resources:

1. **Speed baseline data:** CNC Cookbook, Haas, Sandvik, Iscar (free downloadable charts)
2. **Material classifications:** Machining Doctor, Sandvik material guides, Iscar charts (free)
3. **Insert specifications:** Walter Tools, Carbide Depot, Seco Tools free charts (free)
4. **Taylor coefficients:** Academic papers on ResearchGate, university materials (free)
5. **Surface finish formulas:** Digital Surf guide, willrich.com, polynomial relationships (free)
6. **Tool dimensions:** CustomPartNet, Engineers Edge, manufacturer specs (free)

**Approach:**
- Cross-reference free academic sources with manufacturer data
- Use open-source datasets and community knowledge
- Verify calculations against Machinery's Handbook values where possible
- Include uncertainty ranges since data varies by specific tool/manufacturer

---

## Accessing Standards: Purchase Options

### Where to Buy Full Standards

**1. Official ISO Store**
- Website: iso.org
- Prices: $150-300 per standard (typical)
- Delivery: PDF (electronic) or paper
- Format: Authoritative, complete

**2. ANSI Webstore**
- Website: webstore.ansi.org
- Prices: Similar to ISO
- Coverage: Both ANSI and ISO standards
- Format: PDF or paper

**3. Document Center Inc.**
- Website: document-center.com
- Prices: Competitive with official sources
- Format: PDF or paper, various search options

**4. IHS Global (now part of S&P Global)**
- Website: global.ihs.com
- Specialization: Standards aggregator
- Prices: Subscription or individual purchase

**5. Technical Library/University Access**
- Cost: Free if enrolled/employed
- Resources: Full standard access via institutional subscription
- Recommendation: Check your local university library

**6. Professional Organization Memberships**
- ASME: Includes access to some standards
- SME: Engineering society with technical resources
- Cost: Varies, but may provide standards access benefit

---

## Final Recommendations

### For CNC Feeds & Speeds Calculator Development

1. **Core functionality can be implemented using free resources** - The standards provide theoretical foundation, but practical implementation uses manufacturer data and empirical relationships

2. **Reference the standards in documentation** - Even if not directly purchased, cite them as the authoritative basis for calculations (e.g., "Based on ISO 513 material groups," "Taylor's tool life equation from ISO 3685")

3. **Build data aggregation from free sources:**
   - Haas CNC feeds and speeds tables
   - Sandvik Coromant cutting data
   - Iscar material grades
   - Machining Doctor material classifications
   - Machinery's Handbook formulas

4. **Validate against multiple sources** - Cross-check calculations against Machinery's Handbook, CNC Cookbook, and multiple manufacturer datasheets

5. **Include standard references in documentation** - Users will understand results better with "Based on ISO 513 material classifications" annotations

6. **Consider purchasing ISO 513, ISO 1832, and ISO 3685** if detailed accuracy is critical - These three standards provide the most direct value to the calculator

7. **Plan for updates** - Standards and tool technology evolve; plan to update reference data regularly (annually recommended)

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | November 2025 | Research Team | Initial comprehensive compilation of CNC/machining standards with focus on feeds, speeds, and tooling |

---

*This document is intended as a comprehensive reference for understanding the ISO and ANSI standards applicable to CNC machining, feeds and speeds calculations, and cutting tool selection. It combines information from official standard summaries, manufacturer documentation, academic resources, and practical machining references. Information is current as of November 2025.*

