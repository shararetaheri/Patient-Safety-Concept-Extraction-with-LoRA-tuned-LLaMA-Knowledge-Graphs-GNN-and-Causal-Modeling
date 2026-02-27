import re

class WeakLabeler:

    def __init__(self, ontology_dict):
        self.ontology = ontology_dict

    def label(self, text):
        entities = []

        for concept_id, concept in self.ontology.items():
            if re.search(concept["name"], text, re.IGNORECASE):
                entities.append({
                    "id": concept_id,
                    "name": concept["name"]
                })

        return entities
