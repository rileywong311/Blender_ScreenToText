import bpy
import gpu
import array
from gpu_extras.presets import draw_texture_2d


class STT_offscreen():
    def __init__(self):
        self.depsgraph = bpy.context.evaluated_depsgraph_get()
        self.update_offscreen()
        
    def update_offscreen(self):
        render_width = bpy.context.scene.render.resolution_x
        render_height = bpy.context.scene.render.resolution_y
        
        for area in reversed(bpy.context.screen.areas):
            if area.type == 'VIEW_3D':
                width_ratio = area.width / render_width
                height_ratio = area.height / render_height
                fit_ratio = min([width_ratio, height_ratio])

                self.width = round(render_width * fit_ratio)
                self.height = round(render_height * fit_ratio)

                font_proportion_width = round(self.width / 25)
                font_proportion_height = round(self.height / 25)
                
                self.offscreen = gpu.types.GPUOffScreen(font_proportion_width, font_proportion_height)
                
                #self.offscreen = gpu.types.GPUOffScreen(self.width, self.height)
                break

        #self.offscreen = gpu.types.GPUOffScreen(self.width, self.height)
        
        
    def draw_offscreen(self):
        context = bpy.context
        scene = context.scene

        view_matrix = scene.camera.matrix_world.inverted()
        
        projection_matrix = scene.camera.calc_matrix_camera(
            self.depsgraph, x=self.width, y=self.height)

        self.offscreen.draw_view3d(
            scene,
            context.view_layer,
            context.space_data,
            context.region,
            view_matrix,
            projection_matrix,
            do_color_management=True)
    
    def draw_texture(self):
#        print("Height = ", end="")
#        print(len(self.offscreen.texture_color.read()))
#        print("Width = ", end="")
#        print(len(self.offscreen.texture_color.read()[0]))
        draw_texture_2d(self.offscreen.texture_color, (0, 0), self.width, self.height)