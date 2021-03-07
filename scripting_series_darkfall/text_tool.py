bl_info = {
    "name": "Text Tool",
    "author": "Steponel",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "https://space.bilibili.com/21077855",
    "category": "Add Mesh",
}

import bpy


class OBJECT_PT_TextTool(bpy.types.Panel):
    bl_label = "TextTool"
    bl_idname = "OBJECT_PT_TextTool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    # 分类
    bl_category = 'Text Tool'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("wm.textop", text="Add Text", icon='CUBE')


class WM_OT_textOp(bpy.types.Operator):
    bl_idname = "wm.textop"
    bl_label = "Text Tool Operator"

    # 定义属性
    # Blender自己的定义的类型属性才能出现在面板上
    text = bpy.props.StringProperty(name="Enter Text:")
    scale = bpy.props.FloatProperty(name="Scale:", default=1)
    center = bpy.props.BoolProperty(name="Center Origin", default=False)
    extrude = bpy.props.BoolProperty(name="Exturde", default=False)
    extrude_amount = bpy.props.FloatProperty(name="Exturde Amount", default=0.06)

    def execute(self, context):
        text = self.text
        scale = self.scale
        center = self.center
        extrude = self.extrude
        extrude_amount = self.extrude_amount

        bpy.ops.object.text_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        # delete all
        bpy.ops.font.delete(type='PREVIOUS_WORD')
        # 插入获取的文字
        bpy.ops.font.text_insert(text=text)
        # 模式切换
        bpy.ops.object.editmode_toggle()

        if extrude == True:
            bpy.context.object.data.extrude = extrude_amount

        if center == True:
            bpy.context.object.data.align_x = 'CENTER'
            bpy.context.object.data.align_y = 'CENTER'

        return {'FINISHED'}

    def invoke(self, context, envent):
        # 弹出对话，操作符是self
        return context.window_manager.invoke_props_dialog(self, width=500)


def register():
    bpy.utils.register_class(OBJECT_PT_TextTool)
    bpy.utils.register_class(WM_OT_textOp)


def unregister():
    bpy.utils.unregister_class(OBJECT_PT_TextTool)
    bpy.utils.unregister_class(WM_OT_textOp)


if __name__ == "__main__":
    register()
