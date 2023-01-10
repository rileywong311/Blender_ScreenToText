import bpy

from . STT_offscreen import STT_offscreen

class STT_OT_Operator(bpy.types.Operator):
    bl_idname = "object.screen_to_text_operator"
    bl_label = "Screen To Text Operator Operator"

    def __init__(self):
        self.off_screen = STT_offscreen()
        self.invoked = False
        bpy.context.window_manager.modal_handler_add(self)

    def invoke(self, context, event):
        if not self.invoked:
            self.invoked = True
            self.handler = bpy.types.SpaceView3D.draw_handler_add(self.draw_callback, (), 'WINDOW', 'POST_PIXEL')
            return {'RUNNING_MODAL'}

    def end(self):
        self.invoked = False
        if self.handler:
            bpy.types.SpaceView3D.draw_handler_remove(self.handler, 'WINDOW')
        self.handler = None
        return{'FINISHED'}

    def modal(self, context, event):
        if not context.scene.STT_activated:
            return self.end()

        if self.handler:
            self.off_screen.update_offscreen()
        
        if event.type == 'Y' and self.handler:  # Apply
            bpy.types.SpaceView3D.draw_handler_remove(self.handler, 'WINDOW')
            self.handler = None
            
        elif event.type == 'Y' and not self.handler:
            self.handler = bpy.types.SpaceView3D.draw_handler_add(self.draw_callback, (), 'WINDOW', 'POST_PIXEL')
        
        #return {'RUNNING_MODAL'}
        return {'PASS_THROUGH'}

    def draw_callback(self):
        #self.update_offscreen() doesnt work
        self.off_screen.draw_offscreen()
        self.off_screen.draw_texture()
        
def menu_func(self, context):
    self.layout.operator(STT_OT_Operator.bl_idname, text="Screen To Text Operator")

