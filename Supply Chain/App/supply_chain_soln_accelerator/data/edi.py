#!/usr/bin/python3

import random
from datetime import datetime, timedelta

def generate_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def generate_isa_segment():
    today = datetime.now().strftime("%y%m%d")
    time = datetime.now().strftime("%H%M")
    return f"ISA*00*          *00*          *ZZ*ACME           *ZZ*SUPPLIER       *{today}*{time}*U*00401*000000001*0*P*>"

def generate_gs_segment(functional_id_code):
    today = datetime.now().strftime("%Y%m%d")
    time = datetime.now().strftime("%H%M")
    return f"GS*{functional_id_code}*ACME*SUPPLIER*{today}*{time}*1*X*004010"

def generate_st_segment(transaction_set_id, transaction_set_control_number):
    return f"ST*{transaction_set_id}*{transaction_set_control_number:04d}"

def generate_se_segment(segment_count, transaction_set_control_number):
    return f"SE*{segment_count}*{transaction_set_control_number:04d}"

def generate_ge_iea_segments():
    return "GE*1*1\nIEA*1*000000001"

# 850 Purchase Order
def generate_850_po():
    po_number = f"PO{random.randint(100000, 999999)}"
    date = (datetime.now() + timedelta(days=random.randint(1, 30))).strftime("%Y%m%d")
    quantity = random.randint(1, 1000)
    unit_price = round(random.uniform(10, 1000), 2)
    product_code = f"PROD-{random.randint(1000, 9999)}"
    total_amount = quantity * unit_price

    return [
        f"BEG*00*NE*{po_number}**{date}",
        f"PO1*1*{quantity}*EA*{unit_price}**BP*{product_code}",
        f"CTT*1",
        f"AMT*TT*{total_amount:.2f}"
    ]

# 856 Advance Ship Notice
def generate_856_asn():
    shipment_id = f"SHP{random.randint(100000, 999999)}"
    date = datetime.now().strftime("%Y%m%d")
    quantity = random.randint(1, 1000)
    product_code = f"PROD-{random.randint(1000, 9999)}"

    return [
        f"BSN*00*{shipment_id}*{date}*{datetime.now().strftime('%H%M')}",
        f"DTM*011*{date}",
        f"HL*1**S",
        f"HL*2*1*O",
        f"HL*3*2*I",
        f"LIN**BP*{product_code}",
        f"SN1**{quantity}*EA"
    ]

# 810 Invoice
def generate_810_invoice():
    invoice_number = f"INV{random.randint(100000, 999999)}"
    date = datetime.now().strftime("%Y%m%d")
    amount = round(random.uniform(100, 10000), 2)

    return [
        f"BIG*{date}*{invoice_number}***",
        f"CUR*SE*USD",
        f"IT1*1**{amount}**EA",
        f"TDS*{amount}"
    ]

# 846 Inventory Inquiry/Advice
def generate_846_inventory():
    date = datetime.now().strftime("%Y%m%d")
    product_code = f"PROD-{random.randint(1000, 9999)}"
    quantity = random.randint(1, 10000)

    return [
        f"BIA*00*{date}*",
        f"LIN*1*BP*{product_code}",
        f"QTY*33*{quantity}"
    ]

def generate_edi_message(scenario):
    transaction_set_control_number = random.randint(1, 9999)
    
    if scenario == "new_order":
        transaction_set_id = "850"
        functional_id_code = "PO"
        transaction_segments = generate_850_po()
    elif scenario == "shipment":
        transaction_set_id = "856"
        functional_id_code = "SH"
        transaction_segments = generate_856_asn()
    elif scenario == "invoice":
        transaction_set_id = "810"
        functional_id_code = "IN"
        transaction_segments = generate_810_invoice()
    elif scenario == "inventory_update":
        transaction_set_id = "846"
        functional_id_code = "IB"
        transaction_segments = generate_846_inventory()
    
    message = [
        generate_isa_segment(),
        generate_gs_segment(functional_id_code),
        generate_st_segment(transaction_set_id, transaction_set_control_number)
    ]
    
    message.extend(transaction_segments)
    
    message.extend([
        generate_se_segment(len(message) + 1, transaction_set_control_number),
        generate_ge_iea_segments()
    ])
    
    return "~\n".join(message) + "~"

def generate_realistic_scenario():
    scenarios = [
        ("new_order", 35),
        ("shipment", 30),
        ("invoice", 25),
        ("inventory_update", 10)
    ]
    return random.choices([s[0] for s in scenarios], weights=[s[1] for s in scenarios])[0]

def generate_edi_file(num_messages, filename):
    with open(filename, 'w') as f:
        for _ in range(num_messages):
            scenario = generate_realistic_scenario()
            message = generate_edi_message(scenario)
            f.write(message + '\n\n')

# Generate 10,000 EDI messages with a timestamped filename
timestamp = generate_timestamp()
filename = f'edi_messages_{timestamp}.edi'
generate_edi_file(10000, filename)

print(f"EDI file '{filename}' generated successfully with realistic business scenarios.")

