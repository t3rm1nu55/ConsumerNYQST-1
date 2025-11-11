# Deterministic Data Sources - Government & Official Statistics

**Collection Date:** 2025-11-11
**Primary File:** `01_government_data.py`
**Output Files:**
- `government_data_kb.json` (47KB) - Structured knowledge base
- `government_data_provenance.md` (12KB) - Full provenance report

## Collection Summary

This deterministic data collection focused exclusively on **verifiable government and official industry statistics** with direct URL citations and archivable sources.

### Data Points Collected: 38

### Unique Sources: 11

### Total Source Citations: 42

---

## Data Categories

### 1. Bureau of Labor Statistics (BLS) - Employment Data

**SOC 51-9161: Computer Numerically Controlled Tool Operators**
- Employment (May 2024): **177,100 workers**
- Median Annual Wage: **$49,970**
- Median Hourly Wage: **$24.02**
- Projected Growth (2024-2034): **-1%** (slight decline)
- Projected Annual Job Openings: **13,500**

**SOC 51-9162: Computer Numerically Controlled Tool Programmers**
- Employment (May 2024): **28,300 workers**
- Median Annual Wage: **$65,670** (31% higher than operators)
- Median Hourly Wage: **$31.57**
- Projected Growth (2024-2034): **+7%** (much faster than average)
- Projected Annual Job Openings: **3,100**

**SOC 51-4041: Machinists**
- Employment (2024): **299,500 workers**
- Median Annual Wage: **$56,150**
- Wage Range: $38,100 (10th percentile) to $78,760 (90th percentile)
- Projected Growth (2024-2034): **-2%**
- Projected Annual Job Openings: **34,200**

**Broader Category: Metal and Plastic Machine Workers**
- Employment (2024): **1,000,000 workers**
- Median Annual Wage: **$46,800**
- Projected Growth (2024-2034): **-7%**
- Projected Annual Job Openings: **87,900**

**Combined CNC Workforce**
- Total CNC Operators + Programmers: **205,400 workers**

---

### 2. U.S. Census Bureau - Machine Shop Industry

**NAICS 332710: Machine Shops (2020 Economic Census)**
- Establishments: **17,530 physical locations**
- Businesses/Firms: **17,275 legal entities**
- Total Employment: **209,280 workers**
- Annual Payroll: **$12,316,948,000** ($12.3 billion)
- Average Annual Wage: **$58,852** (calculated)
- Average Workers per Shop: **11.94** (small business industry)

**Current Estimates (2024)**
- Active Companies: **12,981** (decline from 2020)
- Total Employment: **226,270 workers** (8% increase from 2020)

**Key Finding:** CNC operators represent approximately **84.6%** of machine shop workforce (177,100 / 209,280)

---

### 3. Federal Reserve Economic Data (FRED)

**Machine Shop Employment Index (NAICS 332710)**
- 2024 Index Value: **95.435** (base year 2017 = 100)
- 2023 Index Value: **98.502**
- Year-over-Year Change: **-3.1%** (declining employment)

Source: Federal Reserve Bank of St. Louis / BLS Industry Productivity data

---

### 4. Industry Association Statistics

**AMT (Association for Manufacturing Technology) - Machine Tool Orders**
- 2022 Orders: **$5.56 billion**
- 2023 Orders: **$4.94 billion** (-11.2% year-over-year)
- 2024 Orders (Jan-Sep YTD): **$3.35 billion** (-7.7% vs same period 2023)

**NTMA (National Tooling and Machining Association) - Member Data**
- Member Companies: **1,200-1,300** (represents ~9-10% of all US machine shops)
- Combined Member Revenues: **$30+ billion**
- Annual Parts/Components Sales: **$35+ billion**
- Market Share: **>75%** of precision machining tools purchased in US

---

## Key Insights from Government Data

### Employment Trends
1. **CNC operators declining (-1%)** while **CNC programmers growing (+7%)** - indicates automation and skill shift
2. **Metal/plastic machine workers declining fastest (-7%)** - automation replacing manual machine operation
3. **Despite declining employment**, substantial replacement demand creates job openings (13,500/year for CNC operators)

### Industry Economics
1. **Small business dominated**: Average 11.94 workers per machine shop
2. **Machine shop consolidation**: Companies declined from 17,275 (2020) to 12,981 (current) = -25%
3. **Employment grew despite consolidation**: 209,280 (2020) to 226,270 (current) = +8%
4. **Wages competitive**: CNC operators earn $49,970 median, machinists $56,150

### Market Dynamics
1. **Machine tool orders declining**: -11.2% (2023), -7.7% YTD (2024)
2. **NTMA members control majority**: >75% of precision machining tool purchases
3. **Member revenues $30B+**: Small number of shops (1,200) generate significant economic output

---

## Data Quality & Provenance

### Source Hierarchy
1. **Primary Government Sources** (BLS, Census Bureau, FRED): 9 sources
2. **Official Industry Associations** (AMT, NTMA): 2 sources

### Methodology Notes
- **BLS OES Survey**: Conducted in May 2024, published April 2025. Includes data from employers in all sectors, states, and metros. Excludes self-employed workers.
- **Census Economic Census**: 2020 data most recent detailed census. 2022 census data exists but detailed NAICS-level not yet fully published.
- **BLS Employment Projections**: 2024-2034 projections published 2024. Account for automation, technological change, and demographic shifts.
- **AMT USMTO Report**: Monthly survey of machine tool orders. Industry-standard metric for manufacturing technology sector health.

### Data Limitations
1. **Different survey years**: BLS employment (May 2024) vs Census establishment data (2020) limits direct comparison precision
2. **Self-employed excluded**: BLS OES excludes self-employed machinists/operators, underestimating true workforce
3. **SOC code changes**: 51-4011 (old) merged into 51-9161 (new) - historical comparisons challenging
4. **Company count variance**: Census (17,275 in 2020) vs current estimate (12,981) from different methodologies

---

## Files Generated

### 01_government_data.py
**Purpose:** Runnable Python script that populates knowledge base with government data
**Size:** 662 lines, 31KB
**Classes Used:** `KnowledgeBase`, `DataPoint`, `Source` from `kb_infrastructure.py`

**Execution:**
```bash
cd /home/user/ConsumerNYQST-1/knowledge_base/deterministic_sources
python3 01_government_data.py
```

**Output:** Generates JSON knowledge base and markdown provenance report

### government_data_kb.json
**Purpose:** Structured JSON knowledge base with all data points
**Size:** 47KB
**Structure:**
```json
{
  "metadata": {
    "created": "2025-11-11T03:30:55.640927",
    "verification_status": { ... }
  },
  "data_points": {
    "cnc_operators_employment_may2024": {
      "claim": "...",
      "value": 177100,
      "unit": "workers",
      "sources": [ ... ],
      "validation_notes": "..."
    },
    ...
  }
}
```

### government_data_provenance.md
**Purpose:** Human-readable provenance report with full source citations
**Size:** 12KB
**Contents:** All 38 data points with sources, URLs, excerpts, and validation notes

---

## Source URLs (All Direct & Archivable)

### BLS Sources
1. https://www.onetonline.org/link/summary/51-9161.00 (CNC Operators)
2. https://www.onetonline.org/link/summary/51-9162.00 (CNC Programmers)
3. https://www.bls.gov/ooh/production/machinists-and-tool-and-die-makers.htm (Machinists OOH)
4. https://www.bls.gov/oes/current/oes514041.htm (Machinists OES)
5. https://www.bls.gov/ooh/production/metal-and-plastic-machine-workers.htm (Metal/Plastic Workers)

### Census Bureau Sources
6. https://data.census.gov/profile/332710_-_Machine_Shops (Census Profile)
7. https://siccode.com/naics-code/332710/machine-shops (Census data via SIC Code)
8. https://www.census.gov/naics/?input=332710&year=2022&details=332710 (NAICS Definition)

### Federal Reserve Source
9. https://fred.stlouisfed.org/series/IPUEN332710W010000000 (Employment Index)

### Industry Association Sources
10. https://www.amtonline.org/article/2023-manufacturing-technology-orders-beat-expectations-as-december-adds (AMT 2023)
11. https://www.americanmachinist.com/news/article/55242083/more-improvement-in-us-machine-tool-orders-usmto-september-2024 (AMT 2024)
12. https://ntma.org/ (NTMA)

---

## Next Steps for Researchers

1. **Cross-reference with app data**: Compare CNC workforce (205,400) to app user bases
2. **Calculate TAM precision**: Use employment data to validate addressable market estimates
3. **Validate wage assumptions**: Use $49,970 median for willingness-to-pay models
4. **Track industry trends**: Monitor BLS quarterly updates and AMT monthly USMTO reports
5. **Archive sources**: Use Wayback Machine to create permanent archives of all source URLs

---

## Changelog

### 2025-11-11 - Initial Collection
- Collected 38 data points from 11 unique government and official sources
- All sources have direct URLs and are archivable
- Data spans employment, wages, projections, industry statistics, and market data
- Generated structured knowledge base with full provenance tracking
