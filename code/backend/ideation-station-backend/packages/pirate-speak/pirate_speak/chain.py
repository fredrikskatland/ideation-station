from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_anthropic import ChatAnthropic

from rich.console import Console
from rich.markdown import Markdown

gpt4 = ChatOpenAI(model="gpt-4o")
claud3 = ChatAnthropic(model='claude-3-opus-20240229')

first_prompt = ChatPromptTemplate.from_template(
    "Develop a business or product concept and around the following topic: {topic}. List dos and don'ts for the concept. Include a brief description of the concept and the target audience, how to price and market the business or product, and how to make it stand out from competitors. The output should be markdown."
)
second_prompt = ChatPromptTemplate.from_template(
    "Create a milestone plan, a gant chart, a raid chart and a task table. based on the following markdown document: {markdown} "
)

first_chain =  first_prompt | gpt4 | StrOutputParser()

second_chain = second_prompt | gpt4 | StrOutputParser()

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
