"""Reusable 12m road tiles. Separate files; no need to extract them from city geometry."""
import importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('art',ROOT/'Tools/build_teacher_art.py');a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
for name in ['Road_Straight12','Road_Crosswalk12','Road_Gap12']:
    a.reset();a.collection(name);root=a.empty(name);a.PARENT=root
    segments=[(0,12)] if name!='Road_Gap12' else [(-4.5,3),(4.5,3)]
    for y,length in segments:
        a.box('Road_Deck',(0,y,-.18),(8,length,.36),'M_Road',.03)
        for x in [-5.15,5.15]:
            a.box('Sidewalk',(x,y,-.03),(2.3,length,.30),'M_Concrete',.03)
            a.box('Curb',(x/abs(x)*4.05,y,.04),(.15,length,.23),'M_White',.02)
        for x in [-3.66,3.66]:a.box('Edge_Line',(x,y,.008),(.07,length,.016),'M_White',0)
    if name=='Road_Crosswalk12':
        for i in range(9):a.box('Crosswalk_Stripe',(i*.8-3.2,0,.009),(.43,3.1,.018),'M_White',.01)
        a.box('Stop_Line',(1.9,3.2,.008),(3.3,.18,.016),'M_White',0)
    elif name=='Road_Straight12':
        for y in [-4.5,-1.5,1.5,4.5]:a.box('Lane_Dash',(0,y,.008),(.10,1.5,.016),'M_White',0)
    else:
        for y in [-3.1,3.1]:
            a.box('Hazard_Threshold',(0,y,.018),(7.9,.20,.036),'M_Amber',.008)
            for x in [-3,-1,1,3]:a.box('Bridge_Girder',(x,y,-.65),(.25,.48,.75),'M_Trim',.02)
    a.export_asset(name,root)
metrics=json.loads((ROOT/'SourceArt/asset_metrics.json').read_text());metrics=[m for m in metrics if not m['asset'].startswith('Road_')]+a.REPORT
(ROOT/'SourceArt/asset_metrics.json').write_text(json.dumps(metrics,indent=2))
a.reset();r=a.jets();a.lighting((0,.3,.5),.4);a.render('11_JetFX',(-2,-2,1.6),(0,.3,.5),55)
