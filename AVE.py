import csv
# For the average
from statistics import mean
from collections import OrderedDict


def calculate_averages(input_file_name, output_file_name):
    dic = OrderedDict()
    with open(input_file_name) as fc:
        reader = csv.reader(fc)
        for line in reader:
            dic[line[0]] = mean([float(i) for i in line[1:]])
    with open(output_file_name, 'w', newline='') as fc:
        writer = csv.writer(fc)
        for line in dic.keys():
            list = [line, dic[line]]
            writer.writerow(list)


def calculate_sorted_averages(input_file_name, output_file_name):
    dic = OrderedDict()
    with open(input_file_name) as fc:
        reader = csv.reader(fc)
        for line in reader:
            dic[line[0]] = mean([float(i) for i in line[1:]])
    
    sorted_dict = dict(sorted(dic.items(), key=lambda x: x[1]))
    with open(output_file_name, 'w', newline='') as fc:
        writer = csv.writer(fc)
        for line in sorted_dict.keys():
            list = [line, sorted_dict[line]]
            writer.writerow(list)
    

def calculate_three_best(input_file_name, output_file_name):
    dic = OrderedDict()
    with open(input_file_name) as fc:
        reader = csv.reader(fc)
        for line in reader:
            dic[line[0]] = mean([float(i) for i in line[1:]])
    
    sorted_dict = dict(sorted(dic.items(), key=lambda x: x[1]))
    List = [i for i in sorted_dict.keys()]
    with open(output_file_name, 'w', newline='') as fc:
        writer = csv.writer(fc)
        count = 0
        for line in List[::-1]:
            list = [line, sorted_dict[line]]
            writer.writerow(list)
            count += 1
            if count == 3:
                break
    

def calculate_three_worst(input_file_name, output_file_name):
    dic = OrderedDict()
    with open(input_file_name) as fc:
        reader = csv.reader(fc)
        for line in reader:
            dic[line[0]] = mean([float(i) for i in line[1:]])
    
    sorted_dict = dict(sorted(dic.items(), key=lambda x: x[1]))
    List = [i for i in sorted_dict.keys()]
    with open(output_file_name, 'w', newline='') as fc:
        writer = csv.writer(fc)
        count = 0
        for line in List:
            list = [line, sorted_dict[line]]
            writer.writerow(list)
            count += 1
            if count == 3:
                break


def calculate_average_of_averages(input_file_name, output_file_name):
    dic = OrderedDict()
    with open(input_file_name) as fc:
        reader = csv.reader(fc)
        for line in reader:
            dic[line[0]] = mean([int(i) for i in line[1:]])
    
    with open(output_file_name, 'w', newline='') as fc:
        writer = csv.writer(fc)
        writer.writerow([mean([i for i in dic.values()])])