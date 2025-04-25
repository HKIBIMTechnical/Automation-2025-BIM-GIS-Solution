
import pandas as pd
import mapbox
import geojson

def export_to_geojson_and_mapbox(excelPath):
    token_Map_Test="......"
    
    df=pd.read_excel(excelPath)    
    df.fillna("no_value", inplace=True)

    features=[]
    for data in df.values:
        FileName=adfun.my_folderAndfile.get_file_name_by_filepath_without_extension(excelPath)
        Status="Existing" if str(data[50])=="EX" else "Design"
        Name=data[1]
        Type=data[8]
        AsBuiltStatus=str.capitalize(data[87])
        IsOmission="omission" if "omission" in str(Name).lower() else "not_omission"
        # print(AsBuiltStatus)
        if "omission" not in str(Name).lower(): 
            # print(Name)
            if Type=="Pipe":
                x1,y1=adfun.hk1980_Transformer.x_to_lon(float(data[58])),adfun.hk1980_Transformer.y_to_lat(float(data[59]))
                x2,y2=adfun.hk1980_Transformer.x_to_lon(float(data[60])),adfun.hk1980_Transformer.y_to_lat(float(data[61]))
                features.append(
                    geojson.Feature(
                        geometry=geojson.LineString([[x1,y1],[x2,y2]]),
                        properties={
                            "Name":Name,
                            "FileName":FileName,
                            "Status":Status,
                            "Type":Type,
                            "AsBuiltStatus":AsBuiltStatus,
                            "IsOmission":IsOmission
                        }
                    )
                )
            elif Type=="Structure":
                x1,y1=adfun.hk1980_Transformer.x_to_lon(float(data[52])),adfun.hk1980_Transformer.y_to_lat(float(data[53]))
                features.append(
                    geojson.Feature(
                        geometry=geojson.Point([x1,y1]),
                        properties={
                            "Name":Name,
                            "FileName":FileName,
                            "Status":Status,
                            "Type":Type,
                            "AsBuiltStatus":AsBuiltStatus,
                            "IsOmission":IsOmission
                        }
                    )
                )  
            elif Type=="PressurePipe":
                x1,y1=adfun.hk1980_Transformer.x_to_lon(float(data[58])),adfun.hk1980_Transformer.y_to_lat(float(data[59]))
                x2,y2=adfun.hk1980_Transformer.x_to_lon(float(data[60])),adfun.hk1980_Transformer.y_to_lat(float(data[61]))
                features.append(
                    geojson.Feature(
                        geometry=geojson.LineString([[x1,y1],[x2,y2]]),
                        properties={
                            "Name":Name,
                            "FileName":FileName,
                            "Status":Status,
                            "Type":Type,
                            "AsBuiltStatus":AsBuiltStatus,
                            "IsOmission":IsOmission
                        }
                    )
                )  
            elif Type=="CogoPoint":
                float(str(data[88]).split(",")[0])
                x1,y1=adfun.hk1980_Transformer.x_to_lon(float(str(data[88]).split(",")[0])),adfun.hk1980_Transformer.y_to_lat(float(str(data[88]).split(",")[1]))
                features.append(
                    geojson.Feature(
                        geometry=geojson.Point([x1,y1]),
                        properties={
                            "Name":Name,
                            "FileName":FileName,
                            "Status":Status,
                            "Type":Type,
                            "AsBuiltStatus":AsBuiltStatus,
                            "IsOmission":IsOmission
                        }
                    )
                )                   
    feature_collection=geojson.FeatureCollection(features=features)
    
    folder=r"save folder"
    FileName=adfun.my_folderAndfile.get_file_name_by_filepath_without_extension(excelPath)
    
    with open(f"{folder}\\{FileName}.geojson",'w') as f:
        geojson.dump(feature_collection,f,indent=2)
        
    client=mapbox.Uploader(access_token=token_Map_Test)

    
    with open(f"{folder}\\{FileName}.geojson",'rb') as f:
        response=client.upload(f"{folder}\\{FileName}.geojson",str(FileName).split('-')[4] + "-" + str(FileName).split('-')[5])
        print("upload---",response.json())

def export_all_to_geojson_and_mapbox(excelPathList):
    token_Map_Test="......"
    features=[]
    for excelPath in excelPathList:
        df=pd.read_excel(excelPath)    
        df.fillna("no_value", inplace=True)
        
        for data in df.values:
            FileName=adfun.my_folderAndfile.get_file_name_by_filepath_without_extension(excelPath)
            Status="Existing" if str(data[50])=="EX" else "Design"
            Name=data[1]
            Type=data[8]
            AsBuiltStatus=str.capitalize(data[87])
            IsOmission="omission" if "omission" in str(Name).lower() else "not_omission"
            # print(AsBuiltStatus)
            if "omission" not in str(Name).lower(): 
                # print(Name)
                if Type=="Pipe":
                    x1,y1=adfun.hk1980_Transformer.x_to_lon(float(data[58])),adfun.hk1980_Transformer.y_to_lat(float(data[59]))
                    x2,y2=adfun.hk1980_Transformer.x_to_lon(float(data[60])),adfun.hk1980_Transformer.y_to_lat(float(data[61]))
                    features.append(
                        geojson.Feature(
                            geometry=geojson.LineString([[x1,y1],[x2,y2]]),
                            properties={
                                "Name":Name,
                                "FileName":FileName,
                                "Status":Status,
                                "Type":Type,
                                "AsBuiltStatus":AsBuiltStatus,
                                "IsOmission":IsOmission
                            }
                        )
                    )
                elif Type=="Structure":
                    x1,y1=adfun.hk1980_Transformer.x_to_lon(float(data[52])),adfun.hk1980_Transformer.y_to_lat(float(data[53]))
                    features.append(
                        geojson.Feature(
                            geometry=geojson.Point([x1,y1]),
                            properties={
                                "Name":Name,
                                "FileName":FileName,
                                "Status":Status,
                                "Type":Type,
                                "AsBuiltStatus":AsBuiltStatus,
                                "IsOmission":IsOmission
                            }
                        )
                    )  
                elif Type=="PressurePipe":
                    x1,y1=adfun.hk1980_Transformer.x_to_lon(float(data[58])),adfun.hk1980_Transformer.y_to_lat(float(data[59]))
                    x2,y2=adfun.hk1980_Transformer.x_to_lon(float(data[60])),adfun.hk1980_Transformer.y_to_lat(float(data[61]))
                    features.append(
                        geojson.Feature(
                            geometry=geojson.LineString([[x1,y1],[x2,y2]]),
                            properties={
                                "Name":Name,
                                "FileName":FileName,
                                "Status":Status,
                                "Type":Type,
                                "AsBuiltStatus":AsBuiltStatus,
                                "IsOmission":IsOmission
                            }
                        )
                    )  
                elif Type=="CogoPoint":
                    float(str(data[88]).split(",")[0])
                    x1,y1=adfun.hk1980_Transformer.x_to_lon(float(str(data[88]).split(",")[0])),adfun.hk1980_Transformer.y_to_lat(float(str(data[88]).split(",")[1]))
                    features.append(
                        geojson.Feature(
                            geometry=geojson.Point([x1,y1]),
                            properties={
                                "Name":Name,
                                "FileName":FileName,
                                "Status":Status,
                                "Type":Type,
                                "AsBuiltStatus":AsBuiltStatus,
                                "IsOmission":IsOmission
                            }
                        )
                    )                   
    feature_collection=geojson.FeatureCollection(features=features)        
    folder=r"save folder"
        
    with open(f"{folder}\\Pipe_and_Structure.geojson",'w') as f:
        geojson.dump(feature_collection,f,indent=2)
        
    client=mapbox.Uploader(access_token=token_Map_Test)    
    with open(f"{folder}\\Pipe_and_Structure.geojson",'rb') as f:
        response=client.upload(f"{folder}\\Pipe_and_Structure.geojson","Pipe_and_Structure")
        print("upload---",response.json())       

