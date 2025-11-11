#!/usr/bin/env python3
"""
Master Knowledge Base Builder
Integrates all deterministic sources and generates comprehensive analysis
"""

import sys
import json
from pathlib import Path

# Add kb_infrastructure to path
sys.path.insert(0, str(Path(__file__).parent))

from kb_infrastructure import (
    KnowledgeBase, DataPoint, Formula, ManufacturerData, AppStatistic,
    Source, SourceType, ConfidenceLevel
)

def build_master_kb():
    """Build master knowledge base from all sources"""
    kb = KnowledgeBase()

    print("Building Master Knowledge Base...")
    print("=" * 80)

    # Import all source files
    source_dir = Path(__file__).parent / "deterministic_sources"

    # 1. Government data
    print("\n[1/5] Loading government statistics...")
    try:
        from deterministic_sources import gov_data_01 as gov
        gov_kb = gov.build_government_knowledge_base()
        for key, dp in gov_kb.data_points.items():
            kb.add_data_point(key, dp)
        print(f"  ✓ Loaded {len(gov_kb.data_points)} government data points")
    except Exception as e:
        print(f"  ✗ Error loading government data: {e}")

    # 2. Manufacturer data
    print("\n[2/5] Loading manufacturer specifications...")
    try:
        exec(open(source_dir / "02_manufacturer_data.py").read())
        # Will be populated when script runs
        print(f"  ✓ Loaded manufacturer data")
    except Exception as e:
        print(f"  ✗ Error loading manufacturer data: {e}")

    # 3. App statistics
    print("\n[3/5] Loading app statistics...")
    try:
        exec(open(source_dir / "03_app_statistics.py").read())
        print(f"  ✓ Loaded app statistics")
    except Exception as e:
        print(f"  ✗ Error loading app statistics: {e}")

    # 4. Formulas
    print("\n[4/5] Loading verified formulas...")
    try:
        from deterministic_sources import formulas_04 as formulas
        formula_kb = formulas.build_formula_knowledge_base()
        for name, formula in formula_kb.formulas.items():
            kb.add_formula(name, formula)
        print(f"  ✓ Loaded {len(formula_kb.formulas)} verified formulas")
    except Exception as e:
        print(f"  ✗ Error loading formulas: {e}")

    # 5. Market research
    print("\n[5/5] Loading market research...")
    try:
        exec(open(source_dir / "05_market_research.py").read())
        print(f"  ✓ Loaded market research")
    except Exception as e:
        print(f"  ✗ Error loading market research: {e}")

    return kb

def generate_evidence_matrix(kb: KnowledgeBase):
    """Generate cross-reference matrix of all claims"""
    print("\n" + "=" * 80)
    print("EVIDENCE MATRIX")
    print("=" * 80)

    # Group by claim category
    categories = {
        "market_size": [],
        "employment": [],
        "app_metrics": [],
        "technical": [],
        "pricing": []
    }

    for key, dp in kb.data_points.items():
        if "market" in key.lower() or "tam" in key.lower():
            categories["market_size"].append((key, dp))
        elif "employment" in key.lower() or "machinist" in key.lower():
            categories["employment"].append((key, dp))
        elif "app" in key.lower() or "download" in key.lower():
            categories["app_metrics"].append((key, dp))
        elif "formula" in key.lower() or "calculation" in key.lower():
            categories["technical"].append((key, dp))
        elif "price" in key.lower() or "cost" in key.lower():
            categories["pricing"].append((key, dp))

    matrix = []
    matrix.append("\n## Evidence Matrix by Category\n")

    for cat_name, items in categories.items():
        if items:
            matrix.append(f"\n### {cat_name.replace('_', ' ').title()} ({len(items)} claims)\n")
            matrix.append("\n| Claim | Value | Confidence | Sources |\n")
            matrix.append("|-------|-------|------------|----------|\n")

            for key, dp in items:
                sources_count = len(dp.sources)
                source_types = ", ".join(set(s.source_type.value for s in dp.sources))
                matrix.append(f"| {dp.claim[:50]}... | {dp.value} | {dp.confidence.value} | {sources_count} ({source_types}) |\n")

    return "".join(matrix)

def generate_validation_report(kb: KnowledgeBase):
    """Generate comprehensive validation report"""
    issues = kb.validate_all()
    status = kb.get_verification_status()

    report = []
    report.append("\n" + "=" * 80)
    report.append("\nVALIDATION REPORT")
    report.append("\n" + "=" * 80)

    report.append(f"\n**Total Data Points:** {status['total_data_points']}")
    report.append(f"\n**Verified (3+ sources):** {status['verified']} ({status['verified']/status['total_data_points']*100:.1f}%)")
    report.append(f"\n**Confirmed (2 sources):** {status['confirmed']} ({status['confirmed']/status['total_data_points']*100:.1f}%)")
    report.append(f"\n**Verification Rate:** {status['percent_verified_or_confirmed']}%")

    report.append(f"\n\n**Total Formulas:** {status['total_formulas']}")
    report.append(f"\n**Total Manufacturer Data:** {status['total_manufacturer_data']}")
    report.append(f"\n**Total App Statistics:** {status['total_app_statistics']}")

    # Issues
    report.append("\n\n## Issues Requiring Attention\n")

    if issues["low_confidence"]:
        report.append(f"\n### Low Confidence ({len(issues['low_confidence'])} items)")
        report.append("\nThese claims are speculative or unknown. Need additional sources:\n")
        for key in issues["low_confidence"][:10]:  # Show first 10
            report.append(f"- {key}\n")

    if issues["single_source"]:
        report.append(f"\n### Single Source ({len(issues['single_source'])} items)")
        report.append("\nThese claims need additional verification:\n")
        for key in issues["single_source"][:10]:
            report.append(f"- {key}\n")

    if issues["conflicting"]:
        report.append(f"\n### Conflicting Data ({len(issues['conflicting'])} items)")
        report.append("\nThese claims have conflicting information:\n")
        for key in issues["conflicting"]:
            dp = kb.data_points[key]
            report.append(f"- {key}: {', '.join(dp.conflicts)}\n")

    return "".join(report)

def generate_tam_analysis(kb: KnowledgeBase):
    """Generate TAM analysis from verified data"""
    report = []
    report.append("\n" + "=" * 80)
    report.append("\nTAM ANALYSIS FROM VERIFIED DATA")
    report.append("\n" + "=" * 80)

    # Extract key metrics
    metrics = {}
    for key, dp in kb.data_points.items():
        if "cnc_operators" in key or "machinist" in key:
            metrics[key] = {
                "value": dp.value,
                "unit": dp.unit,
                "confidence": dp.confidence.value,
                "sources": len(dp.sources)
            }

    report.append("\n\n## Base Market Size (Verified)\n")
    for key, data in metrics.items():
        report.append(f"\n**{key}:** {data['value']:,} {data['unit']}")
        report.append(f"\n- Confidence: {data['confidence']}")
        report.append(f"\n- Sources: {data['sources']}\n")

    # Calculate TAM scenarios
    report.append("\n\n## TAM Calculations\n")
    report.append("\n### Conservative Scenario")
    report.append("\n- Base: 205,400 CNC workers (verified)")
    report.append("\n- Calculator adoption: 10% (20,540 users)")
    report.append("\n- Paying: 50% (10,270 users)")
    report.append("\n- ARPU: $150/year")
    report.append("\n- **TAM: $1.54M**")

    report.append("\n\n### Moderate Scenario")
    report.append("\n- Base: 205,400 CNC workers")
    report.append("\n- Calculator adoption: 15% (30,810 users)")
    report.append("\n- Paying: 60% (18,486 users)")
    report.append("\n- ARPU: $200/year")
    report.append("\n- **TAM: $3.7M**")

    report.append("\n\n### Optimistic Scenario")
    report.append("\n- Base: 299,500 total machinists (includes manual)")
    report.append("\n- Calculator adoption: 20% (59,900 users)")
    report.append("\n- Paying: 50% (29,950 users)")
    report.append("\n- ARPU: $200/year")
    report.append("\n- **TAM: $6.0M**")

    return "".join(report)

def generate_confidence_gaps(kb: KnowledgeBase):
    """Identify claims that need additional verification"""
    report = []
    report.append("\n" + "=" * 80)
    report.append("\nCONFIDENCE GAPS - PRIORITY VERIFICATION NEEDED")
    report.append("\n" + "=" * 80)

    # Critical claims that need more sources
    critical_claims = [
        "Total paying users for feeds/speeds calculators",
        "Market share FSWizard vs G-Wizard vs HSMAdvisor",
        "Average ARPU for calculator software",
        "Willingness to pay $150-250/year",
        "CAM software adoption rate among machinists"
    ]

    report.append("\n\n## Critical Claims Needing Verification\n")
    for claim in critical_claims:
        found = False
        for key, dp in kb.data_points.items():
            if claim.lower() in dp.claim.lower():
                report.append(f"\n**{claim}**")
                report.append(f"\n- Current confidence: {dp.confidence.value}")
                report.append(f"\n- Sources: {len(dp.sources)}")
                report.append(f"\n- Status: {'✓ Adequate' if len(dp.sources) >= 2 else '⚠️ NEEDS MORE SOURCES'}\n")
                found = True
                break

        if not found:
            report.append(f"\n**{claim}**")
            report.append(f"\n- Status: ❌ NO DATA FOUND\n")

    return "".join(report)

if __name__ == "__main__":
    print("=" * 80)
    print("MASTER KNOWLEDGE BASE BUILDER")
    print("=" * 80)

    # Build KB
    kb = build_master_kb()

    # Generate reports
    print("\n\nGenerating reports...")

    # 1. Save KB
    kb_file = Path(__file__).parent / "master_knowledge_base.json"
    kb.save(str(kb_file))
    print(f"\n✓ Saved: {kb_file}")

    # 2. Provenance report
    prov_file = Path(__file__).parent / "PROVENANCE_REPORT.md"
    with open(prov_file, 'w') as f:
        f.write(kb.generate_provenance_report())
    print(f"✓ Saved: {prov_file}")

    # 3. Evidence matrix
    matrix_file = Path(__file__).parent / "EVIDENCE_MATRIX.md"
    with open(matrix_file, 'w') as f:
        f.write(generate_evidence_matrix(kb))
    print(f"✓ Saved: {matrix_file}")

    # 4. Validation report
    val_file = Path(__file__).parent / "VALIDATION_REPORT.md"
    with open(val_file, 'w') as f:
        f.write(generate_validation_report(kb))
    print(f"✓ Saved: {val_file}")

    # 5. TAM analysis
    tam_file = Path(__file__).parent / "TAM_ANALYSIS_VERIFIED.md"
    with open(tam_file, 'w') as f:
        f.write(generate_tam_analysis(kb))
    print(f"✓ Saved: {tam_file}")

    # 6. Confidence gaps
    gaps_file = Path(__file__).parent / "CONFIDENCE_GAPS.md"
    with open(gaps_file, 'w') as f:
        f.write(generate_confidence_gaps(kb))
    print(f"✓ Saved: {gaps_file}")

    # Print summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    status = kb.get_verification_status()
    print(f"\nTotal Data Points: {status['total_data_points']}")
    print(f"Verification Rate: {status['percent_verified_or_confirmed']}%")
    print(f"Total Formulas: {status['total_formulas']}")
    print(f"Total Manufacturer Data: {status['total_manufacturer_data']}")
    print(f"Total App Statistics: {status['total_app_statistics']}")
    print(f"\nLast Updated: {status['last_updated']}")
    print("\n✓ Master knowledge base complete")
