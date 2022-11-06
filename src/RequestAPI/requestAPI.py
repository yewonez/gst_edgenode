import requests
from dotenv import load_dotenv
import os

def set_register_edge_addr(name:str, address:str):
    load_dotenv()
    if os.environ.get("CLOUD_SERVER_ADDR").endswith("/"):
        URL = os.environ.get("CLOUD_SERVER_ADDR") + "servers/"
    else:
        URL = os.environ.get("CLOUD_SERVER_ADDR") + "/servers/"

    json_data = {"name":name,
                 "address":address}

    response = requests.post(url=URL, json=json_data)

    try:
        if response.text.lower() == "true":
            return True
    except Exception as e:
        print("error : ",e)

    return False

def alert_event(edgeID:int, rtspsrc:str):
    load_dotenv()
    if os.environ.get("CLOUD_SERVER_ADDR").endswith("/"):
        URL = os.environ.get("CLOUD_SERVER_ADDR") + "servers/events/"
    else:
        URL = os.environ.get("CLOUD_SERVER_ADDR") + "/servers/events/"

    json_data = {"edgeID":edgeID,
                 "rtspsrc":rtspsrc}
    response = requests.post(url=URL, json=json_data)
    try:
        if response.text.lower() == "true":
            return True
    except Exception as e:
        print("error : ",e)

    return False
