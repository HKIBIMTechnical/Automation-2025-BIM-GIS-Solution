# Automation-2025-BIM-GIS-Solution

![image](https://github.com/HKIBIMTechnical/Automation-2025-BIM-GIS-Solution/blob/main/image.png)

This project provides automation scripts for converting BIM (Building Information Modeling) and GIS (Geographic Information System) data into formats suitable for visualization and analysis, such as GeoJSON, KML, and Mapbox-compatible data.

## Features

- **Clash_To_Geojson_and_Mapbox.py**: Converts clash detection results from BIM software into GeoJSON and Mapbox formats for spatial analysis and visualization.
- **Pipe_Structure_To_Geojson_and_Mapbox.py**: Converts pipe and structure data from BIM models into GeoJSON and Mapbox formats.
- **geojson_to_kml.py**: Converts GeoJSON files into KML format for use in GIS applications like Google Earth.

## Requirements

- Python 3.7+
- Required Python packages (install via pip):
  - `json`
  - `os`
  - `shapely` (if used for geometry operations)
  - `simplekml` (for KML export)
  - `geojson`

Install dependencies with:

```bash
pip install shapely simplekml geojson
```

## Usage

Run the scripts from the command line. For example:

```bash
python Clash_To_Geojson_and_Mapbox.py
python Pipe_Structure_To_Geojson_and_Mapbox.py
python geojson_to_kml.py
```

Each script may require specific input files (e.g., BIM export files, GeoJSON files). Please refer to the script comments for details on input and output file paths.

## Project Structure

- `Clash_To_Geojson_and_Mapbox.py`
- `Pipe_Structure_To_Geojson_and_Mapbox.py`
- `geojson_to_kml.py`
- `README.md`

## Important Note

Due to the presence of sensitive words, some content has been removed from the scripts. As a result, the programs may encounter errors or fail to run as expected. However, this project still serves as a valuable case for learning and reference purposes.
