def extract_observations(text):
    observations = []

    text_lower = text.lower()

    if "dampness" in text_lower:
        observations.append("Dampness observed on north wall")

    if "tile hollowness" in text_lower:
        observations.append("Tile hollowness observed near entrance")

    return observations