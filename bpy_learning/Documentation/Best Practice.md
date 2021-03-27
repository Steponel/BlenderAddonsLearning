# Best Practice

---

## User Interface Layout

+ #### layout()
    The basic layout is a simple top-to-bottom layout.  
    简单的自上而下布局
  
      layout.prop()
      layout.prop()


+ #### layout.row()
  Use row(), when you want more than one property in a single line.  
  行
  
        row = layout.row()
        row.prop()
        row.prop()


+ #### layout.column()
  Use column(), when you want your properties in a column.  
  列

        col = layout.column()
        col.prop()
        col.prop()

+ #### layout.split()
  This can be used to create more complex layouts. For example, you can split the layout and create two column() layouts next to each other. Do not use split, when you simply want two properties in a row. Use row() instead.  
  分割
  
        split = layout.split()
        
        col = split.column()
        col.prop()
        col.prop()
        
        col = split.column()
        col.prop()
        col.prop()

  
  #### 一般替换示意
    |       |                                                         |
    | ----- | ------------------------------------------------------- |
    | row   | row()                                                   |
    | col   | column()                                                |
    | split | split()                                                 |
    | flow  | column_flow()                                           |
    | sub   | for a sub layout (a column inside a column for example) |



### Tips:我们可以这样写：

    def draw(self, context):
        col = self.layout.column(align=True)
        self.layout.operator(
            operator="mesh.monkey_grid", text="Default Grid", icon="MONKEY"
        )
        # 面板显示操作符按钮，并更改了操作符默认值
        props = self.layout.operator(
            operator="mesh.monkey_grid", text="BigGrid", icon="MONKEY"
        )
        # 在下方更改操作符自己的属性（在另一个按钮生成前），等同于更改按钮的默认值
        props.count_x = 10
        props.count_y = 10
        props.size = 0.8

        # 当新的面板操作符按钮生成后，则可进行同样操作
        props = self.layout.operator(
            operator="mesh.monkey_grid", text="SmallGrid", icon="MONKEY"
        )
        props.count_x = 1
        props.count_y = 1