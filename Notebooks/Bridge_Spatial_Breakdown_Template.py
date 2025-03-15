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

import bonsai.tool as tool
#import bonsai.tool.Project as project

model = tool.Ifc.get()
project_obj = model.by_type("IfcProject")[0]
site = model.by_type("IfcSite")[0]

# Create a bridge, bridge parts and sub parts.
bridge = tool.Project.create_empty("My Bridge") #ifcopenshell.api.root.create_entity(model, ifc_class="IfcBridge", name="My Bridge")
bridgepartSUB = tool.Project.create_empty("Substructure") #ifcopenshell.api.root.create_entity(model, ifc_class="IfcBridgePart", name="Substructure")
bridgepartSUP = tool.Project.create_empty("Superstructure") #ifcopenshell.api.root.create_entity(model, ifc_class="IfcBridgePart", name="Superstructure")
#bridgepartDECK = ifcopenshell.api.root.create_entity(model, ifc_class="IfcBridgePart", name="Deck")
#bridgepartABUTMENT1 = ifcopenshell.api.root.create_entity(model, ifc_class="IfcBridgePart", name="Abutment 1")
#bridgepartABUTMENT1_FOUNDATION = ifcopenshell.api.root.create_entity(model, ifc_class="IfcBridgePart", name="Abutment 1 Foundation")
#bridgepartPIER = ifcopenshell.api.root.create_entity(model, ifc_class="IfcBridgePart", name="Pier 2")
#bridgepartPIER_FOUNDATION = ifcopenshell.api.root.create_entity(model, ifc_class="IfcBridgePart", name="Pier Foundation")
#bridgepartABUTMENT3 = ifcopenshell.api.root.create_entity(model, ifc_class="IfcBridgePart", name="Abutment 3")
#bridgepartABUTMENT3_FOUNDATION = ifcopenshell.api.root.create_entity(model, ifc_class="IfcBridgePart", name="Abutment 3 Foundation")

body = ifcopenshell.util.representation.get_context(model, "Model", "Body", "MODEL_VIEW")

tool.Project.run_root_assign_class(obj=bridge,ifc_class="IfcBridge",context=body)
tool.Project.run_root_assign_class(obj=bridgepartSUB,ifc_class="IfcBridgePart",context=body)
tool.Project.run_root_assign_class(obj=bridgepartSUP,ifc_class="IfcBridgePart",context=body)

tool.Project.run_aggregate_assign_object(relating_obj=site,related_obj=bridge)
tool.Project.run_aggregate_assign_object(relating_obj=bridge,related_obj=bridgepartSUB)
tool.Project.run_aggregate_assign_object(relating_obj=bridge,related_obj=bridgepartSUP)

# Since the site is our top level location, assign it to the project
# Then place our bridge on the site, and our parts in the bridge and so on
#ifcopenshell.api.aggregate.assign_object(model, relating_object=project_obj, products=[site])
#ifcopenshell.api.aggregate.assign_object(model, relating_object=site, products=[bridge])
#ifcopenshell.api.aggregate.assign_object(model, relating_object=bridge, products=[bridgepartSUB])
#ifcopenshell.api.aggregate.assign_object(model, relating_object=bridge, products=[bridgepartSUP])
#ifcopenshell.api.aggregate.assign_object(model, relating_object=bridgepartSUP, products=[bridgepartDECK])
#ifcopenshell.api.aggregate.assign_object(model, relating_object=bridgepartSUB, products=[bridgepartABUTMENT1])
#ifcopenshell.api.aggregate.assign_object(model, relating_object=bridgepartABUTMENT1, products=[bridgepartABUTMENT1_FOUNDATION])
#ifcopenshell.api.aggregate.assign_object(model, relating_object=bridgepartSUB, products=[bridgepartPIER])
#ifcopenshell.api.aggregate.assign_object(model, relating_object=bridgepartPIER, products=[bridgepartPIER_FOUNDATION])
#ifcopenshell.api.aggregate.assign_object(model, relating_object=bridgepartSUB, products=[bridgepartABUTMENT3])
#ifcopenshell.api.aggregate.assign_object(model, relating_object=bridgepartABUTMENT3, products=[bridgepartABUTMENT3_FOUNDATION])

#tool.Spatial.run_spatial_import_spatial_decomposition()

# Write out to a file
#model.write("/content/drive/MyDrive/Colab Notebooks/IFC/4x3model.ifc")