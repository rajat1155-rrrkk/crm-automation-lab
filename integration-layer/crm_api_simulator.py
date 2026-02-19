class CRMAPISimulator:
    """
    Simulates REST-style CRM integration behavior.
    """

    def __init__(self):
        self.database = {}

    def create_lead(self, lead_id, data):
        self.database[lead_id] = data
        return {"status": "success", "message": "Lead created"}

    def get_lead(self, lead_id):
        return self.database.get(lead_id, {"status": "error", "message": "Lead not found"})

    def update_lead(self, lead_id, updates):
        if lead_id not in self.database:
            return {"status": "error", "message": "Lead not found"}

        self.database[lead_id].update(updates)
        return {"status": "success", "message": "Lead updated"}
