# ",/usr/bin/env python,
# ,
# Copyright 2020-present Facebook. All Rights Reserved.,
# ,
# This program file is free software; you can redistribute it and/or modify it,
# under the terms of the GNU General Public License as published by the,
# Free Software Foundation; version 2 of the License.,
# ,
# This program is distributed in the hope that it will be useful, but WITHOUT,
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or,
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License,
# for more details.,
# ,
# You should have received a copy of the GNU General Public License,
# along with this program in a file named COPYING; if not, write to the,
# Free Software Foundation, Inc.,,
# 51 Franklin Street, Fifth Floor,,
# Boston, MA 02110-1301 USA,


plat_i2c_tree = {
    "2-003e": {"name": "scmcpld", "driver": "scmcpld"},
    "3-004a": {"name": "tmp75", "driver": "lm75"},
    "4-0027": {"name": "pca9555", "driver": "pca953x"},
    "5-0060": {"name": "domfpga", "driver": "domfpga"},
    "6-0021": {"name": "pca9534", "driver": "pca953x"},
    "6-0051": {"name": "24c64", "driver": "at24"},
    "8-004a": {"name": "tmp75", "driver": "lm75"},
    "8-0051": {"name": "24c64", "driver": "at24"},
    "12-003e": {"name": "smb_syscpld", "driver": "smb_syscpld"},
    "13-0060": {"name": "domfpga", "driver": "domfpga"},
    "16-004d": {"name": "ir35215", "driver": "ir35215"},
    "17-0040": {"name": "xdpe132g5c", "driver": "xdpe12284"},
    "18-003a": {"name": "powr1220", "driver": "powr1220"},
    "19-0068": {"name": "xdpe12284", "driver": "xdpe12284"},
    "20-000e": {"name": "pxe1211", "driver": "pxe1610"},
    "21-0047": {"name": "ir35215", "driver": "ir35215"},
    "22-0060": {"name": "xdpe12284", "driver": "xdpe12284"},
    "24-0010": {"name": "adm1278", "driver": "adm1275"},
    "25-004c": {"name": "tmp75", "driver": "lm75"},
    "25-004d": {"name": "tmp75", "driver": "lm75"},
    "27-0052": {"name": "24c64", "driver": "at24"},
    "28-0050": {"name": "24c02", "driver": "at24"},
    "32-0048": {"name": "tmp75", "driver": "lm75"},
    "33-0049": {"name": "tmp75", "driver": "lm75"},
    "34-004b": {"name": "tmp75", "driver": "lm75"},
    "35-004c": {"name": "tmp421", "driver": "tmp421"},
    "36-004d": {"name": "tmp421", "driver": "tmp421"},
    "37-004e": {"name": "tmp75", "driver": "lm75"},
    "38-002a": {"name": "net_asic", "driver": "net_asic"},
    "39-004f": {"name": "tmp75", "driver": "lm75"},
    "40-0058": {"name": "psu_driver", "driver": "psu_driver"},
    "41-0058": {"name": "psu_driver", "driver": "psu_driver"},
    "42-0050": {"name": "24c02", "driver": "at24"},
    "43-0050": {"name": "24c02", "driver": "at24"},
    "47-003e": {"name": "smb_pwrcpld", "driver": "smb_pwrcpld"},
    "48-003e": {"name": "fcbcpld", "driver": "fcbcpld"},
    "49-0051": {"name": "24c64", "driver": "at24"},
    "50-0048": {"name": "tmp75", "driver": "lm75"},
    "50-0049": {"name": "tmp75", "driver": "lm75"},
    "51-0010": {"name": "adm1278", "driver": "adm1275"},
    "52-0052": {"name": "24c64", "driver": "at24"},
    "53-0052": {"name": "24c64", "driver": "at24"},
    "54-0052": {"name": "24c64", "driver": "at24"},
    "55-0052": {"name": "24c64", "driver": "at24"},
}