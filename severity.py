def calculate_severity(observations):

    high_risk_keywords = [
        "leakage",
        "structural crack",
        "severe dampness",
        "water seepage"
    ]

    for obs in observations:
        if any(keyword in obs.lower() for keyword in high_risk_keywords):
            return (
                "HIGH",
                "Critical issue detected requiring immediate attention."
            )

    count = len(observations)

    if count >= 3:
        return (
            "HIGH",
            "Multiple affected areas and moisture-related issues detected."
        )
    elif count == 2:
        return (
            "MEDIUM",
            "More than one affected area identified."
        )
    else:
        return (
            "LOW",
            "Limited impact observed."
        )