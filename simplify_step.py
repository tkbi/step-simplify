
import cadquery as cq
import os

for file in os.listdir('.'):
    if file.endswith(".step") and not file.endswith("_simplified.step"):
        model = cq.importers.importStep(file)
        bbox = model.val().BoundingBox()
        length = bbox.xlen
        width = bbox.ylen
        height = bbox.zlen

        box = cq.Workplane("XY").box(length, width, height)
        center_x = (bbox.xmax + bbox.xmin) / 2
        center_y = (bbox.ymax + bbox.ymin) / 2
        center_z = (bbox.zmax + bbox.zmin) / 2
        box = box.translate((center_x, center_y, center_z))

        simplified_file = file.replace(".step", "_simplified.step")
        cq.exporters.export(box, simplified_file)
        print(f"Simplified file saved: {simplified_file}")
