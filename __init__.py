bl_info = {
    "name": "CenBlendInstancer",
    "author": "Lrodas",
    "version": (1, 0),
    "blender": (4, 4, 0),
    "location": "View3D > Sidebar > Centradigon Tab", # Not definitive, just describes it in preferences.
    "description": "Exporting points to json.",
    "category": "Centradigon Tools",
}

import bpy
from bpy.types import Panel, Context
from typing import Type



# Inheriting from Panel to create out own panel in the side bar. 
class CenBlendInstancerPanel(Panel): 
    bl_label = "CenBlend - Instancer"
    bl_idname = "VIEW3D_PT_cenblendinstancer"
    bl_space_type = "VIEW_3D" # Make it go into the 3D viewport, and...
    bl_region_type = "UI" # Make it go into the side panel
    bl_category = "Centradigon" # The name of the side panel category

    def draw(self, context : Context):
        layout = self.layout
        layout.label (text="Hello, World!")
        layout.operator("wm.print_output_path")
        layout.prop(context.scene, "output_directory_path") # Shows a property thats defined in register





class PrintOutputPath(bpy.types.Operator):
    bl_idname = "wm.print_output_path"
    bl_label = "Echo output path"

    def execute(self, context):
        print("You're printing something littlest of cros..." + context.scene.my_file_path)
        return {'FINISHED'}




def register() -> None:
    print("Hello lro...")
    bpy.utils.register_class(CenBlendInstancerPanel)
    bpy.utils.register_class(PrintOutputPath)
    # bpy.utils.register_class(SaveMyPath)

    # Creates the output path as a string property that lives in the .blend file.
    bpy.types.Scene.output_directory_path = bpy.props.StringProperty(
        name="Output Directory",
        description="Choose the folder corresponding to the level associated with this .blend file..",
        subtype='FILE_PATH' 
    )






def unregister() -> None:
    bpy.utils.unregister_class(CenBlendInstancerPanel)
    bpy.utils.unregister_class(PrintOutputPath)
    del bpy.types.Scene.output_directory_path

    print("Goodbye lro...")



def RunFromScript() -> None:
    print("Welcome from the script little cro. How are you, little vro?")
    register()


if __name__ == "__main__":
    RunFromScript()

