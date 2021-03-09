## BlenderAPI
### [Operator(bpy_struct)](https://docs.blender.org/api/master/bpy.ops.html)
___
---
### [**_What do operator methods do? (poll, invoke, execute, draw & modal)_**](https://blender.stackexchange.com/questions/19416/what-do-operator-methods-do-poll-invoke-execute-draw-modal)    
- `poll`    
checked before running the operator, which will never run when poll fails, used to check if an operator can run, menu items will be greyed out and if key bindings should be ignored.   
在运行Operator之前进行检查，当轮询失败时，该操作符将永远不会运行，用于检查操作符是否可以运行，菜单项将变成灰色，以及是否应该忽略键绑定  

- `invoke`  
  Think of this as "run by a person". Called by default when accessed from a key binding and menu, this takes the current context - mouse location, used for interactive operations such as dragging & drawing.  
  类似“由人运行”。默认情况下，通过键绑定和菜单访问时调用，该函数接受当前上下文-鼠标位置，用于像拖动和绘制等交互式操作。
  
- `execute`   
  This runs the operator, assuming values are set by the caller (else use defaults), this is used for undo/redo, and executing operators from Python.  
  运行Operator，假设值由调用者设置（或者用默认值），用于撤销/重做，和从Py执行Operators  
  
- `draw`  
  called to draw options, typically in the tool-bar. Without this, options will draw in the order they are defined. This gives you control over the layout.  
  用于绘制选项，通常在工具栏中。如果不这样做，选项将按照定义的顺序绘制。这样你就可以使用它控制布局。  
    
- `modal `   
  this is used for operators which continuously run, eg: fly mode, knife tool, circle select are all examples of modal operators. Modal operators can handle events which would normally access other operators, they keep running until they return `FINISHED`.  
  这是用于连续运行的操作，例如:飞行模式，切割工具，刷选。模态操作符可以处理通常会访问其他操作符的事件，它们会一直运行直到返回`FINISHED`
    
- `cancel`  
  called when Blender cancels a modal operator, not used often. Internal cleanup can be done here if needed.  
  当BLender取消一个模态操作符时调用，不经常使用。如果需要，可以在这里进行内部清理。
  
- note, button layouts may set the context of operators to invoke or execute.
  See: https://docs.blender.org/api/current/bpy.types.UILayout.html#bpy.types.UILayout.operator_context



  ![xx](./pics/QQ图片20201218235955.jpg)
