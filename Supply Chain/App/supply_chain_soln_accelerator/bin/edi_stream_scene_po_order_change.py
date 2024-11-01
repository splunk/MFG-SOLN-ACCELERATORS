#!/usr/bin/python3

import random
from datetime import datetime, timedelta

# Generate random BUYER and SELLER
buyers = ['QUANTUMLINE']
sellers = ['CircuitCore', 'TechWave_Electronics', 'ElectroFusion_Inc.', 'Precision_Circuits', 'QuantumWires', 'VoltEdge_Systems', 'NanoCircuit_Solutions', 'SiliconStream', 'MicroTek_Electronics', 'PulseCraft_Technologies', 'ElectroSphere', 'DigiParts_Innovations', 'OptiCore_Engineering', 'FluxTech_Systems', 'Precision_Circuits_Pro', 'WireLogic_Solutions', 'NexGen_Electronics', 'Quantum_Circuits', 'VoltCraft_Engineering', 'SparkEdge_Systems', 'Vector_Circuitry', 'HyperLink_Parts', 'ElectroCore_Industries', 'NexuTech_Components', 'Pinnacle_Circuits', 'PowerGrid_Engineering', 'MicroPulse_Innovations', 'BlueWave_Components', 'DigiWave_Technologies', 'CircuitGrid_Engineering', 'Sparkline_Systems', 'PulseCore_Technologies', 'QuantumBridge_Circuits', 'ArcWave_Components', 'ElectroVision_Engineering', 'NanoLink_Systems', 'Innovatech_Circuits', 'VoltEdge_Components', 'OptiWave_Technologies', 'PrecisionTech_Parts', 'CircuitCraft_Engineering', 'PulseTech_Innovations', 'NanoVolt_Systems', 'ElectraCore_Components', 'SparkWave_Solutions', 'NexGen_Circuits', 'VoltCraft_Components' ]
## 'QuantumLine_Engineering', 'WireWave_Systems', 'BlueVolt_Technologies', 'TechLink_Circuits', 'PowerGrid_Parts', 'ElectroLink_Innovations', 'NanoCore_Engineering', 'SparkTech_Systems', 'VoltStream_Components', 'MicroGrid_Circuits', 'ElectroWave_Engineering', 'CircuitVision_Technologies', 'FluxLink_Components', 'QuantumWave_Systems', 'VoltPro_Engineering', 'OptiPulse_Components', 'NanoStream_Circuits', 'WirePulse_Systems', 'DigiCore_Engineering', 'ElectroEdge_Components', 'BlueTech_Circuits', 'PulsePro_Engineering', 'QuantumEdge_Components', 'PowerLink_Circuits', 'VoltCraft_Solutions', 'SparkLine_Technologies', 'WireTek_Systems', 'NexuCore_Components', 'NanoVolt_Engineering', 'CircuitPulse_Solutions', 'OptiCore_Systems', 'ElectroLink_Circuits', 'QuantumGrid_Technologies', 'FluxCore_Engineering', 'PrecisionVolt_Systems', 'SparkGrid_Components', 'CircuitEdge_Technologies', 'BlueCore_Engineering', 'ElectroPro_Solutions', 'NanoTech_Circuits', 'VoltVision_Components', 'DigiGrid_Engineering', 'OptiWave_Solutions', 'SparkEdge_Components', 'PulseVision_Technologies', 'QuantumTek_Systems', 'VoltCore_Engineering', 'CircuitFusion_Solutions', 'PowerPulse_Components', 'BlueWave_Circuits', 'FluxEdge_Systems', 'ElectroGrid_Technologies', 'PrecisionCore_Circuits' ]
products = ['VoltMax_Capacitor', 'NanoFlux_Resistor', 'HyperLink_Transistor', 'QuantumPulse_Diode', 'CircuitWave_Microcontroller', 'PowerCore_Inductor', 'OptiVolt_Transformer', 'PulseLine_MOSFET', 'ElectroEdge_Relay', 'FluxStream_Connector', 'DigiLink_PCB_Board', 'WireTech_Heat_Sink', 'BlueVolt_Power_Supply', 'PrecisionCore_Ferrite_Bead', 'CircuitFlow_IC_Chip', 'SparkPro_LED_Array', 'OptiCore_Crystal_Oscillator', 'VoltEdge_Fuse', 'NanoTek_Signal_Amplifier', 'MicroGrid_Voltage_Regulator', 'PulseVision_Resistor_Network', 'ElectroLine_Zener_Diode', 'QuantumCore_Signal_Transformer', 'SparkGrid_Capacitive_Sensor', 'VoltPro_DC-DC_Converter', 'WireWave_Varistor', 'DigiCore_Optocoupler', 'FluxTek_Thyristor', 'NanoLine_Quartz_Resonator', 'PowerEdge_Precision_Capacitor', 'OptiPulse_Switching_Diode', 'CircuitSphere_Photocoupler', 'PulseCraft_High-Frequency_Inductor', 'ElectroPulse_MEMS_Oscillator', 'VoltStream_SMD_Resistor', 'SparkTech_Schottky_Diode', 'DigiPulse_Electret_Microphone', 'WireLine_Load_Cell', 'BlueWave_Stepper_Motor_Driver', 'PowerTek_BJT_Transistor', 'NanoVolt_Thermistor', 'QuantumLink_Hall_Effect_Sensor', 'FluxEdge_Motor_Capacitor', 'OptiWave_Voltage_Regulator_IC', 'DigiEdge_RF_Connector', 'SparkLine_Piezoelectric_Sensor', 'VoltCraft_Photodiode_Array', 'PowerWave_IGBT_Module', 'CircuitCraft_Potentiometer', 'PulseMax_Silicon_Rectifier', 'ElectroCore_Signal_Filter', 'NanoLink_Optical_Encoder', 'VoltVision_SMT_Fuse', 'SparkEdge_Surface_Mount_Inductor', 'DigiStream_Power_MOSFET', 'FluxGrid_NTC_Thermistor', 'OptiGrid_Current_Sensor', 'QuantumEdge_Temperature_Sensor', 'CircuitVision_Lithium-Ion_Cell', 'NanoCraft_Digital_Potentiometer', 'PowerMax_Power_Resistor', 'WireCore_Magnetic_Sensor', 'DigiVolt_Pulse_Transformer', 'SparkCore_Piezoelectric_Actuator', 'CircuitEdge_Ceramic_Capacitor', 'VoltLine_Logic_Level_Shifter', 'ElectroLink_EMI_Filter', 'OptiFlow_High-Power_LED', 'PulseTek_Multilayer_Capacitor', 'WirePulse_Transient_Voltage_Suppressor', 'FluxLink_Phase-Locked_Loop_IC', 'PowerStream_Voltage_Stabilizer', 'CircuitGrid_Power_Transistor', 'DigiPulse_Signal_Attenuator', 'QuantumLine_Multilayer_Resistor', 'SparkFlow_Piezo_Buzzer', 'VoltSphere_Solid-State_Relay', 'NanoVolt_Low-Power_Oscillator', 'OptiLink_DC_Fan_Controller', 'ElectroMax_High-Voltage_Capacitor', 'PulseLine_Power_Inductor', 'FluxStream_Dual_In-line_Package_IC', 'CircuitLine_Precision_Rectifier', 'DigiWave_Clock_Generator', 'PowerCore_Surface_Mount_LED', 'SparkVision_Audio_Transducer', 'VoltEdge_Logic_Gate_IC', 'QuantumWave_CMOS_Inverter', 'CircuitEdge_RF_Power_Amplifier', 'WireCore_Low_Dropout_Regulator', 'OptiCore_Capacitive_Touch_Sensor', 'NanoVolt_Signal_Generator', 'PowerTek_Peltier_Cooler', 'PulseCraft_Triac_Driver', 'FluxCore_Wire_Wound_Inductor', 'DigiCraft_DC_Motor_Driver', 'SparkPro_Power_Bridge_Rectifier', 'VoltVision_Pulse_Width_Modulator', 'ElectroGrid_Capacitor_Array', 'CircuitCraft_Thermal_Fuse' ]
days_agos = [7, 6, 5, 4]
time_offset_days = [1, 2, 3, 4, 5, 6]
time_offset_hrs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
po_number = f"PO{random.randint(500001, 999999)}"
trans_id = f"TR{random.randint(1000001, 1999999)}"

## Inventory Quantity
item1_qty_inv_temp = random.randint(500, 800)
item1_qty_inv = round(item1_qty_inv_temp / 10) * 10
item2_qty_inv = random.randint(0, 0)

## Order Quantity
item1_qty = random.randint(50, 200)
item2_qty = random.randint(25, 100)
item1_temp = random.randint(20, 300)
item2_temp = random.randint(20, 100)
item1_price = round(item1_temp / 10) * 10
item2_price = round(item2_temp / 10) * 10
total_amount = item1_qty * item1_price + item2_qty * item2_price
total_weight = item1_qty * 15 + item2_qty * 20
item1_qty_change = random.randint(50, 200)
item2_qty_change = random.randint(25, 100)

# Generate dynamic timestamps
def generate_timestamp(base_date, time_offset_days=0, time_offset_hours=0):
    dt = base_date + timedelta(days=time_offset_days, hours=time_offset_hours)
    base_date = dt
    return dt.strftime("%Y%m%d"), dt.strftime("%H%M"), base_date

# Generate EDI 850 (Purchase Order)
def generate_edi_850(buyer, seller, po_number, product1, product2, base_date):
    date, time, base_date = generate_timestamp(base_date)
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
"""
    return edi_850.strip()

# Generate EDI 855 (Purchase Order Acknowledgment)
def generate_edi_855(buyer, seller, po_number, product1, product2, base_date):
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)
    edi_855 = f"""
ISA|00|          |00|          |ZZ|{seller}      |ZZ|{buyer}         |{date}|{time}|U|{trans_id}|000000002|0|T|:~
GS|PO|{seller}|{buyer}|{date}|{time}|2|X|{trans_id}~
ST|855|0002~
BAK|00|AD|{po_number}|{date}~
N1|BY|{buyer}|92|123456~
N1|SE|{seller}|92|654321~
PO1|1|{item1_qty}|EA|{item1_price}|PE|BP|{product1}|IA~  // Accepted: Full Quantity Available
PO1|2|{item2_qty}|EA|{item2_price}|PE|BP|{product2}|BO~  // Backordered: Not enough stock for {product2}
SE|8|0002~
GE|1|2~
IEA|1|000000002~
"""
    return edi_855.strip()

# Generate EDI 860 (Purchase Order Change)
def generate_edi_860(buyer, seller, po_number, product1, product2_change, base_date):
    date, time, base_date = generate_timestamp(base_date)
    edi_860 = f"""
ISA|00|          |00|          |ZZ|{buyer}         |ZZ|{seller}      |{date}|{time}|U|{trans_id}|000000001|0|P|:~
GS|PO|{buyer}|{seller}|{date}|{time}|1|X|{trans_id}~
ST|860|0001~
BCH|00|SA|{trans_id}||{date}|123456||IN~
REF|CO|987654321~
DTM|002|{date}~
N1|ST|{seller}|92|12345~
N3|1234 WAREHOUSE LANE~
N4|PHOENIX|AZ|85001~
POC|1|AI|{item1_qty_change}|EA|{item1_price}||BP|0987654321|VP|54321~
PID|F||||{product1}~
POC|2|AI|{item2_qty}|EA|{item2_qty}||BP|1234567890|VP|98765~
PID|F||||{product2_change}~
CTT|2~
SE|9|0001~
GE|1|1~
IEA|1|000000001~
"""
    return edi_860.strip()


# Generate EDI 855 (Purchase Order Change Acknowledgment)
def generate_edi_855_POC(buyer, seller, po_number, product1, product2_change, base_date):
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)
    edi_855 = f"""
ISA|00|          |00|          |ZZ|{seller}      |ZZ|{buyer}         |{date}|{time}|U|{trans_id}|000000002|0|T|:~
GS|PO|{seller}|{buyer}|{date}|{time}|2|X|{trans_id}~
ST|860|0002~
BAK|00|AD|{po_number}|{date}~
N1|BY|{buyer}|92|123456~
N1|SE|{seller}|92|654321~
PO1|1|{item1_qty_change}|EA|{item1_price}|PE|BP|{product1}|IA~  // Accepted: Quanty Change
PO1|2|{item2_qty}|EA|{item2_price}|PE|BP|{product2_change}|BO~  // Accepted: Product changed
SE|8|0002~
GE|1|2~
IEA|1|000000002~
"""
    return edi_855.strip()


# Generate EDI 856 (Advance Ship Notice)
def generate_edi_856(buyer, seller, po_number, product1, product2, base_date):
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    #date, time, base_date = generate_timestamp(base_date, time_offset_days=2, time_offset_hours=3)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)
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
SN1||{item1_qty}|EA~  // Full Quantity Shipped
HL|3|1|O~
LIN||BP|{product2}~
SN1||0|EA~  // No Quantity Shipped due to Stockout
SE|12|0003~
GE|1|3~
IEA|1|000000003~
"""
    return edi_856.strip()

# Generate EDI 810 (Invoice)
def generate_edi_810(buyer, seller, po_number, product1, product2, base_date):
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    #date, time, base_date = generate_timestamp(base_date, time_offset_days=3, time_offset_hours=5)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)
    edi_810 = f"""
ISA|00|          |00|          |ZZ|{seller}      |ZZ|{buyer}         |{date}|{time}|U|{trans_id}|000000004|0|T|:~
GS|IN|{seller}|{buyer}|{date}|{time}|4|X|{trans_id}~
ST|810|0004~
BIG|{date}|INV567890|{po_number}~
N1|BY|{buyer}|92|123456~
N1|SE|{seller}|92|654321~
IT1|1|{item1_qty_inv}|EA|{item1_price}||BP|{product1}~
IT1|2|{item2_qty_inv}|EA|{item2_price}||BP|{product2}|BO~  // {product2} Backordered
TDS|{total_amount}~  // Total Amount: ${total_amount}
SE|10|0004~
GE|1|4~
IEA|1|000000004~
"""
    return edi_810.strip()

# Generate EDI 846 (Inventory Inquiry/Advice)
def generate_edi_846(buyer, seller, po_number, product1, product2, base_date):
    time_offset_day = random.choice(time_offset_days)
    time_offset_hr = random.choice(time_offset_hrs)
    #date, time, base_date = generate_timestamp(base_date, time_offset_days=4, time_offset_hours=10)
    date, time, base_date = generate_timestamp(base_date, time_offset_days=time_offset_day, time_offset_hours=time_offset_hr)
    edi_846 = f"""
ISA|00|          |00|          |ZZ|{seller}      |ZZ|{buyer}         |{date}|{time}|U|{trans_id}|000000005|0|T|:~
GS|IB|{seller}|{buyer}|{date}|{time}|5|X|{trans_id}~
ST|846|0005~
BIA|00|IB|{date}~
N1|SE|{seller}|92|654321~
LIN||BP|{product1}~
QTY|33|{item1_qty_inv}~  // Available Quantity: {item1_qty_inv} units
LIN||BP|{product2}~
QTY|33|{item2_qty_inv}~  // Available Quantity: {item2_qty_inv} units (Out of Stock)
SE|7|0005~
GE|1|5~
IEA|1|000000005~
REF|BM|{po_number}~
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
    product2_change = random.choice(products)
    po_number = f"PO{random.randint(100000, 999999)}"

    while product1 == product2:
        product2 = random.choice(products)

    days_ago = random.choice(days_agos)
    base_date = datetime.now() - timedelta(days=days_ago)

    print(generate_edi_850(buyer, seller, po_number, product1, product2, base_date))
    print("DESC|EDI_850_Purchase_Order\n\n")

    print(generate_edi_855(buyer, seller, po_number, product1, product2, base_date))
    print("DESC|EDI_855_Purchase_Order_Acknowledgment\n\n")

    print(generate_edi_860(buyer, seller, po_number, product1, product2_change, base_date))
    print("DESC|EDI_860_Purchase_Order_Change\n\n")

    print(generate_edi_855_POC(buyer, seller, po_number, product1, product2_change, base_date))
    print("DESC|EDI_855_Purchase_Order_Change_Acknowledgment\n\n")

    print(generate_edi_856(buyer, seller, po_number, product1, product2, base_date))
    print("DESC|EDI_856_Advance_Ship_Notice\n\n")

    print(generate_edi_810(buyer, seller, po_number, product1, product2, base_date))
    print("DESC|EDI_810_Invoice\n\n")

    #print(generate_edi_846(buyer, seller, po_number, product1, product2, base_date))
    #print("DESC|EDI_846_Inventory_Inquiry_Advice\n\n")

# Generate the EDI transactions
generate_edi_transactions()

