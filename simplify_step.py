# simplify_step.py
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.gp import gp_Pnt
from OCC.Core.Bnd import Bnd_Box
from OCC.Core.BRepBndLib import brepbndlib_Add
from OCC.Extend.DataExchange import write_step_file
import os

def simplify_step_file(input_file, output_file):
    reader = STEPControl_Reader()
    status = reader.ReadFile(input_file)
    if status != 1:
        raise Exception("Fehler beim Einlesen der STEP-Datei.")

    reader.TransferRoots()
    shape = reader.OneShape()

    bbox = Bnd_Box()
    brepbndlib_Add(shape, bbox)
    xmin, ymin, zmin, xmax, ymax, zmax = bbox.Get()

    box = BRepPrimAPI_MakeBox(gp_Pnt(xmin, ymin, zmin), xmax - xmin, ymax - ymin, zmax - zmin).Shape()
    write_step_file(box, output_file)

if __name__ == "__main__":
    for file in os.listdir('.'):
        if file.endswith('.step') and not file.endswith('_simplified.step'):
            output_file = file.replace('.step', '_simplified.step')
            simplify_step_file(file, output_file)
