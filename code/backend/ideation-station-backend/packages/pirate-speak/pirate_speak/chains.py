from operator import itemgetter
from datetime import datetime

from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
#from langchain_anthropic import ChatAnthropic

from pirate_speak.prompts import concept_prompt, plan_prompt, idea_concept_prompt, idea_details_prompt, idea_quality_prompt, idea_scamper_prompt, idea_gantt_chart_prompt
from pirate_speak.parsers import concept_parser, plan_parser, idea_concept_parser, idea_details_parser, idea_quality_parser, idea_scamper_parser, idea_gantt_chart_parser

gpt4 = ChatOpenAI(model="gpt-4o")
#claud3 = ChatAnthropic(model='claude-3-opus-20240229')

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

# New

# Idea concept
idea_concept_chain = idea_concept_prompt | gpt4 | idea_concept_parser

complete_idea_concept_chain = ({
    "topic": itemgetter("topic"),
    "concept": idea_concept_chain
    }
    | RunnablePassthrough.assign(concept=idea_concept_chain)
)


# Idea details
idea_details_chain = idea_details_prompt | gpt4 | idea_details_parser

complete_idea_details_chain = ({
    "concept_description": itemgetter("concept_description"),
    "details": idea_details_chain
    }
    | RunnablePassthrough.assign(details=idea_details_chain)
)

# Idea plans
idea_plans_chain = plan_prompt | gpt4 | plan_parser

complete_idea_plans_chain = ({
    "concept_details": itemgetter("concept_details"),
    "plans": idea_plans_chain
    }
    | RunnablePassthrough.assign(plans=idea_plans_chain)
)

# Idea quality
idea_quality_chain = idea_quality_prompt | gpt4 | idea_quality_parser

complete_idea_quality_chain = ({
    "concept_description": itemgetter("concept_details"),
    "quality": idea_quality_chain
    }
    | RunnablePassthrough.assign(quality=idea_quality_chain)
)

# Idea scamper
idea_scamper_chain = idea_scamper_prompt | gpt4 | idea_scamper_parser

complete_idea_scamper_chain = ({
    "concept_description": itemgetter("concept_description"),
    "scamper": idea_scamper_chain
    }
    | RunnablePassthrough.assign(scamper=idea_scamper_chain)
)

# Idea gantt chart
idea_gantt_chart_chain = idea_gantt_chart_prompt | gpt4 | idea_gantt_chart_parser

complete_idea_gantt_chart_chain = ({
    "concept_details": itemgetter("concept_details"),
    "gantt_chart": idea_gantt_chart_chain
    }
    | RunnablePassthrough.assign(gantt_chart=idea_gantt_chart_chain)
)

