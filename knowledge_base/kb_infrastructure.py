#!/usr/bin/env python3
"""
Knowledge Base Infrastructure for CNC Feeds & Speeds Opportunity Analysis
Deterministic, triple-sourced, with full provenance tracking
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Any
from datetime import datetime
from enum import Enum
import json

class SourceType(Enum):
    """Types of information sources"""
    GOVERNMENT = "government"  # BLS, census, etc.
    MANUFACTURER = "manufacturer"  # Tool/machine vendors
    APP_STORE = "app_store"  # Official app store data
    ACADEMIC = "academic"  # Research papers, university
    INDUSTRY_REPORT = "industry_report"  # Market research
    PUBLIC_DOMAIN = "public_domain"  # Historical handbooks
    COMPANY_OFFICIAL = "company_official"  # Official company data
    FORUM_PRIMARY = "forum_primary"  # Direct user quotes

class ConfidenceLevel(Enum):
    """Confidence in data accuracy"""
    VERIFIED = "verified"  # 3+ independent sources agree
    CONFIRMED = "confirmed"  # 2 independent sources agree
    LIKELY = "likely"  # 1 reliable source
    ESTIMATED = "estimated"  # Derived from other data
    SPECULATIVE = "speculative"  # Educated guess
    UNKNOWN = "unknown"  # No data available

@dataclass
class Source:
    """A single information source with full provenance"""
    url: str
    source_type: SourceType
    retrieved_date: str
    title: str
    author: Optional[str] = None
    publication_date: Optional[str] = None
    excerpt: Optional[str] = None  # Relevant quote/data
    archive_url: Optional[str] = None  # Wayback machine, etc.
    notes: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data['source_type'] = self.source_type.value
        return data

@dataclass
class DataPoint:
    """A single piece of data with provenance and validation"""
    claim: str  # What we're claiming
    value: Any  # The actual data
    unit: Optional[str] = None  # "users", "dollars", "percent", etc.
    confidence: ConfidenceLevel = ConfidenceLevel.UNKNOWN
    sources: List[Source] = field(default_factory=list)
    validation_notes: str = ""
    last_verified: str = field(default_factory=lambda: datetime.now().isoformat())
    conflicts: List[str] = field(default_factory=list)  # Conflicting data points

    def add_source(self, source: Source):
        """Add a source and update confidence"""
        self.sources.append(source)
        self._update_confidence()

    def _update_confidence(self):
        """Update confidence based on number and type of sources"""
        if len(self.sources) == 0:
            self.confidence = ConfidenceLevel.UNKNOWN
        elif len(self.sources) == 1:
            # Single source confidence depends on type
            if self.sources[0].source_type in [SourceType.GOVERNMENT, SourceType.ACADEMIC]:
                self.confidence = ConfidenceLevel.CONFIRMED
            else:
                self.confidence = ConfidenceLevel.LIKELY
        elif len(self.sources) == 2:
            self.confidence = ConfidenceLevel.CONFIRMED
        else:
            self.confidence = ConfidenceLevel.VERIFIED

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data['confidence'] = self.confidence.value
        data['sources'] = [s.to_dict() for s in self.sources]
        return data

@dataclass
class Formula:
    """Mathematical formula with sources and validation"""
    name: str
    formula: str  # LaTeX or plain text
    variables: Dict[str, str]  # Variable name -> description
    sources: List[Source] = field(default_factory=list)
    validation_examples: List[Dict[str, Any]] = field(default_factory=list)
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data['sources'] = [s.to_dict() for s in self.sources]
        return data

@dataclass
class ManufacturerData:
    """Tool/machine manufacturer data"""
    manufacturer: str
    product_line: str
    data_type: str  # "cutting_speeds", "tool_specs", "machine_specs"
    data: Dict[str, Any]
    sources: List[Source] = field(default_factory=list)
    last_updated: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data['sources'] = [s.to_dict() for s in self.sources]
        return data

@dataclass
class AppStatistic:
    """App store or company statistics"""
    app_name: str
    metric: str  # "downloads", "reviews", "rating", "users"
    value: Any
    platform: str  # "iOS", "Android", "Web", "All"
    sources: List[Source] = field(default_factory=list)
    methodology: str = ""  # How metric was derived
    confidence: ConfidenceLevel = ConfidenceLevel.UNKNOWN

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data['sources'] = [s.to_dict() for s in self.sources]
        data['confidence'] = self.confidence.value
        return data

class KnowledgeBase:
    """Central knowledge base with validation and provenance"""

    def __init__(self):
        self.data_points: Dict[str, DataPoint] = {}
        self.formulas: Dict[str, Formula] = {}
        self.manufacturer_data: List[ManufacturerData] = []
        self.app_statistics: List[AppStatistic] = []
        self.validation_rules: List[Dict[str, Any]] = []
        self.last_updated = datetime.now().isoformat()

    def add_data_point(self, key: str, data_point: DataPoint):
        """Add or update a data point"""
        if key in self.data_points:
            # Merge sources
            existing = self.data_points[key]
            for source in data_point.sources:
                existing.add_source(source)
            existing.last_verified = datetime.now().isoformat()
        else:
            self.data_points[key] = data_point
        self.last_updated = datetime.now().isoformat()

    def add_formula(self, name: str, formula: Formula):
        """Add a formula with sources"""
        self.formulas[name] = formula
        self.last_updated = datetime.now().isoformat()

    def add_manufacturer_data(self, data: ManufacturerData):
        """Add manufacturer data"""
        self.manufacturer_data.append(data)
        self.last_updated = datetime.now().isoformat()

    def add_app_statistic(self, stat: AppStatistic):
        """Add app statistic"""
        self.app_statistics.append(stat)
        self.last_updated = datetime.now().isoformat()

    def validate_all(self) -> Dict[str, List[str]]:
        """Validate all data points and return issues"""
        issues = {
            "low_confidence": [],
            "no_sources": [],
            "single_source": [],
            "conflicting": []
        }

        for key, dp in self.data_points.items():
            if dp.confidence in [ConfidenceLevel.UNKNOWN, ConfidenceLevel.SPECULATIVE]:
                issues["low_confidence"].append(key)
            if len(dp.sources) == 0:
                issues["no_sources"].append(key)
            elif len(dp.sources) == 1:
                issues["single_source"].append(key)
            if dp.conflicts:
                issues["conflicting"].append(key)

        return issues

    def get_verification_status(self) -> Dict[str, Any]:
        """Get overall verification status"""
        total = len(self.data_points)
        verified = sum(1 for dp in self.data_points.values()
                      if dp.confidence == ConfidenceLevel.VERIFIED)
        confirmed = sum(1 for dp in self.data_points.values()
                       if dp.confidence == ConfidenceLevel.CONFIRMED)

        return {
            "total_data_points": total,
            "verified": verified,
            "confirmed": confirmed,
            "percent_verified_or_confirmed": round((verified + confirmed) / total * 100, 1) if total > 0 else 0,
            "total_formulas": len(self.formulas),
            "total_manufacturer_data": len(self.manufacturer_data),
            "total_app_statistics": len(self.app_statistics),
            "last_updated": self.last_updated
        }

    def save(self, filename: str):
        """Save knowledge base to JSON"""
        data = {
            "metadata": {
                "created": self.last_updated,
                "verification_status": self.get_verification_status()
            },
            "data_points": {k: v.to_dict() for k, v in self.data_points.items()},
            "formulas": {k: v.to_dict() for k, v in self.formulas.items()},
            "manufacturer_data": [m.to_dict() for m in self.manufacturer_data],
            "app_statistics": [s.to_dict() for s in self.app_statistics]
        }

        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def generate_provenance_report(self) -> str:
        """Generate markdown report of all sources and provenance"""
        lines = ["# Knowledge Base Provenance Report\n"]
        lines.append(f"**Generated:** {datetime.now().isoformat()}\n")
        lines.append(f"**Last Updated:** {self.last_updated}\n\n")

        status = self.get_verification_status()
        lines.append("## Verification Status\n\n")
        lines.append(f"- **Total Data Points:** {status['total_data_points']}\n")
        lines.append(f"- **Verified (3+ sources):** {status['verified']}\n")
        lines.append(f"- **Confirmed (2 sources):** {status['confirmed']}\n")
        lines.append(f"- **Verification Rate:** {status['percent_verified_or_confirmed']}%\n\n")

        lines.append("## Data Points by Confidence\n\n")
        by_confidence = {}
        for key, dp in self.data_points.items():
            conf = dp.confidence.value
            if conf not in by_confidence:
                by_confidence[conf] = []
            by_confidence[conf].append((key, dp))

        for conf in ["verified", "confirmed", "likely", "estimated", "speculative", "unknown"]:
            if conf in by_confidence:
                lines.append(f"### {conf.title()} ({len(by_confidence[conf])})\n\n")
                for key, dp in by_confidence[conf]:
                    lines.append(f"**{key}:** {dp.claim}\n")
                    lines.append(f"- Value: {dp.value} {dp.unit or ''}\n")
                    lines.append(f"- Sources: {len(dp.sources)}\n")
                    if dp.sources:
                        for i, src in enumerate(dp.sources, 1):
                            lines.append(f"  {i}. [{src.source_type.value}] {src.title} - {src.url}\n")
                    lines.append("\n")

        return "".join(lines)


if __name__ == "__main__":
    # Example usage
    kb = KnowledgeBase()

    # Add a verified data point
    bls_source = Source(
        url="https://www.bls.gov/oes/current/oes514011.htm",
        source_type=SourceType.GOVERNMENT,
        retrieved_date="2025-11-11",
        title="BLS Occupational Employment Statistics - CNC Tool Operators",
        author="U.S. Bureau of Labor Statistics",
        publication_date="2024"
    )

    machinist_count = DataPoint(
        claim="Total CNC tool operators employed in United States",
        value=187670,
        unit="workers",
        sources=[bls_source]
    )

    kb.add_data_point("us_cnc_operators_2024", machinist_count)

    # Print status
    print(kb.get_verification_status())
    print("\nKnowledge base infrastructure ready.")
