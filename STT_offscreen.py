import bpy
import gpu
import array
from gpu_extras.presets import draw_texture_2d

class STT_offscreen():
    def __init__(self):
        self.depsgraph = bpy.context.evaluated_depsgraph_get()
        self.offscreen = None

        # TO DO: customizable blank background color
        self.blank = [0.0, 0.0, 0.0, 1.0]
        self.blank_texture = gpu.types.GPUTexture((1, 1), format='RGBA16F')
        self.blank_texture.clear(format='FLOAT', value=self.blank)

        self.update_offscreen()
        
    def update_offscreen(self):
        # this freeing part may not necessary
        scene = bpy.context.scene

        if self.offscreen:
            self.offscreen.free()

        render_width = scene.render.resolution_x
        render_height = scene.render.resolution_y
        
        # it seems the only way to access viewport data is checking Blender's array of screen areas
        for area in reversed(bpy.context.screen.areas):
            if area.type == 'VIEW_3D':
                width_ratio = area.width / render_width
                height_ratio = area.height / render_height
                fit_ratio = min([width_ratio, height_ratio])

                self.width = round(render_width * fit_ratio)
                self.height = round(render_height * fit_ratio)

                font_proportion_width = round(self.width / scene.STT_font_proportion)
                font_proportion_height = round(self.height / scene.STT_font_proportion)
                
                self.offscreen = gpu.types.GPUOffScreen(font_proportion_width, font_proportion_height)
                break
        
    def draw_offscreen(self):
        # based on: docs.blender.org/api/current/gpu.html#rendering-the-3d-view-into-a-texture
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
            do_color_management=False)
    
    def draw_blank_texture(self):
        # TO DO: allow option for user to specify overlay dimensions 
        # instead of automatically fitting to screen
        draw_texture_2d(self.blank_texture, (0, 0), self.width, self.height)

    # draws actual viewport texture rendered off screen
    # not used but good for debugging
    def draw_texture(self):
        draw_texture_2d(self.offscreen.texture_color, (0, 0), self.width, self.height)