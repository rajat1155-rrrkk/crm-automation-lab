import unittest
import sys
import os

# Adjust path for module import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lead-scoring")))

from lead_scoring_engine import LeadScoringEngine


class TestLeadScoringEngine(unittest.TestCase):

    def test_high_value_industry(self):
        engine = LeadScoringEngine("Technology", 300, 20)
        score = engine.calculate_score()
        self.assertGreaterEqual(score, 30)

    def test_company_size_large(self):
        engine = LeadScoringEngine("Retail", 600, 10)
        score = engine.calculate_score()
        self.assertGreaterEqual(score, 25)

    def test_engagement_cap(self):
        engine = LeadScoringEngine("Retail", 50, 100)
        score = engine.calculate_score()
        self.assertLessEqual(score, 70)


if __name__ == "__main__":
    unittest.main()
