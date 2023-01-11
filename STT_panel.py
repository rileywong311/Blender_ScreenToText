import bpy
from . STT_curve_creator import CurveData

# def set_activated(self, value):
#     self['val'] = value
#     if value:
#         print(value)
#         bpy.ops.object.screen_to_text_operator('INVOKE_DEFAULT')

# def get_activated(self):
#     return self['val']

def update_activated(self, value):
    bpy.ops.object.screen_to_text_operator('INVOKE_DEFAULT')

# Create Properties
PROPS = [
    ('STT_convert_text', bpy.props.StringProperty(name='Text', default='. - ; = / % & @ #')),
    ('STT_activated', bpy.props.BoolProperty(name='Activated', default=False, update=update_activated)),
    ('STT_font_proportion', bpy.props.IntProperty(name='Font Proportion', default=25, min=1, max=150)),
    ('STT_font_choice', bpy.props.StringProperty(name='Font', default='cour.ttf'))
]

# for (prop_name, prop_value) in PROPS:
#          setattr(bpy.types.Scene, prop_name, prop_value)

class STT_PT_panel(bpy.types.Panel):
    bl_idname = "STT_PT_panel"
    bl_label = "Screen To Text Panel"
    bl_category = "Screen To Text"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    # def draw_header(self, context):
    #     layout = self.layout
    #     layout.label(text="My Select Panel")

    def draw(self, context):
        col = self.layout.column()
        for (prop_name, _) in PROPS:
            row = col.row()
            row.prop(context.scene, prop_name)

        self.layout.template_curve_mapping(CurveData('STT_CustomCurve'), "mapping")

        row = col.row()
        row.prop(context.space_data, "lock_camera")

# bpy.utils.register_class(STT_PT_panel)