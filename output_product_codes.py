# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 00:20:08 2021

@author: dan
"""
#input product info
Product1 = "item_256732_desc_boxcut_origin_AU_checkin_12232021_destination_US_exparrival_01232022"
#output format '(1)256732(2)boxcut(3)AU(4)12232021(5)/(6)US(7)01232022'
output1 = Product1[5:11] + Product1[17:23] + Product1[31:33] + Product1[42:50] + "/" + Product1[63:65] + Product1[78:]
print(output1)