#!/usr/bin/env python3
"""
App Opportunity Research Framework
Identifies declining popular apps with AI enhancement potential
"""

import json
import re
from dataclasses import dataclass, asdict
from typing import List, Dict, Any
from datetime import datetime
from enum import Enum

class Category(Enum):
    PRODUCTIVITY = "productivity"
    CREATIVE = "creative"
    TECHNICAL = "technical"
    LIFESTYLE = "lifestyle"
    EDUCATION = "education"
    BUSINESS = "business"

class DeclineReason(Enum):
    ABANDONED = "abandoned_by_developer"
    OUTDATED_UX = "outdated_user_experience"
    TECHNICAL_DEBT = "technical_debt"
    MARKET_SHIFT = "market_shift"
    LACK_OF_INNOVATION = "lack_of_innovation"

@dataclass
class AppOpportunity:
    """Data model for app opportunity analysis"""
    name: str
    category: Category
    description: str

    # Popularity metrics
    peak_popularity_year: int
    estimated_peak_users: str
    current_status: str

    # Decline analysis
    decline_reasons: List[DeclineReason]
    last_major_update: str

    # User base analysis
    community_size: str
    user_sentiment: str  # positive/mixed/frustrated
    unmet_needs: List[str]

    # AI enhancement potential
    ai_opportunities: List[str]
    technical_feasibility: str  # high/medium/low
    market_impact_potential: str  # revolutionary/significant/moderate

    # Supporting evidence
    sources: List[str]
    forum_discussions: List[str]

    # Scoring
    opportunity_score: float = 0.0

    def calculate_score(self) -> float:
        """Calculate composite opportunity score (0-100)"""
        score = 0.0

        # User base strength (0-25)
        if "million" in self.estimated_peak_users.lower():
            score += 25
        elif "thousand" in self.estimated_peak_users.lower():
            score += 15
        else:
            score += 10

        # Decline creates opportunity (0-20)
        score += len(self.decline_reasons) * 5

        # Community engagement (0-20)
        if self.user_sentiment == "frustrated":
            score += 20  # Frustrated users = opportunity
        elif self.user_sentiment == "mixed":
            score += 12
        else:
            score += 5

        # AI potential (0-25)
        if self.market_impact_potential == "revolutionary":
            score += 25
        elif self.market_impact_potential == "significant":
            score += 15
        else:
            score += 8

        # Technical feasibility (0-10)
        if self.technical_feasibility == "high":
            score += 10
        elif self.technical_feasibility == "medium":
            score += 6
        else:
            score += 2

        self.opportunity_score = min(score, 100.0)
        return self.opportunity_score

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        data = asdict(self)
        data['category'] = self.category.value
        data['decline_reasons'] = [r.value for r in self.decline_reasons]
        return data


class ResearchAggregator:
    """Aggregates and analyzes research findings"""

    def __init__(self):
        self.opportunities: List[AppOpportunity] = []

    def add_opportunity(self, opp: AppOpportunity):
        """Add and score an opportunity"""
        opp.calculate_score()
        self.opportunities.append(opp)

    def get_top_opportunities(self, n: int = 5) -> List[AppOpportunity]:
        """Get top N opportunities by score"""
        sorted_opps = sorted(
            self.opportunities,
            key=lambda x: x.opportunity_score,
            reverse=True
        )
        return sorted_opps[:n]

    def save_results(self, filename: str = "research_results.json"):
        """Save results to JSON"""
        data = {
            "timestamp": datetime.now().isoformat(),
            "total_opportunities_analyzed": len(self.opportunities),
            "opportunities": [opp.to_dict() for opp in self.opportunities]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def generate_report(self) -> str:
        """Generate markdown report of top opportunities"""
        top_5 = self.get_top_opportunities(5)

        report = ["# Top 5 App Revitalization Opportunities\n"]
        report.append(f"*Analysis completed: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")
        report.append(f"*Total apps analyzed: {len(self.opportunities)}*\n\n")

        for idx, opp in enumerate(top_5, 1):
            report.append(f"## {idx}. {opp.name} (Score: {opp.opportunity_score:.1f}/100)\n")
            report.append(f"**Category:** {opp.category.value}\n")
            report.append(f"**Description:** {opp.description}\n\n")

            report.append(f"### Popularity Timeline\n")
            report.append(f"- **Peak:** {opp.peak_popularity_year} (~{opp.estimated_peak_users})\n")
            report.append(f"- **Current Status:** {opp.current_status}\n")
            report.append(f"- **Last Major Update:** {opp.last_major_update}\n\n")

            report.append(f"### Why It Declined\n")
            for reason in opp.decline_reasons:
                report.append(f"- {reason.value.replace('_', ' ').title()}\n")
            report.append("\n")

            report.append(f"### User Base Analysis\n")
            report.append(f"- **Community Size:** {opp.community_size}\n")
            report.append(f"- **Sentiment:** {opp.user_sentiment}\n")
            report.append(f"- **Unmet Needs:**\n")
            for need in opp.unmet_needs:
                report.append(f"  - {need}\n")
            report.append("\n")

            report.append(f"### AI Revolution Potential\n")
            report.append(f"- **Market Impact:** {opp.market_impact_potential}\n")
            report.append(f"- **Technical Feasibility:** {opp.technical_feasibility}\n")
            report.append(f"- **AI Opportunities:**\n")
            for ai_opp in opp.ai_opportunities:
                report.append(f"  - {ai_opp}\n")
            report.append("\n")

            if opp.forum_discussions:
                report.append(f"### Community Evidence\n")
                for disc in opp.forum_discussions[:3]:  # Top 3
                    report.append(f"- {disc}\n")
                report.append("\n")

            report.append("---\n\n")

        return "".join(report)


# Helper functions for research
def create_search_queries() -> Dict[str, List[str]]:
    """Generate search queries for different research vectors"""
    return {
        "app_decline": [
            "once popular apps that declined",
            "abandoned apps with loyal users",
            "outdated apps that need updates",
            "legacy software with active community",
            "popular apps from 2010-2015 discontinued"
        ],
        "specific_categories": [
            "declining productivity apps AI potential",
            "abandoned creative tools still used",
            "outdated technical software modernization",
            "legacy CNC software feeds speeds",
            "old CAD tools need update"
        ],
        "forums_communities": [
            "reddit apps wish would update",
            "hacker news abandoned software",
            "users frustrated outdated app",
            "app hasn't been updated years still use"
        ],
        "ai_opportunities": [
            "software AI could improve dramatically",
            "manual workflows AI automation",
            "apps need intelligent features",
            "AI enhancement opportunities legacy software"
        ]
    }


if __name__ == "__main__":
    # Initialize aggregator
    aggregator = ResearchAggregator()

    # Example opportunity (to be populated by research)
    example = AppOpportunity(
        name="Feeds & Speeds Calculator for CNC",
        category=Category.TECHNICAL,
        description="CNC machining calculation tools for optimal cutting parameters",
        peak_popularity_year=2012,
        estimated_peak_users="100k machinists",
        current_status="Multiple fragmented apps, mostly outdated",
        decline_reasons=[
            DeclineReason.OUTDATED_UX,
            DeclineReason.LACK_OF_INNOVATION
        ],
        last_major_update="2-5 years ago (varies by app)",
        community_size="Active machinist forums, 50k+ users",
        user_sentiment="frustrated",
        unmet_needs=[
            "Modern, intuitive interface",
            "Integration with CAM software",
            "Material database updates",
            "Machine-specific optimization",
            "Learning from past jobs"
        ],
        ai_opportunities=[
            "AI-powered parameter optimization based on material, tool, and machine",
            "Computer vision to analyze chip formation and suggest adjustments",
            "Predictive modeling for tool wear and surface finish",
            "Natural language interface: 'What feeds/speeds for 6061 aluminum with 1/4 endmill?'",
            "Learning system that improves recommendations based on user outcomes"
        ],
        technical_feasibility="high",
        market_impact_potential="revolutionary",
        sources=[],
        forum_discussions=[]
    )

    aggregator.add_opportunity(example)

    print("Research Framework Initialized")
    print(f"Search Queries Generated: {sum(len(v) for v in create_search_queries().values())}")
    print("\nExample Opportunity Score:", example.opportunity_score)
