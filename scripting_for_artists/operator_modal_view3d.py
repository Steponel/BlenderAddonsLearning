import bpy
from mathutils import Vector
from bpy.props import FloatVectorProperty


class ViewOperator(bpy.types.Operator):
    """Translate the view using mouse events"""
    bl_idname = "view3d.modal_operator"
    bl_label = "Simple View Operator"

    offset: FloatVectorProperty(
        name="Offset",
        size=3,
    )

    def execute(self, context):
        v3d = context.space_data
        rv3d = v3d.region_3d

        rv3d.view_location = self._initial_location + Vector(self.offset)

    def modal(self, context, event):

        if event.type == 'MOUSEMOVE':
            mouse_pos = Vector((event.mouse_x, event.mouse_y, 0.0))
            mouse_move = self._initial_mouse - mouse_pos
            self.offset = mouse_move * 0.02
            self.execute(context)
            context.area.header_text_set(
                "Offset %.4f %.4f %.4f" % tuple(self.offset))  # https://www.runoob.com/python/att-string-format.html

        elif event.type == 'LEFTMOUSE':
            context.area.header_text_set(None)
            return {'FINISHED'}

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            v3d = context.space_data
            rv3d = v3d.region_3d
            rv3d.view_location = self._initial_location
            context.area.header_text_set(None)
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):

        if context.space_data.type != 'VIEW_3D':
            self.report({'WARNING'}, "Active space must be a View3d")
            return {'CANCELLED'}

        v3d = context.space_data
        rv3d = v3d.region_3d

        if rv3d.view_perspective == 'CAMERA':
            rv3d.view_perspective = 'PERSP'

        # 初始鼠标坐标和视角位置
        self._initial_mouse = Vector((event.mouse_x, event.mouse_y, 0.0))
        self._initial_location = rv3d.view_location.copy()  # https://www.programiz.com/python-programming
        # /methods/list/copy

        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}


def register():
    bpy.utils.register_class(ViewOperator)


def unregister():
    bpy.utils.unregister_class(ViewOperator)


if __name__ == "__main__":
    register()
