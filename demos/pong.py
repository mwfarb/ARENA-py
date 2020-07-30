# pong.py

import json

import arena

USERS = {}  # dictionary of user instances
SCL_TABLE = (1.524, 0.05, 2.743)
SCL_NET = (1.829, 0.1, 0.01)
POS_TABLE = (0, 0.76, 0)


def scene_callback(msg):
    # This is the MQTT message callback function for the scene
    json_msg = json.loads(msg)
    if json_msg["action"] == "create" and json_msg["data"]["object_type"] == "camera":
        # camera updates define users present
        camname = json_msg["object_id"]
        if camname not in USERS:
            print(msg)
            USERS[camname] = arena.Object(
                objName=camname+"_paddle",
                objType=arena.Shape.circle,
                location=(0, 0, 0),
                scale=(0.05, 0.05, 0.05),
                data='{"static-body": {"type": "static"}}',
                parent="myCamera",
                transparency=arena.Transparency(True, 0.5),
                persist=False)


arena.init("oz.andrew.cmu.edu", "realm", "pong6", scene_callback)

# once
arena.Object(objName="origin",
             objType=arena.Shape.cube,
             location=(0, 0, 0),
             color=(0, 0, 255),
             scale=(0.1, 0.1, 0.1),
             transparency=arena.Transparency(True, 0.5),
             persist=False)

arena.Object(objName="cwall",
             objType=arena.Shape.cube,
             location=(0, POS_TABLE[1]+2, 0),
             scale=(SCL_TABLE[0], 0.01, SCL_TABLE[2]),
             data='{"static-body": {"type": "static"}}',
             transparency=arena.Transparency(True, 0.5),
             persist=True)

arena.Object(objName="wwall",
             objType=arena.Shape.cube,
             location=(-SCL_TABLE[0]/2, POS_TABLE[1]+1, 0),
             scale=(0.01, 2, SCL_TABLE[2]),
             data='{"static-body": {"type": "static"}}',
             transparency=arena.Transparency(True, 0.5),
             persist=True)
arena.Object(objName="ewall",
             objType=arena.Shape.cube,
             location=(SCL_TABLE[0]/2, POS_TABLE[1]+1, 0),
             scale=(0.01, 2, SCL_TABLE[2]),
             data='{"static-body": {"type": "static"}}',
             transparency=arena.Transparency(True, 0.5),
             persist=True)

arena.Object(objName="nwall",
             objType=arena.Shape.cube,
             location=(0, POS_TABLE[1]+1, -SCL_TABLE[2]/2),
             scale=(SCL_TABLE[0], 2, 0.01),
             data='{"static-body": {"type": "static"}}',
             transparency=arena.Transparency(True, 0.5),
             persist=True)
arena.Object(objName="nwall",
             objType=arena.Shape.cube,
             location=(0, POS_TABLE[1]+1, SCL_TABLE[2]/2),
             scale=(SCL_TABLE[0], 2, 0.01),
             data='{"static-body": {"type": "static"}}',
             transparency=arena.Transparency(True, 0.5),
             persist=True)

arena.Object(objName="table",
             objType=arena.Shape.cube,
             location=POS_TABLE,
             scale=SCL_TABLE,
             data='{"static-body": {"type": "static"}}',
             transparency=arena.Transparency(True, 0.5),
             persist=True)
arena.Object(objName="net",
             objType=arena.Shape.cube,
             location=(0, 0.8, 0),
             scale=SCL_NET,
             data='{"static-body": {"type": "static"}}',
             transparency=arena.Transparency(True, 0.5),
             persist=True)

arena.Object(objName="ball",
             objType=arena.Shape.sphere,
             color=(255, 255, 255),
             scale=(0.02, 0.02, 0.2),
             location=(0, POS_TABLE[1]+1, 0),
             physics=arena.Physics.dynamic,
             persist=True)

arena.handle_events()
