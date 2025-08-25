import ifcopenshell
import ifcopenshell.api.alignment
import ifcopenshell.api.unit
import ifcopenshell.ifcopenshell_wrapper as wrapper
import numpy as np

file = ifcopenshell.file(schema="IFC4X3_ADD2")
project = file.createIfcProject(GlobalId=ifcopenshell.guid.new(),Name="Improper Reusing Horizontal",Description="Validation Service gives False Positive")
length = ifcopenshell.api.unit.add_si_unit(file,unit_type="LENGTHUNIT")
ifcopenshell.api.unit.assign_unit(file,units=[length])
unit_scale = ifcopenshell.util.unit.calculate_unit_scale(file)

alignment = ifcopenshell.api.alignment.create(file,"Test",include_vertical=True)
second_vertical = file.createIfcAlignmentVertical(GlobalId=ifcopenshell.guid.new(),Name="Second_Vertical")
ifcopenshell.api.nest.assign_object(file, related_objects=[second_vertical], relating_object=alignment)
ifcopenshell.api.alignment.add_zero_length_segment(file,second_vertical)


ifcopenshell.api.alignment.util.print_alignment_deep(alignment)

ifcopenshell.file.write(file,"F:\\IfcAlignmentDriver\\Scripts\\Improper_Reusing_Horizontal.ifc")