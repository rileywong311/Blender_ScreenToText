import bpy

def update(self, value):
    print('DEBUG: STT_panel: update')
    pass
    #invoke operator modal

# Create Properties
PROPS = [
    ('STT_convert_text', bpy.props.StringProperty(name='Text', default='. - ; = / % & @ #')),
    ('STT_activated', bpy.props.BoolProperty(name='Activated', default=False, update = update)),
    ('STT_Font_Proportion', bpy.props.FloatProperty(name='Font Proportion', default=5.0, min=0.001, max=100.0))
]


# for (prop_name, prop_value) in PROPS:
#          setattr(bpy.types.Scene, prop_name, prop_value)


# https://blender.stackexchange.com/questions/61618/add-a-custom-curve-mapping-property-for-an-add-on
# return node group containing curve, create node group if none
def STT_CurveNode():
    if 'STT_CustomCurveStorage' not in bpy.data.node_groups:
        ng = bpy.data.node_groups.new('STT_CustomCurveStorage', 'ShaderNodeTree')
        #ng.fake_user = True
    return bpy.data.node_groups['STT_CustomCurveStorage'].nodes

curve_node_mapping = {} # makes node name relevant

# return specific curve node, stored as value given 'curve_name' as a key
# node value will likely be stock 'RGB Curves' stored by Blender
# where subsequent curves will be 'RGB Curves.001' etc
def STT_CurveData(curve_name):
    if curve_name not in curve_node_mapping:
        cn = STT_CurveNode().new('ShaderNodeRGBCurve')
        curve_node_mapping[curve_name] = cn.name
    return STT_CurveNode()[curve_node_mapping[curve_name]]



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
            if prop_name == 'STT_Font_Proportion':
                row.prop(context.scene, prop_name, text="Font Proportion %")
            else:
                row.prop(context.scene, prop_name)
        self.layout.template_curve_mapping(STT_CurveData('STT_CustomCurve'), "mapping")

# bpy.utils.register_class(STT_PT_panel)