from observation_extractor import extract_observations
from severity import calculate_severity
from missing_info import get_missing_info

def generate_ddr(inspection_text, thermal_text):

    observations = extract_observations(inspection_text)

    severity, reason = calculate_severity(
        observations
    )

    missing = get_missing_info(
        inspection_text
    )

    root_cause = """
Possible water seepage through external walls,
moisture ingress, or plumbing leakage.
"""

    report = f"""
PROPERTY ISSUE SUMMARY

Multiple dampness and moisture-related issues were identified during inspection.

AREA-WISE OBSERVATIONS

{chr(10).join(observations)}

THERMAL ANALYSIS

Temperature variations were observed in the thermal report.
These variations may indicate moisture ingress, hidden leakage,
or damp affected areas.

PROBABLE ROOT CAUSE

{root_cause}

SEVERITY ASSESSMENT

Severity Level: {severity}

Reason:
{reason}

RECOMMENDED ACTIONS

1. Inspect plumbing lines.
2. Waterproof affected areas.
3. Repair damp affected wall sections.
4. Replace damaged tiles where necessary.
5. Conduct follow-up thermal inspection after repairs.

MISSING INFORMATION

{chr(10).join(missing)}

ADDITIONAL NOTES

This DDR report was generated automatically using
inspection and thermal reports.
"""

    return report