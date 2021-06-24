# 3D House Project
This repository provides a Jupyter notebook with the goal to let an end user generate a 3D plot of the house or building on a specified address within the entire Belgium. The main dataset being used to do this is publicly available, and originates from a governmental project called DHMV II.

## Project Guidelines

- Repository: `3D_houses`
- Type of Challenge: `Learning & Consolidation`
- Duration: `1 weeks`
- Deadline: `18/06/21 12:30 AM`
- Deployment strategy :
  - Jupyter Notebook
- Team challenge : `Team (3-4)`

## Collaborators and roles

| Collaborators                                         | Role Description                                                                                                                           |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="images/atefeh.jpeg" alt="drawing" width="150" height="150"/> <br/> Atefeh Hossein| - API testing & shapefile processing <br/> - 3D Libraries (Mayavi) <br/> - Research & Documentation <br/>        |
| <img src="images/ceren.jpeg" alt="drawing" width="150" height="150"/> <br/> Ceren Mörey | -  Raster files processing (rasterio) <br/> - API requests to find L-72 coordinates <br/> - Communication strategy <br/>                                             |
| <img src="images/corentin2.png" alt="drawing"  width="150" height="150"/> </br> Corentin Chanet (Project Manager)                                    | - Code optimization & GUI <br/> - Coordination and support to team members <br/> - 3D Libraries (plotly) <br/>
| <img src="images/hugo.jpeg" alt="drawing" width="150" height="150"/> <br/> Hugo Pradier                                     | - 3D rendering <br/> - github / README.md <br/> - Documentation <br/>  - Jupyter Notebook setup <br/>                                                       |
## Mission objectives

Consolidate the knowledge in Python, specifically in :

- [X] NumPy
- [X] GeoPandas, shapely (Geo Data)
- [X] rasterio, rioxarray (Raster Data)
- [X] mayavi, plotly (3D plotting libraries)

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

The results we're interested in are DSM (Digital Surface Map) and DTM (Digital Terrain Map).

Which are already computed and available here :

- [DSM](http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dsm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DSM,%20raster,%201m)
- [DTM](http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dtm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DTM,%20raster,%201m)


## Installation

Install all libraries
```
$ sudo pip install numpy pandas geopandas natsort fiona shapely rasterio open3d PyQt5 mayavi jupyterlab rioxarray plotly 
```
To install jupyterlab, if you are using a Unix derivative (FreeBSD, GNU / Linux, OS X), please use this command line:

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

Visuals exemples of the Sint-Jacob church located in Antwerpen:<br/>
(Lange Nieuwstraat 73, 2000 Antwerpen, Belgique)<br/><br/>

<p align="center">
<img src="images/screenshot2.png" alt="drawing" width="60%" height="60%"/><br/><br/>
<img src="images/screenshot3.png" alt="drawing" width="60%" height="60%"/><br/><br/>
<img src="images/screenshot1.png" alt="drawing" width="60%" height="60%"/><br/><br/>
</p>

<p align="center">
  <img src="images/giphy.gif" alt="animated" width="60%" height="60%" />
</p>

## Timeline
<p align="center">
<img src="images/workflow2.png" alt="drawing"/> <br/>
</p>

Project made at Becode Brussels
