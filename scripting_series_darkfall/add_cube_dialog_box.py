import bpy


# https://docs.blender.org/api/master/bpy.types.Operator.html
class WM_OT_MyOp(bpy.types.Operator):
    """Open the Add Cube Dialog Box"""
    bl_label = "Add Cube Dialog Box"
    bl_idname = "wm.myop"

    # Add Properties
    text = bpy.props.StringProperty(name="Enter the Name", default="")
    scale = bpy.props.FloatVectorProperty(name="scale", default=[1,1,1])

    # execute
    # This runs the operator, assuming values are set by the caller (else use defaults), this is used for undo/redo,
    # and executing operators from Python.
    # 运行Operator，假设值由调用者设置（或者用默认值），用于撤销/重做，和从Py执行Operators
    def execute(self, context):
        text = self.text
        scale = self.scale

        bpy.ops.mesh.primitive_cube_add()
        # obj 为新添加Cube
        obj = bpy.context.object
        # name
        obj.name = text
        # Scale
        obj.scale = scale

        return {'FINISHED'}

    # invoke
    # Think of this as "run by a person". Called by default when accessed from a key binding and menu, this takes
    # the current context - mouse location, used for interactive operations such as dragging & drawing.
    # 类似“由人运行”。默认情况下，通过键绑定和菜单访问时调用，该函数接受当前上下文-鼠标位置，用于像拖动和绘制等交互式操作。
    def invoke(self, context, event):
        # 呼出对话dialog
        return context.window_manager.invoke_props_dialog(self)


def register():
    bpy.utils.register_class(WM_OT_MyOp)


def unregister():
    bpy.utils.unregister_class(WM_OT_MyOp)


if __name__ == "__main__":
    register()

    bpy.ops.wm.myop('INVOKE_DEFAULT')
