"""Execute through the Blender MCP code tool after opening a student COPY of AsterGT.blend.
This only changes the named material in memory. Save As a new file after visual review.
"""
import bpy
material = bpy.data.materials.get('M_BodyPaint')
if material is None:
    raise RuntimeError('M_BodyPaint missing: inspect the imported model before editing.')
color = (0.55, 0.025, 0.045, 1.0)
material.diffuse_color = color
if material.use_nodes:
    shader = material.node_tree.nodes.get('Principled BSDF')
    if shader is None:
        raise RuntimeError('Expected Principled BSDF was not found.')
    shader.inputs['Base Color'].default_value = color
print({'material': material.name, 'color': list(color), 'saved_to_disk': False})
