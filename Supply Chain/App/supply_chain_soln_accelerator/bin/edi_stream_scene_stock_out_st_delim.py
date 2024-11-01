#!/usr/bin/python3

import random
from datetime import datetime, timedelta

# Generate random BUYER and SELLER
buyers = ['BUYER_A', 'BUYER_B', 'BUYER_C']
sellers = ['SUPPLIER_X', 'SUPPLIER_Y', 'SUPPLIER_Z']
products = ['ITEM_100', 'ITEM_200', 'ITEM_300', 'ITEM_400', 'ITEM_500', 'ITEM_600', 'ITEM_700', 'ITEM_800', 'ITEM_900']
days_agos = [7, 6, 5, 4]
time_offset_days = [1, 2, 3, 4, 5, 6]
time_offset_hrs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
po_number = f"PO{random.randint(100000, 999999)}"
item1_qty = random.randint(50, 200)
item2_qty = random.randint(25, 100)
item1_temp = random.randint(20, 300)
item2_temp = random.randint(20, 100)
item1_price = round(item1_temp / 10) * 10
item2_price = round(item2_temp / 10) * 10
total_amount = item1_qty * item1_price + item2_qty * item2_price

# Generate dynamic timestamps
def generate_timestamp(base_date, time_offset_days=0, time_offset_hours=0):
    dt = base_date + timedelta(days=time_offset_days, hours=time_offset_hours)
    base_date = dt
    return dt.strftime("%Y%m%d"), dt.strftime("%H%M"), base_date

# Generate EDI 850 (Purchase Order)
def generate_edi_850(buyer, seller, po_number, product1, product2, base_date):
    date, time, base_date = generate_timestamp(base_date)
    edi_850 = f"""
ISA*00*          *00*          *ZZ*{buyer}         *ZZ*{seller}      *{date}*{time}*U*00401*000000001*0*T*:~
GS*PO*{buyer}*{seller}*{date}*{time}*1*X*004010~
ST*850*0001~
BEG*00*NE*{po_number}*{date}~
REF*ZZ*CONTRACT456~
N1*BY*{buyer}*92*123456~
N1*SE*{seller}*92*654321~
PO1*1*{item1_qty}*EA*20.00*PE*BP*{product1}~  // Order {item1_qty} units of {product1}
PO1*2*{item2_qty}*EA*15.00*PE*BP*{product2}~  // Order {item2_qty} units of {product2}
CTT*2~
SE*9*0001~
GE*1*1~
IEA*1*000000001~
"""
    return edi_850.strip()

# Generate EDI 855 (Purchase Order Acknowledgment)
def generate_edi_855(buyer, seller, po_number, product1, product2, base_date):
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)
    edi_855 = f"""
ISA*00*          *00*          *ZZ*{seller}      *ZZ*{buyer}         *{date}*{time}*U*00401*000000002*0*T*:~
GS*PO*{seller}*{buyer}*{date}*{time}*2*X*004010~
ST*855*0002~
BAK*00*AD*{po_number}*{date}~
N1*BY*{buyer}*92*123456~
N1*SE*{seller}*92*654321~
PO1*1*{item1_qty}*EA*20.00*PE*BP*{product1}*IA~  // Accepted: Full Quantity Available
PO1*2*{item2_qty}*EA*15.00*PE*BP*{product2}*BO~  // Backordered: Not enough stock for {product2}
SE*8*0002~
GE*1*2~
IEA*1*000000002~
"""
    return edi_855.strip()

# Generate EDI 856 (Advance Ship Notice)
def generate_edi_856(buyer, seller, po_number, product1, product2, base_date):
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    #date, time, base_date = generate_timestamp(base_date, time_offset_days=2, time_offset_hours=3)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)
    edi_856 = f"""
ISA*00*          *00*          *ZZ*{seller}      *ZZ*{buyer}         *{date}*{time}*U*00401*000000003*0*T*:~
GS*SH*{seller}*{buyer}*{date}*{time}*3*X*004010~
ST*856*0003~
BSN*00*ASN123456*{date}*{time}~
HL*1**S~
TD1*CTN*2****G*500*LB~  // Total Weight: 500 lbs
TD5*B*2*UPSN*M~
REF*BM*{po_number}~
DTM*011*{date}~
HL*2*1*O~
LIN**BP*{product1}~
SN1**100*EA~  // Full Quantity Shipped
HL*3*1*O~
LIN**BP*{product2}~
SN1**0*EA~  // No Quantity Shipped due to Stockout
SE*12*0003~
GE*1*3~
IEA*1*000000003~
"""
    return edi_856.strip()

# Generate EDI 810 (Invoice)
def generate_edi_810(buyer, seller, po_number, product1, product2, base_date):
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    #date, time, base_date = generate_timestamp(base_date, time_offset_days=3, time_offset_hours=5)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)
    edi_810 = f"""
ISA*00*          *00*          *ZZ*{seller}      *ZZ*{buyer}         *{date}*{time}*U*00401*000000004*0*T*:~
GS*IN*{seller}*{buyer}*{date}*{time}*4*X*004010~
ST*810*0004~
BIG*{date}*INV567890*{po_number}~
N1*BY*{buyer}*92*123456~
N1*SE*{seller}*92*654321~
IT1*1*100*EA*20.00**BP*{product1}~
IT1*2*0*EA*15.00**BP*{product2}*BO~  // {product2} Backordered
TDS*2000~  // Total Amount: $3295
SE*10*0004~
GE*1*4~
IEA*1*000000004~
"""
    return edi_810.strip()

# Generate EDI 846 (Inventory Inquiry/Advice)
def generate_edi_846(buyer, seller, po_number, product1, product2, base_date):
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    #date, time, base_date = generate_timestamp(base_date, time_offset_days=4, time_offset_hours=10)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)
    edi_846 = f"""
ISA*00*          *00*          *ZZ*{seller}      *ZZ*{buyer}         *{date}*{time}*U*00401*000000005*0*T*:~
GS*IB*{seller}*{buyer}*{date}*{time}*5*X*004010~
ST*846*0005~
BIA*00*IB*{date}~
N1*SE*{seller}*92*654321~
LIN**BP*{product1}~
QTY*33*500~  // Available Quantity: {item1_qty} units
LIN**BP*{product2}~
QTY*33*0~  // Available Quantity: {item2_qty} units (Out of Stock)
SE*7*0005~
GE*1*5~
IEA*1*000000005~
REF*BM*{po_number}~
"""
    return edi_846.strip()


##############################################
# Main function to generate all EDI transactions
##############################################

def generate_edi_transactions():
    buyer = random.choice(buyers)
    seller = random.choice(sellers)
    product1 = random.choice(products)
    product2 = random.choice(products)
    po_number = f"PO{random.randint(100000, 999999)}"

    while product1 == product2:
        product2 = random.choice(products)

    days_ago = random.choice(days_agos)
    base_date = datetime.now() - timedelta(days=days_ago)

    print(generate_edi_850(buyer, seller, po_number, product1, product2, base_date))
    print("DESC*EDI_850_Purchase_Order\n\n")

    print(generate_edi_855(buyer, seller, po_number, product1, product2, base_date))
    print("DESC*EDI_855_Purchase_Order_Acknowledgment\n\n")

    print(generate_edi_856(buyer, seller, po_number, product1, product2, base_date))
    print("DESC*EDI_856_Advance_Ship_Notice\n\n")

    print(generate_edi_810(buyer, seller, po_number, product1, product2, base_date))
    print("DESC*EDI_810_Invoice\n\n")

    print(generate_edi_846(buyer, seller, po_number, product1, product2, base_date))
    print("DESC*EDI_846_Inventory_Inquiry_Advice\n\n")

# Generate the EDI transactions
generate_edi_transactions()

