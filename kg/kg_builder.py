from neo4j import GraphDatabase

class KGBuilder:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def create_concept(self, concept_id, name):
        with self.driver.session() as session:
            session.run(
                "MERGE (c:Concept {id:$id, name:$name})",
                id=concept_id,
                name=name
            )

    def create_relation(self, source, target, rel):
        with self.driver.session() as session:
            session.run(
                f"""
                MATCH (a:Concept {{id:$source}})
                MATCH (b:Concept {{id:$target}})
                MERGE (a)-[:{rel}]->(b)
                """,
                source=source,
                target=target
            )
