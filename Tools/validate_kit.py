"""Static consistency checks. Requires PyYAML for real YAML parsing; no Unity execution.
Use: python Tools/validate_kit.py. Does not certify Unity compilation or device performance.
"""
from pathlib import Path
import json,re,math,struct,hashlib
import yaml
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'Assets/AI_VR_Workshop_V4'
external_refs=json.loads((ROOT/'Docs/ExternalPackageReferences.json').read_text())['resolved_package_refs']
errors=[];checks=[]
def check(condition,label):
    checks.append({'check':label,'passed':bool(condition)})
    if not condition:errors.append(label)
def parse_unity(p):
    s=p.read_text(encoding='utf8')
    s=re.sub(r'^%.*\n','',s,flags=re.M)
    s=re.sub(r'^--- !u!\d+ &(-?\d+)(?: stripped)?','---',s,flags=re.M)
    return list(yaml.safe_load_all(s))
guidmap={}
for p in BASE.rglob('*.meta'):
    d=yaml.safe_load(p.read_text());g=d['guid']
    check(g not in guidmap,'Unique GUID '+str(p.relative_to(BASE)));guidmap[g]=p.with_suffix('')
for p in BASE.rglob('*'):
    if p.suffix not in ['.asset','.mat','.prefab','.unity']:continue
    try:docs=parse_unity(p)
    except Exception as exc:check(False,'YAML parse '+str(p)+': '+str(exc));continue
    s=p.read_text();ids=re.findall(r'^--- !u!\d+ &(-?\d+)(?: stripped)?',s,re.M)
    check(len(ids)==len(set(ids)),'Unique local IDs '+p.name)
    for g in re.findall(r'guid: ([a-f0-9]{32})',s):check(g in guidmap or g in external_refs or g.startswith('0000000000000000'),'Resolvable GUID '+p.name+' '+g)
    if p.suffix in ['.unity','.prefab']:
        for fid in re.findall(r'\{fileID: (-?\d+)\}',s):check(fid=='0' or fid in ids,'Local reference '+p.name+' '+fid)
    if p.suffix=='.asset':
        d=docs[0]['Mesh'];vd=d['m_VertexData'];n=vd['m_VertexCount'];raw=bytes.fromhex(vd['_typelessdata'])
        check(len(raw)==vd['m_DataSize']==n*24,'Vertex buffer '+p.name)
        ix=bytes.fromhex(d['m_IndexBuffer']);indices=struct.unpack('<%dI'%(len(ix)//4),ix)
        check(len(indices)%3==0 and max(indices)<n,'Triangle indices '+p.name)
        check(d['m_SubMeshes'][0]['indexCount']==len(indices),'Submesh count '+p.name)
        values=struct.unpack('<%df'%(len(raw)//4),raw)
        check(all(math.isfinite(v) for v in values),'Finite vertex buffer '+p.name)
        # Matches Unity's official quad example: cross(edge1,edge2) aligns with outward normal.
        wrong=0;tested=0
        for i in range(0,len(indices),max(3,((len(indices)//300)//3)*3)):
            tri=indices[i:i+3]
            if len(tri)<3:continue
            a,b,c=[values[j*6:j*6+3] for j in tri];normal=[sum(values[j*6+3+k] for j in tri)/3 for k in range(3)]
            u=[b[k]-a[k] for k in range(3)];v=[c[k]-a[k] for k in range(3)]
            cross=(u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]);dot=sum(cross[k]*normal[k] for k in range(3))
            if abs(dot)>1e-10:tested+=1;wrong+=int(dot<0)
        check(wrong==0,'Clockwise winding vs normals '+p.name+f' ({tested} sampled)')
for p in (ROOT/'Tools').glob('*.py'):
    try:compile(p.read_text(),str(p),'exec');check(True,'Python syntax '+p.name)
    except SyntaxError:check(False,'Python syntax '+p.name)
for p in (ROOT/'.cursor/skills').glob('*/SKILL.md'):
    text=p.read_text();front=text.split('---',2)[1];d=yaml.safe_load(front)
    check(d['name']==p.parent.name and bool(d['description']),'Skill metadata '+p.parent.name)
for p in ROOT.rglob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        if '://' in target or target.startswith('#'):continue
        check((p.parent/target.split('#')[0]).exists(),'Document link '+p.name+' -> '+target)
check(len(list((ROOT/'SourceArt/FBX').glob('*.fbx')))==7,'Seven actual FBX files')
check(len(list((ROOT/'SourceArt/Blender').glob('*.blend')))==8,'Eight actual Blender files including master')
check(len(list((BASE/'Prefabs').glob('*.prefab')))==7,'Seven Unity prefab files')
check(len(list((BASE/'Scenes').glob('*.unity')))==3,'Three assembled Unity scene files')
# Independent physical/layout bounds; no runtime equivalence claim.
check(7.5+2.6 < 14-1.55,'Vehicle front stays before crossing when stopped')
check(32+2.6 < 37 and 48-2.7 > 43,'Whole vehicle clears both gap edges at holds')
for speed in [.25,.85,2]:
    z=0.;v=0.;t=0.
    while z<7.489 and t<120:
        remaining=max(0,7.5-z);goal=min(speed,math.sqrt(2*.65*remaining));delta=.65/60
        v=min(v+delta,goal) if v<goal else max(v-delta,goal)
        z+=min(remaining,v/60);t+=1/60
    check(7.489<=z<=7.5,'Independent stop calculation speed '+str(speed))
report={'kind':'static validation, not Unity execution','checks':len(checks),'failures':errors,'unity_editor_compilation':'See separate Unity_Actual_Validation.json; this tool only performs static checks','windows_mcp':'NOT RUN','quest':'NOT RUN','detail':checks}
(ROOT/'Checkpoints/Static_Validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='detail'},ensure_ascii=False,indent=2))
raise SystemExit(1 if errors else 0)
