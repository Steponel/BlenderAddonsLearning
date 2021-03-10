# *** 10.Shortcut / Custom Keymap ***
import bpy


class WM_OT_dialogop(bpy.types.Operator):
    """Custom Operator - Add txt here """
    bl_label = "Add Cube Menu"
    bl_idname = "wm.dialogop"

    name = bpy.props.StringProperty(name="Name", default="")
    scale = bpy.props.FloatVectorProperty(name="Scale: X,Y,Z", default=(1, 1, 1))
    bool = bpy.props.BoolProperty(name="Array?", default=False)
    array = bpy.props.IntProperty(name="Array Count", default=1)
    bool2 = bpy.props.BoolProperty(name="Rotate?", default=False)

    def execute(self, context):

        n = self.name
        s = self.scale
        b = self.bool
        i = 0
        a = self.array
        b2 = self.bool2

        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.object

        obj.name = n
        obj.scale[0] = s[0]
        obj.scale[1] = s[1]
        obj.scale[2] = s[2]

        if b == True:
            i = 0
            n = self.name
            s = self.scale
            b = self.bool
            b2 = self.bool2
            while i < a:

                bpy.ops.mesh.primitive_cube_add()
                bpy.ops.transform.translate(value=(i * 2, 0, 0))
                obj = bpy.context.object
                obj.name = n
                obj.scale[0] = s[0]
                obj.scale[1] = s[1]
                obj.scale[2] = s[2]
                if b2 == True:
                    bpy.ops.transform.rotate(value=i * 0.3, orient_axis='X')
                i = i + 1

        bpy.ops.object.select_all(action='DESELECT')

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


addon_keymaps = []


def register():
    bpy.utils.register_class(WM_OT_dialogop)

    # 获得本插件的Keyconfigs，它会在执行时添加到活动的配置中
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        # 创建新的keymap，属于VIEW_3D
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        # 添加操作符的对应键在 keymap item 中
        kmi = km.keymap_items.new("wm.dialogop", type='F', value='PRESS', shift=True)
        # 添加到list用于删除
        addon_keymaps.append((km, kmi))


def unregister():
    # 删除操作符的对应键在 keymap item 中
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    # 清空
    addon_keymaps.clear()

    bpy.utils.unregister_class(WM_OT_dialogop)


if __name__ == "__main__":
    register()

    # testcall
    # bpy.ops.wm.dialogop('INVOKE_DEFAULT')
