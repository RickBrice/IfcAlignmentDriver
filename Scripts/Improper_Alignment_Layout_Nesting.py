import ifcopenshell
import ifcopenshell.api.alignment
import ifcopenshell.api.unit
import ifcopenshell.ifcopenshell_wrapper as wrapper
import numpy as np

file = ifcopenshell.file(schema="IFC4X3_ADD2")
project = file.createIfcProject(GlobalId=ifcopenshell.guid.new(),Name="Improper Alignment Layout Nesting",Description="Validation Service gives False Positive")
length = ifcopenshell.api.unit.add_si_unit(file,unit_type="LENGTHUNIT")
ifcopenshell.api.unit.assign_unit(file,units=[length])
unit_scale = ifcopenshell.util.unit.calculate_unit_scale(file)

alignment = ifcopenshell.api.alignment.create(file,"Test",include_vertical=True,include_cant=True)

h = ifcopenshell.api.alignment.get_horizontal_layout(alignment)
v = ifcopenshell.api.alignment.get_vertical_layout(alignment)
c = ifcopenshell.api.alignment.get_cant_layout(alignment)

ifcopenshell.api.nest.reorder_nesting(file, c, -1, 0)

ifcopenshell.api.alignment.util.print_alignment(alignment)

ifcopenshell.file.write(file,"F:\\IfcAlignmentDriver\\Scripts\\Improper_Alignment_Layout_Nesting.ifc")