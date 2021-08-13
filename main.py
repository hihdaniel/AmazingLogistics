from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.config import Config
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from time import time




scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name ("tracking-app\client_secret.json", scope)
client =  gspread.authorize(creds)
sheet = client.open('delivery_products')
product = sheet.values_get('basic')

product_info_web_names = [sheet.values_get('F2:F9')]
product_info_web_names_converter = str(product_info_web_names)
print (product_info_web_names_converter[2])
"""
product_info_web_id_number = [sheet.values_get('A2:A9')]
product_info_web_origin = [sheet.values_get('B2:B9')]
product_info_web_checkin_date = [sheet.values_get('C2:C9')]
product_info_web_destination = [sheet.values_get('D2:D9')]
product_info_web_expected_arrival_date = [sheet.values_get('E2:E9')]

manual_search_input_storage=str()
three_most_recent_check_in_products = ["abc123xyz","bar444rab","clp678plc"]
product_shortcode = three_most_recent_check_in_products[0]
spinner = Spinner(text = "Show Recent",values = product_info_web_names_converter, size_hint =(None,None),size = ("100dp","50dp"))#, id = "bottom_left_button")
Macro_Box_Layout = BoxLayout(orientation = "vertical")
Sub_Layout_V_1 = BoxLayout(orientation = "vertical")
Sub_Layout_H_1 = BoxLayout(orientation = "horizontal")
Sub_Layout_V_2 = BoxLayout(orientation = "vertical")
Sub_Layout_H_2 = BoxLayout(orientation = "horizontal")
btn1 = Button(text = "Menu",size_hint =(None,None),size = ("80dp","50dp"))#, id = "menu_button")
btn2 = Button(text = "",background_color = [0, 0, 0, 0])#, id = "top_middle_spacer")
btn3 = Button(text = "",background_color = [0, 0, 0, 0])#, id = "top_right_spacer")
btn4 = spinner
btn5 = Button(text = "",background_color = [0, 0, 0, 0])#, id = "bottom_middle_spacer")
btn6 = TextInput(text='Search for Info', multiline=False,size_hint =(1,.5)) #Button(text = "Search for Info",size_hint =(1,.5))#, id = "bottom_right_text_input")
btn7 = Label(text="")
btn8 = Label(text = manual_search_input_storage)#, id = "lower_vert_full_info_display")
#
class BoxLayoutApp(App):
    def build(self):
        Sub_Layout_H_1.add_widget(btn1)
        Sub_Layout_H_1.add_widget(btn2)
        Sub_Layout_H_1.add_widget(btn3)
        Sub_Layout_H_2.add_widget(btn4)
        Sub_Layout_H_2.add_widget(btn5)
        Sub_Layout_H_2.add_widget(btn6)
        #self.btn4.bind(text = self.on_spinner_select)
        Sub_Layout_V_1.add_widget(btn7)
        #Sub_Layout_V_1.add_widget(spinnerObject)
        Sub_Layout_V_2.add_widget(btn8)
        Macro_Box_Layout.add_widget(Sub_Layout_H_1)
        Macro_Box_Layout.add_widget(Sub_Layout_H_2)
        Macro_Box_Layout.add_widget(Sub_Layout_V_1)
        Macro_Box_Layout.add_widget(Sub_Layout_V_2)
        return Macro_Box_Layout
    # how to print to labels: def variable of what you want to print, 2 args (self,text), tab in to label name with 2 args (self,text) again. this combo instantly prints to label. if typing it will print letter by letter. 
    def product_shortcode_printer_to_the_bottom_label(self, text):
        btn7.text = (self.text)
    spinner.bind(text=product_shortcode_printer_to_the_bottom_label)
    def manual_search_input_storage(self, text):
        btn8.text = (self.text)
    btn6.bind(text=manual_search_input_storage)


root = BoxLayoutApp()



root.run()
"""
