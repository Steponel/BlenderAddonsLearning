import bpy


class SFA_OT_silly_example(bpy.types.Operator):
    bl_idname = "sfa.silly_example"
    bl_label = "Silly Modal Example"

    # https://docs.blender.org/api/current/bpy.types.Operator.html?highlight=modal#modal-execution
    def modal(self, context: bpy.types.Context, event: bpy.types.Event):
        if event.type == 'MOUSEMOVE':
            print(f"MOUSEMOVE:{event.mouse_x},{event.mouse_y}")

        elif event.type == 'LEFTMOUSE':
            print(f"LEFT {event.value} at {event.mouse_x},{event.mouse_y}")

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            print(f"{event.type}{event.value} -- STOPPING")
            return {'FINISHED'}  # 完成

        return {"RUNNING_MODAL"}

    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        return {"RUNNING_MODAL"}


classes = [
    SFA_OT_silly_example,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
