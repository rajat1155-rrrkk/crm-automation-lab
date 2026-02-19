class OpportunityValidator:
    """
    Simulates stage-based opportunity validation logic
    in a CRM workflow.
    """

    REQUIRED_FIELDS_BY_STAGE = {
        "Qualification": ["budget_confirmed"],
        "Proposal": ["budget_confirmed", "technical_approval"],
        "Closed Won": ["budget_confirmed", "technical_approval", "legal_approval"]
    }

    def __init__(self, stage, data):
        self.stage = stage
        self.data = data

    def validate(self):
        required_fields = self.REQUIRED_FIELDS_BY_STAGE.get(self.stage, [])
        missing_fields = []

        for field in required_fields:
            if not self.data.get(field):
                missing_fields.append(field)

        return {
            "is_valid": len(missing_fields) == 0,
            "missing_fields": missing_fields
        }
