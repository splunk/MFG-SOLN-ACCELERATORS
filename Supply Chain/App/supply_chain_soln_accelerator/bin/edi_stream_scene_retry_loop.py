#!/usr/bin/python3

import random
from datetime import datetime, timedelta

# Transaction Notes
# EDI 850 (Purchase Order): Represents the initial order placed by the customer.
# EDI 855 (Purchase Order Acknowledgment): Confirms receipt and acceptance of the order by the supplier.
# EDI 830 (Planning Schedule with Release Capability): Communicates production plans and schedule forecasts.
# EDI 856 (Advance Ship Notice/Manifest): Details the shipment, including contents, quantities, and shipping dates.
# EDI 810 (Invoice): Represents the invoice sent after shipment.
# EDI 214 (Transportation Carrier Shipment Status Message): Provides updates on the shipment status.
# EDI 862 (Shipping Schedule): Communicates detailed shipping requirements.
# EDI 940 (Warehouse Shipping Order): Directs a warehouse to ship an order.
# EDI 945 (Warehouse Shipping Advice): Confirms the shipment of goods from the warehouse.
# EDI 947 (Warehouse Inventory Adjustment Advice): Communicates inventory adjustments.
# EDI 861 (Receiving Advice/Acceptance Certificate): Confirms receipt of goods and reports discrepancies, damages, or errors.
# EDI 824 (Application Advice): Reports any errors or discrepancies found in the transactions.

# Generate random BUYER and SELLER
buyers = ['VoltStream_Energy', 'QuantumGrid_Utilities', 'PowerWave_Electric', 'BrightVolt_Energy_Solutions', 'FluxNation_Power', 'CircuitFlow_Utilities', 'ElectraCore_Power_Co', 'SparkGrid_Electric', 'NexGen_Energy_Systems', 'BlueVolt_Utilities_Corporation']
sellers = ['QUANTUMLINE']
carriers = ['GLOBAL_TRANPORT', 'TRANS_DN', 'UP_EX' ]
warehouses = ['WAREHOUSE_EAST', 'WAREHOUSE_WEST', 'WAREHOUSE_EU', 'WAREHOUSE_APAC' ]
products = ['QUANTUM_CHARGE_100', 'QUANTUM_CHARGE_200', 'QUANTUM_CHARGE_300', 'QUANTUM_GEN_01', 'QUANTUM_GEN_SP', 'QUANTUM_GEN_XL','QUANTUM_VIEW_MOL', 'QUANTUM_PEAK_1000', 'QUANTUM_PEAK_2000', 'QUANTUM_GPD_30', 'QUANTUM_GPD_40', 'QUANTUM_GPD_50']

# Generate Time realted values
time_offset_days = [1, 2, 3, 4, 5, 6]
time_offset_hrs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
po_number = f"PO{random.randint(100000, 500000)}"
trans_id = f"TR{random.randint(1000001, 1999999)}"
shipment_id = f"SN{random.randint(10000001, 19999999)}"
random_discrepancy = f"{random.randint(1, 9)}"
random_ack_error = f"{random.randint(1, 10)}"

## Inventory Quantity
item1_qty_inv_temp = random.randint(500, 800)
item2_qty_inv_temp = random.randint(800, 1500)
item1_qty_inv = round(item1_qty_inv_temp / 10) * 10
item2_qty_inv = round(item2_qty_inv_temp / 10) * 10

## Order Quantity
item1_qty = random.randint(5, 50)
item2_qty = random.randint(5, 150)
item1_temp = random.randint(500, 5000)
item2_temp = random.randint(300, 1500)
item1_price = round(item1_temp / 10) * 10
item2_price = round(item2_temp / 10) * 10
total_amount = item1_qty * item1_price + item2_qty * item2_price
total_weight = item1_qty * 15 + item2_qty * 20

# Generate dynamic timestamps
def generate_timestamp(base_date, time_offset_days=0, time_offset_hours=0):
    time_offset_days=random.randint(1, 3)
    time_offset_hours=random.randint(1, 12)
    dt = base_date + timedelta(days=time_offset_days, hours=time_offset_hours)
    base_date = dt
    #print(">>>>>> base_date=",base_date)
    #print("base_date_new=",base_date_new)
    return dt.strftime("%Y%m%d"), dt.strftime("%H%M"), base_date

# Generate dynamic timestamps - Forecast
def generate_timestamp_fcast(base_date, time_offset_days=0):
    day_fast_add = random.randint(3, 15)
    dt_fcast = base_date + timedelta(days=time_offset_days+day_fast_add)
    return dt_fcast.strftime("%Y%m%d")

# Random ACK Error Flag
def get_random_ack_status():
    random_ack_status = random.randint(1, 50)
    if random_ack_status == 2 :
        ack_status = "E"
        ack_status_desc = "Error"
    elif random_ack_status == 1 :
        ack_status = "R"
        ack_status_desc = "Rejected"
    else:
        ack_status = "A"
        ack_status_desc = "Accepted"

    return ack_status , ack_status_desc

# ========================================================================
# Generate EDI 850 (Purchase Order) : Represents the initial order placed by the customer
# ========================================================================
def generate_edi_850(buyer, seller, po_number, product1, product2, base_date):
    date, time, base_date = generate_timestamp(base_date)

    random_ack_time_sec = random.randint(20, 500)
    dt_997 = base_date + timedelta(seconds=random_ack_time_sec)
    time_997 = dt_997.strftime("%H%M")
    ack_status , ack_status_desc = get_random_ack_status()

    edi_850 = f"""
ISA|00|          |00|          |ZZ|{buyer}         |ZZ|{seller}      |{date}|{time}|U|{trans_id}|000000001|0|T|:~
GS|PO|{buyer}|{seller}|{date}|{time}|1|X|{trans_id}~
ST|850|0001~
BEG|00|NE|{po_number}|{date}~
REF|ZZ|{po_number}~
N1|BY|{buyer}|92|123456~
N1|SE|{seller}|92|654321~
PO1|1|{item1_qty}|EA|{item1_price}|PE|BP|{product1}~  // Order {item1_qty} units of {product1}
PO1|2|{item2_qty}|EA|{item2_price}|PE|BP|{product2}~  // Order {item2_qty} units of {product2}
CTT|2~
SE|9|0001~
GE|1|1~
IEA|1|000000001~
DESC|EDI_850_Purchase_Order


ISA|00|          |00|          |ZZ|{seller}         |ZZ|{buyer}      |{date}|{time_997}|U|{trans_id}|000000001|0|T|:~
GS|FA|{seller}|{buyer}|{date}|{time_997}|1|X|{trans_id}~
ST|997|0001~
AK1|PO|{po_number}~   // Acknowledging EDI 850 (Purchase Order)
AK2|850|0001~
AK5|{ack_status}~           // Status: {ack_status_desc}
AK9|{ack_status}|1|1|1~
SE|6|0001~
GE|1|21~
IEA|1|000000021~

"""
    return edi_850.strip(), base_date

# ========================================================================
# Generate EDI 855 (Purchase Order Acknowledgment) : Confirms receipt and acceptance of the order by the supplier.
# ========================================================================
def generate_edi_855(buyer, seller, po_number, product1, product2, base_date):
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)

    random_ack_time_sec = random.randint(20, 500)
    dt_997 = base_date + timedelta(seconds=random_ack_time_sec)
    time_997 = dt_997.strftime("%H%M")
    ack_status , ack_status_desc = get_random_ack_status()

    edi_855 = f"""
ISA|00|          |00|          |ZZ|{seller}      |ZZ|{buyer}         |{date}|{time}|U|{trans_id}|000000002|0|T|:~
GS|PO|{seller}|{buyer}|{date}|{time}|2|X|{trans_id}~
ST|855|0002~
BAK|00|AD|{po_number}|{date}~
N1|BY|{buyer}|92|123456~
N1|SE|{seller}|92|654321~
PO1|1|{item1_qty}|EA|{item1_price}|PE|BP|{product1}|IA~  // Accepted: Full Quantity Available
PO1|2|{item2_qty}|EA|{item2_price}|PE|BP|{product2}|BO~  // Accepted: Full Quantity Available
SE|8|0002~
GE|1|2~
IEA|1|000000002~
DESC|EDI_855_Purchase_Order_Acknowledgment


ISA|00|          |00|          |ZZ|{buyer}         |ZZ|{seller}      |{date}|{time_997}|U|{trans_id}|000000001|0|T|:~
GS|FA|{seller}|{buyer}|{date}|{time_997}|1|X|{trans_id}~
ST|997|0001~
AK1|PO|{po_number}~   // Acknowledging EDI 855 (Purchase Order Ack)
AK2|855|0001~
AK5|{ack_status}~           // Status: {ack_status_desc}
AK9|{ack_status}|1|1|1~
SE|8|0002~
GE|1|2~
IEA|1|000000002~

"""
    return edi_855.strip(), base_date


# ========================================================================
# Generate EDI 830 (Planning Schedule with Release Capability): Communicates production plans and schedule forecast
# ========================================================================
def generate_edi_830(buyer, seller, po_number, product1, product2, base_date):
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)

    time_offset_day = random.choice(time_offset_days)
    date_fcast = generate_timestamp_fcast(base_date, time_offset_days=time_offset_day)

    random_ack_time_sec = random.randint(20, 500)
    dt_997 = base_date + timedelta(seconds=random_ack_time_sec)
    time_997 = dt_997.strftime("%H%M")
    ack_status , ack_status_desc = get_random_ack_status()

    edi_830 = f"""
ISA|00|          |00|          |ZZ|{seller}      |ZZ|{buyer}         |{date}|{time}|U|{trans_id}|000000002|0|T|:~
GS|PO|{seller}|{buyer}|{date}|{time}|2|X|{trans_id}~
ST|830|0002~
BFR|00|DL|12345|{date_fcast}|{date_fcast}~
N1|BY|CUSTOMER|92|123456~
LIN||BP|{product1}~
UIT|EA|{item1_qty}~
FST|500|C|20230807~
LIN||BP|{product2}~
UIT|EA|{item2_qty}~
FST|200|C|{date_fcast}~
SE|10|0003~
GE|1|3~
IEA|1*000000003~
DESC|EDI_830_Planning_Schedule_with_Release_Capability


ISA|00|          |00|          |ZZ|{buyer}         |ZZ|{seller}      |{date}|{time_997}|U|{trans_id}|000000001|0|T|:~
GS|FA|{seller}|{buyer}|{date}|{time_997}|1|X|{trans_id}~
ST|997|0001~
AK1|PO|{po_number}~   // Acknowledging EDI 830 (Planning Schedule with Release Capability)
AK2|830|0001~
AK5|{ack_status}~           // Status: {ack_status_desc}
AK9|{ack_status}|1|1|1~
SE|8|0002~
GE|1|2~
IEA|1|000000002~

"""
    return edi_830.strip(), base_date


# ========================================================================
# Generate EDI 856 (Advance Ship Notice)
# ========================================================================
def generate_edi_856(buyer, seller, po_number, product1, product2, base_date):
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    #date, time, base_date = generate_timestamp(base_date, time_offset_days=2, time_offset_hours=3)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)

    random_ack_time_sec = random.randint(20, 500)
    dt_997 = base_date + timedelta(seconds=random_ack_time_sec)
    time_997 = dt_997.strftime("%H%M")
    ack_status , ack_status_desc = get_random_ack_status()

    edi_856 = f"""
ISA|00|          |00|          |ZZ|{seller}      |ZZ|{buyer}         |{date}|{time}|U|{trans_id}|000000003|0|T|:~
GS|SH|{seller}|{buyer}|{date}|{time}|3|X|{trans_id}~
ST|856|0003~
BSN|00|ASN123456|{date}|{time}~
HL|1||S~
TD1|CTN|2||||G|{total_weight}|LB~  // Total Weight: {total_weight} lbs
TD5|B|2|UPSN|M~
REF|BM|{po_number}~
DTM|011|{date}~
HL|2|1|O~
LIN||BP|{product1}~
SN1||{item1_qty}|EA~  // Full Quantity Shipped for {product1}
HL|3|1|O~
LIN||BP|{product2}~
SN1||{item2_qty}|EA~  // Full Quantity Shipped for {product2}
SE|12|0003~
GE|1|3~
IEA|1|000000003~
DESC|EDI_856_Advance_Ship_Notice
"""

#ISA|00|          |00|          |ZZ|{buyer}         |ZZ|{seller}      |{date}|{time_997}|U|{trans_id}|000000001|0|T|:~
#GS|FA|{buyer}|{seller}|{date}|{time_997}|1|X|{trans_id}~
#ST|997|0001~
#AK1|PO|{po_number}~   // Acknowledging EDI 856 (Advance Ship Notice)
#AK2|856|0001~
#AK5|{ack_status}~           // Status: {ack_status_desc}
#AK9|{ack_status}|1|1|1~
#SE|8|0002~
#GE|1|2~
#IEA|1|000000002~
#
#"""
    return edi_856.strip(), base_date



# ========================================================================
# Generate EDI 856 - Retries (Advance Ship Notice)
# ========================================================================
def generate_edi_856_retry(buyer, seller, po_number, product1, product2, base_date):
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    #date, time, base_date = generate_timestamp(base_date, time_offset_days=2, time_offset_hours=3)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)

    random_ack_time_sec = random.randint(20, 500)
    dt_997 = base_date + timedelta(seconds=random_ack_time_sec)
    time_997 = dt_997.strftime("%H%M")
    ack_status , ack_status_desc = get_random_ack_status()

    edi_856_retry = f""" 
ISA|00|          |00|          |ZZ|{seller}      |ZZ|{buyer}         |{date}|{time}|U|{trans_id}|000000003|0|T|:~
GS|SH|{seller}|{buyer}|{date}|{time}|3|X|{trans_id}~
ST|856|0003~
BSN|00|ASN123456|{date}|{time}~
HL|1||S~
TD1|CTN|2||||G|{total_weight}|LB~  // Total Weight: {total_weight} lbs
TD5|B|2|UPSN|M~
REF|BM|{po_number}~
DTM|011|{date}~
HL|2|1|O~
LIN||BP|{product1}~
SN1||{item1_qty}|EA~  // Full Quantity Shipped for {product1}
HL|3|1|O~
LIN||BP|{product2}~
SN1||{item2_qty}|EA~  // Full Quantity Shipped for {product2}
SE|12|0003~
GE|1|3~
IEA|1|000000003~
DESC|EDI_856_Advance_Ship_Notice-retry
"""
    return edi_856_retry.strip(), base_date


# ========================================================================
# Generate EDI 810 (Invoice)
# ========================================================================
def generate_edi_810(buyer, seller, po_number, product1, product2, base_date):
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    #date, time, base_date = generate_timestamp(base_date, time_offset_days=3, time_offset_hours=5)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)

    random_ack_time_sec = random.randint(20, 500)
    dt_997 = base_date + timedelta(seconds=random_ack_time_sec)
    time_997 = dt_997.strftime("%H%M")
    ack_status , ack_status_desc = get_random_ack_status()

    edi_810 = f"""
ISA|00|          |00|          |ZZ|{seller}      |ZZ|{buyer}         |{date}|{time}|U|{trans_id}|000000004|0|T|:~
GS|IN|{seller}|{buyer}|{date}|{time}|4|X|{trans_id}~
ST|810|0004~
BIG|{date}|INV567890|{po_number}~
N1|BY|{buyer}|92|123456~
N1|SE|{seller}|92|654321~
IT1|1|{item1_qty_inv}|EA|{item1_price}||BP|{product1}~
IT1|2|{item2_qty_inv}|EA|{item2_price}||BP|{product2}~
TDS|{total_amount}~  // Total Amount: ${total_amount}
SE|10|0004~
GE|1|4~
IEA|1|000000004~
DESC|EDI_810_Invoice


ISA|00|          |00|          |ZZ|{buyer}         |ZZ|{seller}      |{date}|{time_997}|U|{trans_id}|000000001|0|T|:~
GS|FA|{seller}|{buyer}|{date}|{time_997}|1|X|{trans_id}~
ST|997|0001~
AK1|PO|{po_number}~   // Acknowledging EDI 810 (Invoice)
AK2|810|0001~
AK5|{ack_status}~           // Status: {ack_status_desc}
AK9|{ack_status}|1|1|1~
SE|8|0002~
GE|1|2~
IEA|1|000000002~

"""
    return edi_810.strip(), base_date


# ========================================================================
# Generate EDI 214 (Transportation Carrier Shipment Status Message): Provides updates on the shipment status
# ========================================================================
def generate_edi_214(buyer, seller, carrier, po_number, shipment_id, product1, product2, base_date ):
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    #date, time, base_date = generate_timestamp(base_date, time_offset_days=3, time_offset_hours=5)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)

    random_ack_time_sec = random.randint(20, 500)
    dt_997 = base_date + timedelta(seconds=random_ack_time_sec)
    time_997 = dt_997.strftime("%H%M")
    ack_status , ack_status_desc = get_random_ack_status()

    edi_214 = f"""
ISA|00|          |00|          |ZZ|{seller}      |ZZ|{buyer}         |{date}|{time}|U|{trans_id}|000000004|0|T|:~
GS|QM|{carrier}|{seller}|20230807|0900|6|X|004010~
ST|214|0006~
B10|987654321|{shipment_id}|CC~
L11|PRO123|PO|{po_number}~
MS3|UPSN|M|L~
AT7|CD|NS|||{date}|1000|LT~
SE|7|0006~
GE|1|6~
IEA|1|000000006~


ISA|00|          |00|          |ZZ|{buyer}         |ZZ|{seller}      |{date}|{time_997}|U|{trans_id}|000000001|0|T|:~
GS|FA|{seller}|{buyer}|{date}|{time_997}|1|X|{trans_id}~
ST|997|0001~
AK1|PO|{po_number}~   // Acknowledging EDI 214 (Transportation Carrier Shipment Status Message): Provides updates on the shipment status
AK2|214|0001~
AK5|{ack_status}~           // Status: {ack_status_desc}
AK9|{ack_status}|1|1|1~
SE|8|0002~
GE|1|2~
IEA|1|000000002~

"""
    return edi_214.strip(), base_date


# ========================================================================
# Generate EDI 862 (Shipping Schedule): Communicates detailed shipping requirements.
# ========================================================================
def generate_edi_862(buyer, seller, carrier, po_number, shipment_id, product1, product2, base_date ): 
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    #date, time, base_date = generate_timestamp(base_date, time_offset_days=4, time_offset_hours=10)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)

    random_ack_time_sec = random.randint(20, 500)
    dt_997 = base_date + timedelta(seconds=random_ack_time_sec)
    time_997 = dt_997.strftime("%H%M")
    ack_status , ack_status_desc = get_random_ack_status()

    edi_862 = f"""
ISA|00|          |00|          |ZZ|{buyer}      |ZZ|{seller}         |{date}|{time}|U|{trans_id}|000000005|0|T|:~
GS|RA|{buyer}|{seller}|{date}|{time}|7|X|004010~
ST|862|0007~
BRA|00|RC|{shipment_id}|20230810~
N1|BY|{buyer}|92|123456~
N1|SE|{seller}|92|654321~
PO1|1|{item1_qty}|EA|{item1_price}|BP|{product1}~
PO1|2|{item2_qty}|EA|{item2_price}|BP|{product2}~
SE|9|0007~
GE|1|7~
IEA|1*000000007~


ISA|00|          |00|          |ZZ|{seller}         |ZZ|{buyer}      |{date}|{time_997}|U|{trans_id}|000000001|0|T|:~
GS|FA|{seller}|{buyer}|{date}|{time_997}|1|X|{trans_id}~
ST|997|0001~
AK1|PO|{po_number}~   // Acknowledging EDI 862 (Shipping Schedule): Communicates detailed shipping requirements
AK2|862|0001~
AK5|{ack_status}~           // Status: {ack_status_desc}
AK9|{ack_status}|1|1|1~
SE|8|0002~
GE|1|2~
IEA|1|000000002~

"""
    return edi_862.strip(), base_date


# ========================================================================
# Generate EDI 940 (Warehouse Shipping Order): Directs a warehouse to ship an order.
# ========================================================================
def generate_edi_940(buyer, seller, carrier, warehouse, po_number, shipment_id, product1, product2, base_date ): 
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    #date, time, base_date = generate_timestamp(base_date, time_offset_days=4, time_offset_hours=10)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)

    random_ack_time_sec = random.randint(20, 500)
    dt_997 = base_date + timedelta(seconds=random_ack_time_sec)
    time_997 = dt_997.strftime("%H%M")
    ack_status , ack_status_desc = get_random_ack_status()

    edi_940 = f"""
ISA|00|          |00|          |ZZ|{seller}      |ZZ|{warehouse}         |{date}|{time}|U|{trans_id}|000000005|0|T|:~
GS|OW|{seller}|{warehouse}|{date}|8|X|004010~
ST|940|0008~
W05|{date}|{shipment_id}~
N1|WH|{warehouse}|92|789012~
LX|1~
W01|{item1_qty}|EA|BP|{product1}~
LX|2~
W01|{item2_qty}|EA|BP|{product2}~
SE|10|0008~
GE|1|8~
IEA|1|000000008~


ISA|00|          |00|          |ZZ|{warehouse}         |ZZ|{seller}      |{date}|{time_997}|U|{trans_id}|000000001|0|T|:~
GS|FA|{warehouse}|{seller}|{date}|{time_997}|1|X|{trans_id}~
ST|997|0001~
AK1|PO|{po_number}~   // Acknowledging EDI 940 (Warehouse Shipping Order): Directs a warehouse to ship an order
AK2|940|0001~
AK5|{ack_status}~           // Status: {ack_status_desc}
AK9|{ack_status}|1|1|1~
SE|8|0002~
GE|1|2~
IEA|1|000000002~

"""
    return edi_940.strip(), base_date


# ========================================================================
# Generate EDI 945 (Warehouse Shipping Advice): Confirms the shipment of goods from the warehouse 
# ========================================================================
def generate_edi_945(buyer, seller, carrier, warehouse, po_number, shipment_id, product1, product2, base_date ): 
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    #date, time, base_date = generate_timestamp(base_date, time_offset_days=4, time_offset_hours=10)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)

    random_ack_time_sec = random.randint(20, 500)
    dt_997 = base_date + timedelta(seconds=random_ack_time_sec)
    time_997 = dt_997.strftime("%H%M")
    ack_status , ack_status_desc = get_random_ack_status()

    edi_945 = f"""
ISA|00|          |00|          |ZZ|{warehouse}      |ZZ|{seller}         |{date}|{time}|U|{trans_id}|000000005|0|T|:~
GS|WA|{warehouse}|{seller}|{date}|{time}|8|X|004010~
ST|945|0009~
W06|{shipment_id}~
N1|ST|{buyer}_WAREHOUSE|92|654321~
W12|{item1_qty}|EA|BP|{product1}~
W12|{item2_qty}|EA|BP|{product2}~
SE|9|0009~
GE|1|9~
IEA|1|000000009~


ISA|00|          |00|          |ZZ|{seller}         |ZZ|{warehouse}      |{date}|{time_997}|U|{trans_id}|000000001|0|T|:~
GS|FA|{seller}|{warehouse}|{date}|{time_997}|1|X|{trans_id}~
ST|997|0001~
AK1|PO|{po_number}~   // Acknowledging EDI 945 (Warehouse Shipping Advice): Confirms the shipment of goods from the warehouse
AK2|945|0001~
AK5|{ack_status}~           // Status: {ack_status_desc}
AK9|{ack_status}|1|1|1~
SE|8|0002~
GE|1|2~
IEA|1|000000002~

"""
    return edi_945.strip(), base_date


# ========================================================================
# Generate EDI 947 (Warehouse Inventory Adjustment Advice): Communicates inventory adjustments 
# ========================================================================
def generate_edi_947(buyer, seller, carrier, warehouse, po_number, shipment_id, product1, product2, base_date ): 
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    #date, time, base_date = generate_timestamp(base_date, time_offset_days=4, time_offset_hours=10)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)

    random_ack_time_sec = random.randint(20, 500)
    dt_997 = base_date + timedelta(seconds=random_ack_time_sec)
    time_997 = dt_997.strftime("%H%M")
    ack_status , ack_status_desc = get_random_ack_status()

    edi_947 = f"""
ISA|00|          |00|          |ZZ|{warehouse}      |ZZ|{seller}         |{date}|{time}|U|{trans_id}|000000005|0|T|:~
GS|IW|{warehouse}|{seller}|{date}|{time}|10|X|004010~
ST|947|0009~
W15|ADJ123456~
N1|WH|{warehouse}|92|789012~
LIN||BP|{product1}~
QTY|{item1_qty}|{item1_qty_inv}~  // Adjusting {product1} inventory
LIN||BP|{product2}~
QTY|{item2_qty}|{item2_qty_inv}~


ISA|00|          |00|          |ZZ|{seller}         |ZZ|{warehouse}      |{date}|{time_997}|U|{trans_id}|000000001|0|T|:~
GS|FA|{seller}|{warehouse}|{date}|{time_997}|1|X|{trans_id}~
ST|997|0001~
AK1|PO|{po_number}~   // Acknowledging EDI 947 (Warehouse Inventory Adjustment Advice): Communicates inventory adjustments
AK2|947|0001~
AK5|{ack_status}~           // Status: {ack_status_desc}
AK9|{ack_status}|1|1|1~
SE|8|0002~
GE|1|2~
IEA|1|000000002~
"""
    return edi_947.strip(), base_date


# ========================================================================
# Generate EDI 861 (Receiving Advice/Acceptance Certificate): Confirms receipt of goods and reports discrepancies, damages, or errors.
# ========================================================================
def generate_edi_861(buyer, seller, carrier, warehouse, po_number, shipment_id, product1, product2, base_date ): 
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    #date, time, base_date = generate_timestamp(base_date, time_offset_days=4, time_offset_hours=10)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)
    damaged_cnt = f"{random.randint(0, 20)}"
    product_type = f"{random.randint(1, 2)}"

    random_ack_time_sec = random.randint(20, 500)
    dt_997 = base_date + timedelta(seconds=random_ack_time_sec)
    time_997 = dt_997.strftime("%H%M")
    ack_status , ack_status_desc = get_random_ack_status()

    edi_861 = f"""
ISA|00|          |00|          |ZZ|{buyer}      |ZZ|{seller}         |{date}|{time}|U|{trans_id}|000000005|0|T|:~
GS|RC|{buyer}|{seller}|{date}|{time}|11|X|004010~
ST|861|0001~
BRA|00|RA|123456|20240926~
N1|ST|{buyer}_WAREHOUSE|92|654321~
RCD|AC|{item1_qty}|EA|BP|{product1}~  // Received correct quantity for ITEM100
RCD|RE|{item2_qty}|EA|BP|{product2}~  // Received 40 of 50 ordered, reporting shortage
MEA|WT|G|{total_weight}|LB~  // Recording weight of received goods
NTE|GEN|{damaged_cnt} units of {product1} damaged upon receipt~
SE|8|0001~
GE|1|11~
IEA|1|000000011~

ISA|00|          |00|          |ZZ|{seller}         |ZZ|{buyer}      |{date}|{time_997}|U|{trans_id}|000000001|0|T|:~
GS|FA|{seller}|{buyer}|{date}|{time_997}|1|X|{trans_id}~
ST|997|0001~
AK1|PO|{po_number}~   // Acknowledging 861 (Receiving Advice/Acceptance Certificate)
AK2|861|0001~
AK5|{ack_status}~           // Status: {ack_status_desc}
AK9|{ack_status}|1|1|1~
SE|6|0001~
GE|1|21~
IEA|1|000000021~

"""
    return edi_861.strip(), base_date


# ========================================================================
# Generate EDI 824 (Application Advice): Reports any errors or discrepancies found in the transactions
# ========================================================================
def generate_edi_824(buyer, seller, carrier, warehouse, po_number, shipment_id, product1, product2, base_date ): 
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    #date, time, base_date = generate_timestamp(base_date, time_offset_days=4, time_offset_hours=10)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)

    random_ack_time_sec = random.randint(20, 500)
    dt_997 = base_date + timedelta(seconds=random_ack_time_sec)
    time_997 = dt_997.strftime("%H%M")
    ack_status , ack_status_desc = get_random_ack_status()

    edi_824 = f"""
ISA|00|          |00|          |ZZ|{seller}      |ZZ|{buyer}         |{date}|{time}|U|{trans_id}|000000005|0|T|:~
GS|AG|{seller}|{buyer}|{date}|{time}|12|X|004010~
ST|824|0002~
BGN|00|123456789|20240927~
N1|PR|{seller}|92|123456~
N1|BT|{buyer}|92|654321~
OTI|IA|820|123456789|0001|004010~
TED|848|Error in Quantity Received|~
NTE|GEN|Customer received incorrect quantity for {product1}~  // Discrepancy in receiving quantity
SE|9|0002~
GE|1|12~
IEA|1|000000012~


ISA|00|          |00|          |ZZ|{buyer}         |ZZ|{seller}      |{date}|{time_997}|U|{trans_id}|000000001|0|T|:~
GS|FA|{buyer}|{seller}|{date}|{time_997}|1|X|{trans_id}~
ST|997|0001~
AK1|PO|{po_number}~   // Acknowledging EDI 824 (Application Advice) : Reports any error 
AK2|824|0001~
AK5|{ack_status}~           // Status: {ack_status_desc}
AK9|{ack_status}|1|1|1~
SE|8|0002~
GE|1|2~
IEA|1|000000002~

"""
    return edi_824.strip(), base_date


##############################################
# Main function to generate all EDI transactions
##############################################

def generate_edi_transactions():
    buyer = random.choice(buyers)
    seller = random.choice(sellers)
    carrier = random.choice(carriers)
    warehouse = random.choice(warehouses)
    product1 = random.choice(products)
    product2 = random.choice(products)
    po_number = f"PO{random.randint(100000, 999999)}"

    while product1 == product2:
        product2 = random.choice(products)

    days_ago = random.randint(5, 12)
    base_date = datetime.now() - timedelta(days=days_ago)

    ### ============================================
    ### Generate event outputs
    ### ============================================

    event, base_date = generate_edi_850(buyer, seller, po_number, product1, product2, base_date)
    print(event,"\n\n")
    #print("DESC|EDI_850_Purchase_Order\n\n")

    event, base_date_new = generate_edi_855(buyer, seller, po_number, product1, product2, base_date)
    print(event,"\n\n")
    #print("DESC|EDI_855_Purchase_Order_Acknowledgment\n\n")

    event, base_date_new = generate_edi_830(buyer, seller, po_number, product1, product2, base_date_new)
    print(event,"\n\n")
    #print("DESC|EDI_830_Planning_Schedule_with_Release_Capability\n\n")

    event, base_date_new = generate_edi_856(buyer, seller, po_number, product1, product2, base_date_new)
    print(event,"\n\n")
    #print("DESC|EDI_856_Advance_Ship_Notice\n\n")

    event, base_date_new = generate_edi_856_retry(buyer, seller, po_number, product1, product2, base_date_new)
    print(event,"\n\n")

    event, base_date_new = generate_edi_856_retry(buyer, seller, po_number, product1, product2, base_date_new)
    print(event,"\n\n")

    event, base_date_new = generate_edi_856_retry(buyer, seller, po_number, product1, product2, base_date_new)
    print(event,"\n\n")

    event, base_date_new = generate_edi_856_retry(buyer, seller, po_number, product1, product2, base_date_new)
    print(event,"\n\n")

    event, base_date_new = generate_edi_856_retry(buyer, seller, po_number, product1, product2, base_date_new)
    print(event,"\n\n")

    if random_discrepancy == "6":
    	event, base_date_new = generate_edi_861(buyer, seller, carrier, warehouse, po_number, shipment_id, product1, product2, base_date_new )
    	print(event,"\n\n")
    	print("DESC|EDI_861_Receiving_Advice_Acceptance_Certificate\n\n")
    elif random_discrepancy == "7":
    	event, base_date_new = generate_edi_824(buyer, seller, carrier, warehouse, po_number, shipment_id, product1, product2, base_date_new )
    	print(event,"\n\n")
    	print("DESC|EDI_824_Application_Advice\n\n")
    else:
    	print("")


# Generate the EDI transactions
generate_edi_transactions()

