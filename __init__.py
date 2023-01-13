bl_info = {
    "name": "Screen To Text (ASCII) Overlay",
    "description": "Overlays the viewport as text attributed to pixel brightness",
    "author": "Riley <rnwong@scu.edu>",
    "blender": (3, 4, 1),
    "category": "3D View"
    }

from bpy import types, utils

# . syntax for relative path import works when read by Blender
from . STT_operator import STT_OT_Operator, menu_func
from . STT_panel import PROPS, STT_PT_panel

def register():
    for (prop_name, prop_value) in PROPS:
        setattr(types.Scene, prop_name, prop_value)
    utils.register_class(STT_OT_Operator)
    #types.VIEW3D_MT_object.append(menu_func) do not currently want this
    utils.register_class(STT_PT_panel)

def unregister():
    for (prop_name, _) in PROPS:
        delattr(types.Scene, prop_name)
    utils.unregister_class(STT_OT_Operator)
    #types.VIEW3D_MT_object.remove(menu_func)
    utils.unregister_class(STT_PT_panel)
