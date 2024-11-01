#!/usr/bin/python3

import random
import time
from datetime import datetime, timedelta

# Sample entities
buyers = [
    {"id": "BUY_ACME", "name": "Acme Corp", "address": "123 Buyer St", "city": "BuyerCity", "state": "BC", "zip": "12345"},
    {"id": "BUY_BEYOND_IND", "name": "Beyond Industries", "address": "456 Purchase Ave", "city": "BuyerVille", "state": "BV", "zip": "67890"},
    {"id": "BUY_GAMMA_ENT", "name": "Gamma Enterprises", "address": "789 Order Ln", "city": "BuyerTown", "state": "BT", "zip": "13579"},
]

sellers = [
    {"id": "SEL_XRAY_ELEC", "name": "Xray Electronics", "address": "321 Seller Rd", "city": "SellerCity", "state": "SC", "zip": "54321"},
    {"id": "SEL_YANKEE_PARTS", "name": "Yankee Parts", "address": "654 Supply St", "city": "SellerVille", "state": "SV", "zip": "09876"},
    {"id": "SEL_ZULU_CHEM", "name": "Zulu Chemical", "address": "987 Vendor Ave", "city": "SellerTown", "state": "ST", "zip": "97531"},
]

carriers = ["FEDX", "UPSX", "DHLE"]

products = [
    {"code": "PROD-1001", "name": "Widget A", "price": 25.00},
    {"code": "PROD-1002", "name": "Gadget B", "price": 35.50},
    {"code": "PROD-1003", "name": "Tool C", "price": 45.75},
    {"code": "PROD-1004", "name": "Device D", "price": 55.25},
    {"code": "PROD-1005", "name": "Instrument E", "price": 65.00},
]

# Global counter for unique IDs
global_counter = 1

def generate_unique_id():
    global global_counter
    unique_id = f"{global_counter:09d}"
    global_counter += 1
    return unique_id

def generate_po_number():
    return f"PO{random.randint(1000000, 9999999)}"

def generate_invoice_number():
    return f"INV{random.randint(1000000, 9999999)}"

def generate_shipment_number():
    return f"SHP{random.randint(1000000, 9999999)}"

def generate_isa_segment(sender, receiver):
    current_time = datetime.now()
    return (
        f"ISA*00*          *00*          *ZZ*{sender['id'].ljust(15)}*"
        f"ZZ*{receiver['id'].ljust(15)}*{current_time.strftime('%y%m%d')}*"
        f"{current_time.strftime('%H%M')}*U*00401*{generate_unique_id()}*0*T*>~\n"
    )

def generate_gs_segment(func_id, sender, receiver):
    current_time = datetime.now()
    return (
        f"GS*{func_id}*{sender['id']}*{receiver['id']}*"
        f"{current_time.strftime('%Y%m%d')}*{current_time.strftime('%H%M')}*"
        f"{generate_unique_id()}*X*004010~\n"
    )

def generate_850_purchase_order(buyer, seller, po_number, product, quantity):
    isa = generate_isa_segment(buyer, seller)
    gs = generate_gs_segment("PO", buyer, seller)
    st = f"ST*850*{generate_unique_id()}~\n"
    beg = f"BEG*00*SA*{po_number}**{datetime.now().strftime('%Y%m%d')}~\n"
    ref = f"REF*DP*{random.randint(10000, 99999)}~\n"
    n1_by = f"N1*BY*{buyer['name']}*92*{buyer['id']}~\n"
    n3_by = f"N3*{buyer['address']}~\n"
    n4_by = f"N4*{buyer['city']}*{buyer['state']}*{buyer['zip']}~\n"
    n1_se = f"N1*SE*{seller['name']}*92*{seller['id']}~\n"
    n3_se = f"N3*{seller['address']}~\n"
    n4_se = f"N4*{seller['city']}*{seller['state']}*{seller['zip']}~\n"
    po1 = f"PO1*001*{quantity}*EA*{product['price']}**VP*{product['code']}~\n"
    pid = f"PID*F****{product['name']}~\n"
    ctt = f"CTT*1*{quantity}~\n"
    se = f"SE*{14}*{st.split('*')[2][:-2]}~\n"
    ge = f"GE*1*{gs.split('*')[6]}~\n"
    iea = f"IEA*1*{isa.split('*')[13]}~\n"

    return isa + gs + st + beg + ref + n1_by + n3_by + n4_by + n1_se + n3_se + n4_se + po1 + pid + ctt + se + ge + iea

def generate_855_po_acknowledgment(seller, buyer, po_number):
    isa = generate_isa_segment(seller, buyer)
    gs = generate_gs_segment("PR", seller, buyer)
    st = f"ST*855*{generate_unique_id()}~\n"
    bak = f"BAK*00*AC*{po_number}*{datetime.now().strftime('%Y%m%d')}~\n"
    n1_by = f"N1*BY*{buyer['name']}*92*{buyer['id']}~\n"
    n1_se = f"N1*SE*{seller['name']}*92*{seller['id']}~\n"
    se = f"SE*{6}*{st.split('*')[2][:-2]}~\n"
    ge = f"GE*1*{gs.split('*')[6]}~\n"
    iea = f"IEA*1*{isa.split('*')[13]}~\n"

    return isa + gs + st + bak + n1_by + n1_se + se + ge + iea

def generate_856_advance_ship_notice(seller, buyer, po_number, shipment_number, product, quantity):
    isa = generate_isa_segment(seller, buyer)
    gs = generate_gs_segment("SH", seller, buyer)
    st = f"ST*856*{generate_unique_id()}~\n"
    bsn = f"BSN*00*{shipment_number}*{datetime.now().strftime('%Y%m%d')}*{datetime.now().strftime('%H%M')}~\n"
    hl_s = "HL*1**S~\n"
    hl_o = "HL*2*1*O~\n"
    prf = f"PRF*{po_number}~\n"
    hl_i = "HL*3*2*I~\n"
    lin = f"LIN**VP*{product['code']}~\n"
    sn1 = f"SN1**{quantity}*EA~\n"
    se = f"SE*{10}*{st.split('*')[2][:-2]}~\n"
    ge = f"GE*1*{gs.split('*')[6]}~\n"
    iea = f"IEA*1*{isa.split('*')[13]}~\n"

    return isa + gs + st + bsn + hl_s + hl_o + prf + hl_i + lin + sn1 + se + ge + iea

def generate_810_invoice(seller, buyer, po_number, invoice_number, product, quantity):
    isa = generate_isa_segment(seller, buyer)
    gs = generate_gs_segment("IN", seller, buyer)
    st = f"ST*810*{generate_unique_id()}~\n"
    big = f"BIG*{datetime.now().strftime('%Y%m%d')}*{invoice_number}*{po_number}*{(datetime.now() + timedelta(days=30)).strftime('%Y%m%d')}~\n"
    n1_by = f"N1*BY*{buyer['name']}*92*{buyer['id']}~\n"
    n1_se = f"N1*SE*{seller['name']}*92*{seller['id']}~\n"
    it1 = f"IT1*001*{quantity}*EA*{product['price']}**VP*{product['code']}~\n"
    pid = f"PID*F****{product['name']}~\n"
    tds = f"TDS*{quantity * product['price']}~\n"
    se = f"SE*{9}*{st.split('*')[2][:-2]}~\n"
    ge = f"GE*1*{gs.split('*')[6]}~\n"
    iea = f"IEA*1*{isa.split('*')[13]}~\n"

    return isa + gs + st + big + n1_by + n1_se + it1 + pid + tds + se + ge + iea

def generate_820_payment_order(buyer, seller, invoice_number, amount):
    isa = generate_isa_segment(buyer, seller)
    gs = generate_gs_segment("RA", buyer, seller)
    st = f"ST*820*{generate_unique_id()}~\n"
    bpr = f"BPR*C*{amount}*C*ACH*CTX*01*{random.randint(100000000, 999999999)}*DA*{random.randint(100000000, 999999999)}*{random.randint(100000000, 999999999)}*{datetime.now().strftime('%Y%m%d')}~\n"
    trn = f"TRN*1*PAY{random.randint(100000000, 999999999)}~\n"
    ref = f"REF*IV*{invoice_number}~\n"
    n1_se = f"N1*SE*{seller['name']}*92*{seller['id']}~\n"
    se = f"SE*{7}*{st.split('*')[2][:-2]}~\n"
    ge = f"GE*1*{gs.split('*')[6]}~\n"
    iea = f"IEA*1*{isa.split('*')[13]}~\n"

    return isa + gs + st + bpr + trn + ref + n1_se + se + ge + iea

def simulate_order_to_cash_cycle():
    buyer = random.choice(buyers)
    seller = random.choice(sellers)
    product = random.choice(products)
    quantity = random.randint(10, 1000)
    po_number = generate_po_number()
    shipment_number = generate_shipment_number()
    invoice_number = generate_invoice_number()
    total_amount = quantity * product['price']

    # Purchase Order
    print(generate_850_purchase_order(buyer, seller, po_number, product, quantity))
    time.sleep(random.uniform(1, 5))

    # PO Acknowledgment
    print(generate_855_po_acknowledgment(seller, buyer, po_number))
    time.sleep(random.uniform(2, 8))

    # Advance Ship Notice
    print(generate_856_advance_ship_notice(seller, buyer, po_number, shipment_number, product, quantity))
    time.sleep(random.uniform(3, 10))

    # Invoice
    print(generate_810_invoice(seller, buyer, po_number, invoice_number, product, quantity))
    time.sleep(random.uniform(5, 15))

    # Payment Order
    print(generate_820_payment_order(buyer, seller, invoice_number, total_amount))
    time.sleep(random.uniform(10, 20))

def main():
    print("Starting EDI X12 Order-to-Cash Cycle Simulation. Press Ctrl+C to stop.")
    try:
        while True:
            simulate_order_to_cash_cycle()
    except KeyboardInterrupt:
        print("\nSimulation stopped.")

if __name__ == "__main__":
    main()
