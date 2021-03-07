# 原视频 1 2集
# https://www.youtube.com/watch?v=cyt0O7saU4Q&list=PLFtLHTf5bnym_wk4DcYIMq1DkjqB7kDb-&index=1
# https://www.youtube.com/watch?v=hF-cyH8Z7WQ&list=PLFtLHTf5bnym_wk4DcYIMq1DkjqB7kDb-&index=2
import bpy

# https://wiki.blender.org/wiki/Process/Addons/Guidelines/metainfo#Script_Meta_Info
bl_info = {
    # 插件名
    "name": "Stepone's Addon",
    # 作者
    "author": "My Name",
    # 插件版本
    "version": (1, 0),
    # Blender版本
    "blender": (2, 80, 0),
    # 分类
    "location": "View3d > Tool",
    # 警告
    "warning": "",
    # 链接 Documentation
    "wiki_url": "https://space.bilibili.com/21077855",
    # 插件分类
    "category": "Add Mesh",
}


# User Interface Layout
# 设置一个继承bpy.types.Panel的类
class TestPanel(bpy.types.Panel):
    # 面板标签
    bl_label = "Test Panel"
    # 自定义ID名
    bl_idname = "PT_TestPanel"
    # 面板空间类型
    bl_space_type = "VIEW_3D"
    # 面板区域类型
    bl_region_type = 'UI'
    # 分类
    bl_category = 'my_bl_category'

    # 绘制UI
    def draw(self, context):
        layout = self.layout

        # https://docs.blender.org/api/current/info_best_practice.html#user-interface-layout
        # Use row(), when you want more than one property in a single line.
        # row = layout.row()
        # row.prop()
        # row.prop()
        row = layout.row()

        # 添加Label
        # 插件中打开IconViewer可查看icon名称
        row.label(text="Label", icon='BLENDER')
        # 换行
        row = layout.row()
        # 添加命令按钮
        row.operator("mesh.primitive_cube_add", text='AddCube', icon='CUBE')
        row = layout.row()
        row.operator(operator="object.text_add", text="Add Text", icon='TEXT')


# 添加一个PanelA面板,附属在TestPanel
class PanelA(bpy.types.Panel):
    bl_label = "Scale"
    bl_idname = "PT_PanelA"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = 'my_bl_category'

    # 设置为附属于PT_TestPanel（bl_idname）
    bl_parent_id = 'PT_TestPanel'
    # 默认关闭
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        obj = bpy.context.object
        row = layout.row()
        row.label(
            text="Select an option to scale your object.",
            icon='FONT_DATA')
        row = layout.row()

        # 添加操作符按钮
        # bpy.ops.transform.resize()
        row.operator("transform.resize")
        row = layout.row()

        # 更改布局Y轴间隔
        layout.scale_y = 2

        # 公开一个RNA项并放入布局
        col = layout.column()
        # bpy.context.object.scale
        col.prop(obj, "scale")

        # 拓展：
        # what is self
        # https://docs.python.org/zh-cn/3.7/faq/programming.html?highlight=self#what-is-self
        # DNA&RNA
        # https://www.blendernation.com/2008/12/01/blender-dna-rna-and-backward-compatibility/
        # DNA ：a long string with encoded types for the entire internal structure of Blender's data, saved in every
        # .blend, and in every Blender binary.
        # 一个长字符串，包含所有Blender内部数据结构的编码类型，保存在每个.blend文件，每个Blender二进制文件
        # RNA：自动生成一个Python数据访问API（Py data-access API），并允许特性（Feature）“全部可以动画（everything animatable）”，
        # 数据的自动按钮列表视图（auto-button-list-view of data），甚至处理依赖关系（dependencies）


# 再添加一个PanelB面板,附属在TestPanel
class PanelB(bpy.types.Panel):
    bl_label = "Special"
    bl_idname = "PT_PanelB"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = 'my_bl_category'

    # 设置为附属于PT_TestPanel（bl_idname）
    bl_parent_id = 'PT_TestPanel'
    # 默认关闭
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Select a Special Option", icon='BOLD')

        # bpy.ops.object.shade_smooth()
        row.operator("object.shade_smooth", icon='MOD_SMOOTH', text="Set Smooth Shading")
        # bpy.ops.object.subdivision_set()
        row.operator("object.subdivision_set")
        # bpy.ops.object.modifier_add()
        row.operator("object.modifier_add")


# 注册
def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)


# 注销
def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(PanelB)


# 在此脚本运行时注册
if __name__ == "__main__":
    register()
