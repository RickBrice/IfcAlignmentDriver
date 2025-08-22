import ifcopenshell
import ifcopenshell.api.alignment
import math

# Alignment from https://www.fhwa.dot.gov/bridge/pubs/hif22034.pdf

file = ifcopenshell.file(schema="IFC4X3")
project = file.createIfcProject(GlobalId=ifcopenshell.guid.new(), Name="FHWA Example")
length = ifcopenshell.api.unit.add_conversion_based_unit(file, name="foot")
ifcopenshell.api.unit.assign_unit(file, units=[length])

coordinates = [(500.0, 2500.0), (3340.0, 660.0), (4340.0, 5000.0), (7600.0, 4560.0), (8480.0, 2010.0)]
radii = [(1000.0), (1250.0), (950.0)]
vpoints = [(0.0, 100.0), (2000.0, 135.0), (5000.0, 105.0), (7400.0, 153.0), (9800.0, 105.0), (12800.0, 90.0)]
lengths = [(1600.0), (1200.0), (2000.0), (800.0)]

alignment = ifcopenshell.api.alignment.create_by_pi_method(
    file, "A1", coordinates, radii, vpoints, lengths
)

    
ifcopenshell.file.write(file,"F:\\IfcAlignmentDriver\\Scripts\\FHWA_Alignment_by_PI_Method.ifc")
