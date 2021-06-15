from pyproj import Proj, transform

def to_GPS(file, x, y):
    inProj = Proj(f"epsg:{file.crs.data['init']}")
    outProj = Proj(f'epsg:4326')
    x_geo,y_geo = transform(inProj,outProj,x,y)
    return x_geo, y_geo

def to_pxl(coord):
    pass