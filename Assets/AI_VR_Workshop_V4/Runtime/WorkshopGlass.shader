Shader "AI VR Workshop/Glass and Curtain"
{
    Properties { _Color("Color", Color)=(.1,.2,.3,.12) }
    SubShader {
        Tags { "RenderType"="Transparent" "Queue"="Transparent+100" }
        Pass {
            Tags { "LightMode"="SRPDefaultUnlit" }
            Blend SrcAlpha OneMinusSrcAlpha
            ZWrite Off
            Cull Off
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #pragma multi_compile_instancing
            #include "UnityCG.cginc"
            struct appdata {float4 vertex:POSITION; UNITY_VERTEX_INPUT_INSTANCE_ID};
            struct v2f {float4 vertex:SV_POSITION; UNITY_VERTEX_OUTPUT_STEREO};
            fixed4 _Color;
            v2f vert(appdata v) {v2f o;UNITY_SETUP_INSTANCE_ID(v);UNITY_INITIALIZE_VERTEX_OUTPUT_STEREO(o);o.vertex=UnityObjectToClipPos(v.vertex);return o;}
            fixed4 frag(v2f i):SV_Target { UNITY_SETUP_STEREO_EYE_INDEX_POST_VERTEX(i);return _Color; }
            ENDCG
        }
    }
}
