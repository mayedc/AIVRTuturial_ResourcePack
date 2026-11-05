"""Blender MCP helper: change only M_BodyPaint on an already saved STUDENT .blend.

Inject one of these variables into the Blender script execution context:
  TARGET_HEX = "#1E90FF"           # sRGB CSS hex
  TARGET_LINEAR_RGBA = (r,g,b,a)   # explicitly linear shader RGBA
When neither is present, the course default is the teacher's RED
linear (0.55, 0.025, 0.045, 1.0). Never silently override student choice.
This helper intentionally does NOT save any .blend or export an FBX.
"""
import bpy

def srgb_channel_to_linear(v):
    return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4

linear = globals().get("TARGET_LINEAR_RGBA")
hex_color = globals().get("TARGET_HEX")
if linear is not None and hex_color is not None:
    raise ValueError("Choose only TARGET_HEX or TARGET_LINEAR_RGBA, not both.")
if hex_color is not None:
    h = str(hex_color).strip().lstrip("#")
    if len(h) not in (6, 8) or any(c not in "0123456789abcdefABCDEF" for c in h):
        raise ValueError("TARGET_HEX must be 6 or 8 hexadecimal digits, e.g. #1E90FF.")
    srgb = [int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4)]
    alpha = int(h[6:8], 16) / 255.0 if len(h) == 8 else 1.0
    linear = (*[srgb_channel_to_linear(c) for c in srgb], alpha)
if linear is None:
    linear = (0.55, 0.025, 0.045, 1.0)
if len(linear) != 4 or not all(0.0 <= float(c) <= 1.0 for c in linear):
    raise ValueError("TARGET_LINEAR_RGBA must contain four finite values between 0 and 1.")

material = bpy.data.materials.get("M_BodyPaint")
if material is None:
    raise RuntimeError("M_BodyPaint not found. Check the student vehicle collection.")
if not material.use_nodes:
    raise RuntimeError("Expected Blender shader nodes on M_BodyPaint.")
shader = material.node_tree.nodes.get("Principled BSDF")
if shader is None or "Base Color" not in shader.inputs:
    raise RuntimeError("Principled BSDF Base Color input is missing.")
shader.inputs["Base Color"].default_value = tuple(linear)
material.diffuse_color = tuple(linear)
print({"changed_material": material.name, "linear_rgba": list(linear), "saved_to_disk": False})
