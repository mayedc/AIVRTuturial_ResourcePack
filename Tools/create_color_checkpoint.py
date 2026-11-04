"""Actual local Blender colour-only checkpoint; does not claim MCP execution."""
import bpy,json,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
bpy.ops.wm.open_mainfile(filepath=str(ROOT/'SourceArt/Blender/AsterGT.blend'))
def geometry_signature():
    return {o.name:{'type':o.type,'matrix':[list(r) for r in o.matrix_world], 'vertices':[list(v.co) for v in o.data.vertices] if o.type=='MESH' else []} for o in bpy.data.objects}
before=geometry_signature()
runpy.run_path(str(ROOT/'Tools/blender_safe_recolor.py'))
assert before==geometry_signature(), 'Geometry changed during material-only exercise'
bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/'Checkpoints/CP1_AsterGT_Red.blend'))
(ROOT/'Checkpoints/CP1_Color_Validation.json').write_text(json.dumps({'execution':'Blender Python locally, not MCP','geometry_unchanged':True,'object_count':len(before),'material':'M_BodyPaint','color':list(bpy.data.materials['M_BodyPaint'].diffuse_color)},indent=2))
