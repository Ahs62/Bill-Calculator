import sys  

while True:  
    print("=== Electricity Bill Calculator ===")
    print("--- This app will process two (2) customers ---\n")

    total_customers = 2
    customers_billed = 0

    for i in range(1, total_customers + 1):
        print(f"--- Processing Customer No. {i} ---")
        name = input("Enter Customer Name: ")
        c_type = input("Enter Customer Type ('R' for Residential, 'C' for Commercial): ").upper()
        units = float(input("Enter Units Consumed: "))
        print()

        rate_per_unit = 0
        gst = 0
        discount = 0
        # Check customer type
        if c_type == 'R':
            rate_per_unit = 10.5
            gst = 15.75
            if units <= 200:
                discount = 15.0
        elif c_type == 'C':
            rate_per_unit = 10.5 * 2
            gst = 15.75 * 2
            if units <= 300:
                discount = 30.0
        else:
            print("Invalid customer type! Bill cannot be calculated.\n")
            continue

           # Calculate bill
        electricity_charge = units * rate_per_unit
        total_bill = (electricity_charge + gst) - discount

        print(f"------ Bill for {name} --------")
        print(f"  Units Consumed:  {units}")
        print(f"  Electricity Charge:  {electricity_charge:.2f}")
        print(f"  Service Fee:       {gst:.2f}")
        print(f"  Discount Applied:  {discount:.2f}")
        print("  --------------------------")
        print(f"  TOTAL BILL:        {total_bill:.2f}\n")

        customers_billed += 1

    print(f"Processing complete. {customers_billed} customer(s) billed.\n")

    # Ask user if they want to continue or exit
    ext = input("Do you want to process another set of customers? (y/n): ").lower()
    if ext == 'n':
        print("Program terminated by user.")
        break 
    else:
        print("\nRestarting program...\n")
