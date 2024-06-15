from langchain_core.output_parsers import JsonOutputParser
from pirate_speak.classes import BusinessConcept, BusinessPlan, IdeaConcept, IdeaDetails

# Old
plan_parser = JsonOutputParser(pydantic_object=BusinessPlan)
concept_parser = JsonOutputParser(pydantic_object=BusinessConcept)

# New
idea_concept_parser = JsonOutputParser(pydantic_object=IdeaConcept)
idea_details_parser = JsonOutputParser(pydantic_object=IdeaDetails)

