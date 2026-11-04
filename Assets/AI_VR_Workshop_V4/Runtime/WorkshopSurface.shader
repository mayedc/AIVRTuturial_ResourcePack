Shader "AI VR Workshop/Teaching Surface"
{
    Properties { _Color("Color", Color)=(1,1,1,1) _Emission("Emission", Range(0,3))=0 _Metallic("Metallic", Range(0,1))=0 }
    SubShader
    {
        Tags { "RenderType"="Opaque" "Queue"="Geometry" }
        Pass
        {
            Tags { "LightMode"="SRPDefaultUnlit" }
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #pragma multi_compile_instancing
            #include "UnityCG.cginc"
            struct appdata { float4 vertex:POSITION; float3 normal:NORMAL; UNITY_VERTEX_INPUT_INSTANCE_ID };
            struct v2f { float4 vertex:SV_POSITION; float3 normal:TEXCOORD0; float3 world:TEXCOORD1; UNITY_VERTEX_OUTPUT_STEREO };
            fixed4 _Color; float _Emission, _Metallic;
            v2f vert(appdata v) { v2f o; UNITY_SETUP_INSTANCE_ID(v); UNITY_INITIALIZE_VERTEX_OUTPUT_STEREO(o); o.vertex=UnityObjectToClipPos(v.vertex);o.normal=UnityObjectToWorldNormal(v.normal);o.world=mul(unity_ObjectToWorld,v.vertex).xyz;return o; }
            fixed4 frag(v2f i):SV_Target {
                UNITY_SETUP_STEREO_EYE_INDEX_POST_VERTEX(i);
                float3 n=normalize(i.normal), l=normalize(float3(-.4,.8,-.3));
                float3 eye=normalize(_WorldSpaceCameraPos-i.world);
                float diffuse=.3+.7*max(0,dot(n,l));
                float spec=pow(max(0,dot(n,normalize(l+eye))),48)*_Metallic;
                return fixed4(_Color.rgb*(diffuse+_Emission)+spec*.6,1);
            }
            ENDCG
        }
    }
}
