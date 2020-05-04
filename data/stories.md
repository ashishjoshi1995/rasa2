## happy path
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## register
* register_intent
  - registration_form
  - form{"name": "registration_form"}
  - form{"name": null}
  - slot{"CONTRACTNUM" : "97564"}
  - slot{"ADDRESS": "INDORE"}
  - slot{"PHONENUM": "9756475739"}
  - slot{"EMAIL": "sweta.bhoi@accenture.com"}
  - utter_success

## customer_support_initiatives
* customer_support_initiatives
  - ask_contract_number
  - form{"name": "ask_contract_number"}
  - form{"name": null}
  - slot{"CUSTOMERTYPE" : "NOTFOUND"}
  - slot{"CONTRACTNUM" : "97564"}
  - utter_not_found

## customer_support_initiatives
* customer_support_initiatives
  - ask_contract_number
  - form{"name": "ask_contract_number"}
  - form{"name": null}
  - slot{"CUSTOMERTYPE" : "PREPAIDGOOD"}
  - slot{"CONTRACTNUM" : "97564"}
  - utter_offer_prepaidgood

## customer_support_initiatives
* customer_support_initiatives
  - ask_contract_number
  - form{"name": "ask_contract_number"}
  - form{"name": null}
  - slot{"CUSTOMERTYPE" : "PREPAIDBAD"}
  - slot{"CONTRACTNUM" : "97564"}
  - utter_offer_prepaidgood


## Financial support
* enroll_finanical_support
  - financial_support_form
  - form{"name": "financial_support_form"}
  - form{"name": null}
  - slot{"CONTRACTNUM" : "97564"}
  - slot{"REASON" : "Lost my job"}
  - utter_success 

## bill deferement
* defer_bill_payment
  - defer_bill_form
  - form{"name": "defer_bill_form"}
  - form{"name": null}
  - slot{"CONTRACTNUM" : "97564"}
  - slot{"REASON" : "Lost my job"}
  - utter_success

## customer_support_initiatives
* customer_support_initiatives
  - ask_contract_number
  - form{"name": "ask_contract_number"}
  - form{"name": null}
  - slot{"CUSTOMERTYPE" : "POSTPAIDGOOD"}
  - slot{"CONTRACTNUM" : "97564"}
  - utter_offer_postpaid

## customer_support_initiatives
* customer_support_initiatives
  - ask_contract_number
  - form{"name": "ask_contract_number"}
  - form{"name": null}
  - slot{"CUSTOMERTYPE" : "POSTPAIDBAD"}
  - slot{"CONTRACTNUM" : "97564"}
  - utter_offer_postpaid

## purchase credit loan
* get_credit_loan
  - ask_contract_number
  - form{"name": "ask_contract_number"}
  - form{"name": null}
  - utter_success

## prepaid_increased_credit
* prepaid_increased_credit
  - utter_prepaid_increased_credit

## prepaid_credit_loan
* prepaid_credit_loan
  - utter_prepaid_credit_loan

## prepaid_recharge
* prepaid_recharge
- ask_contract_number
  - form{"name": "ask_contract_number"}
  - form{"name": null}
  - slot{"CUSTOMERTYPE" : "PREPAIDBAD"}
  - slot{"CONTRACTNUM" : "97564"}
  - utter_prepaid_recharge

## disconnection
* disconnection
  - utter_disconnection

## utter_late_payment_enquiry
* late_payment_enquiry
  - utter_late_payment_enquiry


## utter_change_in_tariff
* change_in_tariff
  - utter_change_in_tariff




