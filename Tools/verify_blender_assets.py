"""Reopen .blend and FBX in real Blender; record bounds, topology and animation checks."""
import bpy, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REPORT={'blender':bpy.app.version_string,'platform':'record the machine that actually runs this script','assets':[],'robot_foot_samples':[]}
for name in ['AsterGT','NomaRobot','MeridianCity','JetFX','Road_Straight12','Road_Crosswalk12','Road_Gap12']:
    bpy.ops.wm.open_mainfile(filepath=str(ROOT/'SourceArt/Blender'/(name+'.blend')))
    meshes=[o for o in bpy.data.objects if o.type=='MESH']
    invalid=[];degenerate=0
    for o in meshes:
        for v in o.data.vertices:
            if not all(math.isfinite(x) for x in v.co):invalid.append(o.name)
        degenerate+=sum(p.area<1e-12 for p in o.data.polygons)
    record={'name':name,'blend_mesh_objects':len(meshes),'nonfinite_objects':invalid,'zero_area_faces':degenerate,'fbx_bytes':(ROOT/'SourceArt/FBX'/(name+'.fbx')).stat().st_size}
    if name=='NomaRobot':
        for f in [1,8,16,23,31]:
            bpy.context.scene.frame_set(f);row={'frame':f}
            for side in ['L','R']:
                o=bpy.data.objects['Foot_Sole_'+side];ev=o.evaluated_get(bpy.context.evaluated_depsgraph_get());me=ev.to_mesh();co=[ev.matrix_world@v.co for v in me.vertices]
                row[side]={'min_z':min(v.z for v in co),'mean_y':sum(v.y for v in co)/len(co)};ev.to_mesh_clear()
            REPORT['robot_foot_samples'].append(row)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.fbx(filepath=str(ROOT/'SourceArt/FBX'/(name+'.fbx')))
    coords=[]
    for o in bpy.data.objects:
        if o.type=='MESH':coords.extend(o.matrix_world@v.co for v in o.data.vertices)
    lo=[min(v[k] for v in coords) for k in range(3)];hi=[max(v[k] for v in coords) for k in range(3)]
    record['fbx_reimport_dimensions_metres']=[b-a for a,b in zip(lo,hi)]
    record['fbx_reimport_armatures']=len([o for o in bpy.data.objects if o.type=='ARMATURE'])
    record['fbx_reimport_actions']=[a.name for a in bpy.data.actions]
    record['fbx_reimport_meshes']=len([o for o in bpy.data.objects if o.type=='MESH'])
    if name=='NomaRobot':
        record['fbx_action_frames']=[list(a.frame_range) for a in bpy.data.actions]
        assert record['fbx_reimport_armatures']==1 and len(record['fbx_reimport_actions'])>0
    assert not invalid and coords
    REPORT['assets'].append(record)
out=ROOT/'Checkpoints/Blender_Actual_Validation.json';out.write_text(json.dumps(REPORT,indent=2),encoding='utf8')
print('BLENDER_VERIFICATION',json.dumps(REPORT))
