"""Teacher-only original art generator. Blender 5.2 tested; students use saved assets.
Run blender --background --python Tools/build_teacher_art.py -- --root KIT_ROOT
Coordinates: metres, X right, -Y forward, Z up. No downloaded geometry/textures.
"""
import bpy, math, json, sys, random
from pathlib import Path
from mathutils import Vector
from math import sin, cos, pi, sqrt

args = sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else []
ROOT = Path(args[args.index('--root')+1]).resolve() if '--root' in args else Path(__file__).resolve().parents[1]
ART = ROOT/'SourceArt'; DATA = ROOT/'SourceArt/Generated/ArtData/Editor/ArtData'
for p in [ART/'Blender', ART/'FBX', ART/'Previews', DATA]: p.mkdir(parents=True,exist_ok=True)
random.seed(24)
COL=None; PARENT=None; M={}; REPORT=[]

def material(name, color, metal=0, rough=.4, emission=0, alpha=1):
    m=bpy.data.materials.new(name); m.diffuse_color=(*color,alpha); m.use_nodes=True
    p=m.node_tree.nodes.get('Principled BSDF')
    p.inputs['Base Color'].default_value=(*color,alpha)
    p.inputs['Metallic'].default_value=metal; p.inputs['Roughness'].default_value=rough
    p.inputs['Alpha'].default_value=alpha
    if emission:
        p.inputs['Emission Color'].default_value=(*color,1); p.inputs['Emission Strength'].default_value=emission
    if alpha<1:
        p.inputs['Transmission Weight'].default_value=.85
        m.surface_render_method='DITHERED'
    M[name]=m; return m

def reset():
    global M
    bpy.ops.wm.read_factory_settings(use_empty=True); M={}
    s=bpy.context.scene; s.unit_settings.system='METRIC'; s.unit_settings.scale_length=1
    s.render.fps=30
    material('M_BodyPaint',(.38,.48,.59),.72,.24)
    material('M_Pearl',(.78,.84,.86),.2,.3)
    material('M_Trim',(.018,.029,.042),.35,.33)
    material('M_Rubber',(.012,.016,.022),.02,.68)
    material('M_Alloy',(.42,.49,.55),.85,.22)
    material('M_Glass',(.12,.25,.30),.05,.12,alpha=.42)
    material('M_Seat',(.52,.56,.57),.05,.7)
    material('M_Screen',(.009,.035,.052),.2,.23)
    material('M_Cyan',(.05,.72,1),.15,.3,2)
    material('M_Amber',(1,.29,.04),.1,.4,1.5)
    material('M_Red',(1,.025,.045),.1,.35,2)
    material('M_Road',(.055,.075,.09),0,.82)
    material('M_Concrete',(.25,.30,.34),.05,.8)
    material('M_Building',(.09,.15,.19),.3,.55)
    material('M_Window',(.035,.12,.17),.55,.22)
    material('M_White',(.75,.82,.83),0,.6)

def collection(name):
    global COL,PARENT
    COL=bpy.data.collections.new(name); bpy.context.scene.collection.children.link(COL)
    PARENT=None
    return COL

def finish(obj,name,mat=None,parent=True):
    obj.name=name
    for c in list(obj.users_collection): c.objects.unlink(obj)
    COL.objects.link(obj)
    if parent and PARENT: obj.parent=PARENT
    if mat: obj.data.materials.append(M[mat])
    return obj

def empty(name,loc=(0,0,0)):
    o=bpy.data.objects.new(name,None); COL.objects.link(o); o.location=loc
    if PARENT: o.parent=PARENT
    return o

def mesh(name,verts,faces,mat,smooth=False):
    me=bpy.data.meshes.new(name+'_Mesh'); me.from_pydata(verts,[],faces); me.update()
    o=bpy.data.objects.new(name,me); finish(o,name,mat)
    # Explicitly recalculate winding for mixed construction directions.
    import bmesh
    bm=bmesh.new(); bm.from_mesh(me); bmesh.ops.recalc_face_normals(bm,faces=list(bm.faces)); bm.to_mesh(me); bm.free()
    for p in me.polygons: p.use_smooth=smooth
    return o

def bevel(o,width=.02,segments=3):
    b=o.modifiers.new('Edge highlights','BEVEL'); b.width=width; b.segments=segments
    b=o.modifiers.new('Weighted surface normals','WEIGHTED_NORMAL'); b.keep_sharp=True
    return o

def box(name,loc,dim,mat,bev=.02):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc); o=bpy.context.object
    o.dimensions=dim; bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    finish(o,name,mat)
    if bev: bevel(o,bev)
    return o

def tube(name,points,radius,mat,cyclic=False):
    cu=bpy.data.curves.new(name+'_Curve','CURVE'); cu.dimensions='3D'; cu.resolution_u=2
    sp=cu.splines.new('POLY'); sp.points.add(len(points)-1)
    for p,co in zip(sp.points,points): p.co=(*co,1)
    sp.use_cyclic_u=cyclic; cu.bevel_depth=radius; cu.bevel_resolution=2
    o=bpy.data.objects.new(name,cu); finish(o,name,mat); return o

def cylinder(name,loc,r,depth,mat,axis='Z',vertices=40):
    rot=(pi/2,0,0) if axis=='Y' else ((0,pi/2,0) if axis=='X' else (0,0,0))
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices,radius=r,depth=depth,location=loc,rotation=rot)
    o=finish(bpy.context.object,name,mat); bevel(o,.008,2)
    for p in o.data.polygons:p.use_smooth=len(p.vertices)==4
    return o

def ellipsoid(name,loc,scale,mat):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=24,ring_count=12,location=loc)
    o=finish(bpy.context.object,name,mat);o.scale=scale
    for p in o.data.polygons:p.use_smooth=True
    return o

def loft(name,rings,mat,n=24):
    # Each ring: centre XYZ, half width X, half depth Y. Sculpted anatomical profiles.
    vs=[]
    for x,y,z,rx,ry in rings:
        for j in range(n):
            a=2*pi*j/n;vs.append((x+rx*cos(a),y+ry*sin(a),z))
    fs=[tuple(range(n-1,-1,-1))]
    for i in range(len(rings)-1):
        for j in range(n):fs.append((i*n+j,i*n+(j+1)%n,(i+1)*n+(j+1)%n,(i+1)*n+j))
    fs.append(tuple((len(rings)-1)*n+j for j in range(n)))
    return mesh(name,vs,fs,mat,True)

def panel(name,corners,mat,thickness=.012):
    o=mesh(name,corners,[tuple(range(len(corners)))],mat)
    if thickness:
        m=o.modifiers.new('Panel thickness','SOLIDIFY');m.thickness=thickness
        bevel(o,.008,2)
    return o

# Original 3x5 block-letter geometry; no font files or third-party glyph outlines.
GLYPHS = {
'A':'010/101/111/101/101','B':'110/101/110/101/110','C':'011/100/100/100/011',
'D':'110/101/101/101/110','E':'111/100/110/100/111','F':'111/100/110/100/100',
'G':'011/100/101/101/011','H':'101/101/111/101/101','I':'111/010/010/010/111',
'J':'001/001/001/101/010','K':'101/101/110/101/101','L':'100/100/100/100/111',
'M':'101/111/111/101/101','N':'101/111/111/111/101','O':'010/101/101/101/010',
'P':'110/101/110/100/100','Q':'010/101/101/111/011','R':'110/101/110/101/101',
'S':'011/100/010/001/110','T':'111/010/010/010/010','U':'101/101/101/101/111',
'V':'101/101/101/101/010','W':'101/101/111/111/101','X':'101/101/010/101/101',
'Y':'101/101/010/010/010','Z':'111/001/010/100/111','0':'111/101/101/101/111',
'1':'010/110/010/010/111','2':'110/001/010/100/111','3':'110/001/010/001/110',
'4':'101/101/111/001/001','/':'001/001/010/100/100',' ':'000/000/000/000/000'}
def text_obj(name,text,loc,size,mat,rotation=(pi/2,0,0)):
    vertices=[];faces=[];pixel=size/5;offset=-len(text)*4*pixel/2
    for index,ch in enumerate(text):
        for row,bits in enumerate(GLYPHS.get(ch,GLYPHS[' ']).split('/')):
            for col,bit in enumerate(bits):
                if bit!='1':continue
                x=offset+(index*4+col)*pixel;y=(4-row)*pixel;d=pixel*.92;k=len(vertices)
                vertices.extend([(x,y,0),(x+d,y,0),(x+d,y+d,0),(x,y+d,0)])
                faces.append((k,k+1,k+2,k+3))
    o=mesh(name,vertices,faces,mat);o.location=loc;o.rotation_euler=rotation
    return o

def line_grid(name,func,nu,nv,mat):
    vs=[func(i/nu,j/nv) for i in range(nu+1) for j in range(nv+1)]
    fs=[]
    for i in range(nu):
        for j in range(nv):
            k=i*(nv+1)+j;fs.append((k,k+1,k+nv+2,k+nv+1))
    return mesh(name,vs,fs,mat,True)

def car():
    global PARENT
    collection('01_AsterGT_Editable');root=empty('VehicleRoot');PARENT=root
    def width(y): return .94+.08*cos(y/2.5*pi/2)-.12*(abs(y)/2.5)**5
    def top(y): return 1.015+.045*cos(y*pi/2.6)-.24*max(0,(-y-1.7)/.75)
    def bottom(y):
        z=.27
        for wy in [-1.48,1.48]:
            d=abs(y-wy)
            if d<.505:z=max(z,.46+sqrt(.505**2-d*d))
        return z
    for s,side in [(-1,'L'),(1,'R')]:
        def surface(u,v):
            y=-2.43+4.86*u;lo=bottom(y);hi=max(top(y),lo+.045)
            z=lo+(hi-lo)*v
            return (s*(width(y)-.045*((hi-z)/(hi-.27))**2),y,z)
        o=line_grid('Body_Side_'+side,surface,240,6,'M_BodyPaint')
        so=o.modifiers.new('Editable shell thickness','SOLIDIFY');so.thickness=.015
        # Exact wheel clearance edges. No boolean remesh rippling.
        for wy,ax in [(-1.48,'F'),(1.48,'R')]:
            points=[]
            for j in range(65):
                a=pi*j/64;y=wy+.505*cos(a);points.append((s*(width(y)+.004),y,.46+.505*sin(a)))
            tube('WheelArch_Trim_'+ax+side,points,.012,'M_Trim')
        tube('Door_Seam_'+side,[(s*(width(y)+.004),y,z) for y,z in [(-.93,1.035),(-.8,.67),(-.61,.34),(.72,.34),(.92,.69),(.94,1.055)]],.006,'M_Trim')
        box('FlushHandle_'+side,(s*1.015,.56,.94),(.018,.19,.025),'M_Trim',.009)
        box('Sill_'+side,(s*.98,0,.25),(.11,1.84,.07),'M_Trim')
        # Exterior window opening with independent tint panel and precision borders.
        corners=[(s*.95,-1.05,1.05),(s*.76,-.40,1.52),(s*.76,.59,1.52),(s*.94,1.39,1.07)]
        panel('Windows_Side_'+side,corners,'M_Glass',.004)
        tube('WindowFrame_'+side,corners,.022,'M_Trim',True)
        tube('RoofRail_'+side,[(s*.76,-.40,1.54),(s*.765,.59,1.54),(s*.94,1.43,1.06)],.032,'M_BodyPaint')
        tube('A_Pillar_'+side,[(s*.95,-1.07,1.04),(s*.76,-.41,1.53)],.035,'M_BodyPaint')
        box('Mirror_Stem_'+side,(s*1.02,-.92,1.07),(.18,.04,.035),'M_Trim',.01)
        box('CameraMirror_'+side,(s*1.11,-.94,1.10),(.19,.18,.06),'M_BodyPaint',.025)
        box('Door_Interior_'+side,(s*.90,.15,.69),(.06,1.68,.56),'M_Trim',.04)
        box('Door_Armrest_'+side,(s*.84,.16,.72),(.11,.85,.09),'M_Seat',.035)
        tube('Door_Ambient_'+side,[(s*.858,-.69,.86),(s*.858,.62,.86),(s*.858,.86,.94)],.009,'M_Cyan')
    # Hood and rear deck are shaped grids, sharing side profile dimensions.
    def hood(u,v):
        y=-2.43+1.38*u;x=(2*v-1)*width(y)
        return (x,y,top(y)+.035*(1-(2*v-1)**2))
    line_grid('Hood_ContinuousSurface',hood,32,28,'M_BodyPaint')
    def deck(u,v):
        y=1.38+1.05*u;return ((2*v-1)*width(y),y,top(y)+.025*(1-(2*v-1)**2))
    line_grid('Rear_Deck',deck,24,24,'M_BodyPaint')
    for s in [-1,1]:
        tube('HoodCrease',[(s*(.58+.10*t),-2.29+1.16*t,top(-2.29+1.16*t)+.014) for t in [j/24 for j in range(25)]],.004,'M_Trim')
    panel('Windshield',[(-.95,-1.05,1.055),(.95,-1.05,1.055),(.76,-.4,1.53),(-.76,-.4,1.53)],'M_Glass',.004)
    panel('Rear_Glass',[(-.76,.59,1.53),(.76,.59,1.53),(.94,1.39,1.07),(-.94,1.39,1.07)],'M_Glass',.004)
    roof=line_grid('Roof_Panel',lambda u,v:((2*v-1)*.765,-.40+.99*u,1.54+.045*sin(pi*u)+.025*(1-(2*v-1)**2)),20,20,'M_BodyPaint')
    roof.modifiers.new('Roof thickness','SOLIDIFY').thickness=.025
    box('Cabin_Floor',(0,.08,.31),(1.75,2.30,.08),'M_Trim',.025)
    # Front and rear fascia: clean continuous hard-surface silhouettes.
    for y,label in [(-2.43,'Front'),(2.43,'Rear')]:
        ztop=top(y)
        panel(label+'_Fascia',[(-.83,y,.30),(.83,y,.30),(.89,y,ztop),(-.89,y,ztop)],'M_Trim',.06)
        box(label+'_Splitter',(0,y,.26),(1.83,.16,.045),'M_Trim',.015)
        tube(label+'_LightBar',[(-.85,y*1.035,ztop-.025),(0,y*1.035,ztop-.015),(.85,y*1.035,ztop-.025)],.013,'M_Cyan' if y<0 else 'M_Red')
        for s in [-1,1]:
            box(label+'_Intake',(s*.65,y*1.035,.49),(.32,.025,.20),'M_Rubber',.02)
            for i in range(4):box(label+'_IntakeFin',(s*.65,y*1.04,.43+i*.036),(.28,.016,.012),'M_Alloy',.003)
    text_obj('Nose_Badge','ASTER', (0,-2.456,.64),.07,'M_Alloy')
    # Wheels: profiled tyres, visible rim barrel, swept turbine spokes and brake hardware.
    for s,side in [(-1,'L'),(1,'R')]:
        for y,ax in [(-1.48,'F'),(1.48,'R')]:
            x=s*.985;z=.46; n=64;vs=[]
            profile=[(-.135,.32),(-.145,.38),(-.112,.443),(-.065,.46),(.065,.46),(.112,.443),(.145,.38),(.135,.32)]
            for dx,r in profile:
                for j in range(n):a=2*pi*j/n;vs.append((x+dx,y+r*cos(a),z+r*sin(a)))
            fs=[]
            for k in range(len(profile)):
                for j in range(n):fs.append((k*n+j,k*n+(j+1)%n,((k+1)%len(profile))*n+(j+1)%n,((k+1)%len(profile))*n+j))
            mesh('Tyre_'+ax+side,vs,fs,'M_Rubber',True)
            for dx in [-.065,0,.065]:
                tube('Tyre_Channel_'+ax+side,[(x+dx,y+.461*cos(j*2*pi/64),z+.461*sin(j*2*pi/64)) for j in range(64)],.004,'M_Trim',True)
            cylinder('RimBarrel_'+ax+side,(x,y,z),.335,.25,'M_Trim','X',64)
            cylinder('BrakeDisc_'+ax+side,(x+s*.095,y,z),.265,.018,'M_Alloy','X',48)
            box('BrakeCaliper_'+ax+side,(x+s*.115,y+.20,z),(.045,.085,.24),'M_Amber',.022)
            for i in range(7):
                a=i*2*pi/7;pts=[]
                for r,ang in [(.075,a-.08),(.31,a+.13),(.31,a+.36),(.11,a+.23)]:pts.append((x+s*.151,y+r*cos(ang),z+r*sin(ang)))
                panel('TurbineSpoke_'+ax+side,pts,'M_Alloy',.018)
            tube('RimLip_'+ax+side,[(x+s*.15,y+.325*cos(j*2*pi/64),z+.325*sin(j*2*pi/64)) for j in range(64)],.012,'M_Alloy',True)
            cylinder('WheelHub_'+ax+side,(x+s*.17,y,z),.083,.035,'M_Trim','X')
    # Ergonomic cockpit. Low dashboard keeps a clear driver sightline.
    box('Dashboard_Main',(0,-.86,.88),(1.72,.38,.22),'M_Trim',.065)
    tube('Dashboard_Ambient',[(-.82,-.66,.99),(0,-.65,1.015),(.82,-.66,.99)],.008,'M_Cyan')
    for x in [-.68,.68]:
        box('AirVent',(x,-.65,.90),(.25,.025,.065),'M_Rubber',.015)
        for i in range(5):box('VentBlade',(x-.09+i*.045,-.631,.90),(.012,.015,.05),'M_Alloy',.002)
    for x,y,w,h,label in [(-.44,-.64,.39,.16,'Instrument'),(.22,-.60,.46,.27,'Center')]:
        box(label+'_DisplayFrame',(x,y,1.04),(w+.025,.035,h+.025),'M_Trim',.015)
        box(label+'_Display',(x,y+.021,1.04),(w,.008,h),'M_Screen',.008)
        # Screen content is original vector-like geometry, readable in cockpit.
        text_obj(label+'_Text','READY' if x<0 else 'ASTER / AUTODRIVE',(x,y+.029,1.07),.028,'M_Cyan',(pi/2,0,pi))
        for i in range(3):box(label+'_UI',(x-.09+i*.09,y+.029,.99),(.055,.005,.008),'M_Cyan',.002)
    box('Center_Console',(0,.06,.52),(.24,1.09,.25),'M_Trim',.045)
    box('Console_Pad',(0,.34,.67),(.22,.30,.07),'M_Seat',.025)
    cylinder('Drive_Dial',(0,-.20,.66),.055,.025,'M_Alloy')
    for x,label in [(-.44,'Driver'),(.44,'Passenger')]:
        box(label+'_SeatBase',(x,.26,.48),(.48,.66,.18),'M_Trim',.07)
        box(label+'_SeatCushion',(x,.20,.59),(.39,.57,.12),'M_Seat',.055)
        back=box(label+'_SeatBack',(x,.60,.86),(.46,.15,.66),'M_Trim',.065);back.rotation_euler.x=-.13
        back=box(label+'_BackInset',(x,.505,.88),(.32,.045,.48),'M_Seat',.06);back.rotation_euler.x=-.13
        for s in [-1,1]:
            box(label+'_Bolster',(x+s*.19,.18,.66),(.09,.50,.14),'M_Seat',.04)
            tube(label+'_SeatStitch',[(x+s*.145,.48,.68),(x+s*.145,.53,1.07)],.0025,'M_Cyan')
        box(label+'_Headrest',(x,.64,1.23),(.29,.14,.19),'M_Seat',.045)
    # Compact open-top yoke; independently removable without changing the driving root.
    tube('Steering_Yoke',[(-.62,-.40,1.05),(-.66,-.40,.90),(-.56,-.40,.85),(-.33,-.40,.85),(-.23,-.40,.90),(-.27,-.40,1.05)],.025,'M_Trim')
    box('Steering_Hub',(-.445,-.40,.93),(.21,.065,.11),'M_Trim',.025)
    for s in [-1,1]:
        cylinder('JetNozzle',(s*.40,2.48,.50),.125,.22,'M_Alloy','Y')
        cylinder('JetNozzle_Core',(s*.40,2.601,.50),.092,.015,'M_Cyan','Y')
    empty('DriverEyeAnchor',(-.44,.12,1.24))
    empty('JetAnchor_L',(-.40,2.62,.50));empty('JetAnchor_R',(.40,2.62,.50))
    root['design']='Original Aster GT; editable surface panels; no third-party geometry'
    return root

def robot():
    global PARENT
    collection('02_Noma_Editable');root=empty('RobotRoot');PARENT=root
    groups={}
    def capture(bone,fn):
        before=set(COL.objects);fn();groups.setdefault(bone,[]).extend(set(COL.objects)-before)
    def torso():
        loft('Body_Inner',[(0,0,.89,.13,.10),(0,0,1.03,.12,.09),(0,0,1.18,.18,.11),(0,0,1.40,.23,.12),(0,0,1.47,.16,.08)],'M_Trim')
        loft('Chest_Armor',[(0,-.016,1.11,.115,.095),(0,-.016,1.17,.16,.115),(0,0,1.36,.22,.14),(0,0,1.43,.205,.12),(0,0,1.46,.155,.075)],'M_Pearl')
        tube('Chest_Seam',[(0,-.151,1.35),(0,-.143,1.23),(0,-.12,1.16)],.003,'M_Trim')
        box('Chest_Status',(0,-.142,1.36),(.10,.014,.018),'M_Cyan',.006)
        for z in [1.02,1.055,1.09]:
            loft('Abdomen_Flex',[(0,0,z,.122,.095),(0,0,z+.014,.128,.10)],'M_Alloy',20)
    capture('Spine',torso)
    capture('Pelvis',lambda:loft('Pelvis_Armor',[(0,0,.85,.10,.09),(0,0,.90,.16,.115),(0,0,.99,.15,.11),(0,0,1.03,.12,.09)],'M_Pearl'))
    def head():
        cylinder('Neck_Collar',(0,0,1.485),.066,.08,'M_Trim')
        loft('Head_Shell',[(0,.01,1.52,.055,.065),(0,.005,1.57,.087,.092),(0,0,1.70,.105,.105),(0,.01,1.78,.085,.083),(0,.01,1.81,.035,.04)],'M_Pearl',32)
        # Sculpted visor patch, conforming to head surface; not a spherical face.
        line_grid('Face_Visor',lambda u,v:((2*v-1)*(.068+.017*sin(pi*u)),-.091-.016*sin(pi*u)+.025*(2*v-1)**2,1.565+.185*u),12,12,'M_Trim')
        tube('Visor_Brow',[(-.065,-.095,1.704),(0,-.112,1.71),(.065,-.095,1.704)],.004,'M_Cyan')
        for s in [-1,1]:cylinder('Ear_Sensor',(s*.101,0,1.68),.028,.012,'M_Alloy','X',24)
    capture('Head',head)
    bones=[('Pelvis',(0,0,.88),(0,0,1.04),None),('Spine',(0,0,1.04),(0,0,1.45),'Pelvis'),('Head',(0,0,1.45),(0,0,1.78),'Spine')]
    for s,side in [(-1,'L'),(1,'R')]:
        hip=(s*.12,0,.94);knee=(s*.13,0,.52);ankle=(s*.13,0,.12)
        shoulder=(s*.245,0,1.40);elbow=(s*.31,0,1.13);wrist=(s*.325,-.005,.89)
        bones.extend([(f'Thigh_{side}',hip,knee,'Pelvis'),(f'Shin_{side}',knee,ankle,f'Thigh_{side}'),(f'Foot_{side}',ankle,(s*.13,-.15,.08),f'Shin_{side}'),(f'UpperArm_{side}',shoulder,elbow,'Spine'),(f'Forearm_{side}',elbow,wrist,f'UpperArm_{side}'),(f'Hand_{side}',wrist,(s*.33,0,.77),f'Forearm_{side}')])
        def thigh(s=s,side=side):
            cylinder('HipJoint_'+side,(s*.12,0,.91),.078,.13,'M_Trim','X')
            loft('Thigh_Armor_'+side,[(s*.13,0,.55,.053,.059),(s*.13,0,.64,.075,.082),(s*.12,0,.82,.087,.097),(s*.12,0,.90,.065,.075)],'M_Pearl')
            tube('Thigh_PanelLine_'+side,[(s*.165,-.084,.82),(s*.165,-.075,.66)],.003,'M_Alloy')
        capture(f'Thigh_{side}',thigh)
        def shin(s=s,side=side):
            cylinder('KneeJoint_'+side,(s*.13,0,.52),.053,.12,'M_Trim','X')
            box('Patella_'+side,(s*.13,-.055,.52),(.085,.032,.082),'M_Pearl',.018)
            loft('Shin_Armor_'+side,[(s*.13,0,.16,.042,.047),(s*.13,.018,.27,.048,.063),(s*.13,.015,.42,.066,.075),(s*.13,0,.48,.051,.055)],'M_Pearl')
            tube('Shin_Inlay_'+side,[(s*.13,-.054,.20),(s*.13,-.063,.42)],.006,'M_Alloy')
        capture(f'Shin_{side}',shin)
        def foot(s=s,side=side):
            box('Foot_Sole_'+side,(s*.13,-.056,.025),(.12,.26,.05),'M_Trim',.018)
            loft('Foot_Shell_'+side,[(s*.13,-.055,.055,.061,.124),(s*.13,-.04,.095,.056,.105),(s*.13,0,.14,.041,.048)],'M_Pearl')
        capture(f'Foot_{side}',foot)
        def upper(s=s,side=side):
            ellipsoid('ShoulderJoint_'+side,(s*.245,0,1.40),(.073,.078,.075),'M_Trim')
            loft('ShoulderCap_'+side,[(s*.257,0,1.34,.060,.079),(s*.25,0,1.42,.077,.092),(s*.235,0,1.46,.051,.059)],'M_Pearl')
            loft('UpperArm_Armor_'+side,[(s*.307,0,1.17,.042,.047),(s*.291,0,1.26,.057,.063),(s*.266,0,1.34,.062,.070)],'M_Pearl')
        capture(f'UpperArm_{side}',upper)
        def lower(s=s,side=side):
            cylinder('ElbowJoint_'+side,(s*.31,0,1.13),.044,.094,'M_Trim','X')
            loft('Forearm_Armor_'+side,[(s*.325,0,.91,.034,.036),(s*.322,0,.99,.050,.055),(s*.313,0,1.08,.051,.054)],'M_Pearl')
            box('Wrist_Status_'+side,(s*.325,-.038,.95),(.027,.013,.040),'M_Cyan',.008)
        capture(f'Forearm_{side}',lower)
        def hand(s=s,side=side):
            box('Palm_'+side,(s*.327,0,.84),(.07,.042,.092),'M_Pearl',.017)
            for i in range(4):
                x=s*(.300+i*.018);length=.075-abs(i-1)*.008
                for k in range(3):
                    box('Finger_'+side+str(i)+'_'+str(k),(x,-.004-k*.008,.795-(k+.5)*length/3),(.014,.022,length/3-.003),'M_Pearl',.005)
            tube('Thumb_'+side,[(s*.29,0,.86),(s*.274,-.022,.82),(s*.28,-.035,.795)],.012,'M_Pearl')
        capture(f'Hand_{side}',hand)
    # Actual deforming skeleton; each rigid armour part is weighted to one bone.
    armdata=bpy.data.armatures.new('Noma_Skeleton');arm=bpy.data.objects.new('Armature',armdata);COL.objects.link(arm);arm.parent=root
    bpy.context.view_layer.objects.active=arm;arm.select_set(True);bpy.ops.object.mode_set(mode='EDIT')
    for name,h,t,par in bones:
        b=armdata.edit_bones.new(name);b.head=h;b.tail=t
        if par:b.parent=armdata.edit_bones[par]
    bpy.ops.object.mode_set(mode='OBJECT')
    for bone,obs in groups.items():
        for o in obs:
            if o.type not in {'MESH','CURVE','FONT'}:continue
            if o.type!='MESH':
                bpy.ops.object.select_all(action='DESELECT');o.select_set(True);bpy.context.view_layer.objects.active=o;bpy.ops.object.convert(target='MESH')
            # Bake object matrix into geometry so bind pose is unambiguous.
            o.data.transform(o.matrix_world);o.matrix_world.identity();o.parent=arm
            vg=o.vertex_groups.new(name=bone);vg.add(list(range(len(o.data.vertices))),1,'REPLACE')
            mod=o.modifiers.new('Rigid armour skin','ARMATURE');mod.object=arm
    # In-place walk, 1 second cycle; stance foot y moves +0.36m/s relative to torso.
    for f in range(1,32):
        t=(f-1)/30
        arm.pose.bones['Pelvis'].location=(0,-.02,0)
        arm.pose.bones['Pelvis'].keyframe_insert('location',frame=f)
        for s,side in [(-1,'L'),(1,'R')]:
            phase=(t+(0 if s<0 else .5))%1
            if phase<.6: fy=-.18+.36*(phase/.6);fz=.12
            else:
                u=(phase-.6)/.4;fy=.18-.36*u;fz=.12+.075*sin(pi*u)
            # IK target in YZ; analytical two segment solution.
            dy=fy;dz=fz-.92;d=sqrt(dy*dy+dz*dz);l1=.42;l2=.40;d=min(d,.819)
            direction=math.atan2(dy,-dz);a=math.acos(max(-1,min(1,(l1*l1+d*d-l2*l2)/(2*l1*d))))
            upper=direction-a; bend=pi-math.acos(max(-1,min(1,(l1*l1+l2*l2-d*d)/(2*l1*l2))))
            for bn,ang in [(f'Thigh_{side}',upper),(f'Shin_{side}',bend),(f'Foot_{side}',-bend-upper),(f'UpperArm_{side}',-.32*sin(2*pi*phase)),(f'Forearm_{side}',-.12-.10*sin(2*pi*phase))]:
                pb=arm.pose.bones[bn];pb.rotation_mode='XYZ';pb.rotation_euler.x=ang;pb.keyframe_insert('rotation_euler',frame=f)
    arm.animation_data.action.name='Noma_Walk_InPlace_1s'
    bpy.context.scene.frame_start=1;bpy.context.scene.frame_end=31;bpy.context.scene.frame_set(1)
    root['walk_stride_metres_per_second']=.6
    return root,arm

def city():
    global PARENT
    collection('03_Meridian_Modules');root=empty('CityRoot');PARENT=root
    # Road travels toward -Y; gap is 37..43 m, crossing at 14 m.
    for y,length,name in [(-12.5,49,'Road_Main'),(-55.5,25,'Road_Landing')]:
        box(name,(0,y,-.18),(8,length,.36),'M_Road',.03)
        for x in [-5.15,5.15]:
            box(name+'_Sidewalk',(x,y,-.03),(2.3,length,.30),'M_Concrete',.03)
            box(name+'_Curb',(x/abs(x)*4.05,y,.04),(.15,length,.23),'M_White',.02)
    for y in range(10,-68,-3):
        if -44<y<-36 or -16<y<-12:continue
        box('Lane_Dash',(0,y,.006),(.10,1.5,.012),'M_White',0)
    for x in [-3.66,3.66]:
        for y,length in [(-12.5,49),(-55.5,25)]:box('Road_EdgeLine',(x,y,.008),(.07,length,.014),'M_White',0)
    for x in [i*.80-3.2 for i in range(9)]:box('Crosswalk_Stripe',(x,-14,.009),(.43,3.1,.018),'M_White',.01)
    box('StopLine',(1.9,-10.8,.008),(3.3,.18,.016),'M_White',0)
    for y in [-36.8,-43.2]:
        box('Gap_Threshold',(0,y,.018),(7.9,.30,.035),'M_Amber',.008)
        for x in [-3.7,3.7]:
            for k in range(4):box('Gap_Hazard_Bollard',(x,y+(k*.5 if y>-40 else -k*.5),.42),(.12,.12,.84),'M_Amber',.015)
        # Layered cut ends, visible rebar and structural beams down into void.
        for x in [-3,-1,1,3]:box('Bridge_Girder',(x,y,-.65),(.25,.48,.75),'M_Trim',.02)
    # Each block has a storefront, layered floor plates, glazing, fins and equipment.
    for side in [-1,1]:
        for idx,y in enumerate([5,-6,-19,-30,-49,-61]):
            x=side*(8.0+(idx%2)*.4);h=[10,17,12,21,14,18][idx];w=5.1;depth=8.7
            box('Building_%s_%02d'%(side,idx),(x,y,h/2),(w,depth,h),'M_Building',.10)
            face=x-side*w/2
            box('Shop_Skirting',(face-side*.06,y,.30),(.18,depth,.60),'M_Trim',.02)
            for z in [3.1]+[4.5+k*2.25 for k in range(int((h-4.5)/2.25)+1)]:
                box('Facade_FloorBand',(face-side*.12,y,z),(.30,depth+.15,.18),'M_Concrete',.025)
            # Mesh batches reduce renderer count for windows and mullions on Unity import.
            for j in range(4):
                yy=y-3.2+j*2.1
                box('Shop_Glass',(face-side*.06,yy,1.60),(.04,1.89,2.23),'M_Window',.008)
                box('Shop_Mullion',(face-side*.10,yy-.98,1.65),(.13,.055,2.4),'M_Alloy',.005)
                for k in range(max(1,int((h-4)/2.25))):
                    z=4.1+k*2.25
                    box('Upper_Window',(face-side*.055,yy,z+.6),(.04,1.70,1.5),'M_Window',.006)
                    if (j+k+idx)%4==0:box('Window_Lit',(face-side*.085,yy,z+.55),(.035,1.50,.06),'M_Cyan' if idx%2 else 'M_Amber',.002)
            for j in [-1,1]:
                box('Vertical_Fin',(face-side*.16,y+j*3.3,h*.62),(.42,.16,h*.69),'M_Alloy',.03)
            box('Store_Canopy',(face-side*.56,y,2.98),(1.3,depth-.4,.16),'M_Trim',.04)
            box('Canopy_Light',(face-side*1.19,y,2.93),(.035,depth-.6,.035),'M_Cyan' if idx%2 else 'M_Amber',.005)
            box('Sign_Backplate',(face-side*.23,y+1.8,4.25),(.15,2.3,.82),'M_Trim',.035)
            # Text faces roadway (local text plane faces -Y before Z rotation).
            rot=(pi/2,0,-side*pi/2)
            text_obj('Store_Sign',['MERIDIAN','TRANSIT','ATELIER','NOMA LAB','STATION','ORBIT'][idx],(face-side*.32,y+1.8,4.12),.28,'M_Cyan',rot)
            box('Rooftop_Plant',(x,y,h+.35),(2.4,2.5,.70),'M_Trim',.06)
            for k in range(5):box('HVAC_Louver',(x-1.05+k*.50,y-1.27,h+.35),(.07,.04,.46),'M_Alloy',.005)
            # Vertical lit strips, conduits and street-level furniture.
            tube('Service_Pipe',[(face-side*.24,y-3.9,.40),(face-side*.24,y-3.9,h-1),(face-side*.24,y-2.8,h-1)],.055,'M_Trim')
            cylinder('Streetlight_Pole',(side*4.65,y-3.8,2.6),.045,5.2,'M_Alloy')
            box('Streetlight_Arm',(side*4.1,y-3.8,5.13),(1.15,.09,.09),'M_Trim')
            box('Streetlight_Emitter',(side*3.62,y-3.8,5.09),(.40,.17,.025),'M_Cyan',.01)
            if idx%2==0:
                box('Planter',(side*5.1,y,.30),(.65,1.6,.60),'M_Trim',.08)
                for k in range(7):
                    a=k*2*pi/7
                    tube('Plant_Stem',[(side*5.1,y,.55),(side*5.1+.20*cos(a),y+.5*sin(a),1.25+.15*cos(a))],.016,'M_Concrete')
                    ellipsoid('Plant_Foliage',(side*5.1+.16*cos(a),y+.45*sin(a),1.10),(.14,.23,.32),'M_Building')
            for yy in [y-2.7,y+2.7]:
                cylinder('Bollard',(side*4.36,yy,.4),.065,.8,'M_Trim')
                cylinder('Bollard_Light',(side*4.36,yy,.70),.068,.04,'M_Cyan')
    # Landmark portal and transit signage.
    for x in [-4.8,4.8]:box('Portal_Pillar',(x,-25,3.3),(.32,.48,6.6),'M_Trim',.03)
    box('Portal_Beam',(0,-25,6.5),(9.9,.48,.5),'M_Trim',.04)
    text_obj('Portal_Sign','MERIDIAN  /  04',(0,-24.74,6.39),.27,'M_Cyan',(pi/2,0,pi))
    return root

def jets():
    global PARENT
    collection('04_JetFX_Editable');root=empty('JetFXRoot');PARENT=root
    for x in [-.40,.40]:
        # Exhaust extends rearward (+Y), two nested emissive open cones.
        for r,length,mat in [(.085,.80,'M_Cyan'),(.045,1.05,'M_White')]:
            vs=[];n=24
            for y,rad in [(0,r),(.20,r*.8),(length,.004)]:
                for j in range(n):vs.append((x+rad*cos(j*2*pi/n),y,.50+rad*sin(j*2*pi/n)))
            fs=[(k*n+j,k*n+(j+1)%n,(k+1)*n+(j+1)%n,(k+1)*n+j) for k in range(2) for j in range(n)]
            mesh('Jet_Plume',vs,fs,mat,True)
        for i in range(3):
            tube('Jet_ShockRing',[(x+.065*cos(j*2*pi/32),.15+i*.20,.50+.065*sin(j*2*pi/32)) for j in range(32)],.006,'M_Cyan',True)
    return root

def evaluated_mesh(o):
    return bpy.data.meshes.new_from_object(o.evaluated_get(bpy.context.evaluated_depsgraph_get()))

def export_dataset(name,root):
    # Unity editor assembles these evaluated meshes into editable named objects.
    # Coordinates converted to Unity (x,z,-y); topology winding preserved by det(+1).
    parts=[]
    for o in list(COL.objects):
        if o.type not in {'MESH','CURVE','FONT'}:continue
        me=evaluated_mesh(o);me.calc_loop_triangles();matrix=o.matrix_world
        verts=[];normals=[]
        nm=matrix.to_3x3().inverted().transposed()
        # Per-loop vertices retain hard edges and sharp normals.
        inds=[]
        for tri in me.loop_triangles:
            for li in tri.loops:
                co=matrix@me.vertices[me.loops[li].vertex_index].co
                no=(nm@me.corner_normals[li].vector).normalized()
                verts.extend([round(co.x,6),round(co.z,6),round(-co.y,6)])
                normals.extend([round(no.x,6),round(no.z,6),round(-no.y,6)])
                inds.append(len(inds))
        mat=me.materials[0].name if me.materials else 'M_Trim'
        bone=next((g.name for g in o.vertex_groups), '') if o.type=='MESH' else ''
        parts.append(dict(name=o.name,material=mat,bone=bone,vertices=verts,normals=normals,triangles=inds))
        bpy.data.meshes.remove(me)
    mats=[]
    for n,m in M.items():
        p=m.node_tree.nodes.get('Principled BSDF')
        mats.append(dict(name=n,color=list(m.diffuse_color),metallic=p.inputs['Metallic'].default_value,roughness=p.inputs['Roughness'].default_value,emission=p.inputs['Emission Strength'].default_value))
    anchors=[]
    for o in COL.objects:
        if o.type=='EMPTY' and o!=root:
            c=o.matrix_world.translation;anchors.append(dict(name=o.name,position=[c.x,c.z,-c.y]))
    data=dict(name=name,parts=parts,materials=mats,anchors=anchors)
    (DATA/(name+'.json')).write_text(json.dumps(data,separators=(',',':')),encoding='utf8')
    REPORT.append(dict(asset=name,objects=len(parts),triangles=sum(len(p['triangles'])//3 for p in parts)))

def export_asset(name,root,arm=None):
    bpy.context.view_layer.update()
    if arm:
        arm.data.pose_position='REST';bpy.context.view_layer.update()
    export_dataset(name,root)
    if arm:arm.data.pose_position='POSE';bpy.context.view_layer.update()
    bpy.ops.object.select_all(action='DESELECT')
    for o in COL.objects:o.select_set(True)
    bpy.context.view_layer.objects.active=root
    # FBX exporter ignores curves: export temporary evaluated mesh copies for these.
    temp=[]
    for o in list(COL.objects):
        if o.type in {'CURVE','FONT'}:
            me=evaluated_mesh(o);new=bpy.data.objects.new(o.name+'_Export',me);COL.objects.link(new)
            new.matrix_world=o.matrix_world;new.parent=o.parent;new.select_set(True);o.select_set(False);temp.append(new)
    bpy.ops.export_scene.fbx(filepath=str(ART/'FBX'/(name+'.fbx')),use_selection=True,object_types={'MESH','EMPTY','ARMATURE'},axis_forward='-Z',axis_up='Y',apply_unit_scale=True,add_leaf_bones=False,bake_anim=arm is not None,bake_anim_use_all_actions=False,bake_anim_use_nla_strips=False,bake_anim_simplify_factor=0)
    for o in temp:bpy.data.objects.remove(o,do_unlink=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(ART/'Blender'/(name+'.blend')))

def lighting(target,scale):
    global PARENT
    collection('90_Preview_Only');PARENT=None
    world=bpy.data.worlds.new('StudioWorld');bpy.context.scene.world=world;world.use_nodes=True
    world.node_tree.nodes['Background'].inputs[0].default_value=(.13,.18,.24,1)
    world.node_tree.nodes['Background'].inputs[1].default_value=.35
    for name,pos,power,color,size in [('Key',(-3,-4,6),1200,(.78,.88,1),5),('Rim',(3,2,4),1600,(.23,.65,1),3),('Warm',(-3,3,3),900,(1,.62,.33),3)]:
        ld=bpy.data.lights.new(name,'AREA');lo=bpy.data.objects.new(name,ld);COL.objects.link(lo)
        lo.location=Vector(target)+Vector(pos)*scale;ld.energy=power*scale*scale;ld.color=color;ld.shape='DISK';ld.size=size*scale
        lo.rotation_euler=(Vector(target)-lo.location).to_track_quat('-Z','Y').to_euler()
    scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=24;scene.cycles.use_denoising=True
    scene.render.resolution_x=1400;scene.render.resolution_y=900;scene.render.resolution_percentage=100
    scene.view_settings.view_transform='AgX'
    return COL

def render(name,pos,target,lens=48,ortho=None):
    ca=bpy.data.cameras.new(name);ob=bpy.data.objects.new(name,ca);COL.objects.link(ob);ob.location=pos
    ob.rotation_euler=(Vector(target)-ob.location).to_track_quat('-Z','Y').to_euler();ca.lens=lens;ca.clip_start=.03;ca.clip_end=500
    if ortho:ca.type='ORTHO';ca.ortho_scale=ortho
    bpy.context.scene.camera=ob;bpy.context.scene.render.filepath=str(ART/'Previews'/(name+'.png'))
    bpy.ops.render.render(write_still=True)

def main():
    global PARENT
    reset();r=car();export_asset('AsterGT',r)
    lighting((0,0,.6),1);box('Studio_Floor',(0,0,-.08),(200,200,.12),'M_Road',0)
    render('01_AsterGT_Front',(-6,-7,3.3),(0,0,.7),52)
    render('02_AsterGT_Rear',(6,7,3.0),(0,0,.7),52)
    render('03_AsterGT_Side',(-8,0,1.5),(0,0,.8),ortho=5.8)
    # Driver view: side glass remains, dashboard and road visible through transparent screen.
    render('04_AsterGT_Cockpit',(-.44,.20,1.24),(-.25,-2.5,1.12),20)
    reset();r,arm=robot();export_asset('NomaRobot',r,arm)
    lighting((0,0,.9),.55);box('Studio_Floor',(0,0,-.04),(200,200,.06),'M_Road',0)
    arm.data.pose_position='REST';bpy.context.view_layer.update()
    render('05_NomaRobot',(-3.0,-4.7,2.1),(0,0,.92),62)
    arm.data.pose_position='POSE'
    for f in [1,8,16,23]:
        bpy.context.scene.frame_set(f);render('06_NomaWalk_%02d'%f,(-3.0,-4.7,1.65),(0,0,.91),62)
    reset();r=city();export_asset('MeridianCity',r)
    lighting((0,-15,0),5)
    ld=bpy.data.lights.new('Sun','SUN');lo=bpy.data.objects.new('Sun',ld);COL.objects.link(lo);lo.rotation_euler=(.4,-.5,-.4);ld.energy=2
    render('07_Meridian_Street',(1.8,7,2.1),(0,-22,4),24)
    render('08_Meridian_Gap',(-3,-29,8),(0,-40,-.1),35)
    reset();r=jets();export_asset('JetFX',r)
    (ART/'asset_metrics.json').write_text(json.dumps(REPORT,indent=2),encoding='utf8')
    print('ART_COMPLETE',json.dumps(REPORT))

if __name__=='__main__':main()
