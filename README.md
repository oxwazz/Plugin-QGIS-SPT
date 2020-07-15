.. QGIS Plugin Builder documentation master file, created by
   sphinx-quickstart on Sat Jan  5 14:17:19 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Plugin QGIS SPT
===============================================
![Logo](https://user-images.githubusercontent.com/58234878/87500090-e26d8600-c685-11ea-849a-00fbeadfbf26.png)

Concepts
=================
Plugin QGIS SPT provides you for estimating land surface temperature (LST) with split-window algorithm (SWA) Qin for Landsat 8.

The steps to using Plugin QGIS SPT are fairly simple:

1. Open the plugin QGIS SPT from within QGIS.
2. Fill out the required value and input data band obtained from landsat 8 satellite imagery.
3. If you have the different value, you can change the default value from advance setting.
4. Calculate LST.


Running Plugin QGIS SPT
======================

Tab Parameter
--------------------------

General Setting:

![Parameter](https://user-images.githubusercontent.com/58234878/87500100-e699a380-c685-11ea-9189-ea4580111bcb.png)

- **Data Satellite** is data with values obtained from the metadata used for calculate LST.

- **Output Temp.** is to determine the external value of the resulting temperature.

- **Range Temp.** is the average value of air temperature in the area.

- **Tot. Water Vapor** is the value of total water vapor content.

- **Band Red** is data from landsat 8 satellite imagery.

- **Band NIR** is data from landsat 8 satellite imagery.

- **Band TIR-1** is data from landsat 8 satellite imagery.

- **Band TIR-2** is data from landsat 8 satellite imagery.

- **Save Output** is to determine the external directory of the data LST.

Advance Setting:

![ParameterAdv](https://user-images.githubusercontent.com/58234878/87500102-e8636700-c685-11ea-8e7d-190701308971.png)

- **At-Transmittance** is the value of atmospheric transmittance.

- **NDVI Soil** is the value of NDVI soil.

- **NDVI Vegetation** is the value of NDVI vegetation.

- **TIR-1 Emis. Soil** is the value of TIR-1 emissivity soil.

- **TIR-1 Emis. Veg.** is the value of TIR-1 emissivity vegetation.

- **TIR-2 Emis. Soil** is the value of TIR-2 emissivity soil.

- **TIR-2 Emis. Veg.** is the value of TIR-2 emissivity vegetation.

- **Geomectical** is the value of geomectical factor.


Tab About
--------------------------
![About](https://user-images.githubusercontent.com/58234878/87500085-e00b2c00-c685-11ea-978b-514fd3490167.png)

This is a description of the plugin QGIS SPT (author, version plugin, etc.).

Result
--------------------------
![Result](https://user-images.githubusercontent.com/58234878/87500106-ea2d2a80-c685-11ea-9fc4-ef92f60adc07.png)

This is a log generated from calculating LST.

Other
--------------------------
![Other](https://user-images.githubusercontent.com/58234878/87500097-e5687680-c685-11ea-9499-c54fe50af407.png)

- **Status:** is a text to shows the activity of plugin QGIS SPT.

- **Button Ok** is the button to start the process of calculating LST.

- **Button Close** is the button to close the plugin QGIS SPT.

- **Button Help** is the button to display the help page.


References
======================
[1] Qin, et al. (2014) ‘Derivation of land surface temperature for landsat-8 TIRS using a split window algorithm’, Sensors (Switzerland), 14(4), pp. 5768–5780. doi: 10.3390/s140405768.

[2] Qin, et al. (2015) ‘An improved mono-window algorithm for land surface temperature retrieval from landsat 8 thermal infrared sensor data’, Remote Sensing, 7(4), pp. 4268–4289. doi: 10.3390/rs70404268.

[3] USGS. (2019) ‘Landsat 8 (L8) Data Users Handbook’.

[4] Tsou, J. et al. (2017) ‘Urban Heat Island Assessment Using the Landsat 8 Data: A Case Study in Shenzhen and Hong Kong’, Urban Science, 1(1), p. 10. doi: 10.3390/urbansci1010010.

[5] https://landsat.gsfc.nasa.gov/wp-content/uploads/2013/01/BandpassesL7vL8_Jul20131.pdf

[6] https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature
