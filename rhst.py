import Rhino
import rhino3dm
import compas_rhino
from compas_rhino.conversions import point_to_compas

pt = rhino3dm.Point3d(1,2,3)
compas_pt = point_to_compas(pt)
print(compas_pt)