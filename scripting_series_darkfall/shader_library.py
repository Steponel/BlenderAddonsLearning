bl_info = {
    "name": "Shader Library",
    "author": "Steponel",
    "version": (1, 0),
    "blender": (2, 90, 0),
    "location": "View3D > Toolshelf",
    "description": "Adds a new Shader to your object",
    "warning": "",
    "doc_url": "",
    "category": "Add Shader",
}

import bpy


class ShaderMainPanel(bpy.types.Panel):
    bl_label = "Shader Library"
    bl_idname = "SHADER_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Shader Liabrary'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Select a Shader to be added。")
        # Call shader.diamond_operator  SHADER_OT_DIAMOND
        row.operator('shader.diamond_operator')


# Create a Operator
class SHADER_OT_DIAMOND(bpy.types.Operator):
    bl_label = "Diamond"
    bl_idname = 'shader.diamond_operator'

    def execute(self, context):
        # Creating a New Shader and calling it Diamond
        material_diamond = bpy.data.materials.new(name="Diamond")
        material_diamond.use_nodes = True

        # Remove BSDF
        material_diamond.node_tree.nodes.remove(material_diamond.node_tree.nodes.get('Principled BSDF'))

        # Set location of Material Output
        material_output = material_diamond.node_tree.nodes.get('Material Output')
        material_output.location = (-200, 0)

        # Add Glass Node
        glass1_node = material_diamond.node_tree.nodes.new(type='ShaderNodeBsdfGlass')
        # Set location
        glass1_node.location = (-600, 0)
        # Set the Default Color
        glass1_node.inputs[0].default_value = (1, 1, 0, 1)
        # Set IOR
        glass1_node.inputs[2].default_value = 1.446

        # Add Glass Node
        glass2_node = material_diamond.node_tree.nodes.new(type='ShaderNodeBsdfGlass')
        # Set location
        glass2_node.location = (-600, -150)
        # Set the Default Color
        glass2_node.inputs[0].default_value = (0, 1, 0, 1)
        # Set IOR
        glass2_node.inputs[2].default_value = 1.450

        # Add Glass Node
        glass3_node = material_diamond.node_tree.nodes.new(type='ShaderNodeBsdfGlass')
        # Set location
        glass3_node.location = (-600, -300)
        # Set the Default Color
        glass3_node.inputs[0].default_value = (0, 1, 1, 1)
        # Set IOR
        glass3_node.inputs[2].default_value = 1.450

        add1_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        add1_node.location = (-400, -50)
        # Label Name
        add1_node.label = "Add 1"
        # Hide Node
        add1_node.hide = True
        # Deselect
        add1_node.select = False

        # Link nodes
        material_diamond.node_tree.links.new(glass1_node.outputs[0], add1_node.inputs[0])
        material_diamond.node_tree.links.new(glass2_node.outputs[0], add1_node.inputs[1])
        material_diamond.node_tree.links.new(add1_node.outputs[0], material_output.inputs[0])

        bpy.context.object.active_material = material_diamond

        return {'FINISHED'}


def register():
    bpy.utils.register_class(ShaderMainPanel)
    bpy.utils.register_class(SHADER_OT_DIAMOND)


def unregister():
    bpy.utils.unregister_class(ShaderMainPanel)
    bpy.utils.unregister_class(SHADER_OT_DIAMOND)


if __name__ == "__main__":
    register()
