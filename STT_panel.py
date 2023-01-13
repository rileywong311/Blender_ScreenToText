import bpy
from . STT_curve_creator import CurveData

def update_activated(self, value):
    bpy.ops.object.screen_to_text_operator('INVOKE_DEFAULT')

# Create Properties
PROPS = [
    ('STT_convert_text', bpy.props.StringProperty(name='Text', default='. - ; = / % & @ #')),
    ('STT_activated', bpy.props.BoolProperty(name='Activated', default=False, update=update_activated)),
    ('STT_font_proportion', bpy.props.IntProperty(name='Font Proportion', default=25, min=4, max=150, soft_min=10)),
    ('STT_font_choice', bpy.props.StringProperty(name='Font', default='cour.ttf'))
]

class STT_PT_panel(bpy.types.Panel):
    bl_idname = "STT_PT_panel"
    bl_label = "Screen To Text"
    bl_category = "Screen To Text"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        col = self.layout.column()
        
        for (prop_name, _) in PROPS:
            row = col.row()
            row.prop(context.scene, prop_name)

        self.layout.template_curve_mapping(CurveData('STT_CustomCurve'), "mapping")

        row = col.row()
        row.prop(context.space_data, "lock_camera")