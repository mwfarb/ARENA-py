#
# signage.py
#
# Drop signage in the ARENA that ARB can easily move around.

import arena

HOST = "oz.andrew.cmu.edu"
SCENE = "arb-roomtest"
signs = [
    "models/poster_test/CONIX-mr.png",
    "models/poster_test/CONIX-mr.png",
    "models/poster_test/CONIX-mr.png",
    "models/poster_test/CONIX-mr.png"
]

arena.init(HOST, "realm", SCENE)
arena.Object(
    persist=True,
    objName="gal1",
    objType=arena.Shape.gltf_model,
    location=(0, 8, 0),
    rotation=(0, 0, 0, 1),
    scale=(0.05, 0.05, 0.05),
    url="models/poster_test/vr_gallery_1/scene.gltf",
)
for i in range(len(signs)):
    arena.Object(
        persist=True,
        objName="poster" + str(i),
        objType=arena.Shape.image,
        location=(0,  1.7, -5-(i/10)),
        rotation=(0,  0,  0, 1),
        scale=(3,  3,  3),
        url=signs[i],
        clickable=True,  # clickable for ARB, can be removed after
    )
arena.handle_events()
