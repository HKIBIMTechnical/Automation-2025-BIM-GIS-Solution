
import mapbox
import geojson

token_mapbox="......"
folder="clash folder"

doc=navisComApi.getNavisDoc()
state=navisComApi.getState(doc)
currentOpenedFileName=navisComApi.getOpenedFileName(state)

clashtests=navisComApi.getClashTests(state)


features=[]
interfaceClash="...."
ClashType=""

for ct in clashtests:
    ct_name=navisComApi.getClashTestName(ct)
    crs=navisComApi.getClashResults_underClashTest(ct)
    ClashType="Interface_Clash" if interfaceClash in ct_name else "3310T_Clash"
       
    for cr in ct.results():
        status=navisComApi.get_ClashResult_Status(cr)
        if status!="Resolved":
            crName=navisComApi.get_ClashResultName(cr)
            x,y,z=navisComApi.get_ClashResult_ClashCenter(cr)
            x=adfun.hk1980_Transformer.x_to_lon(x)
            y=adfun.hk1980_Transformer.y_to_lat(y)
            print(x,"_____",y,"_________",navisComApi.get_ClashResult_Status(cr))
            features.append(
                geojson.Feature(
                    geometry=geojson.Point([x,y]),
                    properties={
                        "Name":crName,
                        "Status":status,
                        "Clash_Type":ClashType
                        }
                    )
                )

feature_collection=geojson.FeatureCollection(features=features)

with open(f"{folder}\\Clash_Points.geojson",'w') as f:
    geojson.dump(feature_collection,f,indent=2)
    
client=mapbox.Uploader(access_token=token_mapbox)

with open(f"{folder}\\Clash_Points.geojson",'rb') as f:
    response=client.upload(f"{folder}\\Clash_Points.geojson","Clash_Points")
    print(response.json())

print("finish")
