from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from qgis.core import QgsRasterLayer
from qgis.utils import iface
from pathlib import Path
import os


class Equation():

    # fungsi membuat temporary folder
    def makeTemp(self, dir_output):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(self.dir_output).parent), 'temp_folder')
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def calc_10_toa_L7(self, dir_output, dir_btir1, temp_folder):
        self.temp_folder = temp_folder
        self.dir_output = dir_output
        self.dir_btir1 = dir_btir1
        self.dir_output_temp = str(Path(self.dir_output).parent) + '\\temp_folder\\10 - TOA.tif'

        entries = []

        band10 = QgsRasterLayer(self.dir_btir1)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'band10@1'
        ras.raster = band10
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('((17.04 - 0) / (255 - 1)) * ("band10@1" - 1) + 0', self.dir_output_temp, 'GTiff', band10.extent(), band10.width(), band10.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('((17.04 - 0) / (255 - 1)) * ("band10@1" - 1) + 0', self.dir_output, 'GTiff', band10.extent(), band10.width(), band10.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_11_toa_L7(self, dir_output, dir_btir2, temp_folder):
        self.temp_folder = temp_folder
        self.dir_output = dir_output
        self.dir_btir2 = dir_btir2
        self.dir_output_temp = str(Path(dir_output).parent) + '\temp_folder\\11 - TOA.tif'

        entries = []

        band11 = QgsRasterLayer(self.dir_btir2)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'band11@1'
        ras.raster = band11
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('((17.04 - 0) / (255 - 1)) * ("band11@1" - 1) + 0', self.dir_output_temp, 'GTiff', band11.extent(), band11.width(), band11.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('((17.04 - 0) / (255 - 1)) * ("band11@1" - 1) + 0', self.dir_output, 'GTiff', band11.extent(), band11.width(), band11.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_10_toa(self, dir_output, dir_btir1, temp_folder, val_tir1_rmult, val_tir1_radd):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_btir1 = dir_btir1
        self.dir_output_temp = self.path + '10 - TOA.tif'
        self.val_tir1_rmult = val_tir1_rmult
        self.val_tir1_radd = val_tir1_radd

        entries = []

        band10 = QgsRasterLayer(self.dir_btir1)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'band10@1'
        ras.raster = band10
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator(str(self.val_tir1_rmult) + '* "band10@1" +' + str(self.val_tir1_radd), self.dir_output_temp, 'GTiff', band10.extent(), band10.width(), band10.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator(str(self.val_tir1_rmult) + '* "band10@1" +' + str(self.val_tir1_radd), self.dir_output, 'GTiff', band10.extent(), band10.width(), band10.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_11_toa(self, dir_output, dir_btir2, temp_folder, val_tir2_rmult, val_tir2_radd):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_btir2 = dir_btir2
        self.dir_output_temp = self.path + '11 - TOA.tif'

        self.val_tir2_rmult = val_tir2_rmult
        self.val_tir2_radd = val_tir2_radd

        entries = []

        band11 = QgsRasterLayer(self.dir_btir2)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'band11@1'
        ras.raster = band11
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator(str(self.val_tir2_rmult) + ' * "band11@1" + ' + str(self.val_tir2_radd), self.dir_output_temp, 'GTiff', band11.extent(), band11.width(), band11.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator(str(self.val_tir2_rmult) + ' * "band11@1" + ' + str(self.val_tir2_radd), self.dir_output, 'GTiff', band11.extent(), band11.width(), band11.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    # BELOM
    def calc_10_bt_L7(self, dir_output, dir_toa_10, temp_folder, ):
        self.temp_folder = temp_folder
        dir_output = self.dlg.fw_output.filePath()
        dir_toa_10 = str(Path(dir_output).parent) + '\\temp_folder\\10 - TOA.tif'
        dir_output_temp = str(Path(dir_output).parent) + '\\temp_folder\\10 - BT.tif'

        entries = []

        toa_10 = QgsRasterLayer(output_toa_10)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '10 - TOA@1'
        ras.raster = toa_10
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator(str(L_TIR1_K2_L7) + ' / ln ( ( ' + str(L_TIR1_K1_L7) + ' / "10 - TOA@1" ) + 1 )', output_bt_10, 'GTiff', toa_10.extent(), toa_10.width(), toa_10.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator(str(L_TIR1_K2_L7) + ' / ln ( ( ' + str(L_TIR1_K1_L7) + ' / "10 - TOA@1" ) + 1 )', output_bt_10, 'GTiff', toa_10.extent(), toa_10.width(), toa_10.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    # BELOM
    def calc_11_bt_L7(self):
        dir_output = self.dlg.fw_output.filePath()
        output_toa_11 = str(Path(dir_output).parent) + '\\temp_folder\\11 - TOA.tif'
        output_bt_11 = str(Path(dir_output).parent) + '\\temp_folder\\11 - BT.tif'

        entries = []

        toa_11 = QgsRasterLayer(output_toa_11)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '10 - TOA@1'
        ras.raster = toa_11
        ras.bandNumber = 1
        entries.append(ras)

        if os.path.exists(Path(dir_output).parent):
            calc = QgsRasterCalculator(str(L_TIR2_K2_L7) + ' / ln ( ( ' + str(L_TIR2_K1_L7) + ' / "10 - TOA@1" ) + 1) ', output_bt_11, 'GTiff', toa_11.extent(), toa_11.width(), toa_11.height(), entries)
            calc.processCalculation()
        else:
            print("else")

    def calc_10_bt(self, dir_output, dir_toa_10, temp_folder, val_l_tir1_k1, val_l_tir1_k2):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_toa_10 = dir_toa_10
        self.dir_output_temp = self.path + '10 - BT.tif'

        self.val_l_tir1_k1 = val_l_tir1_k1
        self.val_l_tir1_k2 = val_l_tir1_k2

        entries = []

        toa_10 = QgsRasterLayer(self.dir_toa_10)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '10 - TOA@1'
        ras.raster = toa_10
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator(str(self.val_l_tir1_k2) + ' / ln ( ( ' + str(self.val_l_tir1_k1) + ' / "10 - TOA@1" ) + 1 )', self.dir_output_temp, 'GTiff', toa_10.extent(), toa_10.width(), toa_10.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator(str(self.val_l_tir1_k2) + ' / ln ( ( ' + str(self.val_l_tir1_k1) + ' / "10 - TOA@1" ) + 1 )', self.dir_output, 'GTiff', toa_10.extent(), toa_10.width(), toa_10.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_11_bt(self, dir_output, dir_toa_11, temp_folder, val_l_tir2_k1, val_l_tir2_k2):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_toa_11 = dir_toa_11
        self.dir_output_temp = self.path + '11 - BT.tif'

        self.val_l_tir2_k1 = val_l_tir2_k1
        self.val_l_tir2_k2 = val_l_tir2_k2

        entries = []

        toa_11 = QgsRasterLayer(self.dir_toa_11)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '10 - TOA@1'
        ras.raster = toa_11
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator(str(self.val_l_tir2_k2) + ' / ln ( ( ' + str(self.val_l_tir2_k1) + ' / "10 - TOA@1" ) + 1) ', self.dir_output_temp, 'GTiff', toa_11.extent(), toa_11.width(), toa_11.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator(str(self.val_l_tir2_k2) + ' / ln ( ( ' + str(self.val_l_tir2_k1) + ' / "10 - TOA@1" ) + 1) ', self.dir_output, 'GTiff', toa_11.extent(), toa_11.width(), toa_11.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_ndvi(self, dir_output, dir_bred, dir_bnir, temp_folder):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_bred = dir_bred
        self.dir_bnir = dir_bnir
        self.dir_output_temp = self.path + 'NDVI.tif'

        entries = []

        bred = QgsRasterLayer(self.dir_bred)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'bred@1'
        ras.raster = bred
        ras.bandNumber = 1
        entries.append(ras)

        bnir = QgsRasterLayer(self.dir_bnir)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'bnir@1'
        ras.raster = bnir
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('(bnir@1 - bred@1)/(bnir@1 + bred@1)', self.dir_output_temp, 'GTiff', bnir.extent(), bnir.width(), bnir.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('(band5@1 - band4@1)/(band5@1 + band4@1)', self.dir_output, 'GTiff', bnir.extent(), bnir.width(), bnir.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_pv(self, dir_output, dir_ndvi, temp_folder, val_ndvis, val_ndviv):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_ndvi = dir_ndvi
        self.dir_output_temp = self.path + 'Pv.tif'

        self.val_ndvis = val_ndvis
        self.val_ndviv = val_ndviv

        entries = []

        ndvi = QgsRasterLayer(self.dir_ndvi)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'ndvi@1'
        ras.raster = ndvi
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('( ( "ndvi@1" - ' + str(self.val_ndvis) + ' ) / ( ' + str(self.val_ndviv) + ' - ' + str(self.val_ndvis) + ' ) ) * ( ( "ndvi@1" - ' + str(self.val_ndvis) + ' ) / ( ' + str(self.val_ndviv) + ' - ' + str(self.val_ndvis) + ' ) )', self.dir_output_temp, 'GTiff', ndvi.extent(), ndvi.width(), ndvi.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('( ( "ndvi@1" - ' + str(self.val_ndvis) + ' ) / ( ' + str(self.val_ndviv) + ' - ' + str(self.val_ndvis) + ' ) ) * ( ( "ndvi@1" - ' + str(self.val_ndvis) + ' ) / ( ' + str(self.val_ndviv) + ' - ' + str(self.val_ndvis) + ' ) )', self.dir_output, 'GTiff', ndvi.extent(), ndvi.width(), ndvi.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_10_ckecil(self, dir_output, dir_pv, temp_folder, val_tir1emissivitys, val_tir1emissivityv, val_geometrical):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_pv = dir_pv
        self.dir_output_temp = self.path + '10 - c kecil.tif'

        self.val_tir1emissivitys = val_tir1emissivitys
        self.val_tir1emissivityv = val_tir1emissivityv
        self.val_geometrical = val_geometrical

        entries = []

        pv = QgsRasterLayer(self.dir_pv)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'Pv@1'
        ras.raster = pv
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('( 1 - ' + str(self.val_tir1emissivitys) + ' ) * ' + str(self.val_tir1emissivityv) + ' * ' + str(self.val_geometrical) + ' *  ( 1 - "Pv@1" )', self.dir_output_temp, 'GTiff', pv.extent(), pv.width(), pv.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('( 1 - ' + str(self.val_tir1emissivitys) + ' ) * ' + str(self.val_tir1emissivityv) + ' * ' + str(self.val_geometrical) + ' *  ( 1 - "Pv@1" )', self.dir_output, 'GTiff', pv.extent(), pv.width(), pv.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_10_e(self, dir_output, dir_pv, dir_c_kecil_10, temp_folder, val_tir1emissivitys, val_tir1emissivityv):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_pv = dir_pv
        self.dir_c_kecil_10 = dir_c_kecil_10
        self.dir_output_temp = self.path + '10 - e.tif'

        self.val_tir1emissivitys = val_tir1emissivitys
        self.val_tir1emissivityv = val_tir1emissivityv

        entries = []

        pv = QgsRasterLayer(self.dir_pv)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'Pv@1'
        ras.raster = pv
        ras.bandNumber = 1
        entries.append(ras)

        c_kecil_10 = QgsRasterLayer(self.dir_c_kecil_10)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '10 - c kecil@1'
        ras.raster = c_kecil_10
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator(str(self.val_tir1emissivityv) + ' * "Pv@1" + ' + str(self.val_tir1emissivitys) + ' * ( 1 - "Pv@1" ) + "10 - c kecil@1"', self.dir_output_temp, 'GTiff', pv.extent(), pv.width(), pv.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator(str(self.val_tir1emissivityv) + ' * "Pv@1" + ' + str(self.val_tir1emissivitys) + ' * ( 1 - "Pv@1" ) + "10 - c kecil@1"', self.dir_output, 'GTiff', pv.extent(), pv.width(), pv.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_10_cbesar(self, dir_output, dir_e_10, temp_folder, val_attransmit1):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_e_10 = dir_e_10
        self.dir_output_temp = self.path + '10 - C besar.tif'

        self.val_attransmit1 = val_attransmit1

        entries = []

        e_10 = QgsRasterLayer(self.dir_e_10)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '10 - e@1'
        ras.raster = e_10
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('"10 - e@1" * ' + str(self.val_attransmit1), self.dir_output_temp, 'GTiff', e_10.extent(), e_10.width(), e_10.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('"10 - e@1" * ' + str(self.val_attransmit1), self.dir_output, 'GTiff', e_10.extent(), e_10.width(), e_10.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_10_d(self, dir_output, dir_e_10, temp_folder, val_attransmit1):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_e_10 = dir_e_10
        self.dir_output_temp = self.path + '10 - D.tif'

        self.val_attransmit1 = val_attransmit1

        entries = []

        e_10 = QgsRasterLayer(self.dir_e_10)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '10 - e@1'
        ras.raster = e_10
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('( 1 - ' + str(self.val_attransmit1) + ' ‬ ) * ( 1 + ( 1 - "10 - e@1" ) * ' + str(self.val_attransmit1) + ')', self.dir_output_temp, 'GTiff', e_10.extent(), e_10.width(), e_10.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('( 1 - ' + str(self.val_attransmit1) + ' ‬ ) * ( 1 + ( 1 - "10 - e@1" ) * ' + str(self.val_attransmit1) + ')', self.dir_output, 'GTiff', e_10.extent(), e_10.width(), e_10.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_11_ckecil(self, dir_output, dir_pv, temp_folder, val_tir2emissivitys, val_tir2emissivityv, val_geometrical):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_pv = dir_pv
        self.dir_output_temp = self.path + '11 - c kecil.tif'

        self.val_tir2emissivitys = val_tir2emissivitys
        self.val_tir2emissivityv = val_tir2emissivityv
        self.val_geometrical = val_geometrical

        entries = []

        pv = QgsRasterLayer(self.dir_pv)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'Pv@1'
        ras.raster = pv
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('( 1 - ' + str(self.val_tir2emissivitys) + ' ) * ' + str(self.val_tir2emissivityv) + ' * ' + str(self.val_geometrical) + ' * ( 1 - "Pv@1" )', self.dir_output_temp, 'GTiff', pv.extent(), pv.width(), pv.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('( 1 - ' + str(self.val_tir2emissivitys) + ' ) * ' + str(self.val_tir2emissivityv) + ' * ' + str(self.val_geometrical) + ' * ( 1 - "Pv@1" )', self.dir_output, 'GTiff', pv.extent(), pv.width(), pv.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_11_e(self, dir_output, dir_pv, dir_c_kecil_11, temp_folder, val_tir2emissivitys, val_tir2emissivityv):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_pv = dir_pv
        self.dir_c_kecil_11 = dir_c_kecil_11
        self.dir_output_temp = self.path + '11 - e.tif'

        self.val_tir2emissivitys = val_tir2emissivitys
        self.val_tir2emissivityv = val_tir2emissivityv

        entries = []

        pv = QgsRasterLayer(self.dir_pv)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'Pv@1'
        ras.raster = pv
        ras.bandNumber = 1
        entries.append(ras)

        c_kecil_11 = QgsRasterLayer(self.dir_c_kecil_11)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '11 - c kecil@1'
        ras.raster = c_kecil_11
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator(str(self.val_tir2emissivityv) + ' * "Pv@1" + ' + str(self.val_tir2emissivitys) + ' * ( 1 - "Pv@1" ) + "11 - c kecil@1"', self.dir_output_temp, 'GTiff', c_kecil_11.extent(), c_kecil_11.width(), c_kecil_11.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator(str(self.val_tir2emissivityv) + ' * "Pv@1" + ' + str(self.val_tir2emissivitys) + ' * ( 1 - "Pv@1" ) + "11 - c kecil@1"', self.dir_output, 'GTiff', c_kecil_11.extent(), c_kecil_11.width(), c_kecil_11.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_11_cbesar(self, dir_output, dir_e_11, temp_folder, val_attransmit2):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_e_11 = dir_e_11
        self.dir_output_temp = self.path + '11 - C besar.tif'

        self.val_attransmit2 = val_attransmit2

        entries = []

        e_11 = QgsRasterLayer(self.dir_e_11)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '11 - e@1'
        ras.raster = e_11
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('"11 - e@1" * ' + str(self.val_attransmit2), self.dir_output_temp, 'GTiff', e_11.extent(), e_11.width(), e_11.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('"11 - e@1" * ' + str(self.val_attransmit2), self.dir_output, 'GTiff', e_11.extent(), e_11.width(), e_11.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_11_d(self, dir_output, dir_e_11, temp_folder, val_attransmit2):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_e_11 = dir_e_11
        self.dir_output_temp = self.path + '11 - D.tif'

        self.val_attransmit2 = val_attransmit2

        entries = []

        e_11 = QgsRasterLayer(self.dir_e_11)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '11 - e@1'
        ras.raster = e_11
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('( 1 - ' + str(self.val_attransmit2) + ' )* ( 1 + ( 1 - "11 - e@1" ) * ' + str(self.val_attransmit2)+')', self.dir_output_temp, 'GTiff', e_11.extent(), e_11.width(), e_11.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('( 1 - ' + str(self.val_attransmit2) + ' )* ( 1 + ( 1 - "11 - e@1" ) * ' + str(self.val_attransmit2)+')', self.dir_output, 'GTiff', e_11.extent(), e_11.width(), e_11.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_e0(self, dir_output, dir_D_11, dir_C_besar_10, dir_D_10, dir_C_besar_11, temp_folder):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_D_11 = dir_D_11
        self.dir_C_besar_10 = dir_C_besar_10
        self.dir_D_10 = dir_D_10
        self.dir_C_besar_11 = dir_C_besar_11
        self.dir_output_temp = self.path + 'E0.tif'

        entries = []

        D_11 = QgsRasterLayer(self.dir_D_11)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '11 - D@1'
        ras.raster = D_11
        ras.bandNumber = 1
        entries.append(ras)

        C_besar_10 = QgsRasterLayer(self.dir_C_besar_10)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '10 - C besar@1'
        ras.raster = C_besar_10
        ras.bandNumber = 1
        entries.append(ras)

        D_10 = QgsRasterLayer(self.dir_D_10)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '10 - D@1'
        ras.raster = D_10
        ras.bandNumber = 1
        entries.append(ras)

        C_besar_11 = QgsRasterLayer(self.dir_C_besar_11)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '11 - C besar@1'
        ras.raster = C_besar_11
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('"11 - D@1" * "10 - C besar@1" - "10 - D@1" * "11 - C besar@1"', self.dir_output_temp, 'GTiff', C_besar_11.extent(), C_besar_11.width(), C_besar_11.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('"11 - D@1" * "10 - C besar@1" - "10 - D@1" * "11 - C besar@1"', self.dir_output, 'GTiff', C_besar_11.extent(), C_besar_11.width(), C_besar_11.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_e2(self, dir_output, dir_D_10, dir_C_besar_11, dir_D_11, dir_E0, temp_folder):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_D_10 = dir_D_10
        self.dir_C_besar_11 = dir_C_besar_11
        self.dir_D_11 = dir_D_11
        self.dir_E0 = dir_E0
        self.dir_output_temp = self.path + 'E2.tif'

        entries = []

        D_10 = QgsRasterLayer(self.dir_D_10)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '10 - D@1'
        ras.raster = D_10
        ras.bandNumber = 1
        entries.append(ras)

        C_besar_11 = QgsRasterLayer(self.dir_C_besar_11)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '11 - C besar@1'
        ras.raster = C_besar_11
        ras.bandNumber = 1
        entries.append(ras)

        D_11 = QgsRasterLayer(self.dir_D_11)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '11 - D@1'
        ras.raster = D_11
        ras.bandNumber = 1
        entries.append(ras)

        E0 = QgsRasterLayer(self.dir_E0)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'E0@1'
        ras.raster = E0
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('"10 - D@1" * ( 1 - "11 - C besar@1" - "11 - D@1" ) / "E0@1"', self.dir_output_temp, 'GTiff', E0.extent(), E0.width(), E0.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('"10 - D@1" * ( 1 - "11 - C besar@1" - "11 - D@1" ) / "E0@1"', self.dir_output, 'GTiff', E0.extent(), E0.width(), E0.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_e1(self, dir_output, dir_D_11, dir_C_besar_10, dir_D_10, dir_E0, temp_folder):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_D_11 = dir_D_11
        self.dir_C_besar_10 = dir_C_besar_10
        self.dir_D_10 = dir_D_10
        self.dir_E0 = dir_E0
        self.dir_output_temp = self.path + 'E1.tif'

        entries = []

        D_11 = QgsRasterLayer(self.dir_D_11)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '11 - D@1'
        ras.raster = D_11
        ras.bandNumber = 1
        entries.append(ras)

        C_besar_10 = QgsRasterLayer(self.dir_C_besar_10)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '10 - C besar@1'
        ras.raster = C_besar_10
        ras.bandNumber = 1
        entries.append(ras)

        D_10 = QgsRasterLayer(self.dir_D_10)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '10 - D@1'
        ras.raster = D_10
        ras.bandNumber = 1
        entries.append(ras)

        E0 = QgsRasterLayer(self.dir_E0)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'E0@1'
        ras.raster = E0
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('"11 - D@1" * ( 1 - "10 - C besar@1" - "10 - D@1" ) / "E0@1"', self.dir_output_temp, 'GTiff', E0.extent(), E0.width(), E0.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('"11 - D@1" * ( 1 - "10 - C besar@1" - "10 - D@1" ) / "E0@1"', self.dir_output, 'GTiff', E0.extent(), E0.width(), E0.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_a(self, dir_output, dir_D_10, dir_E0, temp_folder):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_D_10 = dir_D_10
        self.dir_E0 = dir_E0
        self.dir_output_temp = self.path + 'A.tif'

        entries = []

        D_10 = QgsRasterLayer(self.dir_D_10)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '10 - D@1'
        ras.raster = D_10
        ras.bandNumber = 1
        entries.append(ras)

        E0 = QgsRasterLayer(self.dir_E0)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'E0@1'
        ras.raster = E0
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('"10 - D@1" / "E0@1"', self.dir_output_temp, 'GTiff', E0.extent(), E0.width(), E0.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('"10 - D@1" / "E0@1"', self.dir_output, 'GTiff', E0.extent(), E0.width(), E0.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_a2(self, dir_output, dir_A, dir_E2, temp_folder, B11):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_A = dir_A
        self.dir_E2 = dir_E2
        self.dir_output_temp = self.path + 'A2.tif'

        self.B11 = B11

        entries = []

        A = QgsRasterLayer(self.dir_A)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'A@1'
        ras.raster = A
        ras.bandNumber = 1
        entries.append(ras)

        E2 = QgsRasterLayer(self.dir_E2)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'E2@1'
        ras.raster = E2
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('"A@1" + "E2@1" * ' + self.B11 + ' ', self.dir_output_temp, 'GTiff', E2.extent(), E2.width(), E2.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('"A@1" + "E2@1" * ' + self.B11 + ' ', self.dir_output, 'GTiff', E2.extent(), E2.width(), E2.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_a1(self, dir_output, dir_A, dir_E1, temp_folder, B10):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_A = dir_A
        self.dir_E1 = dir_E1
        self.dir_output_temp = self.path + 'A1.tif'

        self.B10 = B10

        entries = []

        A = QgsRasterLayer(self.dir_A)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'A@1'
        ras.raster = A
        ras.bandNumber = 1
        entries.append(ras)

        E1 = QgsRasterLayer(self.dir_E1)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'E1@1'
        ras.raster = E1
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('1 + "A@1" + "E1@1" * ' + self.B10, self.dir_output_temp, 'GTiff', E1.extent(), E1.width(), E1.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('1 + "A@1" + "E1@1" * ' + self.B10, self.dir_output, 'GTiff', E1.extent(), E1.width(), E1.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_a0(self, dir_output, dir_E1, dir_E2, temp_folder, A10, A11):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_E1 = dir_E1
        self.dir_E2 = dir_E2
        self.dir_output_temp = self.path + 'A0.tif'

        self.A10 = A10
        self.A11 = A11

        entries = []

        E1 = QgsRasterLayer(self.dir_E1)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'E1@1'
        ras.raster = E1
        ras.bandNumber = 1
        entries.append(ras)

        E2 = QgsRasterLayer(self.dir_E2)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'E2@1'
        ras.raster = E2
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('"E1@1" * ' + self.A10 + ' + "E2@1" * ' + self.A11, self.dir_output_temp, 'GTiff', E2.extent(), E2.width(), E2.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('"E1@1" * ' + self.A10 + ' + "E2@1" * ' + self.A11, self.dir_output, 'GTiff', E2.extent(), E2.width(), E2.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))

    def calc_lst(self, dir_output, dir_bt_10, dir_bt_11, dir_A2, dir_A1, dir_A0, temp_folder, TEMP):
        self.dir_output = dir_output
        self.path = os.path.join(str(Path(dir_output).parent), 'temp_folder', '')

        self.temp_folder = temp_folder
        self.dir_bt_10 = dir_bt_10
        self.dir_bt_11 = dir_bt_11
        self.dir_A2 = dir_A2
        self.dir_A1 = dir_A1
        self.dir_A0 = dir_A0
        self.dir_output_temp = self.path + 'SPT.tif'

        self.TEMP = TEMP

        entries = []

        band10 = QgsRasterLayer(self.dir_bt_10)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '10 - BT@1'
        ras.raster = band10
        ras.bandNumber = 1
        entries.append(ras)

        band11 = QgsRasterLayer(self.dir_bt_11)
        ras = QgsRasterCalculatorEntry()
        ras.ref = '11 - BT@1'
        ras.raster = band11
        ras.bandNumber = 1
        entries.append(ras)

        A2 = QgsRasterLayer(self.dir_A2)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'A2@1'
        ras.raster = A2
        ras.bandNumber = 1
        entries.append(ras)

        A1 = QgsRasterLayer(self.dir_A1)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'A1@1'
        ras.raster = A1
        ras.bandNumber = 1
        entries.append(ras)

        A0 = QgsRasterLayer(self.dir_A0)
        ras = QgsRasterCalculatorEntry()
        ras.ref = 'A0@1'
        ras.raster = A0
        ras.bandNumber = 1
        entries.append(ras)

        if self.temp_folder == 'yes':
            calc = QgsRasterCalculator('(("A0@1" + "A1@1" * "10 - BT@1" - "A2@1" * "11 - BT@1") - 273.15)' + self.TEMP, self.dir_output_temp, 'GTiff', A0.extent(), A0.width(), A0.height(), entries)
            calc.processCalculation()
        elif self.temp_folder == 'no':
            calc = QgsRasterCalculator('(("A0@1" + "A1@1" * "10 - BT@1" - "A2@1" * "11 - BT@1") - 273.15)' + self.TEMP, self.dir_output, 'GTiff', A0.extent(), A0.width(), A0.height(), entries)
            calc.processCalculation()
            iface.addRasterLayer(str(self.dir_output))
