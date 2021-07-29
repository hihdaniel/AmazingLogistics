# -*- coding: utf-8 -*-

"""
Created on Thu Jul 15 00:20:08 2021

@author: dan
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('spreadsheet1-320520-59ecaf623ee9.json', scope)
client =  gspread.authorize(creds)

sheet = client.open('delivery_products')

product = sheet.values_get('basic')
print(product)

#input product info
product_info = ["item_256732_desc_boxcut_origin_AU_checkin_12232021_destination_US_exparrival_01232022","item_546563_desc_pillow_origin_PH_checkin_07152021_destination_US_exparrival_08162021","item_587141_desc_dumbel_origin_RU_checkin_05052021_destination_US_exparrival_08162021"]
product_info_web_names = [sheet.values_get('F2:F9')]
product_info_web_id_number = [sheet.values_get('A2:A9')]
product_info_web_origin = [sheet.values_get('B2:B9')]
product_info_web_checkin_date = [sheet.values_get('C2:C9')]
product_info_web_destination = [sheet.values_get('D2:D9')]
product_info_web_expected_arrival_date = [sheet.values_get('E2:E9')]
#print(product_info_web_checkin_date)
#converts product_list items into an int
product_list_item_count = len(product_info)
#first check working correctly
##print(product_info)
##print(product_list_item_count)
#depreciated code below.
#output format '(1)256732(2)boxcut(3)AU(4)12232021(5)/(6)US(7)01232022'
#output1 = Product1[5:11] + Product1[17:23] + Product1[31:33] + Product1[42:50] + "/" + Product1[63:65] + Product1[78:]
#output2 = Product2[5:11] + Product2[17:23] + Product2[31:33] + Product2[42:50] + "/" + Product2[63:65] + Product2[78:]
#output3 = Product3[5:11] + Product3[17:23] + Product3[31:33] + Product3[42:50] + "/" + Product3[63:65] + Product3[78:]
#end depreciated
#---------------------------------------
#translation step int indexes -> str indexes
output1 = str(product_info[0])
output2 = str(product_info[1])
output3 = str(product_info[2])
#reads int, prints str simutaneously converting to short code
output_list = []
for item in product_info:
    output_list.append(str(item[5:11] + item[17:23] + item[31:33] + item[42:50] + "/" + item[63:65] + item[78:]))
##    print(len(output_list))
##    print(output_list)
#next-need input from user and print based on selection
user_selection = input("choose a product number to display. 0 to " + str(len(output_list)-1) + ": ")
print(output_list[int(user_selection)])
#next-recieve product info from nonlocal spreadsheet
#next-create userfriendly webapp
#next-create scan friendly product data storage.
