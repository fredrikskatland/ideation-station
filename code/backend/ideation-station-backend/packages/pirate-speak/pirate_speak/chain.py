from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_anthropic import ChatAnthropic
from langchain_core.pydantic_v1 import BaseModel, Field

from rich.console import Console
from rich.markdown import Markdown

from typing import List, Optional
from datetime import date

class MilestoneTask(BaseModel):
    id: int
    name: str
    description: str
    status: str
    due_date: date

class Milestone(BaseModel):
    id: int
    name: str
    description: str
    start_date: date
    end_date: date
    tasks: List[MilestoneTask]

class MilestonePlan(BaseModel):
    project_name: str
    milestones: List[Milestone]

class Task(BaseModel):
    id: int
    name: str
    start_date: date
    end_date: date
    status: str

class GanttChart(BaseModel):
    project_name: str
    tasks: List[Task]

class Risk(BaseModel):
    id: int
    description: str
    probability: str
    impact: str
    mitigation_plan: str

class Assumption(BaseModel):
    id: int
    description: str
    status: str
    owner: str

class Issue(BaseModel):
    id: int
    description: str
    severity: str
    resolution_plan: str

class Dependency(BaseModel):
    id: int
    description: str
    due_date: date
    status: str

class RAID(BaseModel):
    risks: List[Risk]
    assumptions: List[Assumption]
    issues: List[Issue]
    dependencies: List[Dependency]

class RAIDChart(BaseModel):
    project_name: str
    raid: RAID

class BusinessConcept(BaseModel):
    headline: str = Field(description="Business or product concept headline")
    description: str = Field(description="Brief description of the concept")
    target_audience: str = Field(description="Target audience for the concept")
    pricing: str = Field(description="How to price the business or product")
    marketing: str = Field(description="How to market the business or product")
    stand_out: str = Field(description="How to make the business or product stand out from competitors")
    dos: List[str] = Field(description="List of dos for the concept")
    donts: List[str] = Field(description="List of don'ts for the concept")

class BusinessPlan(BaseModel):
    milestone_plan: MilestonePlan = Field(description="Milestone plan for the business or product")
    gant_chart: GanttChart = Field(description="Gant chart for the business or product")
    raid_chart: RAIDChart = Field(description="Raid chart for the business or product")
    task_table: str = Field(description="Task table for the business or product")


gpt4 = ChatOpenAI(model="gpt-4o")
claud3 = ChatAnthropic(model='claude-3-opus-20240229')

first_prompt = ChatPromptTemplate.from_template(
    "Develop a business or product concept and around the following topic: {topic}. List dos and don'ts for the concept. Include a brief description of the concept and the target audience, how to price and market the business or product, and how to make it stand out from competitors. The output should be markdown."
)
second_prompt = ChatPromptTemplate.from_template(
    "Create a milestone plan, a gant chart, a raid chart and a task table. based on the following json file: {concept} "
)

concept_parser = JsonOutputParser(pydantic_object=BusinessConcept)
plan_parser = JsonOutputParser(pydantic_object=BusinessPlan)

concept_prompt = PromptTemplate(
    #template="Answer the user query.\n{format_instructions}\n{query}\n",
    template="Develop a business or product concept and around the following topic: {topic}. List dos and don'ts for the concept. Include a brief description of the concept and the target audience, how to price and market the business or product, and how to make it stand out from competitors. \n{format_instructions}.",
    input_variables=["topic"],
    partial_variables={"format_instructions": concept_parser.get_format_instructions()},
)

plan_prompt = PromptTemplate(
    #template="Answer the user query.\n{format_instructions}\n{query}\n",
    template="Create a milestone plan, a gant chart, a raid chart and a task table based on the following json file: {concept} \n{format_instructions}.",
    input_variables=["concept"],
    partial_variables={"format_instructions": plan_parser.get_format_instructions()},
)

#first_chain =  first_prompt | gpt4 | StrOutputParser()
first_chain =  concept_prompt | gpt4 | concept_parser

#second_chain = second_prompt | gpt4 | StrOutputParser()
second_chain =  plan_prompt | gpt4 | plan_parser

complete_chain = ({
    "topic": itemgetter("topic"),
    "concept": first_chain
    }
    | RunnablePassthrough.assign(plans=second_chain)
    | RunnablePassthrough.assign(concept=first_chain)
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
