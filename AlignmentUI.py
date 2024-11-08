import bpy
from bpy.props import StringProperty, FloatProperty, BoolProperty, CollectionProperty
from bpy.types import Operator, Panel, PropertyGroup

# Define a PropertyGroup for each row in the grid
class AlignmentRow(PropertyGroup):
    x: FloatProperty(name="X")
    y: FloatProperty(name="Y")
    radius: FloatProperty(name="Radius", default=0.0)
    radius_enabled: BoolProperty(name="Radius Enabled", default=False)

# Operator to add a new row
class OT_AddRowOperator(Operator):
    bl_idname = "alignment.add_row"
    bl_label = "Add Row"
    bl_description = "Add a new row to the alignment grid"

    def execute(self, context):
        alignment_props = context.scene.alignment_props
        # Enable radius for the previous last row if it exists
        if len(alignment_props.rows) > 0:
            alignment_props.rows[-1].radius_enabled = True
        
        # Add a new row and disable its radius
        new_row = alignment_props.rows.add()
        new_row.radius_enabled = False
        return {'FINISHED'}

# Operator to process data and create alignment
class OT_CreateAlignmentOperator(Operator):
    bl_idname = "alignment.create_alignment"
    bl_label = "Create Alignment"
    bl_description = "Create alignment from input data using IfcOpenShell"

    def execute(self, context):
        alignment_props = context.scene.alignment_props
        name = alignment_props.name
        
        # Extract x, y pairs and radius values
        coordinates = [(row.x, row.y) for row in alignment_props.rows]
        radii = [row.radius for row in alignment_props.rows]
        radii = radii[1:-1] # remove the first and last values

        # Process the data (example with IfcOpenShell's IfcAlignmentHelper)
        try:
            import ifcopenshell
            import ifcopenshell.alignment

            helper = ifcopenshell.alignment.IfcAlignmentHelper()
            helper.add_alignment(name,coordinates,radii)
            
            helper.save_file("F:/IfcAlignmentDriver/TestAlignment.ifc")
            
            # Example usage of IfcAlignmentHelper (requires IfcOpenShell API)
            #alignment_helper = ifcopenshell.api.run("alignment.initialize", name=name, coordinates=coordinates, radii=radii)
            self.report({'INFO'}, f"Alignment '{name}' created.")
        except ImportError:
            self.report({'ERROR'}, "IfcOpenShell is not installed.")
            return {'CANCELLED'}

        return {'FINISHED'}

# Property group to store panel properties
class AlignmentProperties(PropertyGroup):
    name: StringProperty(name="Name", description="Name of the alignment")
    rows: CollectionProperty(type=AlignmentRow)

# UI panel definition
class PT_AlignmentPanel(Panel):
    bl_label = "Alignment"
    bl_idname = "OBJECT_PT_alignment"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Alignment'

    def draw(self, context):
        layout = self.layout
        alignment_props = context.scene.alignment_props

        # Text input for Name
        layout.prop(alignment_props, "name")

        # Create header row
        header = layout.row()
        header.label(text="X")
        header.label(text="Y")
        header.label(text="Radius")

        # Display rows in the grid
        for row_data in alignment_props.rows:
            row = layout.row()
            row.prop(row_data, "x", text="")
            row.prop(row_data, "y", text="")
            row.prop(row_data, "radius", text="")
            
#            # Check if row_data and radius_enabled property exist before accessing enabled
#            if row_data and hasattr(row_data, "radius_enabled"):
#                radius_field = row.prop(row_data, "radius", text="")
#                radius_field.enabled = row_data.radius_enabled
#            else:
#                row.label(text="")

        # Add buttons at the bottom
        layout.separator()
        button_column = layout.column(align=True)
        button_column.operator("alignment.add_row", text="Add Row")
        button_column.operator("alignment.create_alignment", text="Create")


# Register classes
classes = [AlignmentRow, OT_AddRowOperator, OT_CreateAlignmentOperator, AlignmentProperties, PT_AlignmentPanel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.alignment_props = bpy.props.PointerProperty(type=AlignmentProperties)
    
    # Initialize with 3 rows if empty
    alignment_props = bpy.context.scene.alignment_props
    if len(alignment_props.rows) == 0:
        for i in range(3):
            new_row = alignment_props.rows.add()
            new_row.radius_enabled = (i != 0 and i != 2)  # Enable radius for the middle row only

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.alignment_props

if __name__ == "__main__":
    register()
