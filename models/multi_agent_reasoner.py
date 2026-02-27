class MultiAgentReasoner:

    def __init__(self,
                 ontology_agent,
                 kg_agent,
                 rag_agent,
                 llm_agent,
                 temporal_agent):

        self.ontology = ontology_agent
        self.kg = kg_agent
        self.rag = rag_agent
        self.llm = llm_agent
        self.temporal = temporal_agent

    def analyze(self, ehr_text, timeline):

        ontology_context = self.ontology.label(ehr_text)
        evidence = self.rag.generate(ehr_text)
        llm_analysis = self.llm.generate(ehr_text)

        temporal_risk = self.temporal(timeline)

        return {
            "ontology_entities": ontology_context,
            "evidence": evidence,
            "llm_analysis": llm_analysis,
            "temporal_risk_score": temporal_risk.item()
}
