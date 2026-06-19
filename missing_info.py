def get_missing_info(text):

    missing = []

    if "Customer Name" in text:
        missing.append("Customer Name: Not Available")

    if "Email:" in text:
        missing.append("Email: Not Available")

    if "Address:" in text:
        missing.append("Address: Not Available")

    if not missing:
        missing.append("No missing information detected.")

    return missing