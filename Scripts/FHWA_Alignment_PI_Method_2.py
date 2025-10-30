import ifcopenshell
import ifcopenshell.api.alignment
import math

# Alignment from https://www.fhwa.dot.gov/bridge/pubs/hif22034.pdf

file = ifcopenshell.file(schema="IFC4X3")
project = file.createIfcProject(GlobalId=ifcopenshell.guid.new(), Name="FHWA Example")
length = ifcopenshell.api.unit.add_conversion_based_unit(file, name="foot")
ifcopenshell.api.unit.assign_unit(file, units=[length])

alignment = ifcopenshell.api.alignment.create_from_csv(file,"C:\\Users\\rickb\\OneDrive\\Desktop\\FHWA_Alignment.csv")

#ifcopenshell.api.alignment.util.print_alignment_deep(alignment)
#ifcopenshell.api.alignment.util.print_composite_curve_deep(ifcopenshell.api.alignment.get_basis_curve(alignment))
#ifcopenshell.api.alignment.util.print_positioned_products(file)

    
ifcopenshell.file.write(file,"F:\\IfcAlignmentDriver\\Scripts\\FHWA_Alignment_by_PI_Method_2.ifc")


