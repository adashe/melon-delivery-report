# print("Day 1")
# the_file = open("um-deliveries-day-1.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-day-2.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-day-3.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()

# creates a function that opens a delivery report
# prints out a string with type of melons, count, and amount

def delivery_report(file):

    print("*** Report from " + str(file) + " ***")

    # opens files

    the_file = open(file)

    # iterates through each line in the file

    for line in the_file:

        # cleans up each line

        line = line.rstrip()
        words = line.split('|')

        # assigns names to items in each line

        melon = words[0]
        count = words[1]
        amount = words[2]

        #prints summary statement

        print(f"Delivered {count} {melon}s for total of ${amount}")
    
    # closes file

    the_file.close()

delivery_report("um-deliveries-day-1.txt")
delivery_report("um-deliveries-day-2.txt")
delivery_report("um-deliveries-day-3.txt")

# next steps: create dictionaries instead of single-string tallies