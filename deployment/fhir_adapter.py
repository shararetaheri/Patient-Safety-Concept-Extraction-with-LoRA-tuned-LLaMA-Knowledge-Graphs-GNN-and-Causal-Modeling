import requests

class FHIRAdapter:

    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_patient_records(self, patient_id):
        response = requests.get(
            f"{self.base_url}/Patient/{patient_id}"
        )
        return response.json()
