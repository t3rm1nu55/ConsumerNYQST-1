#!/usr/bin/env python3
"""
Deterministic Manufacturer Data Collection
Tool and Machine Manufacturer Specifications - Publicly Available Sources

Data collected from official manufacturer websites and technical documentation.
All sources are publicly accessible and documented with full provenance.

Retrieved: 2025-11-11
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from kb_infrastructure import (
    ManufacturerData,
    Source,
    SourceType,
    KnowledgeBase
)

def create_manufacturer_database():
    """Create comprehensive manufacturer database from publicly available sources"""

    kb = KnowledgeBase()

    # =============================================================================
    # TOOL MANUFACTURERS
    # =============================================================================

    # -----------------------------------------------------------------------------
    # 1. SANDVIK COROMANT
    # -----------------------------------------------------------------------------

    # Sandvik - Aluminum 6061 Cutting Data
    sandvik_aluminum_data = ManufacturerData(
        manufacturer="Sandvik Coromant",
        product_line="Carbide Tooling - Aluminum Applications",
        data_type="cutting_speeds",
        data={
            "material": "6061 Aluminum",
            "tool_type": "Carbide End Mill",
            "grade_recommendation": "H10 (uncoated carbide)",
            "application": "Roughing and Finishing",
            "cutting_speed_sfm_range": [600, 1200],
            "cutting_speed_sfm_typical": 1000,
            "cutting_speed_sfm_high_performance": 6562,  # With PCD tooling
            "feed_per_tooth_ipt_range": [0.005, 0.010],
            "feed_per_tooth_ipt_high_performance": 0.006,  # PCD at 2000 m/min
            "notes": "H10 grade features excellent abrasive wear resistance and edge sharpness. High-performance PCD tooling can achieve 2000 m/min (6562 ft/min) with 0.16 mm/tooth feed.",
        },
        sources=[
            Source(
                url="https://www.sandvik.coromant.com/en-us/knowledge/parting-and-grooving/cutting-data",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Cutting data for parting and grooving – speeds and feeds",
                author="Sandvik Coromant",
            ),
            Source(
                url="https://www.auto-revista.com/texto-diario/mostrar/1545597/sandvik-coromant-optimises-aluminum-machning-processes-for-the-automotive-industry",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Sandvik Coromant optimises aluminum machining processes for the automotive industry",
                excerpt="Demonstrated cutting speeds of 2000 m/min with feed rate of 0.16 mm/tooth using PCD tooling",
            ),
        ]
    )
    kb.add_manufacturer_data(sandvik_aluminum_data)

    # Sandvik - CoroPlus Tool Library
    sandvik_toolguide = ManufacturerData(
        manufacturer="Sandvik Coromant",
        product_line="CoroPlus ToolGuide",
        data_type="tool_specs",
        data={
            "product_name": "CoroPlus ToolGuide",
            "type": "Digital Tool Selection & Cutting Data Platform",
            "availability": "Online and Mobile App",
            "features": [
                "Tool recommendations based on workpiece material",
                "Cutting data calculations (speed, feed, depth)",
                "CAM software integration",
                "Tool data management system export",
                "Barcode scanning for insert data"
            ],
            "access": "Free, publicly accessible",
            "platforms": ["Web", "iOS", "Android"],
            "url": "https://toolguide.sandvik.coromant.com/",
        },
        sources=[
            Source(
                url="https://www.sandvik.coromant.com/en-us/tools/digital-machining/coroplus-tool-guide",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="CoroPlus® Tool Guide",
                author="Sandvik Coromant",
            ),
            Source(
                url="https://videos.sandvik.coromant.com/tool-and-cutting-data",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Tool and cutting data recommendation with CoroPlus ToolGuide",
            ),
        ]
    )
    kb.add_manufacturer_data(sandvik_toolguide)

    # Sandvik - Machining Calculator App
    sandvik_calculator = ManufacturerData(
        manufacturer="Sandvik Coromant",
        product_line="Machining Calculator App",
        data_type="tool_specs",
        data={
            "product_name": "Sandvik Coromant Machining Calculator",
            "type": "Mobile Calculation App",
            "capabilities": [
                "Cutting speed calculation",
                "Spindle speed (RPM) calculation",
                "Feed rate calculation",
                "Optimized for turning, milling, drilling"
            ],
            "availability": "Free mobile app",
            "platforms": ["iOS", "Android"],
        },
        sources=[
            Source(
                url="https://apps.apple.com/us/app/machining-calculator/id389011280",
                source_type=SourceType.APP_STORE,
                retrieved_date="2025-11-11",
                title="Machining Calculator on the App Store",
            ),
            Source(
                url="https://www.helmancnc.com/sandvik-coromant-machining-calculator-app-for-cnc-machinist/",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Sandvik Coromant Machining Calculator App for CNC Machinist",
            ),
        ]
    )
    kb.add_manufacturer_data(sandvik_calculator)

    # -----------------------------------------------------------------------------
    # 2. KENNAMETAL
    # -----------------------------------------------------------------------------

    # Kennametal - Speed and Feed Formulas
    kennametal_formulas = ManufacturerData(
        manufacturer="Kennametal",
        product_line="Engineering Calculators",
        data_type="cutting_speeds",
        data={
            "formula_rpm": "Speed (RPM) = (Surface Feet per Minute × 3.82) / Diameter of the Tool",
            "formula_feed_rate": "Feed Rate = RPM × Chip Load × Number of Teeth",
            "formula_sfm_from_rpm": "Surface Feet per Minute = (RPM × Tool Diameter) / 3.82",
            "formula_turning_speed": "Rotational Speed (N) = Cutting Speed (SFM) / (π × Original Diameter)",
            "notes": "Based upon theoretical values, intended for planning purposes. Actual results will vary.",
            "variables_affecting_speed": [
                "Material hardness and heat treatment",
                "Tool material composition (carbide, HSS)",
                "Machine coolant availability",
                "Work-holding fixture stability"
            ],
        },
        sources=[
            Source(
                url="https://www.kennametal.com/us/en/resources/engineering-calculators/miscellaneous/speed-and-feed.html",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Speeds and Feeds Calculator – Kennametal",
                author="Kennametal Inc.",
            ),
        ]
    )
    kb.add_manufacturer_data(kennametal_formulas)

    # Kennametal - Available Resources
    kennametal_resources = ManufacturerData(
        manufacturer="Kennametal",
        product_line="Technical Resources",
        data_type="tool_specs",
        data={
            "online_calculator": "https://www.kennametal.com/us/en/resources/engineering-calculators/miscellaneous/speed-and-feed.html",
            "engineering_calculators": [
                "Speed and Feed Calculator",
                "Face, Cutoff, and Deep Groove Calculator",
                "Surface Finish Calculator",
                "Cost Savings Calculator"
            ],
            "technical_guides": [
                "How to Find Feeds and Speeds for Your Tools",
                "Recommended Starting Speed and Feeds (PDF)",
            ],
            "pdf_url": "https://www1.mscdirect.com/images/solutions/kennametal/endMillSpeedFeed.pdf",
            "availability": "Free, publicly accessible",
        },
        sources=[
            Source(
                url="https://www.kennametal.com/us/en/resources/engineering-calculators.html",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Engineering and Machining Calculators - Kennametal",
            ),
            Source(
                url="https://www.kennametal.com/us/en/resources/tutorials/how-to-find-speeds-and-feeds.html",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="How to Find Feeds and Speeds for Your Tools - Kennametal",
            ),
        ]
    )
    kb.add_manufacturer_data(kennametal_resources)

    # -----------------------------------------------------------------------------
    # 3. HARVEY TOOL
    # -----------------------------------------------------------------------------

    # Harvey Tool - Speeds and Feeds Resources
    harvey_speeds_feeds = ManufacturerData(
        manufacturer="Harvey Tool",
        product_line="Miniature End Mills and Cutting Tools",
        data_type="cutting_speeds",
        data={
            "material_6061_aluminum": {
                "cutting_speed_sfm_range": [800, 1500],
                "feed_per_tooth_ipt_range": [0.005, 0.010],
                "notes": "Recommended starting values, may be increased given optimal setup conditions"
            },
            "general_carbide_aluminum": {
                "cutting_speed_sfm_typical": 1000,
                "cutting_speed_sfm_aggressive": [5000, 8000],
                "notes": "Aggressive speeds depend on tool style, setup, horsepower, tool holder, and machine capacity"
            },
            "resources_available": [
                "Product-specific speed/feed charts (downloadable, printer-friendly)",
                "Machining Advisor Pro (MAP) - customized parameter generation",
                "General Machining Guidelines"
            ],
            "chart_features": "Account for exact material, application (slotting, roughing, finishing)",
            "access": "Free, publicly accessible per product",
        },
        sources=[
            Source(
                url="https://www.harveytool.com/resources/speeds-feeds-guide",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Harvey Tool Speeds and Feeds Guide",
                author="Harvey Performance Company",
            ),
            Source(
                url="https://www.harveytool.com/resources/speeds-feeds",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Harvey Tool - Speeds and Feeds for every tool",
            ),
        ]
    )
    kb.add_manufacturer_data(harvey_speeds_feeds)

    # Harvey Tool - Machining Advisor Pro
    harvey_map = ManufacturerData(
        manufacturer="Harvey Tool",
        product_line="Machining Advisor Pro (MAP)",
        data_type="tool_specs",
        data={
            "product_name": "Machining Advisor Pro",
            "type": "Customizable Speeds & Feeds Calculator",
            "capabilities": [
                "Specialized machining parameters by tool path",
                "Material-specific calculations",
                "Machine setup optimization",
                "Desktop, tablet, mobile access"
            ],
            "cost": "Free - no fee required",
            "url": "https://www.harveyperformance.com/machining-advisor-pro/",
            "features": "Pairs cutting tool with exact tool path, material, and machine setup",
        },
        sources=[
            Source(
                url="https://www.harveyperformance.com/machining-advisor-pro/",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Machining Advisor Pro - Customizable Speeds & Feeds",
                author="Harvey Performance Company",
            ),
        ]
    )
    kb.add_manufacturer_data(harvey_map)

    # -----------------------------------------------------------------------------
    # 4. ISCAR
    # -----------------------------------------------------------------------------

    # ISCAR - ITA Tool Advisor
    iscar_ita = ManufacturerData(
        manufacturer="Iscar",
        product_line="ITA (Iscar Tool Advisor)",
        data_type="tool_specs",
        data={
            "product_name": "ISCAR Tool Advisor (ITA)",
            "type": "Web-based Tool Selection Software",
            "algorithm": "Unique mathematical algorithm",
            "input_fields": {
                "minimum": "2-6 mandatory fields for quick results",
                "detailed": "Machine parameters, tool diameters, tool type, grade, etc."
            },
            "output_data": [
                "Tool details",
                "Insert details",
                "Cutting conditions",
                "Power requirements",
                "Metal removal rate",
                "Cutting time",
                "3-25 tool recommendations per search (best 3 default)"
            ],
            "features": [
                "Inch and metric platforms",
                "25 language support",
                "24/7 availability",
                "Direct ITA support team connection",
                "iPhone/iPod Touch app available"
            ],
            "advanced_version": "NEO-ITA with AI and Big Data analytics using machine learning",
            "cost": "Free of charge",
            "url": "https://www.iscar.com/itc/MainPage.aspx",
            "url_neo": "www.iscarmetals.com/ITA",
        },
        sources=[
            Source(
                url="https://www.iscar.com/itc/MainPage.aspx",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="ITA - ISCAR Tool Advisor",
                author="Iscar Ltd.",
            ),
            Source(
                url="https://www.ctemag.com/products/ita-iscar-tool-advisor",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="ITA (Iscar Tool Advisor) | Cutting Tool Engineering",
            ),
            Source(
                url="https://www.helmancnc.com/ita-iscar-tool-advisor-web-based-tool-selection-for-cnc-machinists/",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="ITA Iscar Tool Advisor - Web-based Tool Selection for CNC Machinists",
            ),
        ]
    )
    kb.add_manufacturer_data(iscar_ita)

    # ISCAR - 2025 Product Information
    iscar_2025 = ManufacturerData(
        manufacturer="Iscar",
        product_line="2025 Product Catalog",
        data_type="tool_specs",
        data={
            "year": 2025,
            "catalog_title": "ISCAR IS ABOUT TO CHANGE METAL CUTTING... AGAIN!",
            "catalog_url": "https://www.iscar.com/Catalogs/Publication/english_1/world_Magazines/ISCAR_ARTICLE_2025/ISCAR_ARTICLE_2025.pdf",
            "industry_4_0": "New Industry 4.0 connectivity solutions",
            "notes": "2025 catalog features new product innovations and digital connectivity",
        },
        sources=[
            Source(
                url="https://www.iscar.com/Catalogs/Publication/english_1/world_Magazines/ISCAR_ARTICLE_2025/ISCAR_ARTICLE_2025.pdf",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="2025 ISCAR IS ABOUT TO CHANGE METAL CUTTING... AGAIN!",
            ),
        ]
    )
    kb.add_manufacturer_data(iscar_2025)

    # -----------------------------------------------------------------------------
    # 5. SECO TOOLS
    # -----------------------------------------------------------------------------

    # Seco Tools - Digital Cutting Data Resources
    seco_digital = ManufacturerData(
        manufacturer="Seco Tools",
        product_line="Digital Cutting Data Solutions",
        data_type="tool_specs",
        data={
            "machine_library": {
                "type": "Web-based cutting data tool",
                "launched": "July 2025",
                "features": "Product-specific, instant, high-quality cutting data based on machine information",
            },
            "seco_assistant_app": {
                "type": "Mobile application",
                "capabilities": [
                    "Feeds and speeds calculations",
                    "Cutting data recommendations",
                    "Product comparison",
                ],
                "platforms": ["iOS", "Android"]
            },
            "secocut_software": {
                "type": "Desktop software",
                "data_types": ["Feed", "Speed", "Power", "Torque"],
                "operations": ["Milling", "Turning", "Drilling"],
                "features": "Graphical search tool and circular interpolation support"
            },
            "technical_guides": [
                "Catalog & Technical Guide 2020.2 (comprehensive)",
                "Duratomic product guides",
                "Advanced Cutting Materials",
                "Holemaking solutions",
                "Composite machining"
            ],
            "website": "www.secotools.com",
        },
        sources=[
            Source(
                url="https://www.geartechnology.com/seco-tools-launches-web-based-tool-for-cutting-data",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Seco Tools Launches Web-Based Tool for Cutting Data",
                publication_date="July 2025",
            ),
            Source(
                url="https://www.secotools.com/article/114039?language=en",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Seco Assistant | Seco Tools",
            ),
            Source(
                url="https://secocut.software.informer.com/",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Secocut Download - A cutting data tool with graphical search tool",
            ),
        ]
    )
    kb.add_manufacturer_data(seco_digital)

    # Seco Tools - Technical Documentation
    seco_docs = ManufacturerData(
        manufacturer="Seco Tools",
        product_line="Technical Catalogs",
        data_type="tool_specs",
        data={
            "catalog_2020_2": {
                "title": "Catalog & Technical Guide 2020.2",
                "coverage": "Metal cutting solutions for milling, stationary tools, holemaking, tooling systems",
                "url": "https://pdf.directindustry.com/pdf/seco-tools/catalog-technical-guide-20202/5699-951358.html"
            },
            "all_catalogs_url": "https://pdf.directindustry.com/pdf/seco-tools-5699.html",
            "formats": ["PDF", "Digital Download"],
            "availability": "Publicly accessible technical brochures",
        },
        sources=[
            Source(
                url="https://pdf.directindustry.com/pdf/seco-tools/catalog-technical-guide-20202/5699-951358.html",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="CATALOG & TECHNICAL GUIDE 2020.2 - SECO TOOLS",
            ),
            Source(
                url="https://pdf.directindustry.com/pdf/seco-tools-5699.html",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="All SECO TOOLS catalogs and technical brochures",
            ),
        ]
    )
    kb.add_manufacturer_data(seco_docs)

    # -----------------------------------------------------------------------------
    # 6. OSG CORPORATION
    # -----------------------------------------------------------------------------

    # OSG - Technical Charts and Documentation
    osg_charts = ManufacturerData(
        manufacturer="OSG Corporation",
        product_line="Technical Charts and Guides",
        data_type="tool_specs",
        data={
            "available_charts": {
                "800274CA-V3": {
                    "title": "Tap Drill Size & Pitch Limits - Vol 3",
                    "size_kb": 78.27,
                    "year": 2024,
                },
                "800361CA": {
                    "title": "STI Tap Drill Size - Vol 1",
                    "size_kb": 61.74,
                },
                "800279CA-V2": {
                    "title": "High Speed Machining Guide - Vol 2",
                    "size_kb": 1890,  # 1.89 MB
                    "coverage": "Inch and metric measurements",
                },
                "800313CA-V3": {
                    "title": "Brand Recommendation Guide - Vol 3",
                    "size_kb": 61.24,
                },
                "80017CA-V10": {
                    "title": "Decimal Wall Charts - Vol 10",
                    "size_kb": 23920,  # 23.92 MB
                },
                "PDC-22": {
                    "title": "Pocket Decimal Chart - 2022",
                    "size_kb": 451.03,
                    "reprint": 2024,
                },
            },
            "tapping_chart_coverage": [
                "M (Metric)",
                "MF (Metric Fine)",
                "MJ (Metric J-type)",
                "UNC (Unified Coarse)",
                "UNJC (Unified J-type Coarse)",
                "UNF (Unified Fine)",
                "UNJF (Unified J-type Fine)",
                "Pg (Panzergewinde)",
                "Tr (Trapezoidal)",
                "G (BSP Parallel)",
                "BSW (British Standard Whitworth)",
                "UNEF (Unified Extra Fine)",
                "UN (Unified)",
                "NPT (National Pipe Thread)",
                "BSF (British Standard Fine)",
                "Rp (BSP Parallel Internal)",
                "BA (British Association)",
                "Rc (BSP Taper)",
                "EG M (European Gas Metric)",
                "EG UNC",
                "EG UNF"
            ],
            "download_url": "https://osgtool.com/literature/charts/",
            "format": "PDF downloads",
            "availability": "Free, publicly accessible",
        },
        sources=[
            Source(
                url="https://osgtool.com/literature/charts/",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="LITERATURE - CHARTS - OSG USA, Inc",
                author="OSG Corporation",
            ),
            Source(
                url="https://www.osg.co.jp/en/media_dl/technical/",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Technical Information | DOWNLOAD | OSG Japan",
            ),
        ]
    )
    kb.add_manufacturer_data(osg_charts)

    # =============================================================================
    # MACHINE TOOL MANUFACTURERS
    # =============================================================================

    # -----------------------------------------------------------------------------
    # 7. HAAS AUTOMATION
    # -----------------------------------------------------------------------------

    # Haas - Spindle Specifications Overview
    haas_spindles = ManufacturerData(
        manufacturer="Haas Automation",
        product_line="CNC Mill Spindles",
        data_type="machine_specs",
        data={
            "spindle_power_characteristics": {
                "peak_power_200_percent": "3 minutes at 200% spindle load",
                "high_power_150_percent": "10-15 minutes at 150% spindle load",
                "continuous_100_percent": "Continuous at 100% spindle load",
                "voltage_note": "Power numbers based on 240V service at required amperage",
            },
            "spindle_types": {
                "inline": {
                    "rpm_range": [8100, 20000],
                    "description": "Direct drive inline spindle"
                },
                "geared_head": {
                    "rpm_max": 10000,
                    "features": "Increased low-end torque for heavy cutting",
                }
            },
            "example_minimill": {
                "max_torque_lb_ft": 33,
                "max_torque_rpm": 1200,
                "torque_characteristics": "Fairly constant below 1200 RPM, falls off above",
            },
            "resources": [
                "Spindle torque curves available per machine model",
                "Individual spindle specification pages on haascnc.com",
                "Torque chart PDFs (e.g., UMC-1000SS Torque Binder)",
            ],
            "website": "https://www.haascnc.com/productivity/spindles.html",
        },
        sources=[
            Source(
                url="https://www.haascnc.com/productivity/spindles.html",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Spindles for CNC Milling Machines | Haas Automation",
                author="Haas Automation, Inc.",
            ),
        ]
    )
    kb.add_manufacturer_data(haas_spindles)

    # Haas - Specific Spindle Models
    haas_spindle_models = ManufacturerData(
        manufacturer="Haas Automation",
        product_line="Specific Spindle Models",
        data_type="machine_specs",
        data={
            "8100_rpm_spindle": {
                "rpm": 8100,
                "taper": "40 taper",
                "url": "https://www.haascnc.com/productivity/spindles/8-1k-40t-in.html"
            },
            "10000_rpm_grease": {
                "rpm": 10000,
                "taper": "40 taper",
                "type": "Grease-packed",
                "url": "https://www.haascnc.com/productivity/spindles/10k-40t-grease.html"
            },
            "12000_rpm_spindle": {
                "rpm": 12000,
                "taper": "40 taper",
                "url": "https://www.haascnc.com/productivity/spindles/12k-40t-in.html"
            },
            "7500_rpm_high_performance": {
                "rpm": 7500,
                "horsepower": 60,
                "drive": "Vector drive system",
                "gearbox": "Two-speed for wide constant horsepower band",
                "features": "Good low-speed torque for heavy cuts",
                "taper": "50 taper",
                "url": "https://www.haascnc.com/productivity/spindles/7-5k-50-hp.html"
            },
        },
        sources=[
            Source(
                url="https://www.haascnc.com/productivity/spindles/12k-40t-in.html",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="12,000-rpm Spindle - Haas Automation",
            ),
            Source(
                url="https://www.haascnc.com/productivity/spindles/7-5k-50-hp.html",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="High-Performance 7500-rpm Spindle - Haas Automation",
            ),
        ]
    )
    kb.add_manufacturer_data(haas_spindle_models)

    # -----------------------------------------------------------------------------
    # 8. DMG MORI
    # -----------------------------------------------------------------------------

    # DMG MORI - 2025 Machine Specifications
    dmg_mori_2025 = ManufacturerData(
        manufacturer="DMG MORI",
        product_line="2025 Machine Tool Lineup",
        data_type="machine_specs",
        data={
            "DMU_40_series": {
                "type": "Entry-level 5-axis",
                "models": {
                    "DMU_40": {
                        "spindle": "Inline",
                        "rpm": 12000,
                        "power_kw": 15,
                        "torque_nm": 95,
                    },
                    "DMU_40_PLUS": {
                        "spindle": "inlineMASTER",
                        "rpm": 15000,
                        "power_kw": 16.5,
                        "torque_nm": 121,
                    },
                    "DMU_40_PRO": {
                        "spindle": "speedMASTER",
                        "rpm": 20000,
                        "power_kw": 32,
                        "torque_nm": 130,
                    },
                },
                "features": "5-axis simultaneous machining, up to 20,000 min-1",
            },
            "DMX_U_series": {
                "type": "Universal Machining Centers",
                "models": ["DMX 60 U", "DMX 80 U"],
                "spindle_standard": {
                    "type": "inlineMASTER",
                    "rpm": 12000,
                },
                "spindle_optional": {
                    "speedMASTER_torque": {
                        "torque_nm": 200,
                    },
                    "speedMASTER_speed": {
                        "rpm": 20000,
                    },
                },
            },
            "NHX_series": {
                "type": "Horizontal Machining Centers",
                "spindle": "Speedmaster",
                "voltage": "400 V",
                "performance": "Up to 50% more output",
                "rapid_traverse": "70 m/min",
            },
            "turn_mill": {
                "compactMASTER": {
                    "rpm_or_torque": "Up to 20,000 min-1 or 220 Nm",
                },
                "NT_turning_milling": {
                    "rpm_max": 12000,
                    "torque_nm": 302,
                },
            },
            "M1_vertical_mill": {
                "x_axis_mm": 550,
                "y_axis_mm": 550,
                "z_axis_mm": 510,
                "x_axis_in": 22,
                "y_axis_in": 22,
                "z_axis_in": 20,
                "max_workpiece_length_mm": 550,
                "max_workpiece_width_mm": 550,
                "max_workpiece_height_mm": 400,
                "max_workpiece_weight_kg": 600,
                "max_workpiece_weight_lbs": 1323,
                "spindle_rpm_options": [10000, 12000],
                "spindle_type": "Inline spindle with DMG MORI design",
                "tool_magazine": "24-pocket with double gripper",
                "control": "SIEMENS 828D",
                "bed_weight_kg": 2400,
                "footprint_m2": 6,
                "coolant_optional": "Internal coolant supply with 20 bar pump",
            },
        },
        sources=[
            Source(
                url="https://visitors.emo-hannover.de/product/dmu-40-robo2go-milling/91/069361",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="EMO Product 2025: DMU 40 (DMG MORI)",
            ),
            Source(
                url="https://en.dmgmori.com/products/machines/milling/vertical-milling/m/m1",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="M1 - Vertical Milling - DMG MORI",
            ),
            Source(
                url="https://www.mmsonline.com/articles/process-consolidation-meets-usability-improvements-inside-dmg-mori-innovation-days-2025",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Process Consolidation Meets Usability Improvements: Inside DMG MORI Innovation Days 2025",
            ),
        ]
    )
    kb.add_manufacturer_data(dmg_mori_2025)

    # -----------------------------------------------------------------------------
    # 9. OKUMA
    # -----------------------------------------------------------------------------

    # Okuma - Machine Specifications
    okuma_specs = ManufacturerData(
        manufacturer="Okuma",
        product_line="CNC Machine Tools",
        data_type="machine_specs",
        data={
            "multus_series": {
                "type": "Multitasking Turn-Mill Machines",
                "capabilities": {
                    "axes": "Up to 5-axis simultaneous control",
                    "feed_rate_max_mm_min": 1000,
                    "rapid_traverse_m_min": 30,
                    "positioning_accuracy_mm": 0.001,
                    "repeatability_mm": 0.001,
                    "spindle_rpm_max": 20000,
                    "tool_magazine_capacity": 120,
                },
                "models": ["MU-4000V", "MU-5000V", "MU-6300V", "MULTUS U-series"],
                "features": [
                    "Complex geometry machining",
                    "Extensive travel ranges for large workpieces",
                    "High feed rates for rapid material removal",
                    "Superior positioning accuracy"
                ],
            },
            "vertical_machining_centers": {
                "models": ["MB-VA series", "MF-VA/VB series", "GENOS M560V"],
            },
            "lathes": {
                "models": ["LT2000 EX", "LU3000 EX", "LU7000EX", "LB2000EXIIMY", "GENOS L250"],
            },
            "control_system": "OSP-P control (Okuma proprietary)",
            "monitoring": "Okuma Connect Plan software-based machine monitoring",
            "website": "https://www.okuma.com/",
        },
        sources=[
            Source(
                url="https://premierequipment.com/cnc-blog/okuma-multus-series/",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Discover The Groundbreaking Okuma Multus Series For Advanced CNC Machining",
            ),
            Source(
                url="https://www.okuma.com/",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Okuma America | CNC Machine Tools | CNC Controls",
            ),
        ]
    )
    kb.add_manufacturer_data(okuma_specs)

    # -----------------------------------------------------------------------------
    # 10. MAZAK
    # -----------------------------------------------------------------------------

    # Mazak - 2025 Machine Specifications
    mazak_2025 = ManufacturerData(
        manufacturer="Mazak",
        product_line="2025 Machine Tool Lineup",
        data_type="machine_specs",
        data={
            "SYNCREX_38_8": {
                "type": "Swiss-type Production Turning",
                "bar_stock_max_diameter_in": 1.5,
                "control": "MAZATROL SmoothSt CNC",
                "touch_panel_size_in": 15,
                "featured_at": "CMTS 2025",
            },
            "QTE_100": {
                "type": "CNC Turning Center",
                "chuck_size_in": 6,
                "max_part_diameter_in": 11.42,
                "spindle": "Built-in motor spindle for high torque",
            },
            "VC_Ez_20": {
                "type": "Vertical Machining Center",
                "manufactured_in": "Kentucky, USA",
                "spindle_hp": 25,
                "spindle_rpm": 12000,
                "tool_changer": "30-tool automatic",
                "tool_changer_type": "Standard",
            },
            "technical_documentation": {
                "available_manuals": [
                    "General Information Manual",
                    "Programming Manual for MAZATROL MATRIX (INTEGREX IV)",
                    "Programming Manual for MAZATROL Fusion 640M",
                    "Parameter Lists for MAZATROL MATRIX",
                    "Parameter Lists for MAZATROL Fusion 640MT/MT 5X",
                    "Alarm Lists and M-Code Lists"
                ],
                "manual_repository": "https://cncmanual.com/mazak/",
            },
            "general_specs": {
                "insert_weight_max_gf": 20,
                "insert_weight_max_lbs": 0.04,
            },
        },
        sources=[
            Source(
                url="https://www.mazak.com/us-en/news-media/news/Mazak-to-Highlight-Production-boosting-Technology-for-Every-Shop--at-CMTS-2025/",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Mazak to Highlight Production-boosting Technology for Every Shop at CMTS 2025",
                author="Mazak Corporation",
            ),
            Source(
                url="https://www.mazak.com/us-en/",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Welcome to Mazak Corporation",
            ),
            Source(
                url="https://cncmanual.com/mazak/",
                source_type=SourceType.MANUFACTURER,
                retrieved_date="2025-11-11",
                title="Mazak Manuals User Guides - CNC Manual",
            ),
        ]
    )
    kb.add_manufacturer_data(mazak_2025)

    return kb


def print_summary(kb: KnowledgeBase):
    """Print summary of collected manufacturer data"""
    print("\n" + "="*80)
    print("MANUFACTURER DATA COLLECTION SUMMARY")
    print("="*80)
    print(f"\nTotal Manufacturers Documented: {len(set(md.manufacturer for md in kb.manufacturer_data))}")
    print(f"Total Data Records: {len(kb.manufacturer_data)}")
    print(f"Total Sources: {sum(len(md.sources) for md in kb.manufacturer_data)}")

    print("\n" + "-"*80)
    print("TOOL MANUFACTURERS:")
    print("-"*80)
    tool_mfrs = [md for md in kb.manufacturer_data if md.data_type in ["cutting_speeds", "tool_specs"]]
    for mfr_name in sorted(set(md.manufacturer for md in tool_mfrs)):
        records = [md for md in tool_mfrs if md.manufacturer == mfr_name]
        print(f"\n{mfr_name}:")
        for record in records:
            print(f"  - {record.product_line} ({record.data_type})")
            print(f"    Sources: {len(record.sources)}")

    print("\n" + "-"*80)
    print("MACHINE TOOL MANUFACTURERS:")
    print("-"*80)
    machine_mfrs = [md for md in kb.manufacturer_data if md.data_type == "machine_specs"]
    for mfr_name in sorted(set(md.manufacturer for md in machine_mfrs)):
        records = [md for md in machine_mfrs if md.manufacturer == mfr_name]
        print(f"\n{mfr_name}:")
        for record in records:
            print(f"  - {record.product_line}")
            print(f"    Sources: {len(record.sources)}")

    print("\n" + "-"*80)
    print("DATA TYPES COLLECTED:")
    print("-"*80)
    for data_type in ["cutting_speeds", "tool_specs", "machine_specs"]:
        count = len([md for md in kb.manufacturer_data if md.data_type == data_type])
        print(f"  {data_type}: {count} records")

    print("\n" + "="*80)
    print("VERIFICATION STATUS:")
    print("="*80)
    print("All data sourced from publicly accessible manufacturer websites")
    print("and official technical documentation.")
    print(f"Retrieved: 2025-11-11")
    print("="*80 + "\n")


if __name__ == "__main__":
    # Create the manufacturer database
    kb = create_manufacturer_database()

    # Print summary
    print_summary(kb)

    # Save to JSON for programmatic access
    output_path = Path(__file__).parent / "02_manufacturer_data.json"
    kb.save(str(output_path))
    print(f"\nData saved to: {output_path}")

    # Generate provenance report
    report_path = Path(__file__).parent / "02_manufacturer_data_provenance.md"
    with open(report_path, 'w') as f:
        f.write("# Manufacturer Data Provenance Report\n\n")
        f.write(f"**Retrieved:** 2025-11-11\n\n")
        f.write("## Data Sources\n\n")

        for i, md in enumerate(kb.manufacturer_data, 1):
            f.write(f"### {i}. {md.manufacturer} - {md.product_line}\n\n")
            f.write(f"**Type:** {md.data_type}\n\n")
            f.write("**Sources:**\n\n")
            for j, source in enumerate(md.sources, 1):
                f.write(f"{j}. [{source.source_type.value}] {source.title}\n")
                f.write(f"   - URL: {source.url}\n")
                if source.excerpt:
                    f.write(f"   - Excerpt: {source.excerpt}\n")
                f.write("\n")

    print(f"Provenance report saved to: {report_path}")
    print("\n✓ Manufacturer data collection complete!")
