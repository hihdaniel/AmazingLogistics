# -*- coding: utf-8 -*-

"""
Created on Thu Jul 15 00:20:08 2021

@author: dan
"""


#input product info
product_info = ["item_256732_desc_boxcut_origin_AU_checkin_12232021_destination_US_exparrival_01232022","item_546563_desc_pillow_origin_PH_checkin_07152021_destination_US_exparrival_08162021","item_587141_desc_dumbel_origin_RU_checkin_05052021_destination_US_exparrival_08162021"]
#contains products
product_list = range(len(product_info))
print(product_info)
#output format '(1)256732(2)boxcut(3)AU(4)12232021(5)/(6)US(7)01232022'
#output1 = Product1[5:11] + Product1[17:23] + Product1[31:33] + Product1[42:50] + "/" + Product1[63:65] + Product1[78:]
#output2 = Product2[5:11] + Product2[17:23] + Product2[31:33] + Product2[42:50] + "/" + Product2[63:65] + Product2[78:]
#output3 = Product3[5:11] + Product3[17:23] + Product3[31:33] + Product3[42:50] + "/" + Product3[63:65] + Product3[78:]
output1 = str(product_info[0])
output2 = str(product_info[1])
output3 = str(product_info[2])
output_list = []
for item in product_info:
    output_list.append(str(item[5:11] + item[17:23] + item[31:33] + item[42:50] + "/" + item[63:65] + item[78:]))
    print(len(output_list))