#!/usr/bin/python3

import random
import datetime

# Function to generate random EDI timestamps
def generate_timestamp():
    now = datetime.datetime.now()
    return now.strftime('%y%m%d'), now.strftime('%H%M')

# Function to generate random EDI events for different documents
def generate_edi_850(buyer, seller, po_number):
    date, time = generate_timestamp()
    #item1_qty = random.randint(50, 150)
    #item2_qty = random.randint(25, 100)
    edi_850 = f"""ISA*00*          *00*          *ZZ*{buyer}         *ZZ*{seller}      *{date}*{time}*U*00401*000000001*0*T*:~
GS*PO*{buyer}*{seller}*{date}*{time}*1*X*004010~
ST*850*0001~
BEG*00*NE*{po_number}*{date}~
REF*ZZ*CONTRACT456~
N1*BY*{buyer}*92*123456~
N1*SE*{seller}*92*654321~
PO1*1*{item1_qty}*EA*20.00*PE*BP*ITEM100~  // Order {item1_qty} units of ITEM100
PO1*2*{item2_qty}*EA*15.00*PE*BP*ITEM200~  // Order {item2_qty} units of ITEM200
CTT*2~
SE*9*0001~
GE*1*1~
IEA*1*000000001~"""
    return edi_850

def generate_edi_855(buyer, seller, po_number, item1_qty, item2_qty):
    date, time = generate_timestamp()
    item1_status = "IA"  # Accepted
    item2_status = "BO"  # Backordered
    edi_855 = f"""ISA*00*          *00*          *ZZ*{seller}      *ZZ*{buyer}         *{date}*{time}*U*00401*000000002*0*T*:~
GS*PO*{seller}*{buyer}*{date}*{time}*2*X*004010~
ST*855*0002~
BAK*00*AD*{po_number}*{date}~
N1*BY*{buyer}*92*123456~
N1*SE*{seller}*92*654321~
PO1*1*{item1_qty}*EA*20.00*PE*BP*ITEM100*{item1_status}~  // Accepted: Full Quantity Available
PO1*2*{item2_qty}*EA*15.00*PE*BP*ITEM200*{item2_status}~  // Backordered: Not enough stock for ITEM200
SE*8*0002~
GE*1*2~
IEA*1*000000002~"""
    return edi_855

def generate_edi_856(buyer, seller, po_number, item1_qty, item2_qty):
    date, time = generate_timestamp()
    edi_856 = f"""ISA*00*          *00*          *ZZ*{seller}      *ZZ*{buyer}         *{date}*{time}*U*00401*000000003*0*T*:~
GS*SH*{seller}*{buyer}*{date}*{time}*3*X*004010~
ST*856*0003~
BSN*00*ASN123456*{date}*{time}~
HL*1**S~
TD1*CTN*2****G*500*LB~  // Total Weight: 500 lbs
TD5*B*2*UPSN*M~
REF*BM*{po_number}~
DTM*011*{date}~
HL*2*1*O~
LIN**BP*ITEM100~
SN1**{item1_qty}*EA~  // Full Quantity Shipped
HL*3*1*O~
LIN**BP*ITEM200~
SN1**0*EA~  // No Quantity Shipped due to Stockout
SE*12*0003~
GE*1*3~
IEA*1*000000003~"""
    return edi_856

def generate_edi_810(buyer, seller, po_number, total_amount, backordered):
    date, time = generate_timestamp()
    edi_810 = f"""ISA*00*          *00*          *ZZ*{seller}      *ZZ*{buyer}         *{date}*{time}*U*00401*000000004*0*T*:~
GS*IN*{seller}*{buyer}*{date}*{time}*4*X*004010~
ST*810*0004~
BIG*{date}*INV567890*{po_number}~
N1*BY*{buyer}*92*123456~
N1*SE*{seller}*92*654321~
IT1*1*{total_amount//20}*EA*20.00**BP*ITEM100~
IT1*2*0*EA*15.00**BP*ITEM200*{backordered}~  // ITEM200 Backordered
TDS*{total_amount}~  // Total Amount: ${total_amount}
SE*10*0004~
GE*1*4~
IEA*1*000000004~"""
    return edi_810

def generate_edi_846(buyer, seller, item1_stock, item2_stock):
    date, time = generate_timestamp()
    edi_846 = f"""ISA*00*          *00*          *ZZ*{seller}      *ZZ*{buyer}         *{date}*{time}*U*00401*000000005*0*T*:~
GS*IB*{seller}*{buyer}*{date}*{time}*5*X*004010~
ST*846*0005~
BIA*00*IB*{date}~
N1*SE*{seller}*92*654321~
LIN**BP*ITEM100~
QTY*33*{item1_stock}~  // Available Quantity: {item1_stock} units
LIN**BP*ITEM200~
QTY*33*{item2_stock}~  // Available Quantity: {item2_stock} units (Out of Stock)
SE*7*0005~
GE*1*5~
IEA*1*000000005~"""
    return edi_846

def event_break():
    event_breaker = "\r\n"
    return event_breaker


# Example Usage
buyers = ["BUYER1", "BUYER2", "BUYER3"]
sellers = ["SELLER1", "SELLER2", "SELLER3"]

for i in range(1):
    buyer = random.choice(buyers)
    seller = random.choice(sellers)
    po_number = f"PO{random.randint(100000, 999999)}"
    item1_qty = random.randint(50, 150)
    item2_qty = random.randint(25, 100)
    total_amount = item1_qty * 20 + item2_qty * 15

    print(generate_edi_850(buyer, seller, po_number))
    print("\r\n") 
    print(generate_edi_855(buyer, seller, po_number, item1_qty, item2_qty))
    print("\r\n") 
    print(generate_edi_856(buyer, seller, po_number, item1_qty, item2_qty))
    print("\r\n") 
    print(generate_edi_810(buyer, seller, po_number, total_amount, "BO"))
    print("\r\n") 
    print(generate_edi_846(buyer, seller, random.randint(0, 500), random.randint(0, 500)))
    print("\r\n") 
    #print("\n" + "="*80 + "\n")

