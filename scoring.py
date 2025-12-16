def calculate_score(row):
    score = 0

    # Role Fit
    high_intent_titles = [
        "Director of Toxicology",
        "Head of Preclinical Safety",
        "VP Safety Assessment"
    ]
    if any(title.lower() in row["Title"].lower() for title in high_intent_titles):
        score += 30

    # Funding Intent
    if row["Funding_Stage"] in ["Series A", "Series B"]:
        score += 20

    # Scientific Intent
    if row["Published_Last_2_Years"] == "Yes":
        score += 40

    # Keywords relevance
    keywords = row["Keywords"].lower()
    if any(k in keywords for k in ["3d", "liver", "toxicity", "hepatic"]):
        score += 15

    # Location Hub
    hubs = ["boston", "cambridge", "bay area", "basel"]
    if any(hub in row["Company_HQ"].lower() for hub in hubs):
        score += 10

    return min(score, 100)