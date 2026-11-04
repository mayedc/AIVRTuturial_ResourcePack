"""Serialize editable Unity native assets without opening or altering a Unity project.
Generated YAML is structurally checked locally; Unity Editor acceptance is mandatory.
The accompanying editor validator creates an actual Unity acceptance report.
"""
from pathlib import Path
import json, hashlib, struct, math, collections
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'Assets/AI_VR_Workshop_V4'
HEADER='%YAML 1.1\n%TAG !u! tag:unity3d.com,2011:\n'
def guid(path):return hashlib.md5(('ai-vr-workshop-v4/'+str(Path(path).relative_to(BASE))).encode()).hexdigest()
def write(path,text,importer='NativeFormatImporter',main=0):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text,encoding='utf8')
    extra=f'  mainObjectFileID: {main}\n' if importer=='NativeFormatImporter' else ''
    path.with_name(path.name+'.meta').write_text(f'fileFormatVersion: 2\nguid: {guid(path)}\n{importer}:\n  externalObjects: {{}}\n'+extra+'  userData: \n  assetBundleName: \n  assetBundleVariant: \n')
    return guid(path)
def ref(fid,g=None):return '{fileID: '+str(fid)+((', guid: '+g+', type: 2') if g else '')+'}'
def xyz(v):return '{x: %.7g, y: %.7g, z: %.7g}'%tuple(v)
def bounds(v):
    mi=[min(v[k::3]) for k in range(3)];ma=[max(v[k::3]) for k in range(3)]
    return [(a+b)/2 for a,b in zip(mi,ma)],[(b-a)/2 for a,b in zip(mi,ma)]
def meshasset(name,vertices,normals,indices):
    n=len(vertices)//3;c,e=bounds(vertices)
    raw=b''.join(struct.pack('<6f',*(vertices[i:i+3]+normals[i:i+3])) for i in range(0,len(vertices),3))
    ix=struct.pack('<%dI'%len(indices),*indices)
    channels=''
    for i in range(14):
        channels+=f'    - stream: 0\n      offset: {12 if i==1 else 0}\n      format: 0\n      dimension: {3 if i<2 else 0}\n'
    txt=HEADER+f'''--- !u!43 &4300000
Mesh:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_Name: {name}
  serializedVersion: 11
  m_SubMeshes:
  - serializedVersion: 2
    firstByte: 0
    indexCount: {len(indices)}
    topology: 0
    baseVertex: 0
    firstVertex: 0
    vertexCount: {n}
    localAABB:
      m_Center: {xyz(c)}
      m_Extent: {xyz(e)}
  m_Shapes:
    vertices: []
    shapes: []
    channels: []
    fullWeights: []
  m_BindPose: []
  m_BoneNameHashes:
  m_RootBoneNameHash: 0
  m_BonesAABB: []
  m_VariableBoneCountWeights:
    m_Data:
  m_MeshCompression: 0
  m_IsReadable: 1
  m_KeepVertices: 1
  m_KeepIndices: 1
  m_IndexFormat: 1
  m_IndexBuffer: "{ix.hex()}"
  m_VertexData:
    serializedVersion: 3
    m_VertexCount: {n}
    m_Channels:
{channels}    m_DataSize: {len(raw)}
    _typelessdata: "{raw.hex()}"
  m_LocalAABB:
    m_Center: {xyz(c)}
    m_Extent: {xyz(e)}
  m_MeshUsageFlags: 0
  m_CookingOptions: 30
  m_BakedConvexCollisionMesh:
  m_BakedTriangleCollisionMesh:
  m_MeshMetrics[0]: 1
  m_MeshMetrics[1]: 1
  m_StreamData:
    serializedVersion: 2
    offset: 0
    size: 0
    path:
'''
    return write(BASE/'Meshes'/(name+'.asset'),txt,main=4300000)

def matasset(m):
    glass=m['name'] in ['M_Glass','M_Curtain'];sh=BASE/'Runtime'/('WorkshopGlass.shader' if glass else 'WorkshopSurface.shader')
    c=m['color'];alpha=.12 if m['name']=='M_Glass' else c[3]
    txt=HEADER+f'''--- !u!21 &2100000
Material:
  serializedVersion: 8
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_Name: {m['name']}
  m_Shader: {{fileID: 4800000, guid: {guid(sh)}, type: 3}}
  m_Parent: {{fileID: 0}}
  m_ModifiedSerializedProperties: 0
  m_ValidKeywords: []
  m_InvalidKeywords: []
  m_LightmapFlags: 4
  m_EnableInstancingVariants: 1
  m_DoubleSidedGI: 0
  m_CustomRenderQueue: {5000 if m['name']=='M_Curtain' else -1}
  stringTagMap: {{}}
  disabledShaderPasses: []
  m_LockedProperties:
  m_SavedProperties:
    serializedVersion: 3
    m_TexEnvs: []
    m_Ints: []
    m_Floats:
    - _Metallic: {m['metallic']}
    - _Emission: {m['emission']}
    m_Colors:
    - _Color: {{r: {c[0]}, g: {c[1]}, b: {c[2]}, a: {alpha}}}
'''
    return write(BASE/'Materials'/(m['name']+'.mat'),txt,main=2100000)

class Graph:
    def __init__(self):self.nodes=[];self.nextid=1000
    def node(self,name,parent=None,pos=(0,0,0),rot=(0,0,0,1),active=True):
        n=dict(name=name,id=self.nextid,t=self.nextid+1,comps=[],parent=parent,pos=pos,rot=rot,active=active,children=[])
        self.nextid+=10;self.nodes.append(n)
        if parent:parent['children'].append(n)
        return n
    def comp(self,n,typ,body):
        i=self.nextid;self.nextid+=1;n['comps'].append((i,typ,body));return i
    def script(self,n,name,fields):
        return self.comp(n,114,'  m_Enabled: 1\n  m_EditorHideFlags: 0\n  m_Script: {fileID: 11500000, guid: '+guid(BASE/'Runtime'/(name+'.cs'))+', type: 3}\n  m_Name:\n  m_EditorClassIdentifier:\n'+fields)
    def render(self,n,mg,matg):
        self.comp(n,33,'  m_Mesh: '+ref(4300000,mg)+'\n')
        return self.comp(n,23,'''  m_Enabled: 1
  m_CastShadows: 0
  m_ReceiveShadows: 0
  m_DynamicOccludee: 1
  m_StaticShadowCaster: 0
  m_MotionVectors: 0
  m_LightProbeUsage: 0
  m_ReflectionProbeUsage: 0
  m_RayTracingMode: 0
  m_RenderingLayerMask: 1
  m_RendererPriority: 0
  m_Materials:
  - '''+ref(2100000,matg)+'''
  m_StaticBatchInfo:
    firstSubMesh: 0
    subMeshCount: 0
  m_StaticBatchRoot: {fileID: 0}
  m_ProbeAnchor: {fileID: 0}
  m_LightProbeVolumeOverride: {fileID: 0}
  m_ScaleInLightmap: 1
  m_ReceiveGI: 1
  m_PreserveUVs: 0
  m_IgnoreNormalsForChartDetection: 0
  m_ImportantGI: 0
  m_StitchLightmapSeams: 0
  m_SelectedEditorRenderState: 3
  m_MinimumChartSize: 4
  m_AutoUVMaxDistance: 0.5
  m_AutoUVMaxAngle: 89
  m_LightmapParameters: {fileID: 0}
  m_SortingLayerID: 0
  m_SortingLayer: 0
  m_SortingOrder: 0
''')
    def serialize(self,scene=False):
        txt=HEADER
        for n in self.nodes:
            txt+=f'''--- !u!1 &{n['id']}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {n['t']}}}
'''
            for i,_,_ in n['comps']:txt+=f'  - component: {{fileID: {i}}}\n'
            txt+=f'''  m_Layer: 0
  m_Name: {n['name']}
  m_TagString: {'MainCamera' if n['name']=='DesktopCamera' else 'Untagged'}
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: {1 if n['active'] else 0}
--- !u!4 &{n['t']}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {n['id']}}}
  serializedVersion: 2
  m_LocalRotation: {{x: {n['rot'][0]}, y: {n['rot'][1]}, z: {n['rot'][2]}, w: {n['rot'][3]}}}
  m_LocalPosition: {xyz(n['pos'])}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children:'''+(' []\n' if not n['children'] else '\n'+''.join(f"  - {{fileID: {c['t']}}}\n" for c in n['children']))
            txt+=f"  m_Father: {{fileID: {n['parent']['t'] if n['parent'] else 0}}}\n  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}\n"
            for i,typ,body in n['comps']:
                title={114:'MonoBehaviour',33:'MeshFilter',23:'MeshRenderer',20:'Camera',81:'AudioListener',65:'BoxCollider'}[typ]
                txt+=f'''--- !u!{typ} &{i}
{title}:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {n['id']}}}
'''+body
        if scene:
            txt+='--- !u!1660057539 &9223372036854775807\nSceneRoots:\n  m_ObjectHideFlags: 0\n  m_Roots:\n'
            for n in self.nodes:
                if not n['parent']:txt+='  - '+ref(n['t'])+'\n'
        return txt

# Independent native rig with metre pivots and zero local rotations in its rest pose.
BONES={'Pelvis':((0,.88,0),None),'Spine':((0,1.04,0),'Pelvis'),'Head':((0,1.45,0),'Spine')}
for s,side in [(-1,'L'),(1,'R')]:
    BONES.update({f'Thigh_{side}':((s*.12,.94,0),'Pelvis'),f'Shin_{side}':((s*.13,.52,0),f'Thigh_{side}'),f'Foot_{side}':((s*.13,.12,0),f'Shin_{side}'),f'UpperArm_{side}':((s*.245,1.40,0),'Spine'),f'Forearm_{side}':((s*.31,1.13,0),f'UpperArm_{side}'),f'Hand_{side}':((s*.325,.89,0),f'Forearm_{side}')})

def normalize_dataset(d):
    if d.get('lettering_handedness_fixed'): return d
    for part in d['parts']:
     n=part['name'];v=part['vertices'];ix=part['triangles']
     if any(n.startswith(x) for x in ['Nose_Badge','Instrument_Text','Center_Text','Portal_Sign','Store_Sign']):
      axis=2 if n.startswith('Store_Sign') else 0
      centre=(min(v[axis::3])+max(v[axis::3]))/2
      for i in range(axis,len(v),3):v[i]=2*centre-v[i]
      part['triangles']=[ix[i+j] for i in range(0,len(ix),3) for j in (0,2,1)]
     if part['material']=='M_Glass':
      # Flat normals on the extremely thin solidify edge strips, avoiding flipped interpolated normals.
      for i in range(0,len(ix),3):
       inds=part['triangles'][i:i+3];a,bb,c=[v[j*3:j*3+3] for j in inds]
       u=[bb[k]-a[k] for k in range(3)];w=[c[k]-a[k] for k in range(3)]
       no=[u[1]*w[2]-u[2]*w[1],u[2]*w[0]-u[0]*w[2],u[0]*w[1]-u[1]*w[0]];length=sum(t*t for t in no)**.5
       if length:
        for j in inds:part['normals'][j*3:j*3+3]=[t/length for t in no]
    d['lettering_handedness_fixed']=True
    return d

def main():
    for p in (BASE/'Runtime').glob('*'):
        if p.suffix in ['.cs','.shader']:write(p,p.read_text(), 'MonoImporter' if p.suffix=='.cs' else 'ShaderImporter')
    datasets={}
    for name in ['AsterGT','NomaRobot','MeridianCity','JetFX','Road_Straight12','Road_Crosswalk12','Road_Gap12']:
        p=BASE/'Editor/ArtData'/(name+'.json')
        if not p.exists():p=BASE/'Resources/WorkshopV4'/(name+'.json')
        datasets[name]=normalize_dataset(json.loads(p.read_text()))
    mats={m['name']:matasset(m) for m in datasets['AsterGT']['materials']}
    mats['M_Curtain']=matasset(dict(name='M_Curtain',color=[0,0,0,0],metallic=0,emission=0))
    components={};metrics={}
    for name,data in datasets.items():
        groups=collections.defaultdict(list)
        for p in data['parts']:
            if name=='MeridianCity':
                c,_=bounds(p['vertices']);key=(str(math.floor(c[2]/12)),p['material'],'')
            elif name=='NomaRobot':key=('',p['material'],p['bone'])
            else:key=('',p['material'],'')
            groups[key].append(p)
        result=[]
        for idx,(key,parts) in enumerate(groups.items()):
            vertices=[];normals=[];triangles=[];bone=key[2];pivot=BONES[bone][0] if bone else (0,0,0)
            for p in parts:
                offset=len(vertices)//3
                vertices.extend([v-pivot[i%3] for i,v in enumerate(p['vertices'])]);normals.extend(p['normals'])
                triangles.extend(i+offset for i in p['triangles'])
            label=name+'_'+(bone or key[0] or 'Surface')+'_'+key[1]
            mg=meshasset(label,vertices,normals,triangles)
            result.append((label,mg,mats[key[1]],bone))
        components[name]=result;metrics[name]=dict(renderers=len(result),triangles=sum(len(p['triangles'])//3 for p in data['parts']))
    curtainmesh=meshasset('ComfortCurtain',[-2,-2,0,2,-2,0,2,2,0,-2,2,0],[0,0,-1]*4,[0,2,1,0,3,2])
    def asset(g,name,parent=None,pos=(0,0,0),rot=(0,0,0,1)):
        root=g.node(name,parent,pos,rot);bones={};anchors={}
        if name=='NomaRobot':
            for bn,(co,par) in BONES.items():
                origin=BONES[par][0] if par else (0,0,0)
                bones[bn]=g.node(bn,bones.get(par,root),tuple(a-b for a,b in zip(co,origin)))
        for label,mg,matg,bone in components[name]:g.render(g.node(label,bones.get(bone,root)),mg,matg)
        for a in datasets[name]['anchors']:anchors[a['name']]=g.node(a['name'],root,a['position'])
        return root,bones,anchors
    for name in datasets:
        g=Graph();asset(g,name);write(BASE/'Prefabs'/(name+'.prefab'),g.serialize(),main=1000)
    g=Graph();world=g.node('AI_VR_Workshop_V4');asset(g,'MeridianCity',world)
    car,_,anchors=asset(g,'AsterGT',world,(1.8,0,0))
    robot,bones,_=asset(g,'NomaRobot',world,(-4.5,.12,14),(0,math.sqrt(.5),0,math.sqrt(.5)))
    # .12 is sidewalk top; crossing animation root moves to road height before crossing.
    robot['pos']=(-4.5,.10,14)
    walkfields='  walking: 0\n'
    for field,bn in [('leftThigh','Thigh_L'),('rightThigh','Thigh_R'),('leftShin','Shin_L'),('rightShin','Shin_R'),('leftFoot','Foot_L'),('rightFoot','Foot_R'),('leftArm','UpperArm_L'),('rightArm','UpperArm_R'),('leftForearm','Forearm_L'),('rightForearm','Forearm_R')]:walkfields+=f"  {field}: {ref(bones[bn]['t'])}\n"
    walk=g.script(robot,'WorkshopRobotWalk',walkfields)
    jets,_,_=asset(g,'JetFX',car,(0,0,-2.62));jets['active']=False
    speed=g.script(car,'WorkshopSpeedControl','  targetSpeedMps: 0.85\n')
    cam=g.node('DesktopCamera',anchors['DriverEyeAnchor'])
    g.comp(cam,20,'''  m_Enabled: 1
  serializedVersion: 2
  m_ClearFlags: 2
  m_BackGroundColor: {r: 0.09, g: 0.14, b: 0.19, a: 1}
  m_projectionMatrixMode: 1
  m_GateFitMode: 2
  m_FOVAxisMode: 0
  m_SensorSize: {x: 36, y: 24}
  m_LensShift: {x: 0, y: 0}
  m_FocalLength: 20
  m_NormalizedViewPortRect:
    serializedVersion: 2
    x: 0
    y: 0
    width: 1
    height: 1
  near clip plane: 0.03
  far clip plane: 250
  field of view: 80
  orthographic: 0
  orthographic size: 5
  m_Depth: -1
  m_CullingMask:
    serializedVersion: 2
    m_Bits: 4294967295
  m_RenderingPath: -1
  m_TargetTexture: {fileID: 0}
  m_TargetDisplay: 0
  m_TargetEye: 3
  m_HDR: 0
  m_AllowMSAA: 1
  m_AllowDynamicResolution: 0
  m_ForceIntoRT: 0
  m_OcclusionCulling: 1
  m_StereoConvergence: 10
  m_StereoSeparation: 0.022
''');g.comp(cam,81,'  m_Enabled: 1\n')
    curtain=g.node('ComfortCurtain',cam,(0,0,.10));curtainRenderer=g.render(curtain,curtainmesh,mats['M_Curtain'])
    drive=g.script(car,'WorkshopDrive',f'''  pedestrian: {ref(robot['t'])}
  pedestrianWalk: {ref(walk)}
  jets: {ref(jets['id'])}
  comfortCurtain: {ref(curtainRenderer)}
  allowJetFlight: 0
  acceleration: 0.65
  paused: 0
  stage: 0
''')
    g.script(world,'WorkshopDesktopPanel',f'  drive: {ref(drive)}\n  speed: {ref(speed)}\n  showDesktopControls: 1\n')
    # Road colliders are simple, visible-gap aware. Vehicle follows a scripted route.
    for name,pos,size in [('RoadCollider_Main',(0,-.18,12.5),(8,.36,49)),('RoadCollider_Landing',(0,-.18,55.5),(8,.36,25))]:
        n=g.node(name,world,pos)
        g.comp(n,65,f'''  m_Material: {{fileID: 0}}
  m_IncludeLayers:
    serializedVersion: 2
    m_Bits: 0
  m_ExcludeLayers:
    serializedVersion: 2
    m_Bits: 0
  m_LayerOverridePriority: 0
  m_IsTrigger: 0
  m_ProvidesContacts: 0
  m_Enabled: 1
  serializedVersion: 3
  m_Size: {xyz(size)}
  m_Center: {{x: 0, y: 0, z: 0}}
''')
    write(BASE/'Scenes/Workshop_Desktop.unity',g.serialize(scene=True),'DefaultImporter')
    # A separate saved scene for XR wiring; desktop camera remains until teacher configures rig.
    write(BASE/'Scenes/Workshop_XR_Setup.unity',g.serialize(scene=True),'DefaultImporter')
    (ROOT/'SourceArt/unity_asset_metrics.json').write_text(json.dumps(metrics,indent=2))
    print(json.dumps(metrics,indent=2))

if __name__=='__main__':main()
