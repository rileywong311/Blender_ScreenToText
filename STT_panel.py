import bpy


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
    ('STT_Font_Proportion', bpy.props.IntProperty(name='Font Proportion', default=25, min=3, max=300))
]

# for (prop_name, prop_value) in PROPS:
#          setattr(bpy.types.Scene, prop_name, prop_value)


# https://blender.stackexchange.com/questions/61618/add-a-custom-curve-mapping-property-for-an-add-on
# return node group containing curve, create node group if none
def CurveNode():
    if 'STT_CustomCurveStorage' not in bpy.data.node_groups:
        ng = bpy.data.node_groups.new('STT_CustomCurveStorage', 'ShaderNodeTree')
        #ng.fake_user = True
    return bpy.data.node_groups['STT_CustomCurveStorage'].nodes

curve_node_mapping = {} # makes node name relevant

# return specific curve node, stored as value given 'curve_name' as a key
# node value will likely be stock 'RGB Curves' stored by Blender
# where subsequent curves will be 'RGB Curves.001' etc
def CurveData(curve_name):
    if curve_name not in curve_node_mapping:
        cn = CurveNode().new('ShaderNodeRGBCurve')
        curve_node_mapping[curve_name] = cn.name
    return CurveNode()[curve_node_mapping[curve_name]]

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