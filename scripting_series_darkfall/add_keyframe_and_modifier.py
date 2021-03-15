import bpy


class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Name your New Tab'
    bl

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()

        row.operator('shader.neon_operator')


class SHADER_OT_NEON(bpy.types.Operator):
    bl_label = "Add Neon Shader"
    bl_idname = 'shader.neon_operator'

    # Execute the Operater
    def execute(self, context):
        # Current Frame
        current_frame = bpy.context.scene.frame_current

        # Creating a New Shader and calling it Neon
        material_neon = bpy.data.materials.new(name="Neon")
        material_neon.use_nodes = True

        tree = material_neon.node_tree

        # Remove BSDF
        material_neon.node_tree.nodes.remove(material_neon.node_tree.nodes.get('Principled BSDF'))

        # Set location of Material Output
        material_output = material_neon.node_tree.nodes.get('Material Output')
        material_output.location = (400, 0)

        # Add Emission Node
        emiss_node = material_neon.node_tree.nodes.new(type='ShaderNodeEmission')
        # Set location
        emiss_node.location = (200, 0)
        # Set the Default Color
        emiss_node.inputs[0].default_value = (1, 1, 0, 1)
        # Set Strength
        emiss_node.inputs[1].default_value = 1.446

        # Insert Frame
        emiss_node.inputs[1].keyframe_insert(data_path='default_value', frame=current_frame)

        # === f-string ===
        # 返回的字符串，大括号中会变为结果
        # https://realpython.com/python-f-strings/
        # >>> f"{name.lower()} is funny."
        # 'eric idle is funny.'
        # >>> f"{2 * 37}"
        # '74'
        # 设置要更改的数据为 emiss_node 的 第二个输入的值
        data_path = f'nodes["{emiss_node.name}"].inputs[1].default_value'
        # f-curves(function curves)
        # https://docs.blender.org/manual/zh-hans/2.92/editors/graph_editor/fcurves/index.html
        fcurves = tree.animation_data.action.fcurves
        fc = fcurves.find(data_path)
        # 有这个fcurves的话
        if fc:
            # Set NOISE mod
            new_mod = fc.modifiers.new('NOISE')
            new_mod.strength = 10
            new_mod.depth = 1

        material_neon.node_tree.links.new(emiss_node.outputs[0], material_output.inputs[0])

        return {'FINISHED'}


def register():
    bpy.utils.register_class(HelloWorldPanel)
    bpy.utils.register_class(SHADER_OT_NEON)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)
    bpy.utils.unregister_class(SHADER_OT_NEON)


if __name__ == "__main__":
    register()
