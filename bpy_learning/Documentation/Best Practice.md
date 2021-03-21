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

  
|       |                                                         |
| ----- | ------------------------------------------------------- |
| row   | row()                                                   |
| col   | column()                                                |
| split | split()                                                 |
| flow  | column_flow()                                           |
| sub   | for a sub layout (a column inside a column for example) |