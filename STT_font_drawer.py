import bpy
import blf
import os
from . STT_curve_creator import curve_node_mapping

class STT_font():

    def __init__(self):
        self.font_id = None
        self.width = -1
        self.update_font()
        
    def update_font(self):
        self.font = bpy.context.scene.STT_font_choice
        font_path = bpy.path.abspath('C:\Windows\Fonts\\' + self.font)
        if os.path.exists(font_path):
            self.font_id = blf.load(font_path)
        else:
            # Default font.
            self.font_id = 0
        blf.enable(self.font_id, blf.WORD_WRAP)
    
    def draw_string_from_texture(self, texture, overlay_width, overlay_height):
        string = ""

        text = bpy.context.scene.STT_convert_text
        text.replace(" ", "")

        if self.width != overlay_width:
            font_size = self.get_font_size(overlay_width)
            blf.size(self.font_id, font_size)

        points = len(text)
        step = 1/points
        start = step/2
        map_locations = {i:(start + step*i) for i in range(points)}

        ng = bpy.context.blend_data.node_groups['STT_CustomCurveStorage']
        c_map = ng.nodes[curve_node_mapping['STT_CustomCurve']].mapping

        for i in texture:
            for j in i:
                # TO DO: color channel specifier in panel
                for color in [0,1,2]:
                    x = j[color]
                x /= 3
                y = c_map.evaluate(c_map.curves[3], x)
                y = min(map_locations, key=lambda x: abs(x.value - y))
                string += text[y]
            
            string += " "

        blf.position(self.font_id, 0, overlay_height - blf.dimensions(self.font_id, "O")[1], 0)
        blf.draw(self.font_id, string)

    def get_font_size(self, overlay_width):
        target = round(overlay_width / bpy.context.scene.STT_font_proportion)
        # TO DO: change range values
        font_size = min(range(1,200), key=lambda x: self.compare_font_size(x, target))
        return font_size

    def compare_font_size(self, font_size, target):
        blf.size(self.font_id, font_size)
        size = blf.dimensions(self.font_id, "O")[0]
        return abs(target - size)

