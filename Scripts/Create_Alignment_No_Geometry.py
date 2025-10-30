import ifcopenshell.api.alignment
import ifcopenshell.api.context
import ifcopenshell.api.unit


file = ifcopenshell.file(schema="IFC4X3_ADD2")
project = file.createIfcProject(GlobalId=ifcopenshell.guid.new(), Name="Test")
length = ifcopenshell.api.unit.add_si_unit(file, unit_type="LENGTHUNIT")
ifcopenshell.api.unit.assign_unit(file, units=[length])

# creates an IfcAlignment with an IfcAlignmentHorizontal layout containing only the zero length segment
ali = ifcopenshell.api.alignment.create(file, "A1", include_vertical=True,include_geometry=False)

# append a segment to the horizontal layout
horizontal_alignment = ifcopenshell.api.alignment.get_horizontal_layout(ali)
vertical_alignment = ifcopenshell.api.alignment.get_vertical_layout(ali)

design_parameters = file.create_entity(
    type="IfcAlignmentHorizontalSegment",
    StartTag=None,
    EndTag=None,
    StartPoint=file.createIfcCartesianPoint(Coordinates=((0.0, 0.0))),
    StartDirection=0.0,
    StartRadiusOfCurvature=0.0,
    EndRadiusOfCurvature=0.0,
    SegmentLength=100.0,
    GravityCenterLineHeight=None,
    PredefinedType="LINE",
)
end = ifcopenshell.api.alignment.create_layout_segment(file, horizontal_alignment, design_parameters)

design_parameters = file.createIfcAlignmentVerticalSegment(
    StartDistAlong=0.0,
    HorizontalLength=50.0,
    StartHeight=20.0,
    StartGradient=1.0 / 100.0,
    EndGradient=1.0 / 100.0,
    PredefinedType="CONSTANTGRADIENT",
)
end = ifcopenshell.api.alignment.create_layout_segment(file, vertical_alignment, design_parameters)

ifcopenshell.api.alignment.util.print_alignment_deep(ali)
