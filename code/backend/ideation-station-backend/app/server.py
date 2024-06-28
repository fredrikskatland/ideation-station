from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from langserve import add_routes
from pirate_speak.chains import (
    complete_chain, 
    complete_idea_concept_chain as idea_concept_chain,
    complete_idea_details_chain as idea_details_chain,
    complete_idea_plans_chain as idea_plans_chain,
    complete_idea_quality_chain as idea_quality_chain,
    complete_idea_scamper_chain as idea_scamper_chain,
    complete_idea_gantt_chart_chain as idea_gantt_chart_chain,
)

app = FastAPI()

origins = [
    "http://localhost:5173",  # Vue app
    "http://localhost:8000",  # FastAPI server (change to your FastAPI server URL)
    "https://ideation-station.vercel.app",  # Vercel deployment
    "https://ideationstation.ai",
    "https://www.ideationstation.ai",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
add_routes(app, complete_chain, path="/complete-chain")
add_routes(app, idea_concept_chain, path="/idea-concept-chain")
add_routes(app, idea_details_chain, path="/idea-details-chain")
add_routes(app, idea_plans_chain, path="/idea-plans-chain")
add_routes(app, idea_quality_chain, path="/idea-quality-chain")
add_routes(app, idea_scamper_chain, path="/idea-scamper-chain")
add_routes(app, idea_gantt_chart_chain, path="/idea-gantt-chart-chain")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)