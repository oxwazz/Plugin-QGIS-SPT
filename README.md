![Logo](https://user-images.githubusercontent.com/58234878/87500090-e26d8600-c685-11ea-849a-00fbeadfbf26.png)

# Plugin QGIS SPT

## Concepts
[Plugin QGIS SPT][7] provides you for estimating Land Surface Temperature (LST) with [Split-Window Algorithm (SWA)][1] for Landsat 8.

The steps to using are fairly simple:
1. Open the [plugin QGIS SPT][7] from within [QGIS][8].
2. Fill out the required value and input data band obtained from landsat 8 satellite imagery.
3. If you have the different value, you can change the default value from advance setting.
4. Calculate LST.

**Link**: [Plugin QGIS SPT][7] <br>
**Other**: [Video Comparison Between Plugin QGIS SPT and Raster Calculator (Manual)][9]

## Running Plugin QGIS SPT

### Tab Parameter

**General Setting:**

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

**Advance Setting:**

![ParameterAdv](https://user-images.githubusercontent.com/58234878/87500102-e8636700-c685-11ea-8e7d-190701308971.png)

- **At-Transmittance** is the value of atmospheric transmittance.
- **NDVI Soil** is the value of NDVI soil.
- **NDVI Vegetation** is the value of NDVI vegetation.
- **TIR-1 Emis. Soil** is the value of TIR-1 emissivity soil.
- **TIR-1 Emis. Veg.** is the value of TIR-1 emissivity vegetation.
- **TIR-2 Emis. Soil** is the value of TIR-2 emissivity soil.
- **TIR-2 Emis. Veg.** is the value of TIR-2 emissivity vegetation.
- **Geomectical** is the value of geomectical factor.


### Tab About
![About](https://user-images.githubusercontent.com/58234878/87500085-e00b2c00-c685-11ea-978b-514fd3490167.png)

This is a description of the plugin (author, version plugin, etc.).

### Result
![Result](https://user-images.githubusercontent.com/58234878/87500106-ea2d2a80-c685-11ea-9fc4-ef92f60adc07.png)

This is a log generated from calculating LST.

### Other
![Other](https://user-images.githubusercontent.com/58234878/87500097-e5687680-c685-11ea-9499-c54fe50af407.png)

- **Status:** is a text to shows the activity.
- **Button Ok** is the button to start the process of calculating LST.
- **Button Close** is the button to close.
- **Button Help** is the button to display the help page.


## References
1. [Paper - Qin, et al. (2014) - Derivation of Land Surface Temperature for Landsat-8 TIRS Using a Split Window Algorithm][1]
2. [Paper - Qin, et al. (2015) - An Improved Mono-Window Algorithm for Land Surface Temperature Retrieval from Landsat 8 Thermal Infrared Sensor Data][2]
3. [Book - Landsat 8 Data Users Handbook][3]
4. [Paper - Tsou, et al. (2017) - Urban Heat Island Assessment Using the Landsat 8 Data: A Case Study in Shenzhen and Hong Kong][4]
5. [Web - NASA Landsat - Band Passes Landsat 7 and Landsat 8][5]
6. [Web - Wikipedia - Conversion of Units of Temperature][6]

<!-- References -->
[1]: https://www.mdpi.com/1424-8220/14/4/5768/pdf "Paper - Qin, et al. (2014) - Derivation of Land Surface Temperature for Landsat-8 TIRS Using a Split Window Algorithm"
[2]: https://www.mdpi.com/2072-4292/7/4/4268 "Paper - Qin, et al. (2015) - An Improved Mono-Window Algorithm for Land Surface Temperature Retrieval from Landsat 8 Thermal Infrared Sensor Data"
[3]: https://www.usgs.gov/core-science-systems/nli/landsat/landsat-8-data-users-handbook "Book - Landsat 8 Data Users Handbook"
[4]: https://www.mdpi.com/2413-8851/1/1/10 "Paper - Tsou, et al. (2017) - Urban Heat Island Assessment Using the Landsat 8 Data: A Case Study in Shenzhen and Hong Kong"
[5]: https://landsat.gsfc.nasa.gov/wp-content/uploads/2013/01/BandpassesL7vL8_Jul20131.pdf "Web - NASA Landsat - Band Passes Landsat 7 and Landsat 8"
[6]: https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature "Web - Wikipedia - Conversion of Units of Temperature"

[7]: https://plugins.qgis.org/plugins/qgis_spt/ "SPT - Plugin QGIS"
[8]: https://qgis.org/en/site/ "QGIS - Desktop Application"
[9]: https://www.youtube.com/watch?v=WUp0tTu890Y
