import matplotlib.pyplot as plt
import numpy as np

#_______________________________________________________________________________________________________________
filenames    = ["IV_light_35.txt", "IV_light_45.txt", "IV_light_55.txt", "IV_light_65.txt", "IV_light_75.txt"]
Plot_Title   = "I/V Characteristics for different temperatures"
x_axis_label = "Voltage (V)"
y_axis_label = "Current (I)"
number_of_curves_in_plot = 1
LOG_OF_X = False
is_first_order_derivative = False
#_______________________________________________________________________________________________________________

x_axis_colum_number = 3
y_axis_column_start = 2

global readings
global x_readings
global y_readings

x_readings = []
y_readings = []

numbers =['0','1','2','3','4','5','6','7','8','9']

#This function read the file and returns the x and y axis values
def read_file(axis_index, filename):
    axis_readings = []
    readings_file = open(filename, "r")

    # read file line by line
    for x in readings_file:
        if x == "":
            #skip blank lines
            continue
        elif not(x[0] in numbers):
            # skip  lines which do not contain readings
            continue

        # remove new line character from each
        x = x.replace("\n", "")

        # seperate three numbers from line -> Index x_value y_value
        readings = [float(d) for d in x.split()]
        #print("readings-->",readings)
        try:
            axis_readings.append(readings[axis_index])
        except:
            print("________________________________________________________________________________________")
            print("***************Column number mismatch Error*************")
            print("Column number mismatch Error: Number of curves in the given output file are less than number_of_curves_in_plot")
            print("________________________________________________________________________________________")
            exit(0)

    return axis_readings

if __name__ == '__main__':
    #Read file and get x and y axis values in following two arrays
    readings_35_x = read_file(x_axis_colum_number, filenames[0])
    readings_45_x = read_file(x_axis_colum_number, filenames[1])
    readings_55_x = read_file(x_axis_colum_number, filenames[2])
    readings_65_x = read_file(x_axis_colum_number, filenames[3])
    readings_75_x = read_file(x_axis_colum_number, filenames[4])

    readings_35_y = []
    readings_45_y = []
    readings_55_y = []
    readings_65_y = []
    readings_75_y = []
    for column in range(y_axis_column_start, number_of_curves_in_plot + y_axis_column_start):
        readings_35_y.append(read_file(column, filenames[0]))
        readings_45_y.append(read_file(column, filenames[1]))
        readings_55_y.append(read_file(column, filenames[2]))
        readings_65_y.append(read_file(column, filenames[3]))
        readings_75_y.append(read_file(column, filenames[4]))

    #Plot all graphs in single plot
    for column in range(0, number_of_curves_in_plot):
        plt.plot(readings_35_x , readings_35_y[column], label = r"$35^{\circ}$C")
        plt.plot(readings_45_x , readings_45_y[column], label = r"$45^{\circ}$C")
        plt.plot(readings_55_x , readings_55_y[column], label = r"$55^{\circ}$C")
        plt.plot(readings_65_x , readings_65_y[column], label = r"$65^{\circ}$C")
        plt.plot(readings_75_x , readings_75_y[column], label = r"$75^{\circ}$C")
    
    plt.title(Plot_Title)
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.savefig("light-iv-temp.png")
    plt.show()
