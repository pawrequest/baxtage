import contextlib
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from neontology import init_neontology


@contextlib.asynccontextmanager
async def lifespan(app):
    init_neontology(
        neo4j_uri="bolt://localhost:7687",
        neo4j_username="neo4j",
        neo4j_password="password",
    )
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"foo": "bar"}


@app.post("/teams/")
async def create_(team: TeamNode):
    team.create()

    return team


@app.get("/teams/")
async def get_teams() -> List[TeamNode]:
    return TeamNode.match_nodes()


@app.get("/teams/{pp}")
async def get_team(pp: str) -> Optional[TeamNode]:
    return TeamNode.match(pp)


@app.post("/team-members/")
async def create_team_member(member: TeamMemberNode, team_name: str):
    team = TeamNode.match(team_name)

    if team is None:
        raise HTTPException(status_code=404, detail="Team doesn't exist")

    member.create()

    rel = BelongsTo(source=member, target=team)
    rel.merge()

    return member


@app.get("/team-members/")
async def get_team_members() -> List[TeamMemberNode]:
    return TeamMemberNode.match_nodes()


@app.get("/team-members/{pp}")
async def get_team_member(pp: str) -> Optional[TeamMemberNode]:
    return TeamMemberNode.match(pp)
