# source:
# https://community.osarch.org/discussion/2266/bbim-ifc-4x3-class-and-predefined-type-quick-guide-for-beginners

#import libraries
import ifcopenshell.api.root
import ifcopenshell.api.unit
import ifcopenshell.api.context
import ifcopenshell.api.project
import ifcopenshell.api.spatial
import ifcopenshell.api.geometry
import ifcopenshell.api.aggregate
# Create a blank model
model = ifcopenshell.api.project.create_file("IFC4X3_ADD2")

# All projects must have one IFC Project element
project = ifcopenshell.api.root.create_entity(model, ifc_class="IfcProject", name="My4x3Project")

# Set units to meter square meter and cubic meter
length = ifcopenshell.api.unit.add_si_unit(model, unit_type="LENGTHUNIT") 
area = ifcopenshell.api.unit.add_si_unit(model, unit_type="AREAUNIT")
volume = ifcopenshell.api.unit.add_si_unit(model, unit_type="VOLUMEUNIT")

# Assigning with arguments to metric units
ifcopenshell.api.unit.assign_unit(model, units=[length, area,volume])

# Create a modeling geometry context, to store 3D geometry 
context = ifcopenshell.api.context.add_context(model, context_type="Model")

# Store the 3D "body" geometry of objects, i.e. the body shape
body = ifcopenshell.api.context.add_context(model, context_type="Model",
    context_identifier="Body", target_view="MODEL_VIEW", parent=context)

# Create a bridge, bridge parts and sub parts.
site = ifcopenshell.api.root.create_entity(model, ifc_class="IfcSite", name="My Site")
bridge = ifcopenshell.api.root.create_entity(model, ifc_class="IfcBridge", name="BridgeA")
bridgepartSUB = ifcopenshell.api.root.create_entity(model, ifc_class="IfcBridgePart", name="Substructure")
bridgepartSUP = ifcopenshell.api.root.create_entity(model, ifc_class="IfcBridgePart", name="Superstructure")
bridgepartDECK = ifcopenshell.api.root.create_entity(model, ifc_class="IfcBridgePart", name="Deck")
bridgepartPIER = ifcopenshell.api.root.create_entity(model, ifc_class="IfcBridgePart", name="Pier")
bridgepartABUTMENT = ifcopenshell.api.root.create_entity(model, ifc_class="IfcBridgePart", name="Abutment")

# Since the site is our top level location, assign it to the project
# Then place our bridge on the site, and our parts in the bridge and so on
ifcopenshell.api.aggregate.assign_object(model, relating_object=project, products=[site])
ifcopenshell.api.aggregate.assign_object(model, relating_object=site, products=[bridge])
ifcopenshell.api.aggregate.assign_object(model, relating_object=bridge, products=[bridgepartSUB])
ifcopenshell.api.aggregate.assign_object(model, relating_object=bridge, products=[bridgepartSUP])
ifcopenshell.api.aggregate.assign_object(model, relating_object=bridgepartSUP, products=[bridgepartDECK])
ifcopenshell.api.aggregate.assign_object(model, relating_object=bridgepartSUB, products=[bridgepartPIER])
ifcopenshell.api.aggregate.assign_object(model, relating_object=bridgepartSUB, products=[bridgepartABUTMENT])

# Write out to a file
model.write("/content/drive/MyDrive/Colab Notebooks/IFC/4x3model.ifc")