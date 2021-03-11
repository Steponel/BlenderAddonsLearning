import bpy


# Create compositor group
def create_comp_group(context, operator, group_name):
    # Create a group
    test_group = bpy.data.node_groups.new(group_name, 'CompositorNodeTree')

    # Create group inputs
    group_inputs = test_group.nodes.new('NodeGroupInput')
    group_inputs.location = (-350, 0)
    test_group.inputs.new('NodeSocketFloat', 'in_to_greater')
    test_group.inputs.new('NodeSocketFloat', 'in_to_less')

    # Create group outputs
    group_outputs = test_group.nodes.new('NodeGroupOutput')
    group_outputs.location = (300, 0)
    test_group.outputs.new('NodeSocketFloat', 'out_result')

    # Create three math nodes in a group
    node_add = test_group.nodes.new('CompositorNodeMath')
    node_add.operation = 'ADD'
    node_add.location = (100, 0)

    node_greater = test_group.nodes.new('CompositorNodeMath')
    node_greater.operation = 'GREATER_THAN'
    node_greater.label = 'greater'
    node_greater.location = (-100, 100)

    node_less = test_group.nodes.new('CompositorNodeMath')
    node_less.operation = 'LESS_THAN'
    node_less.label = 'less'
    node_less.location = (-100, -100)

    # Link nodes together
    test_group.links.new(node_add.inputs[0], node_greater.outputs[0])
    test_group.links.new(node_add.inputs[1], node_less.outputs[0])

    # Link inputs
    test_group.links.new(group_inputs.outputs['in_to_greater'], node_greater.inputs[0])
    test_group.links.new(group_inputs.outputs['in_to_less'], node_less.inputs[0])

    # link output
    test_group.links.new(node_add.outputs[0], group_outputs.inputs['out_result'])

    # return the group
    return test_group


# Operator
class NODE_OT_compGroup(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "node.simple_operator"
    bl_label = "Add Group (Operator)"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def execute(self, context):
        # Create the group
        custom_node_name = "my_node"
        my_group = create_comp_group(self, context, custom_node_name)
        comp_node = context.scene.node_tree.nodes.new('CompositorNodeGroup')
        comp_node.node_tree = bpy.data.node_groups[my_group.name]
        comp_node.location = 100, 0

        return {'FINISHED'}


# Panel
class NODE_PT_customPanel(bpy.types.Panel):
    bl_idname = "NODE_PT_customPanel"
    bl_space_type = 'NODE_EDITOR'
    bl_label = "Custom Panel"
    bl_region_type = "UI"
    bl_category = "Custom Category"

    @classmethod
    def poll(self, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        layout.operator(NODE_OT_compGroup.bl_idname)
        layout.separator()
        layout.separator()


# NEW Registration Method
# 使用for 循环减少重复写入
classes = [NODE_OT_compGroup, NODE_PT_customPanel]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()

# # OLD Registration Method
# # Register
# def register():
#     bpy.utils.register_class(NODE_OT_compGroup)
#     bpy.utils.register_class(NODE_PT_customPanel)
#
#
# def unregister():
#     bpy.utils.unregister_class(NODE_OT_compGroup)
#     bpy.utils.unregister_class(NODE_PT_customPanel)
#
#
# if __name__ == "__main__":
#     register()

