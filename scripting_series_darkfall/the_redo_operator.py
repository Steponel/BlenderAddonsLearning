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
    # https://docs.blender.org/api/current/bpy.types.Operator.html?highlight=bl_option#bpy.types.Operator.bl_options
    # REGISTER Register, Display in the info window and support the redo toolbar panel.（REDO面板）
    # UNDO Undo, Push an undo event (needed for operator redo).（可撤销）
    # 设定为REDO面板（Blender左下角更改弹窗）
    bl_options = {'REGISTER','UNDO'}

    loc: bpy.props.FloatVectorProperty()

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add(location=self.loc)

        return {'FINISHED'}
    # 当用invoke时

    def invoke(self, context, event) :
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


classes = [ADDONNAME_PT_main_panel, ADDONNAME_OT_my_op]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
