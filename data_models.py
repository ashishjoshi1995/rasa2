class BILL:
    """A sample Employee class"""

    def __init__(self, NAME, PHONENUM, BILLID, METERREADING, BILLAMOUNT, BILL_STATUS, PAYMENT_LAST_DATE, CONTRACTNUM):
        self.NAME = FIRSTNAME
        self.PHONENUM = PHONENUM
        self.METERREADING = METERREADING
        self.BILLID = BILLID
        self.BILLAMOUNT = BILLAMOUNT
        self.BILL_STATUS = BILL_STATUS
        self.PAYMENT_LAST_DATE = PAYMENT_LAST_DATE
        self.CONTRACTNUM = CONTRACTNUM

    def __repr__(self):
        return "Employee('{}', '{}', '{}', '{}', '{}', '{}', '{}', {}')".format(self.NAME, self.PHONENUM, self.BILLID, self.METERREADING, self.BILLAMOUNT, self.BILL_STATUS, self.PAYMENT_LAST_DATE, self.CONTRACTNUM)

class TOPUP:
    """A sample Employee class"""

    def __init__(self, NAME, PHONENUM, TOPUPID, CREDIT_VALUE, RECHARGE_DATE, CONTRACTNUM):
        self.NAME = FIRSTNAME
        self.PHONENUM = PHONENUM
        self.TOPUPID = TOPUPID
        self.CREDIT_VALUE = CREDIT_VALUE
        self.RECHARGE_DATE = RECHARGE_DATE
        self.CONTRACTNUM = CONTRACTNUM

    def __repr__(self):
        return "Employee('{}', '{}', '{}', '{}', '{}', '{}')".format(self.NAME, self.PHONENUM, self.TOPUPID, self.CREDIT_VALUE, self.RECHARGE_DATE, self.CONTRACTNUM)


class CUSTOMER:
    """A sample Employee class"""

    def __init__(self, FIRSTNAME, LASTNAME, PHONENUM, ADDRESS, EMAIL, CUSTOMERTYPE, CONTRACTNUM):
        self.NAME = FIRSTNAME
        self.PASSWORD = LASTNAME
        self.PHONENUM = PHONENUM
        self.ADDRESS = ADDRESS
        self.EMAIL = EMAIL
        self.CUSTOMERTYPE = CUSTOMERTYPE
        self.CONTRACTNUM = CONTRACTNUM

    def __repr__(self):
        return "Employee('{}', '{}', '{}', '{}', '{}', '{}', '{}'')".format(self.NAME, self.PASSWORD, self.PHONENUM, self.ADDRESS, self.EMAIL, self.CUSTOMERTYPE, self.CONTRACTNUM)

class SERVICE_REQUEST:
    """A sample Employee class"""

    def __init__(self, FIRSTNAME, PHONENUM, ADDRESS, BILLAMOUNT, BILL_STATUS, SERVICE_ID, CONTRACTNUM):
        self.NAME = FIRSTNAME
        self.PHONENUM = LASTNAME
        self.ADDRESS = PHONENUM
        self.REQUEST_TYPE = BILLID
        self.STATUS = BILLAMOUNT
        self.SERVICE_ID = BILL_STATUS
        self.CONTRACTNUM = CONTRACTNUM

    def __repr__(self):
        return "Employee('{}', '{}', '{}', '{}', '{}', '{}')".format(self.NAME, self.PHONENUM, self.ADDRESS, self.REQUEST_TYPE, self.STATUS, self.SERVICE_ID, self.CONTRACTNUM)
