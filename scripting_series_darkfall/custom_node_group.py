import bpy

# 面板
class NODE_PT_MAINPANEL(bpy.types.Panel):
    bl_label = "Custom Node Group"
    bl_idname = "NODE_PT_MAINPANEL"
    # 设定用的地方是节点编辑器
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "New Tab"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('node.test_operator')

# 函数，用于创建node_group
def create_test_group(context, operator, group_name):
    # Enable Use Nodes
    bpy.context.object.active_material.use_nodes = True

    # 添加新的Group
    test_group = bpy.data.node_groups.new(group_name, "CompositorNodeTree")

    # Node id_name在操作Blender 添加时暂留可以看见
    group_in = test_group.nodes.new('NodeGroupInput')
    group_in.location = (-200, 0)
    test_group.inputs.new('NodeSocketColor', 'Color Input')  # 0
    test_group.inputs.new('NodeSocketFactor', 'Color Value')  # 1

    group_out = test_group.nodes.new('NodeGroupOutput')  # 0
    group_out.location = (400, 0)
    test_group.outputs.new('NodeSocketColor', 'Output')

    mask_node = test_group.nodes.new(type='CompositorNodeBoxMask')
    mask_node.location = (0, 0)
    # box mask . rotation
    mask_node.rotation = 1

    mix_node = test_group.nodes.new(type='CompositorNodeMixRGB')
    mix_node.location = (200, 0)
    # use clamp
    mix_node.use_clamp = True
    mix_node.blend_type = 'OVERLAY'

    # link all
    link = test_group.links.new

    link(mask_node.outputs[0], mix_node.inputs[0])

    link(group_in.outputs[0],mix_node.inputs[1])
    link(group_in.outputs[1],mix_node.inputs[2])

    link(mix_node.outputs[0],group_out.inputs[0])

    return test_group

# 新Operator 用于面板
class NODE_OT_TEST(bpy.types.Operator):
    bl_label = "Add Custom Node Group"
    bl_idname = "node.test_operator"

    def execute(self,context):
        custom_node_name = "Test Node"
        # Add my_group as create_test_group
        my_group = create_test_group(self,context,custom_node_name)
        # Add my_group as Node tree
        test_node = context.scene.node_tree.nodes.new('CompositorNodeGroup')
        test_node.node_tree = bpy.data.node_groups[my_group.name]
        # add node custom color
        test_node.use_custom_color = True
        test_node.color = (0.005,0.021,0.129)

        return {'FINISHED'}




def register():
    bpy.utils.register_class(NODE_PT_MAINPANEL)
    bpy.utils.register_class(NODE_OT_TEST)
# Tips：Ctrl D 复制行

def unregister():
    bpy.utils.unregister_class(NODE_PT_MAINPANEL)
    bpy.utils.unregister_class(NODE_OT_TEST)


if __name__ == "__main__":
    register()
