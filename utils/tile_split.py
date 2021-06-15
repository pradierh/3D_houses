import os
from osgeo import gdal

# The original code Maxim posted + 1 line
cpt=0
for x in range(1,44):
    if x < 10:
        tile = f"0{x}"
    else :
        tile = str(x)
    print(f"Getting map n°{tile}, total tiles : {cpt}")

    # relative paths, you need to have the files in your folder
    # Thanks to Hugo's .gitignore, the .tif won't get pushed so no worry
    in_path = "./DHMVIIDSMRAS1m_k"+tile+"/GeoTIFF/"
    input_filename = "DHMVIIDSMRAS1m_k"+tile+".tif"

    out_path = "/Users/Corty/Downloads/DSM_split/"
    output_filename = "tile_"

    tile_size_x = 1000
    tile_size_y = 500

    ds = gdal.Open(in_path + input_filename)
    band = ds.GetRasterBand(1)

    # Added line to get the array (whose values are the elevations)
    array = band.ReadAsArray()

    xsize = band.XSize
    ysize = band.YSize
    for i in range(0, xsize, tile_size_x):
        for j in range(0, ysize, tile_size_y):
            cpt+=1
            com_string = "gdal_translate -of GTIFF -srcwin "+str(i)+", "+str(j)+", "+str(tile_size_x)+", "+str(tile_size_y)+" "+str(in_path)+str(input_filename)+" "+str(out_path)+str(output_filename)+str(cpt)+".tif"
            os.system(com_string)


