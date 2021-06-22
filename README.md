# 3D House Project

- Repository: `3D_houses`
- Type of Challenge: `Learning & Consolidation`
- Duration: `1 weeks`
- Deadline: `18/06/21 12:30 AM`
- Deployment strategy :
  - Jupyter Notebook
- Team challenge : `Team (3-4)`

## Collaborators and Roles

| Collaborators                                         | Roles Description                                                                                                                           |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="images/atefeh.jpeg" alt="drawing" style="width:100px;"/> <br/> Atefeh Hossein| - [X] Understand API and how to find L-72 coordinates from an address <br/> - [X] Understand API and how to find L-72 coordinates from an address <br/> - [X] Understand API and how to find L-72 coordinates from an address <br/>        |
| <img src="images/ceren.jpeg" alt="drawing" style="width:100px;"/> <br/> Ceren Mörey | - [X] Understand API and how to find L-72 coordinates from an address <br/> - [X] Understand API and how to find L-72 coordinates from an address <br/> - [X] Understand API and how to find L-72 coordinates from an address <br/>                                             |
| <img src="images/corentin.png" alt="drawing" style="width:100px;"/> </br> Corentin Chanet (Project Manager)                                    | - [X] Optimization for handling large geo & raster files <br/> - [X] Coordination and support to team members <br/> - [X] Clipping rasters with polygons <br/> |
| <img src="images/hugo.jpeg" alt="drawing" style="width:100px;"/> <br/> Hugo Pradier                                     | - [X] Understand API and how to find L-72 coordinates from an address <br/> - [X] Understand API and how to find L-72 coordinates from an address <br/> - [X] Understand API and how to find L-72 coordinates from an address <br/>                                                       |
## Mission objectives

Consolidate the knowledge in Python, specifically in :

- [X] NumPy
- [X] GeoPandas, shapely (Geo Data)
- [X] rasterio, rioxarray (Raster Data)
- [X] mayavi (3D plotting libraries)

## Learning Objectives

- [X] to be able to search and implement new libraries
- [X] to be able to read and use the [shapefile](https://en.wikipedia.org/wiki/Shapefile) format
- [X] to be able to read and use geoTIFFs
- [X] to be able to render a 3D plot
- [X] to be able to present a final product

## The Mission

> We are _LIDAR PLANES_, active in the Geospatial industry. We would like to use our data to launch a new branch in the insurance business. So, we need you to build a solution with our data to model a house in 3D with only a home address.

### Must-have features

- 3D lookup of houses.

### Nice-to-have features

- Optimize your solution to have the result as fast as possible.
- Features like the living area of the house in m², how many floors, if there is a pool, the vegetation in the neighborhood, etc...
- Better visualization.

### Miscellaneous information

#### What is LIDAR ?

LIDAR is a method to measure distance using light. The device will illuminate a target with a laser light and a sensor will measure the reflection. Differences in wavelength and return times will be used to get 3D representations of an area.

Here is a LIDAR segmentation :

<img src="images/lidar.png" alt="drawing"/> <br/>

With those points clouds we can easily identify houses, vegetation, roads, etc...

The results we're interested in are DSM (Digital Surface Map) and DTM (Digital Terrain Map).

Which are already computed and available here :

- [DSM](http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dsm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DSM,%20raster,%201m)
- [DTM](http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dtm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DTM,%20raster,%201m)


## Installation

Install all libraries
```
$ sudo pip install numpy pandas geopandas matplotlib geopy folium natsort fiona shapely rasterio earthpy open3d PyQt5 mayavi jupyterlab rioxarray 
```
for jupyterlab, if you are using a Unix derivative (FreeBSD, GNU / Linux, OS X), you can achieve this by using:

```
$ export PATH="$HOME/.local/bin:$PATH"
```
If you are interested in the mayavi jupyter notebook support as well, do the following (after ensuring that you have jupyter installed of course):

```
$ jupyter nbextension install --py mayavi --user
$ jupyter nbextension enable --py mayavi --user
```

## Usage
Navigate to the repo root on your terminal then write this command line:
```
$ jupyter notebook
```

## Visuals

## Timeline
<img src="images/workflow2.png" alt="drawing"/> <br/>

Project made at Becode Brussels
