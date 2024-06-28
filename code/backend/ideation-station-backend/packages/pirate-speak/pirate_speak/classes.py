from langchain_core.pydantic_v1 import BaseModel, Field
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
    name: str = Field(description="Short descriptive name of the task")
    start_date: date = Field(description="Start date of the task")
    end_date: date = Field(description="End date of the task")
    status: str = Field(description="Status of the task")
    label: str = Field(description="Label of the task, for example marketing, UX, development, administration, etc.")

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
    gantt_chart: GanttChart = Field(description="Gant chart for the business or product")
    raid_chart: RAIDChart = Field(description="Raid chart for the business or product")

class IdeaConcept(BaseModel):
    headline: str = Field(description="Concept headline. Not too tabloid.")
    description: str = Field(description="Brief description of the concept/product. Do not be too tabloid, be concise and to the point and describe the concept/product in a clear manner.")

class IdeaDetails(BaseModel):
    target_audience: str = Field(description="Target audience for the concept. Take the type of product or concept into deep consideration and come up with a target audience that would be interested in the product or concept.")
    pricing: str = Field(description="How to price the business or product. Do not be generic, think about the target audience and the product or concept and come up with a pricing strategy that would be appealing to the target audience.")
    marketing: str = Field(description="How to market the business or product. Think about the target audience and the product or concept and come up with a marketing strategy that would be appealing to the target audience.")
    stand_out: str = Field(description="How to make the business or product stand out from competitors. Consider the competitive landscape, and come up with a unique selling proposition that would make the product or concept stand out from competitors, if there is any.")
    dos: List[str] = Field(description="List of dos for the concept. Do not be too generic. Consider the target audience and the product or concept and come up with a list of dos that would be appealing to the target audience.")
    donts: List[str] = Field(description="List of don'ts for the concept. Do not be too generic. Consider the target audience and the product or concept and come up with a list of don'ts that would be appealing to the target audience.")

class IdeaQuality(BaseModel):
    originality: float = Field(description="How original is the idea, totally unique or copy-cat. Give a rating from 0 to 100 where 0 is complete copy and 100 is totally unique")    
    feasibility: float = Field(description="Feasibility of the idea. Give a rating from 0 to 100 where 0 is not feasible and 100 is totally feasible")
    difficulty: float = Field(description="Technical difficulty executing the idea. Give a rating from 0 to 100 where 0 very easy and 100 very difficult")
    profitability: float = Field(description="Profitability of the idea. How easy is it to monetize this idea? Give a rating from 0 to 100 where 0 is not profitable and 100 is very profitable")
    description: str = Field(description="Brief rundown of reasons and arguments for the ratings")

class Scamper(BaseModel):
    substitute: str = Field(description="Substitute something in the idea")
    combine: str = Field(description="Combine the idea with something else")
    adapt: str = Field(description="Adapt something in the idea")
    modify: str = Field(description="Modify something in the idea")
    put_to_other_use: str = Field(description="Put the idea to other uses")
    eliminate: str = Field(description="Eliminate something in the idea")
    rearrange: str = Field(description="Reverse something in the idea")