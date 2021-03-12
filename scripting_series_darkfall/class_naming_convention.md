
https://blender.stackexchange.com/questions/80804/what-are-the-class-naming-conventions-for-blender  
https://b3d.interplanety.org/en/class-naming-conventions-in-blender-2-8-python-api/  
https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/Addons  

# Class Registration
See T52599 for proposal and details.

## Access (bpy.types)
Classes registered by addons are no longer available in bpy.types. Instead addons can import their own modules and access the classes directly.

However subclasses of `[Header, Menu, Operator, Panel, UIList]` remain accessible from bpy.types.

## Naming
In Blender2.7x it was too easy to accidentally register multiple classes with the same name.

To prevent collisions 2.8x enforces naming conventions (already in use across much of Blender's code-base) for class names.

For operator bl_idname, the same naming conventions as in 2.7x remain. For headers, menus and panels, the bl_idname is expected to match the class name (automatic if none is specified).

The class name convention is: `UPPER_CASE_{SEPARATOR}_mixed_case`, in the case of a menu the regular expression is:

        [A-Z][A-Z0-9_]*_MT_[A-Za-z0-9_]+

The separator for each class is listed below:

        Header -> _HT_
        Menu -> _MT_
        Operator -> _OT_
        Panel -> _PT_
        UIList -> _UL_
Valid Examples:

        class OBJECT_OT_fancy_tool (and bl_idname = "object.fancy_tool")
        class MyFancyTool (and bl_idname = "MYADDON_MT_MyFancyTool")
        class SOME_HEADER_HT_my_header
        class PANEL123_PT_myPanel (lower case is preferred but mixed case is supported).
At the time of writing this, names that don't conform to this convention will produce a warning on startup. Eventually we will make this into an error, eg:

    Warning: 'Oscurart Files Tools' doesn't contain '_PT_' with prefix & suffix
    Warning: 'Oscurart Overrides' doesn't contain '_PT_' with prefix & suffix
    Warning: 'Oscurart Animation Tools' doesn't contain '_PT_' with prefix & suffix



&nbsp;  
&nbsp;  
&nbsp;  

### ADDONNAME_PT_main_panel
`ADDONNAME` - Using Uppercase, we type the Name of the Add-on. An underscore can be used if the name is more than one word.

`_PT_` - it is then separated by two letters which denotes the Class Type (from which the type is inherited).

`main_panel` - using lowercase, we can type the name of the Operator/Panel/Header ect.

Other Class Types:  

        HT – Header  
        MT – Menu  
        OT – Operator  
        PT – Panel  
        UL – UI list  
