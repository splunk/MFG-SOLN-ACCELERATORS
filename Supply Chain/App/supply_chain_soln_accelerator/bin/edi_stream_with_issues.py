#!/usr/bin/python3

import random
import time
from datetime import datetime, timedelta

def generate_isa_header(sender, receiver, control_number):
    now = datetime.now()
    return f"ISA*00*          *00*          *ZZ*{sender:<15}*ZZ*{receiver:<15}*{now:%y%m%d}*{now:%H%M}*U*00401*{control_number:09d}*0*T*:~"

def generate_gs_header(func_id, sender, receiver, control_number):
    now = datetime.now()
    return f"GS*{func_id}*{sender}*{receiver}*{now:%Y%m%d}*{now:%H%M}*{control_number}*X*004010~"

def generate_gs_trailer(control_number):
    return f"GE*1*{control_number}~"

def generate_isa_trailer(control_number):
    return f"IEA*1*{control_number:09d}~"

def generate_po(order_number, buyer, seller, product, quantity, price):
    now = datetime.now()
    delivery_date = now + timedelta(days=random.randint(5, 15))
    return f"""ST*850*{order_number:04d}~
BEG*00*NE*{order_number}*{now:%Y%m%d}~
REF*DP*{random.randint(1000, 9999)}~
DTM*002*{delivery_date:%Y%m%d}~
N1*BY*{buyer}*92*{random.randint(1000000000, 9999999999)}~
PO1*1*{quantity}*EA*{price:.2f}*PE*BP*{product}~
CTT*1~
SE*8*{order_number:04d}~"""

def generate_po_ack(order_number, seller, buyer, product, quantity, price):
    now = datetime.now()
    ship_date = now + timedelta(days=random.randint(3, 10))
    return f"""ST*855*{order_number:04d}~
BAK*00*AC*{order_number}*{now:%Y%m%d}~
PO1*1*{quantity}*EA*{price:.2f}*BP*{product}~
DTM*068*{ship_date:%Y%m%d}~
N1*ST*{buyer}*92*{random.randint(1000000000, 9999999999)}~
SE*6*{order_number:04d}~"""

#def generate_asn(order_number, seller, buyer, product, quantity, price):
#    now = datetime.now()
#    errors = random.choices(['None', 'WrongQuantity', 'Damaged'], weights=[70, 15, 15])[0]
#    actual_quantity = quantity if errors == 'None' else random.randint(1, quantity-1)
#    damaged_quantity = random.randint(1, actual_quantity) if errors == 'Damaged' else 0
#    return f"""ST*856*{order_number:04d}~
#BSN*00*{order_number}*{now:%Y%m%d}*{now:%H%M}~
#DTM*011*{now:%Y%m%d}~
#HL*1**S~
#TD1*CTN*{max(1, actual_quantity // 50)}****G*{actual_quantity * price:.2f}~
#REF*BM*{random.randint(100000000, 999999999)}~
#HL*2*1*O~
#LIN**BP*{product}~
#SN1**{actual_quantity}*EA~
#PID*F****Product Description~
#{"HL*3*2*I~\nLIN**BP*{product}~\nSN1**{damaged_quantity}*EA*ZZ*Damaged~" if damaged_quantity > 0 else ""}SE*{11 if damaged_quantity > 0 else 9}*{order_number:04d}~"""


def generate_asn(order_number, seller, buyer, product, quantity, price):
    now = datetime.now()
    errors = random.choices(['None', 'WrongQuantity', 'Damaged'], weights=[70, 15, 15])[0]
    actual_quantity = quantity if errors == 'None' else random.randint(1, quantity-1)
    damaged_quantity = random.randint(1, actual_quantity) if errors == 'Damaged' else 0
    damaged_line = f"HL*3*2*I~\nLIN**BP*{product}~\nSN1**{damaged_quantity}*EA*ZZ*Damaged~" if damaged_quantity > 0 else ""
    se_count = 11 if damaged_quantity > 0 else 9
    return f"""ST*856*{order_number:04d}~
BSN*00*{order_number}*{now:%Y%m%d}*{now:%H%M}~
DTM*011*{now:%Y%m%d}~
HL*1**S~
TD1*CTN*{max(1, actual_quantity // 50)}****G*{actual_quantity * price:.2f}~
REF*BM*{random.randint(100000000, 999999999)}~
HL*2*1*O~
LIN**BP*{product}~
SN1**{actual_quantity}*EA~
PID*F****Product Description~
{damaged_line}SE*{se_count}*{order_number:04d}~"""


def generate_invoice(order_number, seller, buyer, product, quantity, price):
    now = datetime.now()
    return f"""ST*810*{order_number:04d}~
BIG*{now:%Y%m%d}*{random.randint(100000000, 999999999)}*{order_number}~
REF*DP*{random.randint(1000, 9999)}~
N1*BY*{buyer}*92*{random.randint(1000000000, 9999999999)}~
IT1**{quantity}*EA*{price:.2f}*BP*{product}~
TDS*{quantity * price:.2f}~
SE*7*{order_number:04d}~"""

def generate_transaction():
    buyers = ["ACME_CORP", "GLOBEX_INC", "UMBRELLA_CO", "STARK_IND", "WAYNE_TECH"]
    sellers = ["SUPPLIER_A", "SUPPLIER_B", "SUPPLIER_C", "SUPPLIER_D", "SUPPLIER_E"]
    products = ["WIDGET_X", "GADGET_Y", "DOOHICKEY_Z", "THINGAMAJIG_W", "GIZMO_V"]
    
    buyer = random.choice(buyers)
    seller = random.choice(sellers)
    product = random.choice(products)
    quantity = random.randint(10, 100)
    price = round(random.uniform(10, 100), 2)
    
    order_number = random.randint(100000000, 999999999)
    control_number = random.randint(1, 999999999)
    
    po = (f"{generate_isa_header(buyer, seller, control_number)}\n"
          f"{generate_gs_header('PO', buyer, seller, control_number)}\n"
          f"{generate_po(order_number, buyer, seller, product, quantity, price)}\n"
          f"{generate_gs_trailer(control_number)}\n"
          f"{generate_isa_trailer(control_number)}\n"
          f"DESC*PO_INITIAL_WITH_DETAILS\n")
    
    yield po
    time.sleep(random.uniform(1, 5))
    
    control_number = random.randint(1, 999999999)
    po_ack = (f"{generate_isa_header(seller, buyer, control_number)}\n"
              f"{generate_gs_header('PR', seller, buyer, control_number)}\n"
              f"{generate_po_ack(order_number, seller, buyer, product, quantity, price)}\n"
              f"{generate_gs_trailer(control_number)}\n"
              f"{generate_isa_trailer(control_number)}\n"
              f"DESC*PO_ACK_ORDER_PROCESSING\n")
    
    yield po_ack
    time.sleep(random.uniform(1, 5))
    
    control_number = random.randint(1, 999999999)
    asn = (f"{generate_isa_header(seller, buyer, control_number)}\n"
           f"{generate_gs_header('SH', seller, buyer, control_number)}\n"
           f"{generate_asn(order_number, seller, buyer, product, quantity, price)}\n"
           f"{generate_gs_trailer(control_number)}\n"
           f"{generate_isa_trailer(control_number)}\n"
           f"DESC*ASN_INFORM_BUYER\n")
    
    yield asn
    time.sleep(random.uniform(1, 5))
    
    control_number = random.randint(1, 999999999)
    invoice = (f"{generate_isa_header(seller, buyer, control_number)}\n"
               f"{generate_gs_header('IN', seller, buyer, control_number)}\n"
               f"{generate_invoice(order_number, seller, buyer, product, quantity, price)}\n"
               f"{generate_gs_trailer(control_number)}\n"
               f"{generate_isa_trailer(control_number)}\n"
               f"DESC*INVOICE\n")
    
    yield invoice

def main():
    while True:
        for event in generate_transaction():
            print(event)
            #print("\n" + "="*50 + "\n")
        time.sleep(random.uniform(5, 15))

if __name__ == "__main__":
    main()
