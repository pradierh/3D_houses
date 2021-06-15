import rasterio

def chmer(inpath, outpath):
    DSM = rasterio.open(inpath, driver="GTiff")
    DTM = rasterio.open(inpath, driver="GTiff")

    # CHM is a numpy.array
    CHM = DSM.read() - DTM.read()

    kwargs = DSM.meta  # Copy metadata of rasterio.io.DatasetReader
    with rasterio.open(outpath, 'w', **kwargs) as file:
        file.write(CHM.astype(rasterio.float32))