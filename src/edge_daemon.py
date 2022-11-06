from fastapi import FastAPI, Body
from src.ServiceAPI.serviceAPI import *
from dotenv import load_dotenv

app = FastAPI()

@app.on_event("startup")
def do_init():
    load_dotenv()

@app.post("/edges/",tags=["Register-Setting"])
async def p_set_register_edge(edgeID:int = Body(...)):
    try:
        return set_register_edge_id(edgeID)
    except Exception as e:
        print("error",e)
        return False

