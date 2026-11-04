"""Assemble the delivered .blend files into a real editable master scene and render it."""
import bpy, importlib.util, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('art',ROOT/'Tools/build_teacher_art.py');a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
a.reset()
for name,col in [('MeridianCity','03_Meridian_Modules'),('AsterGT','01_AsterGT_Editable'),('NomaRobot','02_Noma_Editable'),('JetFX','04_JetFX_Editable')]:
    with bpy.data.libraries.load(str(ROOT/'SourceArt/Blender'/(name+'.blend')),link=False) as (src,dst):dst.collections=[col]
    for c in dst.collections:bpy.context.scene.collection.children.link(c)
car=bpy.data.objects['VehicleRoot'];car.location.x=1.8
robot=bpy.data.objects['RobotRoot'];robot.location=(-4.5,-14,.12);robot.rotation_euler.z=math.pi/2
jets=bpy.data.objects['JetFXRoot'];jets.hide_render=True
for o in jets.children_recursive:o.hide_render=True
a.lighting((0,-15,0),5)
ld=bpy.data.lights.new('Daylight','SUN');lo=bpy.data.objects.new('Daylight',ld);a.COL.objects.link(lo);lo.rotation_euler=(.4,-.5,-.4);ld.energy=2
a.render('09_Master_CarAndStreet',(4,6,3),(1.8,0,.8),30)
a.render('10_Driver_StreetView',(1.36,.12,1.24),(1.36,-10,1.24),18)
bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/'SourceArt/Blender/Workshop_Master.blend'))
