#!/usr/bin/python3

import random
import time
from datetime import datetime, timedelta
import os

# Global variables for more realistic scenarios
products = [
    {"code": "PROD-1001", "name": "Widget A", "price": 19.99},
    {"code": "PROD-1002", "name": "Gadget B", "price": 29.99},
    {"code": "PROD-1003", "name": "Tool C", "price": 39.99},
    {"code": "PROD-1004", "name": "Device D", "price": 49.99},
    {"code": "PROD-1005", "name": "Instrument E", "price": 59.99},
]

companies = [
    {"id": "ACME01", "name": "ACME Corporation"},
    {"id": "GLOBEX02", "name": "Globex Industries"},
    {"id": "INITECH03", "name": "Initech Systems"},
]

# EDI message generation functions
def generate_isa_segment(sender, receiver):
    today = datetime.now().strftime("%y%m%d")
    time = datetime.now().strftime("%H%M")
    return f"ISA*00*          *00*          *ZZ*{sender.ljust(15)}*ZZ*{receiver.ljust(15)}*{today}*{time}*U*00401*000000001*0*P*>"

def generate_gs_segment(transaction_type, sender, receiver):
    today = datetime.now().strftime("%Y%m%d")
    time = datetime.now().strftime("%H%M")
    return f"GS*{transaction_type}*{sender}*{receiver}*{today}*{time}*1*X*004010"

def generate_st_segment(transaction_set, transaction_set_control_number):
    return f"ST*{transaction_set}*{transaction_set_control_number:04d}"

def generate_se_segment(segment_count, transaction_set_control_number):
    return f"SE*{segment_count}*{transaction_set_control_number:04d}"

def generate_ge_iea_segments():
    return "GE*1*1\nIEA*1*000000001"

# Specific transaction set generators
def generate_850_po():
    sender = random.choice(companies)
    receiver = random.choice([c for c in companies if c != sender])
    product = random.choice(products)
    po_number = f"PO{random.randint(100000, 999999)}"
    quantity = random.randint(1, 1000)
    total_amount = round(quantity * product['price'], 2)

    message = [
        generate_isa_segment(sender['id'], receiver['id']),
        generate_gs_segment("PO", sender['id'], receiver['id']),
        generate_st_segment("850", random.randint(1, 9999)),
        f"BEG*00*NE*{po_number}**{datetime.now().strftime('%Y%m%d')}",
        f"PO1*1*{quantity}*EA*{product['price']}**BP*{product['code']}",
        f"CTT*1",
        f"AMT*TT*{total_amount:.2f}",
    ]
    
    message.extend([
        generate_se_segment(len(message) - 2, int(message[2].split('*')[2])),
        generate_ge_iea_segments()
    ])
    
    return "~\n".join(message) + "~"

def generate_856_asn():
    sender = random.choice(companies)
    receiver = random.choice([c for c in companies if c != sender])
    product = random.choice(products)
    shipment_id = f"SHP{random.randint(100000, 999999)}"
    quantity = random.randint(1, 1000)

    message = [
        generate_isa_segment(sender['id'], receiver['id']),
        generate_gs_segment("SH", sender['id'], receiver['id']),
        generate_st_segment("856", random.randint(1, 9999)),
        f"BSN*00*{shipment_id}*{datetime.now().strftime('%Y%m%d')}*{datetime.now().strftime('%H%M')}",
        f"DTM*011*{datetime.now().strftime('%Y%m%d')}",
        "HL*1**S",
        "HL*2*1*O",
        f"PRF*PO{random.randint(100000, 999999)}",
        "HL*3*2*I",
        f"LIN**BP*{product['code']}",
        f"SN1**{quantity}*EA",
    ]
    
    message.extend([
        generate_se_segment(len(message) - 2, int(message[2].split('*')[2])),
        generate_ge_iea_segments()
    ])
    
    return "~\n".join(message) + "~"

def generate_810_invoice():
    sender = random.choice(companies)
    receiver = random.choice([c for c in companies if c != sender])
    product = random.choice(products)
    invoice_number = f"INV{random.randint(100000, 999999)}"
    quantity = random.randint(1, 1000)
    total_amount = round(quantity * product['price'], 2)

    message = [
        generate_isa_segment(sender['id'], receiver['id']),
        generate_gs_segment("IN", sender['id'], receiver['id']),
        generate_st_segment("810", random.randint(1, 9999)),
        f"BIG*{datetime.now().strftime('%Y%m%d')}*{invoice_number}*{(datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y%m%d')}",
        f"N1*ST*{receiver['name']}",
        f"IT1*1*{quantity}*EA*{product['price']}**BP*{product['code']}",
        f"TDS*{total_amount:.2f}",
    ]
    
    message.extend([
        generate_se_segment(len(message) - 2, int(message[2].split('*')[2])),
        generate_ge_iea_segments()
    ])
    
    return "~\n".join(message) + "~"

def generate_random_edi_message():
    generators = [generate_850_po, generate_856_asn, generate_810_invoice]
    return random.choice(generators)()

def generate_edi_file(num_messages, filename):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename_with_timestamp = f"{os.path.splitext(filename)[0]}_{timestamp}{os.path.splitext(filename)[1]}"
    
    with open(filename_with_timestamp, 'w') as f:
        for _ in range(num_messages):
            message = generate_random_edi_message()
            f.write(message + '\n\n')
    
    return filename_with_timestamp

def generate_realtime_events():
    try:
        while True:
            events_count = random.randint(2, 15)
            for _ in range(events_count):
                message = generate_random_edi_message()
                #print(f"Generated EDI message at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:")
                print(message)
                print(" ")
                #print("\n" + "="*50 + "\n")
            time.sleep(1)  # Wait for 1 second before generating the next batch
    except KeyboardInterrupt:
        print("Event generation stopped.")

# Main execution
if __name__ == "__main__":
    print("Starting real-time EDI event generation. Press Ctrl+C to stop.")
    generate_realtime_events()
