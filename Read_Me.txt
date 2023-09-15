
*********************** Required Packages to be installed *************************

1. Pandas
2. scikit-learn
3. Matplotlib
4. Geopy



*********************** Note for path loss of "CSV" file  *************************

The "Data_for_Sub_Station" is a csv file that consists of a geographical 
informations of an area. These informations will be used so as to find the 
most suitable placement of the substations based on clustering. 

Please Note that the csv file location would be a bit different with mine 
after downloading the project.

Please, alter the path from line 11 of the code (main) changing the "USERNAME"
based on your device user. Therefore, the code will work with the corresponding 
csv file named as "Data_for_Sub_Station" and provide result accordingly. 


************************* Number of Substation Decision ***************************

# Starting with the "Number of Substation" as 1. Finding the power loss, the 
  efficiency of each house is calculated

# Then average efficiency with all houses is calculated

# If avg efficiency is less than 95 percent, increment the number of substation 
  by one and check avg efficiency again

# Once the average efficiency reaches at least 95 percent, that number of substation
  is considered as sufficient for that place