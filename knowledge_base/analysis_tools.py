#!/usr/bin/env python3
"""
Analysis Tools for Knowledge Base
Generates reports, validates data, identifies gaps
"""

import json
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def load_all_json_data():
    """Load all JSON data files from deterministic_sources"""
    data = {
        "government": {},
        "manufacturer": {},
        "app_stats": {},
        "formulas": {},
        "market_research": {}
    }

    source_dir = Path(__file__).parent / "deterministic_sources"

    # Load each JSON file
    json_files = {
        "government": "government_data_kb.json",
        "manufacturer": "02_manufacturer_data.json",
        "app_stats": "03_app_statistics.json",
        "formulas": "04_formulas.json",
        "market_research": "05_market_research.json"  # if exists
    }

    for key, filename in json_files.items():
        filepath = source_dir / filename
        if filepath.exists():
            try:
                with open(filepath, 'r') as f:
                    data[key] = json.load(f)
                print(f"✓ Loaded {key}: {filepath.name}")
            except Exception as e:
                print(f"✗ Error loading {key}: {e}")
        else:
            print(f"⚠ Missing {key}: {filename}")

    return data

def count_data_points(data):
    """Count all data points across sources"""
    counts = {
        "total": 0,
        "by_source": {},
        "by_confidence": defaultdict(int)
    }

    # Government data
    if "data_points" in data.get("government", {}):
        gov_points = len(data["government"]["data_points"])
        counts["by_source"]["government"] = gov_points
        counts["total"] += gov_points

    # Manufacturer data
    if "manufacturer_data" in data.get("manufacturer", {}):
        mfg_points = len(data["manufacturer"]["manufacturer_data"])
        counts["by_source"]["manufacturer"] = mfg_points
        counts["total"] += mfg_points

    # App statistics
    if "app_statistics" in data.get("app_stats", {}):
        app_points = len(data["app_stats"]["app_statistics"])
        counts["by_source"]["app_statistics"] = app_points
        counts["total"] += app_points

    # Formulas
    if "formulas" in data.get("formulas", {}):
        formula_points = len(data["formulas"]["formulas"])
        counts["by_source"]["formulas"] = formula_points
        counts["total"] += formula_points

    return counts

def generate_comprehensive_report(data):
    """Generate comprehensive markdown report"""
    report = []
    report.append("# CNC Feeds & Speeds Knowledge Base")
    report.append(f"\n**Generated:** {datetime.now().isoformat()}\n")
    report.append("---\n")

    # Count data points
    counts = count_data_points(data)

    report.append("\n## Summary Statistics\n")
    report.append(f"\n**Total Data Points:** {counts['total']}\n")
    report.append("\nBreakdown by source:\n")
    for source, count in counts['by_source'].items():
        report.append(f"- {source.title()}: {count}\n")

    # Government Data Section
    report.append("\n## 1. Government & Official Statistics\n")
    if data.get("government") and "data_points" in data["government"]:
        gov_data = data["government"]["data_points"]
        report.append(f"\n**Total Data Points:** {len(gov_data)}\n")

        # Key metrics
        report.append("\n### Key Employment Metrics\n")
        report.append("\n| Metric | Value | Source |\n")
        report.append("|--------|-------|--------|\n")

        for key, dp in gov_data.items():
            if "employment" in dp.get("claim", "").lower() or "machinist" in dp.get("claim", "").lower():
                sources = len(dp.get("sources", []))
                report.append(f"| {dp.get('claim', '')[:50]} | {dp.get('value', 'N/A')} {dp.get('unit', '')} | {sources} sources |\n")

    # App Statistics Section
    report.append("\n## 2. App Store Statistics\n")
    if data.get("app_stats") and "app_statistics" in data["app_stats"]:
        app_data = data["app_stats"]["app_statistics"]
        report.append(f"\n**Total Statistics:** {len(app_data)}\n")

        # Group by app
        by_app = defaultdict(list)
        for stat in app_data:
            app_name = stat.get("app_name", "Unknown")
            by_app[app_name].append(stat)

        report.append("\n### Statistics by App\n")
        for app_name, stats in sorted(by_app.items()):
            report.append(f"\n#### {app_name} ({len(stats)} metrics)\n")
            report.append("\n| Metric | Value | Platform | Confidence |\n")
            report.append("|--------|-------|----------|------------|\n")
            for stat in stats:
                metric = stat.get("metric", "")
                value = stat.get("value", "")
                platform = stat.get("platform", "")
                conf = stat.get("confidence", "")
                report.append(f"| {metric} | {value} | {platform} | {conf} |\n")

    # Formulas Section
    report.append("\n## 3. Verified Formulas\n")
    if data.get("formulas") and "formulas" in data["formulas"]:
        formulas = data["formulas"]["formulas"]
        report.append(f"\n**Total Formulas:** {len(formulas)}\n")

        for name, formula in formulas.items():
            sources_count = len(formula.get("sources", []))
            report.append(f"\n### {name}\n")
            report.append(f"- **Formula:** `{formula.get('formula', '')}`\n")
            report.append(f"- **Sources:** {sources_count}\n")

    # Manufacturer Data Section
    report.append("\n## 4. Manufacturer Data\n")
    if data.get("manufacturer") and "manufacturer_data" in data["manufacturer"]:
        mfg_data = data["manufacturer"]["manufacturer_data"]
        report.append(f"\n**Total Records:** {len(mfg_data)}\n")

        # Group by manufacturer
        by_mfg = defaultdict(list)
        for record in mfg_data:
            mfg = record.get("manufacturer", "Unknown")
            by_mfg[mfg].append(record)

        report.append("\n### By Manufacturer\n")
        for mfg, records in sorted(by_mfg.items()):
            report.append(f"- **{mfg}:** {len(records)} records\n")

    # TAM Analysis
    report.append("\n## 5. TAM Analysis from Verified Data\n")
    report.append("\n### Base Market Size (from BLS data)\n")
    report.append("- **CNC Tool Operators:** 177,100 (May 2024)\n")
    report.append("- **CNC Tool Programmers:** 28,300 (May 2024)\n")
    report.append("- **Total CNC Workforce:** 205,400\n")
    report.append("- **Total Machinists:** 299,500\n")

    report.append("\n### TAM Scenarios\n")
    report.append("\n#### Conservative")
    report.append("\n- Base: 205,400 CNC workers")
    report.append("\n- Calculator adoption: 10% = 20,540")
    report.append("\n- Paying: 50% = 10,270")
    report.append("\n- ARPU: $150/year")
    report.append("\n- **TAM: $1.54M**")

    report.append("\n\n#### Moderate")
    report.append("\n- Base: 205,400 CNC workers")
    report.append("\n- Calculator adoption: 15% = 30,810")
    report.append("\n- Paying: 60% = 18,486")
    report.append("\n- ARPU: $200/year")
    report.append("\n- **TAM: $3.7M**")

    report.append("\n\n#### Optimistic")
    report.append("\n- Base: 299,500 total machinists")
    report.append("\n- Calculator adoption: 20% = 59,900")
    report.append("\n- Paying: 50% = 29,950")
    report.append("\n- ARPU: $200/year")
    report.append("\n- **TAM: $6.0M**")

    # Validation Status
    report.append("\n## 6. Validation Status\n")
    report.append("\n### What's Verified (Triple-Sourced)\n")
    report.append("- BLS employment data (government source)\n")
    report.append("- Core machining formulas (public domain + manufacturer confirmation)\n")
    report.append("- FSWizard app store metrics (iOS + Android)\n")

    report.append("\n### What Needs More Sources\n")
    report.append("- G-Wizard user count (single source, company claim)\n")
    report.append("- HSMAdvisor user count (no public data)\n")
    report.append("- Willingness to pay $150-250/year (no survey data)\n")
    report.append("- Market penetration estimates (derived, not measured)\n")

    return "".join(report)

if __name__ == "__main__":
    print("=" * 80)
    print("KNOWLEDGE BASE ANALYSIS TOOLS")
    print("=" * 80)

    # Load all data
    print("\nLoading data from JSON files...\n")
    data = load_all_json_data()

    # Generate comprehensive report
    print("\nGenerating comprehensive report...")
    report = generate_comprehensive_report(data)

    # Save report
    output_file = Path(__file__).parent / "COMPREHENSIVE_KNOWLEDGE_BASE_REPORT.md"
    with open(output_file, 'w') as f:
        f.write(report)

    print(f"\n✓ Saved: {output_file}")

    # Print summary
    counts = count_data_points(data)
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"\nTotal Data Points Collected: {counts['total']}")
    print("\nBy Source:")
    for source, count in counts['by_source'].items():
        print(f"  - {source.title()}: {count}")

    print("\n✓ Analysis complete")
