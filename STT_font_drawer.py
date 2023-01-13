import bpy
import blf
import os
from . STT_curve_creator import curve_node_mapping

class STT_font():

    def __init__(self):
        self.font = None
        self.font_id = None
        self.update_font()
        
    def update_font(self):
        if self.font != bpy.context.scene.STT_font_choice:
            self.font = bpy.context.scene.STT_font_choice
            font_path = bpy.path.abspath('C:\Windows\Fonts\\' + self.font)
            if os.path.exists(font_path):
                self.font_id = blf.load(font_path)
            else:
                self.font_id = 0 # Default font.
        # TO DO: customizable color
        blf.color(self.font_id, 1,1,1,1)
    
    def draw_string_from_texture(self, texture, overlay_width, overlay_height):
        # remove spaces in string, but add one at beginning for lowest value
        text = " " + bpy.context.scene.STT_convert_text.replace(" ", "")

        font_size = self.get_font_size(overlay_width)
        blf.size(self.font_id, font_size)

        points = len(text)
        step = 1/points
        start = step/2
        map_locations = {i:(start + step*i) for i in range(points)}

        ng = bpy.context.blend_data.node_groups['STT_CustomCurveStorage']
        c_map = ng.nodes[curve_node_mapping['STT_CustomCurve']].mapping

        strings = []
        for i  in texture:
            string = ""
            for j in i:
                # TO DO: color channel specifier in panel
                x=0
                for color in [0,1,2]:
                    x += j[color]
                x /= (3 * 255)   
                y = c_map.evaluate(c_map.curves[3], x)
                y = min(map_locations.keys(), key=lambda x: abs(map_locations[x] - y))
                string += text[y] 
            strings.insert(0, string)


        for row in range(len(strings)):
            blf.position(self.font_id, 0, overlay_height - blf.dimensions(self.font_id, "O")[0]*(row+1), 0)
            blf.draw(self.font_id, strings[row])

    def get_font_size(self, overlay_width):
        target = round(overlay_width / (overlay_width / bpy.context.scene.STT_font_proportion))
        # TO DO: change range values
        font_size = min(range(1,250), key=lambda x: self.compare_font_size(x, target))
        return font_size

    def compare_font_size(self, font_size, target):
        blf.size(self.font_id, font_size)
        size = blf.dimensions(self.font_id, "O")[0]
        return abs(target - size)