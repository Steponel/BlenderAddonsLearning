import bpy

# https://docs.blender.org/api/master/bpy.types.Operator.html
class WM_OT_MyOp(bpy.types.Operator):
    """Open the Add Cube Dialog Box"""
    bl_label = "Add Cube Dialog Box"
    bl_idname = "wm.myop"

    # Add Properties
    text = bpy.props.StringProperty(name="Enter Text", default="")
    number = bpy.props.FloatProperty(name="scale Z Axis", default=1)

    def execute(self, context):
        text = self.text
        bpy.ops.mesh.primitive_cube_add()
        # obj 为新添加Cube
        obj = bpy.context.object
        # 改名为键入的text属性值
        obj.name = text

        return {'FINISHED'}

    def invoke(self, context, event):

        return context.window_manager.invoke_props_dialog(self)



def register():
    bpy.utils.register_class(WM_OT_MyOp)


def unregister():
    bpy.utils.unregister_class(WM_OT_MyOp)


if __name__ == "__main__":
    register()

    bpy.ops.wm.myop('INVOKE_DEFAULT')