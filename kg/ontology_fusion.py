class OntologyFusionEngine:

    def __init__(self, umls, snomed, icps):
        self.umls = umls
        self.snomed = snomed
        self.icps = icps

    def merge(self):
        unified = {}

        for concept in self.umls:
            unified[concept["id"]] = concept

        for concept in self.snomed:
            unified.setdefault(concept["id"], concept)

        for concept in self.icps:
            unified.setdefault(concept["id"], concept)

        return unified
