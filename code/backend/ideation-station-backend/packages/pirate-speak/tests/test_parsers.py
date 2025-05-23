import types
import sys
import json

# Stub langchain_core modules if not installed
if 'langchain_core' not in sys.modules:
    langchain_core = types.ModuleType('langchain_core')
    sys.modules['langchain_core'] = langchain_core

if 'langchain_core.pydantic_v1' not in sys.modules:
    import pydantic
    pydantic_v1 = types.ModuleType('langchain_core.pydantic_v1')
    pydantic_v1.BaseModel = pydantic.BaseModel
    pydantic_v1.Field = pydantic.Field
    sys.modules['langchain_core.pydantic_v1'] = pydantic_v1
    langchain_core.pydantic_v1 = pydantic_v1

if 'langchain_core.output_parsers' not in sys.modules:
    class JsonOutputParser:
        def __init__(self, pydantic_object):
            self.pydantic_object = pydantic_object
        def parse(self, text):
            data = json.loads(text)
            return self.pydantic_object.parse_obj(data)
    output_parsers = types.ModuleType('langchain_core.output_parsers')
    output_parsers.JsonOutputParser = JsonOutputParser
    sys.modules['langchain_core.output_parsers'] = output_parsers
    langchain_core.output_parsers = output_parsers

# Now import the parser and model
sys.path.append('code/backend/ideation-station-backend/packages/pirate-speak')
from pirate_speak.parsers import plan_parser
from pirate_speak.classes import BusinessPlan


def test_plan_parser_parses_business_plan():
    sample = {
        "milestone_plan": {
            "project_name": "Treasure Hunt",
            "milestones": [
                {
                    "id": 1,
                    "name": "Start",
                    "description": "Plan the map",
                    "start_date": "2024-01-01",
                    "end_date": "2024-01-05",
                    "tasks": [
                        {
                            "id": 1,
                            "name": "Gather crew",
                            "description": "Find mates",
                            "status": "complete",
                            "due_date": "2024-01-02"
                        }
                    ]
                }
            ]
        },
        "gantt_chart": {
            "project_name": "Treasure Hunt",
            "tasks": [
                {
                    "id": 1,
                    "name": "Sail",
                    "start_date": "2024-01-01",
                    "end_date": "2024-01-10",
                    "status": "ongoing",
                    "label": "voyage"
                }
            ]
        },
        "raid_chart": {
            "project_name": "Treasure Hunt",
            "raid": {
                "risks": [
                    {
                        "id": 1,
                        "description": "Storm",
                        "probability": "low",
                        "impact": "medium",
                        "mitigation_plan": "Check weather"
                    }
                ],
                "assumptions": [
                    {
                        "id": 1,
                        "description": "Crew healthy",
                        "status": "open",
                        "owner": "captain"
                    }
                ],
                "issues": [
                    {
                        "id": 1,
                        "description": "Leak",
                        "severity": "high",
                        "resolution_plan": "Fix hull"
                    }
                ],
                "dependencies": [
                    {
                        "id": 1,
                        "description": "Supplies",
                        "due_date": "2024-01-01",
                        "status": "confirmed"
                    }
                ]
            }
        }
    }

    result = plan_parser.parse(json.dumps(sample))
    assert isinstance(result, BusinessPlan)
    assert result.milestone_plan.project_name == "Treasure Hunt"
    assert result.gantt_chart.tasks[0].label == "voyage"
    assert result.raid_chart.raid.risks[0].description == "Storm"
