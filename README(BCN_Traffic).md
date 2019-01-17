
BCN_Traffic:

A project that analyzes the traffic in Barcelona for the year 2018 (January to November) from data located in .CSV files in http://opendata-ajuntament.barcelona.cat/data/organization/transport

Uses Pandas to read the files and extract the data and Matplotlib to show the results in a graphical representation.

The approach is first read the files one by one in the "Concat" functionwith the use of 'glob' library and calculate the average traffic of each month through functions of Pandas libraries, return the results (average of each month and the name of the month) to the main function and then pass them to the "Graph" function so we can use "Matplotlib" library to demonstrate the results in a graphical representation.
