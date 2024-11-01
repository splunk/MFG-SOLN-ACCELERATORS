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
    {"code": "PROD-1006", "name": "Material A", "price": 29.99},
    {"code": "PROD-1007", "name": "Tool D", "price": 89.99},
    {"code": "PROD-1008", "name": "Part A", "price": 69.99},
    {"code": "PROD-1009", "name": "Paet B", "price": 49.99},
    {"code": "PROD-1010", "name": "Instrument D", "price": 39.99},
]

companies = [
    {"id": "ACME01", "name": "ACME Corporation"},
    {"id": "GLOBEX02", "name": "Globex Industries"},
    {"id": "INITECH03", "name": "Initech Systems"},
    {"id": "TRANS_QUAL", "name": "Trans Quality Enterprises"},
]

# IDoc generation helper functions
def generate_control_record(idoc_type, sender, receiver):
    current_time = datetime.now()
    return (
        f"EDI_DC40 {current_time.strftime('%Y%m%d%H%M%S')} "
        f"{sender['id'].ljust(10)} {receiver['id'].ljust(10)} "
        f"{idoc_type.ljust(30)} {current_time.strftime('%Y%m%d')} "
        f"{current_time.strftime('%H%M%S')} 740"
    )

def generate_data_record(segment, fields):
    return f"{segment.ljust(30)}{''.join(f'{field}'.ljust(45) for field in fields)}"

# Specific IDoc type generators
def generate_orders_idoc():
    sender = random.choice(companies)
    receiver = random.choice([c for c in companies if c != sender])
    product = random.choice(products)
    po_number = f"PO{random.randint(100000, 999999)}"
    quantity = random.randint(1, 1000)
    total_amount = round(quantity * product['price'], 2)

    idoc = [
        generate_control_record("ORDERS05", sender, receiver),
        generate_data_record("E1EDK01", [po_number, datetime.now().strftime('%Y%m%d')]),
        generate_data_record("E1EDK14", [total_amount, "USD"]),
        generate_data_record("E1EDP01", ["1", quantity, "EA", product['price']]),
        generate_data_record("E1EDP19", [product['code'], product['name']]),
    ]
    
    return "\n".join(idoc)

def generate_desadv_idoc():
    sender = random.choice(companies)
    receiver = random.choice([c for c in companies if c != sender])
    product = random.choice(products)
    shipment_id = f"SHP{random.randint(100000, 999999)}"
    quantity = random.randint(1, 1000)

    idoc = [
        generate_control_record("DESADV02", sender, receiver),
        generate_data_record("E1EDK01", [shipment_id, datetime.now().strftime('%Y%m%d')]),
        generate_data_record("E1EDK03", [f"PO{random.randint(100000, 999999)}", "001"]),
        generate_data_record("E1EDP01", ["1", quantity, "EA"]),
        generate_data_record("E1EDP19", [product['code'], product['name']]),
    ]
    
    return "\n".join(idoc)

def generate_invoic_idoc():
    sender = random.choice(companies)
    receiver = random.choice([c for c in companies if c != sender])
    product = random.choice(products)
    invoice_number = f"INV{random.randint(100000, 999999)}"
    quantity = random.randint(1, 1000)
    total_amount = round(quantity * product['price'], 2)

    idoc = [
        generate_control_record("INVOIC02", sender, receiver),
        generate_data_record("E1EDK01", [invoice_number, datetime.now().strftime('%Y%m%d')]),
        generate_data_record("E1EDK14", [total_amount, "USD"]),
        generate_data_record("E1EDP01", ["1", quantity, "EA", product['price']]),
        generate_data_record("E1EDP19", [product['code'], product['name']]),
    ]
    
    return "\n".join(idoc)

def generate_random_idoc():
    generators = [generate_orders_idoc, generate_desadv_idoc, generate_invoic_idoc]
    return random.choice(generators)()

def generate_idoc_file(num_messages, filename):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename_with_timestamp = f"{os.path.splitext(filename)[0]}_{timestamp}{os.path.splitext(filename)[1]}"
    
    with open(filename_with_timestamp, 'w') as f:
        for _ in range(num_messages):
            message = generate_random_idoc()
            f.write(message + '\n\n')
    
    return filename_with_timestamp

def generate_realtime_events():
    try:
        while True:
            events_count = random.randint(2, 15)
            for _ in range(events_count):
                message = generate_random_idoc()
                #print(f"Generated SAP IDoc message at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:")
                print(message)
                print("\n")
                #print("\n" + "="*50 + "\n")
            time.sleep(1)  # Wait for 1 second before generating the next batch
    except KeyboardInterrupt:
        print("Event generation stopped.")

# Main execution
if __name__ == "__main__":
    print("Starting real-time SAP IDoc event generation. Press Ctrl+C to stop.")
    generate_realtime_events()
