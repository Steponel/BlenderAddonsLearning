import bpy
from bpy.types import Panel, Operator


def mist_comp_action(context):
    tree = context.scene.node_tree

    comp_node = tree.nodes.get('Composite')
    comp_node.location = (700, 0)

    render_layer_node = tree.nodes.get('Render Layers')
    render_layer_node.location = (-200, 0)

    mix_node = tree.nodes.new('CompositorNodeMixRGB')
    mix_node.location = (500, 0)
    mix_node.blend_type = 'ADD'
    mix_node.use_clamp = True

    mix2_node = tree.nodes.new('CompositorNodeMixRGB')
    mix2_node.location = (300, 0)
    mix2_node.blend_type = 'MULTIPLY'
    mix2_node.use_clamp = True

    cr_node = tree.nodes.new('CompositorNodeValToRGB')
    cr_node.location = (100, 0)
    cr_node.color_ramp.elements[0].color = (0.2, 0.2, 0.2, 1)
    cr_node.color_ramp.elements.new(position=0.27)

    link = tree.links.new
    link(mix_node.outputs[0], comp_node.inputs[0])
    link(mix2_node.outputs[0], mix_node.inputs[1])


class INSTAMIST_PT_main_panel(Panel):
    bl_label = "INSTA-MIST"
    bl_idname = "INSTAMIST_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "INSTA_MIST"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        world = scene.world.mist_settings

        # 2.92面板中已经无这些选项，但仍可运行
        layout.prop(world, "start")
        layout.prop(world, "depth")
        layout.prop(world, "falloff")

        layout.operator("instamist.add_mist_operator")


class INSTAMIST_OT_add_mist(bpy.types.Operator):
    bl_idname = "instamist.add_mist_operator"
    bl_label = "Enable/Disable Mist"

    def execute(self, context):
        scene = context.scene
        camera = bpy.data.cameras['Camera']
        vl = scene.view_layers["View Layer"]
        tree = scene.node_tree

        # FlipFlop
        if not vl.use_pass_mist:
            vl.use_pass_mist = True
            camera.show_mist = True
            if not scene.use_nodes:
                scene.use_nodes = True
            mist_comp_action(context)

        elif vl.use_pass_mist:
            vl.use_pass_mist = False
            camera.show_mist = False

            mix1 = tree.nodes.remove(tree.nodes.get('Mix'))
            mix2 = tree.nodes.remove(tree.nodes.get('Mix.001'))
            cr = tree.nodes.remove(tree.nodes.get('ColorRamp'))

        return {"RUNNING_MODAL"}


classes = [INSTAMIST_PT_main_panel, INSTAMIST_OT_add_mist]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
