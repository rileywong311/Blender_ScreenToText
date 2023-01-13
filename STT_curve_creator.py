import bpy

# https://blender.stackexchange.com/questions/61618/add-a-custom-curve-mapping-property-for-an-add-on
# return node group containing curve, create node group if none
def CurveGroup():
    if 'STT_CustomCurveStorage' not in bpy.data.node_groups:
        ng = bpy.data.node_groups.new('STT_CustomCurveStorage', 'ShaderNodeTree')
        ng.fake_user = True
    return bpy.data.node_groups['STT_CustomCurveStorage'].nodes

curve_node_mapping = {} # makes node name relevant

# return specific curve node, stored as value given 'curve_name' as a key
# node value will likely be stock 'RGB Curves' stored by Blender
# where subsequent curves will be 'RGB Curves.001' etc
def CurveData(curve_name):
    # needs to check if the node is in there also when new project is loaded
    curve_group = CurveGroup()
    if (curve_name not in curve_node_mapping) or (curve_node_mapping[curve_name] not in curve_group): 
        curve_node = curve_group.new('ShaderNodeRGBCurve')
        curve_node_mapping[curve_name] = curve_node.name
    return curve_group[curve_node_mapping[curve_name]]