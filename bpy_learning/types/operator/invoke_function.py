# https://docs.blender.org/api/current/bpy.types.Operator.html#invoke-function


import bpy


class SimpleMouseOperator(bpy.types.Operator):
    """ This operator shows the mouse location,
        this string is used for the tooltip and API docs
    """
    bl_idname = "wm.mouse_position"
    bl_label = "Invoke Mouse Operator"

    # 类型注解，x和y为IntProperty类型
    # https://blog.csdn.net/ybdesire/article/details/102633291
    x: bpy.props.IntProperty()
    y: bpy.props.IntProperty()

    def execute(self, context):
        # rather than printing, use the report function,
        # this way the message appears in the header,
        # 打开System Console 可以看见report
        self.report({'INFO'}, "Mouse coords are %d %d" % (self.x, self.y))
        return {'FINISHED'}

    def invoke(self, context, event):
        self.x = event.mouse_x
        self.y = event.mouse_y
        return self.execute(context)


bpy.utils.register_class(SimpleMouseOperator)

# Test call to the newly defined operator.
# Here we call the operator and invoke it, meaning that the settings are taken
# from the mouse.
bpy.ops.wm.mouse_position('INVOKE_DEFAULT')

# Another test call, this time call execute() directly with pre-defined settings.
bpy.ops.wm.mouse_position('EXEC_DEFAULT', x=20, y=66)
