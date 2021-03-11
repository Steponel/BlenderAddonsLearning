import bpy


class ADDONNAME_PT_TemplatePanel(bpy.types.Panel):
    bl_label = "Name of the Panel"
    bl_idname = "ADDONNAME_PT_TemplatePanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Template Tab"

    def draw(self, context):
        layout = self.layout

        layout.operator("wm.template_operator")


class ADDONAME_OT_TemplateOperator(bpy.types.Operator):
    bl_label = "Template Operator"
    bl_idname = "wm.template_operator"

    # 添加一个枚举属性
    preset_enum: bpy.props.EnumProperty(
        # items[(identifier, name, description, icon, number), ...]
        items=[
            ('OP1', "Cube", "Add a Cube to the scene"),
            ('OP2', "Sphere", ""),
            ('OP3', "Suzanne", "Add Suzanne to the scene")
        ],
        name="",
        description="Select an option"
    )

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        # 枚举布局在上面
        layout.prop(self,"preset_enum")

    def execute(self, context):
        # 根据选择的枚举值执行
        if self.preset_enum == 'OP1':
            bpy.ops.mesh.primitive_cube_add()
        if self.preset_enum == 'OP2':
            bpy.ops.mesh.primitive_ico_sphere_add()
        if self.preset_enum == 'OP3':
            bpy.ops.mesh.primitive_monkey_add()


        return {'FINISHED'}


classes = [ADDONNAME_PT_TemplatePanel, ADDONAME_OT_TemplateOperator]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
