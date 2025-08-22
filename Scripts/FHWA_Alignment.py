import ifcopenshell
import ifcopenshell.api.alignment
import ifcopenshell.api.cogo
import math

# Alignment from https://www.fhwa.dot.gov/bridge/pubs/hif22034.pdf

file = ifcopenshell.file(schema="IFC4X3_ADD2")
project = file.createIfcProject(GlobalId=ifcopenshell.guid.new(),Name="FHWA Example")
length = ifcopenshell.api.unit.add_conversion_based_unit(file, name="foot")
ifcopenshell.api.unit.assign_unit(file, units=[length])
unit_scale = ifcopenshell.util.unit.calculate_unit_scale(file)

alignment = ifcopenshell.api.alignment.create(file,"A1",include_vertical=True)

horizontal_layout = ifcopenshell.api.alignment.get_horizontal_layout(alignment)

# build the horizontal layout

segment1 = file.createIfcAlignmentHorizontalSegment(
    StartPoint=file.createIfcCartesianPoint(Coordinates=((500.,2500.))),
      StartDirection=math.radians(ifcopenshell.api.cogo.bearing2dd("S 57 03 41 E")),
    StartRadiusOfCurvature=0.0,
    EndRadiusOfCurvature=0.0,
    SegmentLength=1956.78,
    PredefinedType = "LINE"
)

end = ifcopenshell.api.alignment.create_layout_segment(file,horizontal_layout,segment1)

x = float(end[0,3])/unit_scale
y = float(end[1,3])/unit_scale
dx = float(end[0,0])
dy = float(end[1,0])
dir = math.atan2(dy,dx)


segment2 = file.createIfcAlignmentHorizontalSegment(
    StartPoint=file.createIfcCartesianPoint(Coordinates=((x,y))),
    StartDirection=dir,
    StartRadiusOfCurvature=1000.0,
    EndRadiusOfCurvature=1000.0,
    SegmentLength=1919.22,
    PredefinedType = "CIRCULARARC"
)

end = ifcopenshell.api.alignment.create_layout_segment(file,horizontal_layout,segment2)

x = float(end[0,3])/unit_scale
y = float(end[1,3])/unit_scale
dx = float(end[0,0])
dy = float(end[1,0])
dir = math.atan2(dy,dx)


segment3 = file.createIfcAlignmentHorizontalSegment(
    StartPoint=file.createIfcCartesianPoint(Coordinates=((x,y))),
    StartDirection=dir,
    StartRadiusOfCurvature=0.0,
    EndRadiusOfCurvature=0.0,
    SegmentLength=1886.90,
    PredefinedType = "LINE"
)

end = ifcopenshell.api.alignment.create_layout_segment(file,horizontal_layout,segment3)

x = float(end[0,3])/unit_scale
y = float(end[1,3])/unit_scale
dx = float(end[0,0])
dy = float(end[1,0])
dir = math.atan2(dy,dx)


segment4 = file.createIfcAlignmentHorizontalSegment(
    StartPoint=file.createIfcCartesianPoint(Coordinates=((x,y))),
    StartDirection=dir,
    StartRadiusOfCurvature=-1250.,
    EndRadiusOfCurvature=-1250.,
    SegmentLength=1848.12,
    PredefinedType = "CIRCULARARC"
)

end = ifcopenshell.api.alignment.create_layout_segment(file,horizontal_layout,segment4)

x = float(end[0,3])/unit_scale
y = float(end[1,3])/unit_scale
dx = float(end[0,0])
dy = float(end[1,0])
dir = math.atan2(dy,dx)


segment5 = file.createIfcAlignmentHorizontalSegment(
    StartPoint=file.createIfcCartesianPoint(Coordinates=((x,y))),
    StartDirection=dir,
    StartRadiusOfCurvature=0.0,
    EndRadiusOfCurvature=0.0,
    SegmentLength=1564.63,
    PredefinedType = "LINE"
)

end = ifcopenshell.api.alignment.create_layout_segment(file,horizontal_layout,segment5)

x = float(end[0,3])/unit_scale
y = float(end[1,3])/unit_scale
dx = float(end[0,0])
dy = float(end[1,0])
dir = math.atan2(dy,dx)

segment6 = file.createIfcAlignmentHorizontalSegment(
    StartPoint=file.createIfcCartesianPoint(Coordinates=((x,y))),
    StartDirection=dir,
    StartRadiusOfCurvature=-950.,
    EndRadiusOfCurvature=-950.,
    SegmentLength=1049.12,
    PredefinedType = "CIRCULARARC"
)

end = ifcopenshell.api.alignment.create_layout_segment(file,horizontal_layout,segment6)

x = float(end[0,3])/unit_scale
y = float(end[1,3])/unit_scale
dx = float(end[0,0])
dy = float(end[1,0])
dir = math.atan2(dy,dx)


segment7 = file.createIfcAlignmentHorizontalSegment(
    StartPoint=file.createIfcCartesianPoint(Coordinates=((x,y))),
    StartDirection=dir,
    StartRadiusOfCurvature=0.0,
    EndRadiusOfCurvature=0.0,
    SegmentLength=2112.28,
    PredefinedType = "LINE"
)

end = ifcopenshell.api.alignment.create_layout_segment(file,horizontal_layout,segment7)

# Build the vertical layout

vertical_layout = ifcopenshell.api.alignment.get_vertical_layout(alignment)

vsegment1 = file.createIfcAlignmentVerticalSegment(
    StartDistAlong=0.,
    HorizontalLength=1200.,
    StartHeight=100.,
    StartGradient=1.75/100.,
    EndGradient=1.75/100.,
    PredefinedType = "CONSTANTGRADIENT"
)

end = ifcopenshell.api.alignment.create_layout_segment(file,vertical_layout,vsegment1)

x = float(end[0,3])/unit_scale
y = float(end[1,3])/unit_scale
dx = float(end[0,0])
dy = float(end[1,0])


vsegment2 = file.createIfcAlignmentVerticalSegment(
    StartDistAlong=x,
    HorizontalLength=1600.,
    StartHeight=y,
    StartGradient=dy/dx,
    EndGradient=1.0/100.,
    PredefinedType = "PARABOLICARC"
)

end = ifcopenshell.api.alignment.create_layout_segment(file,vertical_layout,vsegment2)

x = float(end[0,3])/unit_scale
y = float(end[1,3])/unit_scale
dx = float(end[0,0])
dy = float(end[1,0])


vsegment3 = file.createIfcAlignmentVerticalSegment(
    StartDistAlong=x,
    HorizontalLength=1600.,
    StartHeight=y,
    StartGradient=dy/dx,
    EndGradient=dy/dx,
    PredefinedType = "CONSTANTGRADIENT"
)

end = ifcopenshell.api.alignment.create_layout_segment(file,vertical_layout,vsegment3)

x = float(end[0,3])/unit_scale
y = float(end[1,3])/unit_scale
dx = float(end[0,0])
dy = float(end[1,0])



vsegment4 = file.createIfcAlignmentVerticalSegment(
    StartDistAlong=x,
    HorizontalLength=1200.,
    StartHeight=y,
    StartGradient=dy/dx,
    EndGradient=2.0/100.,
    PredefinedType = "PARABOLICARC"
)

end = ifcopenshell.api.alignment.create_layout_segment(file,vertical_layout,vsegment4)

x = float(end[0,3])/unit_scale
y = float(end[1,3])/unit_scale
dx = float(end[0,0])
dy = float(end[1,0])


vsegment5 = file.createIfcAlignmentVerticalSegment(
    StartDistAlong=x,
    HorizontalLength=800.,
    StartHeight=y,
    StartGradient=dy/dx,
    EndGradient=dy/dx,
    PredefinedType = "CONSTANTGRADIENT"
)

end = ifcopenshell.api.alignment.create_layout_segment(file,vertical_layout,vsegment5)

x = float(end[0,3])/unit_scale
y = float(end[1,3])/unit_scale
dx = float(end[0,0])
dy = float(end[1,0])


vsegment6 = file.createIfcAlignmentVerticalSegment(
    StartDistAlong=x,
    HorizontalLength=2000.,
    StartHeight=y,
    StartGradient=dy/dx,
    EndGradient=-2.0/100.,
    PredefinedType = "PARABOLICARC"
)

end = ifcopenshell.api.alignment.create_layout_segment(file,vertical_layout,vsegment6)

x = float(end[0,3])/unit_scale
y = float(end[1,3])/unit_scale
dx = float(end[0,0])
dy = float(end[1,0])


vsegment7 = file.createIfcAlignmentVerticalSegment(
    StartDistAlong=x,
    HorizontalLength=1000.,
    StartHeight=y,
    StartGradient=dy/dx,
    EndGradient=dy/dx,
    PredefinedType = "CONSTANTGRADIENT"
)

end = ifcopenshell.api.alignment.create_layout_segment(file,vertical_layout,vsegment7)

x = float(end[0,3])/unit_scale
y = float(end[1,3])/unit_scale
dx = float(end[0,0])
dy = float(end[1,0])


vsegment8 = file.createIfcAlignmentVerticalSegment(
    StartDistAlong=x,
    HorizontalLength=800.,
    StartHeight=y,
    StartGradient=dy/dx,
    EndGradient=-0.5/100.,
    PredefinedType = "PARABOLICARC"
)

end = ifcopenshell.api.alignment.create_layout_segment(file,vertical_layout,vsegment8)

x = float(end[0,3])/unit_scale
y = float(end[1,3])/unit_scale
dx = float(end[0,0])
dy = float(end[1,0])


vsegment9 = file.createIfcAlignmentVerticalSegment(
    StartDistAlong=x,
    HorizontalLength=2600.,
    StartHeight=y,
    StartGradient=dy/dx,
    EndGradient=dy/dx,
    PredefinedType = "CONSTANTGRADIENT"
)

end = ifcopenshell.api.alignment.create_layout_segment(file,vertical_layout,vsegment9)

ifcopenshell.file.write(file,"F:\\IfcAlignmentDriver\\Scripts\\FHWA_Alignment.ifc")