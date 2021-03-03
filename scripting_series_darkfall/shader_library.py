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
    """Creates a Panel in the Object properties window"""
    bl_label = "Shader Library"
    bl_idname = "SHADER_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Shader Liabrary'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text)
