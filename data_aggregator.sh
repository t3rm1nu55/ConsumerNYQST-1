#!/bin/bash
# Data Aggregation Script for Research Results

RESULTS_DIR="./research_results"
mkdir -p "$RESULTS_DIR"

echo "Data Aggregator Initialized"
echo "Results directory: $RESULTS_DIR"
echo ""
echo "This script will aggregate findings from parallel research streams"
echo "Each agent will write to: $RESULTS_DIR/<agent_id>.json"
echo ""
echo "Aggregation strategy:"
echo "  1. Deduplication by app name"
echo "  2. Sentiment scoring"
echo "  3. Opportunity ranking"
echo "  4. Top 5 selection"
