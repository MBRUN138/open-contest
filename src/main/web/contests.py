from code.util import register
from code.util.db import Contest, Problem
import json

def deleteContest(params, setHeader, user):
    id = params["id"]
    Contest.get(id).delete()
    return "ok"

def editContest(params, setHeader, user):
    id = params.get("id")
    contest = Contest.get(id) or Contest()

    contest.name     = params["name"]
    contest.start    = int(params["start"])
    contest.end      = int(params["end"])
    contest.scoreboardOff = int(params["scoreboardOff"])
    contest.showProblInfoBlocks = params["showProblInfoBlocks"]
    contest.problems = [Problem.get(id) for id in json.loads(params["problems"])]
    if str(params["tieBreaker"]).lower() == "true":
        contest.tieBreaker = True
    else:
        contest.tieBreaker = False

    contest.save()

    return contest.id

register.post("/deleteContest", "admin", deleteContest)
register.post("/editContest", "admin", editContest)