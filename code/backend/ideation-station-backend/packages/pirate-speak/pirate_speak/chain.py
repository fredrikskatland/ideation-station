from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_anthropic import ChatAnthropic
from langchain_core.pydantic_v1 import BaseModel, Field

from rich.console import Console
from rich.markdown import Markdown

class BusinessConcept(BaseModel):
    headline: str = Field(description="Business or product concept headline")
    description: str = Field(description="Brief description of the concept")
    target_audience: str = Field(description="Target audience for the concept")
    pricing: str = Field(description="How to price the business or product")
    marketing: str = Field(description="How to market the business or product")
    stand_out: str = Field(description="How to make the business or product stand out from competitors")
    dos: str = Field(description="List of dos for the concept")
    donts: str = Field(description="List of don'ts for the concept")

class BusinessPlan(BaseModel):
    milestone_plan: str = Field(description="Milestone plan for the business or product")
    gant_chart: str = Field(description="Gant chart for the business or product")
    raid_chart: str = Field(description="Raid chart for the business or product")
    task_table: str = Field(description="Task table for the business or product")


gpt4 = ChatOpenAI(model="gpt-4o")
claud3 = ChatAnthropic(model='claude-3-opus-20240229')

first_prompt = ChatPromptTemplate.from_template(
    "Develop a business or product concept and around the following topic: {topic}. List dos and don'ts for the concept. Include a brief description of the concept and the target audience, how to price and market the business or product, and how to make it stand out from competitors. The output should be markdown."
)
second_prompt = ChatPromptTemplate.from_template(
    "Create a milestone plan, a gant chart, a raid chart and a task table. based on the following markdown document: {markdown} "
)

concept_parser = JsonOutputParser(pydantic_object=BusinessConcept)
plan_parser = JsonOutputParser(pydantic_object=BusinessPlan)

concept_prompt = PromptTemplate(
    #template="Answer the user query.\n{format_instructions}\n{query}\n",
    template="Develop a business or product concept and around the following topic: {topic}. List dos and don'ts for the concept. Include a brief description of the concept and the target audience, how to price and market the business or product, and how to make it stand out from competitors. \n{format_instructions}. \nInside the json the output should be markdown.",
    input_variables=["topic"],
    partial_variables={"format_instructions": concept_parser.get_format_instructions()},
)

plan_prompt = PromptTemplate(
    #template="Answer the user query.\n{format_instructions}\n{query}\n",
    template="Create a milestone plan, a gant chart, a raid chart and a task table. based on the following json/markdown document: {markdown} \n{format_instructions}. \nInside the json the output should be markdown, without any ```markdown annotations.",
    input_variables=["markdown"],
    partial_variables={"format_instructions": plan_parser.get_format_instructions()},
)

#first_chain =  first_prompt | gpt4 | StrOutputParser()
first_chain =  concept_prompt | gpt4 | concept_parser

#second_chain = second_prompt | gpt4 | StrOutputParser()
second_chain =  plan_prompt | gpt4 | plan_parser

complete_chain = ({
    "topic": itemgetter("topic"),
    "markdown": first_chain
    }
    | RunnablePassthrough.assign(plans=second_chain)
    | RunnablePassthrough.assign(markdown=first_chain)
)

# Testing chain

from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Translate user input into pirate speak",
        ),
        MessagesPlaceholder("chat_history"),
        ("human", "{text}"),
    ]
)
_model = ChatOpenAI()

# if you update this, you MUST also update ../pyproject.toml
# with the new `tool.langserve.export_attr`
chain = _prompt | _model
