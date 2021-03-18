import bpy


# 定义PropertyGroup
class MyProperties(bpy.types.PropertyGroup):
    my_string: bpy.props.StringProperty(name="Enter Text")
    my_float_vector: bpy.props.FloatVectorProperty(name="Enter Value", soft_min=0, soft_max=1000)
    my_enum: bpy.props.EnumProperty(
        name="Enumerator/Dropdown",
        description="sample text",
        items=[
            ('OP1', "Add Cube", ""),
            ('OP2', "Add Sphere", ""),
            ('OP3', "Add Monkey", "")

        ]
    )


class ADDONNAME_PT_main_panel(bpy.types.Panel):
    bl_label = "Main Panel"
    bl_idname = "ADDONNAME_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "New Tab"

    def draw(self, context):
        layout = self.layout
        # 使用my_tool
        scene = context.scene
        mytool = scene.my_tool

        layout.prop(mytool, "my_string")
        layout.prop(mytool, "my_float_vector")
        layout.prop(mytool, "my_enum")

        row = layout.row()
        row.operator("addonname.myop_operator")


class ADDONNAME_OT_my_op(bpy.types.Operator):
    bl_label = "Operator"
    bl_idname = "addonname.myop_operator"

    def execute(self, context):
        my_tool = context.scene.my_tool

        if my_tool.my_enum == 'OP1':
            bpy.ops.mesh.primitive_cube_add()
            bpy.context.object.name = my_tool.my_string
            bpy.context.object.scale = my_tool.my_float_vector

        if my_tool.my_enum == 'OP2':
            bpy.ops.mesh.primitive_uv_sphere_add()
            bpy.context.object.name = my_tool.my_string
            bpy.context.object.scale = my_tool.my_float_vector

        if my_tool.my_enum == 'OP3':
            bpy.ops.mesh.primitive_monkey_add()
            bpy.context.object.name = my_tool.my_string
            bpy.context.object.scale = my_tool.my_float_vector

        return {"FINISHED"}


classes = [MyProperties, ADDONNAME_PT_main_panel, ADDONNAME_OT_my_op]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        # 实例化MyProperties 生成my_tool
        bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=MyProperties)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        # 删除my_tool
        del bpy.types.Scene.my_tool


if __name__ == "__main__":
    register()
