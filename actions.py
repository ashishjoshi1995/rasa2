# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import sqlite3
from data_models import BILL, CUSTOMER
from rasa_sdk.events import SlotSet
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class GetContractNum(FormAction):
	def name(self) -> Text:
		return "ask_contract_number"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		return ["CONTRACTNUM"]

	def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict]:
		conn = sqlite3.connect('tutorial.db')
		c = conn.cursor()
		print("Hello2")
		c.execute("SELECT * FROM CUSTOMERS WHERE (CONTRACTNUM='"+tracker.get_slot("CONTRACTNUM")+"')")
		customer_data = c.fetchall();
		print("Hello3")
		
		print(c)
		conn.commit()
		c.close()
		conn.close()
		if(len(customer_data)==0):
			print("Hello4")
			return[SlotSet("CUSTOMERTYPE", "NOTFOUND")]
			
		else:
			
			customer_data2 = CUSTOMER(customer_data[0][0],customer_data[0][1],customer_data[0][2],customer_data[0][3],customer_data[0][4],customer_data[0][5],customer_data[0][6])
			message = "Hello "+customer_data2.NAME
			dispatcher.utter_message(message)
			SlotSet("NAME", customer_data2.NAME)
			print("AHello4")
			print(customer_data2)
			print(customer_data2.CUSTOMERTYPE)
			print(customer_data[0][6])
			return[SlotSet("CUSTOMERTYPE", customer_data2.CUSTOMERTYPE)]

		return []

	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
		return {"CONTRACTNUM": self.from_entity(entity="CONTRACTNUM", intent="my_contractnum_is"),}

class FinancialSupportForm(FormAction):
	def name(self) -> Text:
		return "financial_support_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		return ["CONTRACTNUM", "REASON"]

	def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict]:
		print("hello from the financial financial_support_forms")

		return []

	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
		return {"CONTRACTNUM": self.from_entity(entity="CONTRACTNUM", intent="my_contractnum_is"),"REASON": self.from_text(intent="inform"),}


class BillDefermentForm(FormAction):
	def name(self) -> Text:
		return "defer_bill_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		return ["CONTRACTNUM", "REASON"]

	def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict]:
		print("hello from the defement form")

		return []

	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
		return {"CONTRACTNUM": self.from_entity(entity="CONTRACTNUM", intent="my_contractnum_is"),"REASON": self.from_text(intent="inform"),}


class RegistrationForm(FormAction):
	def name(self) -> Text:
		return "registration_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		return ["CONTRACTNUM", "PHONENUM", "ADDRESS", "EMAIL"]

	def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict]:
		conn = sqlite3.connect('tutorial.db')
		c = conn.cursor()
		print("hello from the registration form")
		c.execute("INSERT INTO CUSTOMERS VALUES('"+tracker.get_slot("CONTRACTNUM")+"', 'pwd', '"+tracker.get_slot("PHONENUM")+"', '"+tracker.get_slot("ADDRESS")+"', '"+tracker.get_slot("EMAIL")+"', 'PREPAIDBAD', '"+tracker.get_slot("CONTRACTNUM")+"')")
		conn.commit()
		c.close()
		conn.close()
		return []

	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
		return {"CONTRACTNUM": self.from_entity(entity="CONTRACTNUM", intent="my_contractnum_is"),"PHONENUM": self.from_text(intent="inform"),"ADDRESS": self.from_text(intent="inform"),"EMAIL": self.from_text(intent="inform"),}



