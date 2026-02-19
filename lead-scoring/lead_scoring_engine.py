class LeadScoringEngine:
    """
    Basic CRM Lead Scoring Engine.
    Simulates enterprise-style scoring logic based on business rules.
    """

    def __init__(self, industry, company_size, engagement_score):
        self.industry = industry
        self.company_size = company_size
        self.engagement_score = engagement_score

    def calculate_score(self):
        score = 0

        # Industry weighting
        high_value_industries = ["Technology", "Finance", "Healthcare"]
        if self.industry in high_value_industries:
            score += 30

        # Company size weighting
        if self.company_size > 500:
            score += 25
        elif self.company_size > 100:
            score += 15
        else:
            score += 5

        # Engagement weighting (capped at 40)
        score += min(self.engagement_score, 40)

        return score


if __name__ == "__main__":
    lead = LeadScoringEngine(
        industry="Technology",
        company_size=300,
        engagement_score=32
    )
    print("Lead Score:", lead.calculate_score())
