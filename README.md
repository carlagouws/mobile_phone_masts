# mobile_phone_masts

## Requirements
1. Read in the attached file
- Produce a list sorted by “Current Rent” in ascending order
- Obtain the first 5 items from the resultant list and output to the console
2. From the list of all mast data, create a new list of mast data with “Lease Years” = 25 years.
- Output the list to the console, including all data fields
- Output the total rent for all items in this list to the console
3.	Create a dictionary containing tenant name and a count of masts for each tenant
- Output the dictionary to the console in a readable form
4.	List the data for rentals with “Lease Start Date” between 1st June 1999 and 31st August 2007
- Output the data to the console with dates formatted as DD/MM/YYYY

The dataset is a CSV which contains publicly available data about mobile phone masts in an area of the UK. 
This file contains un-normalised data (such as multiple variations of Tenant Name) – treat these as individual tenants.

## Assumptions
- "treat these as individual" means don't group by tenant name
- "total rent for all items" in a list is the sum of the current rent for all the items

## To run:
- change your csv name to "dataset.csv" and place in folder
- run 'main.py'