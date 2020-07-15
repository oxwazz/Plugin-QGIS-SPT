.. QGIS Plugin Builder documentation master file, created by
   sphinx-quickstart on Sat Jan  5 14:17:19 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Plugin QGIS SPT
===============================================
.. image:: images/Logo.png

Concepts
=================
Plugin QGIS SPT provides you for estimating land surface temperature (LST) with split-window algorithm (SWA) Qin for Landsat 8.

The steps to using Plugin QGIS SPT are fairly simple:

#. Open the plugin QGIS SPT from within QGIS.
#. Fill out the required value and input data band obtained from landsat 8 satellite imagery.
#. If you have the different value, you can change the default value from advance setting.
#. Calculate LST.


Running Plugin QGIS SPT
======================

Tab Parameter
--------------------------

General Setting:

.. image:: images/Parameter.png

**Data Satellite**
 Data Satellite is data with values obtained from the metadata used for calculate LST.

**Output Temp.**
 Output temperature is to determine the external value of the resulting temperature
 , see :ref:`Temperature Conversion title`.

**Range Temp.**
 Range temperature is the average value of air temperature in the area
 , see :ref:`Table Regression Coefficients title`.

**Tot. Water Vapor**
 Total water vapor is the value of total water vapor content
 , see :ref:`Total Water Vapor Content title`.

**Band Red**
 Band red is data from landsat 8 satellite imagery
 , see :ref:`Table band Red, NIR, TIR-1, and TIR-2 Landsat 8 title`.

**Band NIR**
 Band near-infrared (NIR) is data from landsat 8 satellite imagery
 , see :ref:`Table band Red, NIR, TIR-1, and TIR-2 Landsat 8 title`.

**Band TIR-1**
 Band thermal-infrared 1 (TIR-1) is data from landsat 8 satellite imagery
 , see :ref:`Table band Red, NIR, TIR-1, and TIR-2 Landsat 8 title`.

**Band TIR-2**
 Band thermal-infrared 2 (TIR-2) is data from landsat 8 satellite imagery
 , see :ref:`Table band Red, NIR, TIR-1, and TIR-2 Landsat 8 title`.

**Save Output**
 Save output is to determine the external directory of the data LST.


Advance Setting:

.. image:: images/ParameterAdv.png

**At-Transmittance**
 This is the value of atmospheric transmittance
 , see :ref:`Attrans title`.

**NDVI Soil**
 This is the value of NDVI soil
 , see :ref:`Table NDVI Soil and Vegetation title`.

**NDVI Vegetation**
 This is the value of NDVI vegetation
 , see :ref:`Table NDVI Soil and Vegetation title`.

**TIR-1 Emis. Soil**
 This is the value of TIR-1 emissivity soil
 , see :ref:`Table Emissivity Soil and Vegetation title`.

**TIR-1 Emis. Veg.**
 This is the value of TIR-1 emissivity vegetation
 , see :ref:`Table Emissivity Soil and Vegetation title`.

**TIR-2 Emis. Soil**
 This is the value of TIR-2 emissivity soil
 , see :ref:`Table Emissivity Soil and Vegetation title`.

**TIR-2 Emis. Veg.**
 This is the value of TIR-2 emissivity vegetation
 , see :ref:`Table Emissivity Soil and Vegetation title`.

**Geomectical**
 This is the value of geomectical factor
 , see :ref:`Table Geometrical Factor title`.


Tab About
--------------------------

.. image:: images/About.png

This is a description of the plugin QGIS SPT (author, version plugin, etc.).

Result
--------------------------

.. image:: images/Result.png

This is a log generated from calculating LST.

Other
--------------------------

.. image:: images/Other.png

**Status:**
 This is a text to shows the activity of plugin QGIS SPT.

**Button Ok**
 This is the button to start the process of calculating LST
 , see :ref:`LST title`.

**Button Close**
 This is the button to close the plugin QGIS SPT.

**Button Help**
 This is the button to display the help page.


References
======================
.. [1] Qin, et al. (2014) ‘Derivation of land surface temperature for landsat-8 TIRS using a split window algorithm’, Sensors (Switzerland), 14(4), pp. 5768–5780. doi: 10.3390/s140405768.

.. [2] Qin, et al. (2015) ‘An improved mono-window algorithm for land surface temperature retrieval from landsat 8 thermal infrared sensor data’, Remote Sensing, 7(4), pp. 4268–4289. doi: 10.3390/rs70404268.

.. [3] USGS. (2019) ‘Landsat 8 (L8) Data Users Handbook’.

.. [4] Tsou, J. et al. (2017) ‘Urban Heat Island Assessment Using the Landsat 8 Data: A Case Study in Shenzhen and Hong Kong’, Urban Science, 1(1), p. 10. doi: 10.3390/urbansci1010010.

.. [5] https://landsat.gsfc.nasa.gov/wp-content/uploads/2013/01/BandpassesL7vL8_Jul20131.pdf

.. [6] https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature
