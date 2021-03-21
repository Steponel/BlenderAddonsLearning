import bpy
from bpy.types import Panel, Operator


class ADDONNAME_PT_main_panel(Panel):
    bl_label = "Main Panel"
    bl_idname = "ADDONNAME_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "New Tab"

    def draw(self, context):
        layout = self.layout

        layout.operator("addonname.myop_operator")


class ADDONNAME_OT_my_op(Operator):
    bl_label = "Button"
    bl_idname = "addonname.myop_operator"

    int: bpy.props.IntProperty(default=100)

    def execute(self, context):
        message = f"The Special Number is {self.int}"
        # report
        self.report({'INFO'}, message)
        self.report({'WARNING'}, "Warning!")
        self.report({'ERROR'}, "ERROR!")

        return {'FINISHED'}


classes = [ADDONNAME_PT_main_panel, ADDONNAME_OT_my_op]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
