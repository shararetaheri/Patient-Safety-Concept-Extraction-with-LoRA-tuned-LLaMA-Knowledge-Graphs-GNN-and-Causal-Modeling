class AutoAnnotator:

    def __init__(self, weak_labeler):
        self.labeler = weak_labeler

    def annotate(self, text):
        entities = self.labeler.label(text)

        relations = []
        for e in entities:
            if "medication" in text.lower():
                relations.append(
                    (e["name"], "ASSOCIATED_WITH", "Medication")
                )

        return {
            "text": text,
            "entities": entities,
            "relations": relations
        }
