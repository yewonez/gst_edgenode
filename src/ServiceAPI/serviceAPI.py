import os
from dotenv import load_dotenv

def set_register_edge_id(edgeID:int):
    load_dotenv()
    print("edgeId :", edgeID)
    os.environ['EDGEID'] = str(edgeID)
    #print(int(os.environ.get("EDGEID")))
    return True