bl_info = {
    "name": "Screen To Text Overlay",
    "description": "Overlays a version of the viewport as text attributed to color brightness",
    "author": "Riley <rnwong@scu.edu>",
    "blender": (3, 4, 1),
    "category": "3D View"
    }


import bpy

# . for relative path works read by Blender
from . STT_panel import PROPS, STT_PT_panel


def register():
    print("Hello World!!")
    for (prop_name, prop_value) in PROPS:
        setattr(bpy.types.Scene, prop_name, prop_value)
    bpy.utils.register_class(STT_PT_panel)
  
def unregister():
    print("Goodbye World!!")
    for (prop_name, prop_value) in PROPS:
        delattr(bpy.types.Scene, prop_name)
    bpy.utils.unregister_class(STT_PT_panel)