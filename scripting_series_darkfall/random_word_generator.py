import bpy
from bpy.types import Panel, Operator, PropertyGroup
from bpy.props import IntProperty, PointerProperty
from random import randint


class MyProperties(PropertyGroup):
    list_a = ["A", "The", "Our"]
    list_b = ["Adorable", "Ocean", "Frozen"]
    list_c = ["1", "2", "3"]

    number_1: IntProperty(default=0)
    number_2: IntProperty(default=0)
    number_3: IntProperty(default=0)


class ADDONNAME_PT_main_panel(Panel):
    bl_label = "Main Panel"
    bl_idname = "ADDONNAME_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "New Tab"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        layout.label(text=mytool.list_a[mytool.number_1])
        layout.label(text=mytool.list_b[mytool.number_2])
        layout.label(text=mytool.list_c[mytool.number_3])

        layout.operator("addonname.myop_operator")


class ADDONNAME_OT_my_op(Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operator"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        r1 = randint(0, len(mytool.list_a)-1)
        mytool.number_1 = r1
        r1 = randint(0, len(mytool.list_b)-1)
        mytool.number_2 = r1
        r1 = randint(0, len(mytool.list_c)-1)
        mytool.number_3 = r1

        return {'FINISHED'}


classes = [MyProperties, ADDONNAME_PT_main_panel, ADDONNAME_OT_my_op]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.my_tool = PointerProperty(type=MyProperties)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.my_tool


if __name__ == "__main__":
    register()
