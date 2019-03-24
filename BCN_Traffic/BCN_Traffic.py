'''
@author Neke_Kala
20-12-2018
'''

#importing libraries that we'll use
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import time

#Using a defining methods aproach, so we define our Methods, 'concat','graph' and 'Main'

#THe function that will read the files and calculate the average traffic
def concat (indir):
    os.chdir(indir)     # change working directory in our files folder
    average = []  #Create a list for the average values of each month
    months = []   #Create a list with the names of the months for the graph
    filelist = glob.glob('data/*.csv')  # grab every .csv file that exists in this folder
    for filename in filelist:
        df = pd.read_csv(filename, low_memory=False) #read each file and create a dataframe...
        avg = df['estatActual'].mean() #...find the average of the real traffic of the month...
        print ('The average traffic state for ',filename[13:-16], "is: ",
               df['estatActual'].mean()) #...show it on the console
        average.append(avg) # Fill the average list with the values of eash month
        months.append(filename[10:-16]) # Keep the months names in the months list
    return average, months #return the average and Months lists

#The function that will represent the values in a graphical representation
def graph(average, months): #Plot the results
        # we set the x-axis and y-axis
        plt.bar(months, average, align='center',
                color=['olive', 'yellowgreen', 'lawngreen', 'lightgreen', 'g', 'mediumseagreen', 'mediumaquamarine',
                       'mediumturquoise', 'darkcyan','royalblue', 'navy'])
        plt.tick_params(axis='x', which='major',
                        labelsize=6)  # We reduce the size of the axis label so we can see all the months
        plt.ylim(0.8,1.1) #we set a limit for a better visualization of the values
        plt.xticks(rotation=30) #rotation of the x-axis to skip month name overlaping
        # Set names for the Graph and the axis
        plt.ylabel('Traffic average')
        plt.xlabel('Months')
        plt.title('Monthly average traffic state of Barcelona')
        plt.show()


# Main function
def main():
    start_time = time.time()  # start  a timer to evaluate the performance of the code
    average, months = concat('Path') #Location of the .CSV files
    print("time execution: %s s" % (time.time() - start_time))  # stop the timer and show us the result
    graph (average, months) # Show us a graphic representation of the results


if __name__ == "__main__":
    main()
