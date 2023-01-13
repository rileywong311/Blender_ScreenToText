import bpy

from . STT_offscreen import STT_offscreen
from . STT_font_drawer import STT_font

class STT_OT_Operator(bpy.types.Operator):
    bl_idname = "object.screen_to_text_operator"
    bl_label = "Screen To Text Operator Operator"

    def __init__(self):
        self.off_screen = STT_offscreen()
        self.font_drawer = STT_font()

        self.invoked = False
        bpy.context.window_manager.modal_handler_add(self)

    def invoke(self, context, event):
        if not self.invoked:
            self.invoked = True
            self.handler = self.add_handler()
            return {'RUNNING_MODAL'}

    def end(self):
        self.invoked = False
        if self.handler:
            self.remove_handler()
        self.handler = None
        return{'FINISHED'}

    def modal(self, context, event):
        if not context.scene.STT_activated:
            return self.end()

        if self.handler:
            self.off_screen.update_offscreen()
            self.font_drawer.update_font()
        
        if event.type == 'Y' and self.handler:
            self.remove_handler()
            self.handler = None
            
        elif event.type == 'Y' and not self.handler:
            self.handler = self.add_handler()
        
        return {'PASS_THROUGH'}

    def draw_callback(self):
        self.off_screen.draw_offscreen()
        #self.off_screen.draw_texture()
        self.off_screen.draw_blank_texture()
        self.font_drawer.draw_string_from_texture(self.off_screen.offscreen.texture_color.read(), self.off_screen.width, self.off_screen.height)

    def add_handler(self):
        return bpy.types.SpaceView3D.draw_handler_add(self.draw_callback, (), 'WINDOW', 'POST_PIXEL')

    def remove_handler(self):
        bpy.types.SpaceView3D.draw_handler_remove(self.handler, 'WINDOW')

# needed to make the operator accessible in the f3 menu        
def menu_func(self, context):
    self.layout.operator(STT_OT_Operator.bl_idname, text="Screen To Text Operator")

