#!/usr/bin/env python3

# Delow is the function containing out code
def main():
    # pause the program and wait for the user to provide input
    ipv4 = input("Please enter an IPv4 address: ")

    # display the input back to the user
    print("You told me the IPv4 address is: ", ipv4)

    # gather vendor info
    vendor_info = input("Please enter vendor name: ")

    #Display vendor info
    print("You stated that the vendor is: ", vendor_info)

# this calls main
main()
