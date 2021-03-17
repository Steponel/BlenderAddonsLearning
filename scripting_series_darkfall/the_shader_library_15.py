import bpy


class ADDONNAME_PT_main_panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Add Shader Panel"
    bl_idname = "ADDONNAME_PT_main_panel"

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Steponel'

    def draw(self, context):
        layout = self.layout

        layout.operator("addonname.addbasic_operator")


class ADDONNAME_OT_add_basic(bpy.types.Operator):
    bl_label = "Add Basic Shader"
    bl_idname = "addonname.addbasic_operator"

    col = bpy.props.FloatVectorProperty(name='Color', subtype='COLOR_GAMMA', size=4, default=(0, 0, 0, 1))

    def excute(self, context):
        # new material
        material_basic = bpy.data.materials.new(name="Basic")
        material_basic.use_nodes = True
        bpy.context.object.active_material = material_basic
        # material set
        principled_node = material_basic.node_tree.nodes.get('Principled BSDF')
        principled_node.inputs[0].default_value = (1, 0, 1, 1)
        principled_node.inputs[7].default_value = 0.08
        rgb_node = material_basic.node_tree.nodes.new("ShaderNodeRGB")
        rgb_node.location = (-250, 0)
        rgb_node.outputs[0].default_value = (1, 0, 1, 1)

        # links
        link = material_basic.node_tree.links.new
        link(rgb_node.outputs[0], principled_node.inputs[0])

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


classes = [ADDONNAME_PT_main_panel, ADDONNAME_OT_add_basic]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
