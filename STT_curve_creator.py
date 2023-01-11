import bpy

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