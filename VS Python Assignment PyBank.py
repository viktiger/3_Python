# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("PyBank", "budget_data.csv")
# print(csvpath)

# Set variable to check if we found the file
found = False

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

#     for row in csvreader:
#         print (row) # Testing data is printing 
#         print (row[1]) # Testing data is printing amounts
#         print (int(row[1])) # Converting amounts into integers from strings

    # Total months
    count = 0 
    # Total profit/loss
    total = 0

    for row in csvreader:
        count = count +1
        total = total + int(row[1])

    # print("--------------------")
    print("Financial Analysis")
    print("--------------------")
    # Total months    
    print("Total number of months: ", count)
    # Total profit/loss
    print("Total profit/ loss: $", total)

# Changes in profit/loss and averaging those changes
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    first_row = next(csvreader)
    previous_row_net=int(first_row[1])
    net_difference = 0
    difference_total = []
    dates = []

    for row in csvreader:
        # Track the net change
        net_difference = int(row[1])-previous_row_net
        previous_row_net=int(row[1])
        date = row[0]
        # print(net_difference)
        difference_total.append(net_difference)
        dates.append(row[0])

        # Calculating & formatting the sum of the difference between each month divided by the number of months or iterations
        average_change = sum(difference_total)/len(difference_total)
        format_average_change = "{:.2f}".format(average_change)

        # Calculating & formatting the max difference between two months
        greatest_increase = max(difference_total)
        format_greatest_increase = "({})".format(greatest_increase)
        # Finding the corresponding max difference month
        greatest_date = difference_total.index(greatest_increase)
        greatest_date_value = dates[greatest_date]
        
        # Calculating & formatting the min difference between two months
        greatest_decrease = min(difference_total)
        format_greatest_decrease = "({})".format(greatest_decrease)
        # Finding the corresponding max difference month
        lowest_date = difference_total.index(greatest_decrease)
        lowest_date_value = dates[lowest_date]
      

    # Average Change in profit/loss of 85 rows
    print("Average Change: $",format_average_change)

    # Greatest increase in profit/loss change
    print("Greatest Increase in Profits: ", greatest_date_value, "$", format_greatest_increase)
    # Greatest decrease in profit/loss change
    print("Greatest Decrease in Profits: ", lowest_date_value, "$", format_greatest_decrease)

# Exporting a text file
output = open("output_pybank.txt", "w")

line1 = "--------------------"
line2 = "Financial Analysis"
line3 = "--------------------"
line4 = str(f"Total number of months: {str(count)}")
line5 = str(f"Total profit/ loss: $ {str(total)}")
line6 = str(f"Average Change: $ {str(format_average_change)}")
line7 = str(f"Total profit/ loss: $ {str(total)}")
line8 = str(f"Greatest Increase in Profits: {greatest_date_value} (${str(format_greatest_increase)}")
line9 = str(f"Greatest Decrease in Profits: {lowest_date_value} (${str(format_greatest_decrease)}")
line10 = "--------------------"

output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4,line5,line6,line7,line8,line9,line10))