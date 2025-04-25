import json
import simplekml

def geojson_to_kml(geojsonPath,saveAsPath):
    # Parse the GeoJSON data
    with open(geojsonPath,'r') as f:
        geojson1 =json.load(f)
        # geojson = json.loads(geojson_data)

        # Create a KML object
        kml = simplekml.Kml()

        # Convert each feature in the GeoJSON to a KML Placemark
        # Convert each feature in the GeoJSON to a KML Placemark
        for feature in geojson1['features']:
            geom_type = feature['geometry']['type']
            coordinates = feature['geometry']['coordinates']

            # Add properties as KML ExtendedData
            extended_data = simplekml.ExtendedData()
            for key, value in feature['properties'].items():
                extended_data.newdata(name=key, value=str(value))

            if geom_type == 'Point':
                pnt = kml.newpoint(coords=[(coordinates[0], coordinates[1])])
                pnt.extendeddata = extended_data

            elif geom_type == 'LineString':
                ls = kml.newlinestring(coords=[(coord[0], coord[1]) for coord in coordinates])
                ls.extendeddata = extended_data

            elif geom_type == 'Polygon':
                coords=[(coord[0], coord[1]) for coord in coordinates[0]]
                coords.append(coords[0])
                pol = kml.newpolygon(outerboundaryis=coords)
                # pol = kml.newpolygon(outerboundaryis=[(coord[0], coord[1]) for coord in coordinates[0]])
                pol.extendeddata = extended_data

            else:
                print(f"Geometry type {geom_type} not supported.")
        
        kml.save(saveAsPath)