import pyTigerGraph as tg

conn = tg.TigerGraphConnection(host="http://127.0.0.1", graphname="social", username="tigergraph", password="tigergraph",
                 restppPort="9000", gsPort="14240", gsqlVersion="", version="", apiToken="", useCert=True,
                 certPath=None,
                 debug=False, sslPort="443",gcp=False)

gsUrl=conn.gsUrl
print(conn.gsUrl)
getSchema=conn.getSchema()
print('schema is ',getSchema)
print('api token',conn.apiToken)
print('username',conn.username)
print('authHeader',conn.authHeader)

print(getSchema.keys())
VertexTypes=getSchema['VertexTypes']
print(VertexTypes[0])
#print(conn.allPaths())   #'sourceVertices', 'targetVertices', and 'maxLength'
print(conn.beta)
print('base64key',conn.base64_credential)
print(conn.echo())
#print(conn.certLocation)
print(conn.password)

