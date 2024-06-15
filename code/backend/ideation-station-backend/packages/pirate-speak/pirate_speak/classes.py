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
    gantt_chart: GanttChart = Field(description="Gant chart for the business or product")
    raid_chart: RAIDChart = Field(description="Raid chart for the business or product")

class IdeaConcept(BaseModel):
    headline: str = Field(description="Concept headline")
    description: str = Field(description="Brief description of the concept/product")

class IdeaDetails(BaseModel):
    target_audience: str = Field(description="Target audience for the concept")
    pricing: str = Field(description="How to price the business or product")
    marketing: str = Field(description="How to market the business or product")
    stand_out: str = Field(description="How to make the business or product stand out from competitors")
    dos: List[str] = Field(description="List of dos for the concept")
    donts: List[str] = Field(description="List of don'ts for the concept")

