import bpy


class ExportSomeData(bpy.types.Operator):
    """Test exporter which just writes hello world"""
    bl_idname = "export.some_data"
    bl_label = "Export Some Data"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    # https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner
    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        file = open(self.filepath, 'w')
        file.write("Hello World " + context.object.name)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


# Only needed if you want to add into a dynamic menu
def menu_func(self, context):
    self.layout.operator_context = 'INVOKE_DEFAULT'
    self.layout.operator(ExportSomeData.bl_idname, text="Text Export Operator")


# Register and add to the file selector
bpy.utils.register_class(ExportSomeData)
bpy.types.TOPBAR_MT_file_export.append(menu_func)


# test call
# https://docs.blender.org/api/current/bpy.ops.html#execution-context
bpy.ops.export.some_data('INVOKE_DEFAULT')