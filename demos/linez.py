import json

import arena

def scene_callback(msg):
    jsonMsg = json.loads(msg)
    # if jsonMsg["action"] != "clientEvent":
    #     return
    if jsonMsg["type"] == "mouseenter" or jsonMsg["type"] == "mouseleave":
        print(jsonMsg["action"]+" "+jsonMsg["type"] + " " + jsonMsg["object_id"])


arena.init("oz.andrew.cmu.edu", "realm", "linez", scene_callback)
arena.Object( # purple line
    objType=arena.Shape.line,
    objName="line_1",
    line=arena.Line((-1, 1, -2), (-1, 2, -2), 1, "#CE00FF"),
)
arena.Object( # blue sphere
    objType=arena.Shape.sphere,
    objName="sphere_1",
    location=(-1, 2, -2),
    color=(0, 0, 255),
    scale=(0.05, 0.05, 0.05),
    clickable=True,
)
arena.Object( # green thickline
    objType=arena.Shape.thickline,
    objName="line_2",
    thickline=arena.Thickline({(1, 1, -2), (1, 2, -2)}, 1, "#00FF00"),
)
arena.Object( # red sphere
    objType=arena.Shape.sphere,
    objName="sphere_2",
    location=(1, 2, -2),
    color=(255, 0, 0),
    scale=(0.05, 0.05, 0.05),
    clickable=True,
)
arena.handle_events()
