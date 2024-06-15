from langchain_core.prompts import PromptTemplate
from pirate_speak.parsers import concept_parser, plan_parser, idea_concept_parser, idea_details_parser

# Old
concept_prompt = PromptTemplate(
    #template="Answer the user query.\n{format_instructions}\n{query}\n",
    template="Develop a business or product concept and around the following topic: {topic}. List dos and don'ts for the concept. Include a brief description of the concept and the target audience, how to price and market the business or product, and how to make it stand out from competitors. \n{format_instructions}.",
    input_variables=["topic"],
    partial_variables={"format_instructions": concept_parser.get_format_instructions()},
)

plan_prompt = PromptTemplate(
    #template="Answer the user query.\n{format_instructions}\n{query}\n",
    template="Create a milestone plan, a gant chart, a raid chart and a task table based on the following concept details: {concept_details} \n{format_instructions}.",
    input_variables=["concept_details"],
    partial_variables={"format_instructions": plan_parser.get_format_instructions()},
)

# New
idea_concept_prompt = PromptTemplate(
    template="Develop a business or product concept and around the following topic: {topic}. Create a catchy headline and a detailed description which captures the readers interest. \n{format_instructions}.",
    input_variables=["topic"],
    partial_variables={"format_instructions": idea_concept_parser.get_format_instructions()},
)

idea_details_prompt = PromptTemplate(
    template="Based on the following concept, create useful details that helps the user understand and execute the idea/business concept. \n\nConcept: {concept_description}. \n\nList dos and don'ts for the concept. Include a description of the target audience, how to price and market the business or product, and how to make it stand out from potential competitors. \n{format_instructions}.",
    input_variables=["concept_description"],
    partial_variables={"format_instructions": idea_details_parser.get_format_instructions()},
)