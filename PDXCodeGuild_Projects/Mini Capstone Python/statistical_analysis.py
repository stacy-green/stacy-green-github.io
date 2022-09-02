"""
Let's write a program that calculates and displays statistical data
Goals:
    Calculate the distribution of a dataset
    Display that data

    T-tests
        -Independent t-test
        -Paired t-test
        -One sample t-test

Stretch Goals:
    Chi-square test
    ANOVA
    Z-test
    MANOVA (Multivariant ANOVA)
"""

#######################################################################################################

""" Import modules """

import requests
import random

#######################################################################################################

""" Functions for mathematical operations """

def mean(dataset):
    n = len(dataset)
    sum = 0
    for num in dataset:
        sum += num
    mean = sum / n
    return mean

def sum_of_squares(mean: float, dataset: list): # mean and list of values
    sum = 0 
    for num in dataset:
        sum += ((num - mean) ** 2)
    return sum

def variance(sum_of_squares: float, dataset: list): # sum of squares and list of values
    n = len(dataset)
    variance = sum_of_squares/(n-1)
    return variance

def standard_deviation(variance: float): # variance and list of values
    standard_deviation = variance ** (1/2)
    return standard_deviation

#######################################################################################################

""" API """
# This project uses FakerAPI to generate fake people, including email, phone, gender, DoB etc
subject_data_request = requests.get('https://fakerapi.it/api/v1/persons?_quantity=100')
subject_data_request_unpacked = subject_data_request.json()
# print(subject_data_request_unpacked)
subject_data = subject_data_request_unpacked['data']
# print(subject_data)

#######################################################################################################

""" Data """

dataset = []
for index, data in enumerate(subject_data):
    subject = {}
    subject_ID = index + 1
    gender = data['gender']
    if gender == 'male':
        dependent_value = (random.randint(30 , 60) + random.randint(30 , 60))
        # dependent_value = (random.randint(30 , 60) + random.randint(40 , 50))
    elif gender == 'female':
        dependent_value = (random.randint(24, 54) + random.randint(24, 54))
        # dependent_value = (random.randint(24, 54) + random.randint(38, 48))
    subject['ID'] = subject_ID
    subject['gender'] = gender
    subject['dependent value'] = dependent_value
    dataset.append(subject)
# print(dataset)

dataset_2 = []
for index, data in enumerate(subject_data):
    subject = {}
    subject_ID = index + 1
    gender = data['gender']
    if gender == 'male':
        dependent_value = (random.randint(20 , 50) + random.randint(20 , 50))
        # dependent_value = (random.randint(30 , 60) + random.randint(40 , 50))
    elif gender == 'female':
        dependent_value = (random.randint(14, 44) + random.randint(14, 44))
        # dependent_value = (random.randint(24, 54) + random.randint(38, 48))
    subject['ID'] = subject_ID
    subject['gender'] = gender
    subject['dependent value'] = dependent_value
    dataset_2.append(subject)
#######################################################################################################

""" Classes """

class Dataset:
    def __init__(self, dataset: list):
        self.dependent_variable_name = 'weight'
        self.dependent_variable_type = 'ratio'
        self.dependent_variable_data_type = 'continuous'
        self.independent_variable_name = 'gender'
        self.independent_variable_type = 'nominal'
        self.independent_variable_data_type = 'discrete'
        self.subject_IDs = []
        for subject in dataset:
            self.subject_IDs.append(subject.get('ID'))
        self.dependent_values = []
        for subject in dataset:
            self.dependent_values.append(subject.get('dependent value'))
        self.independent_values = []
        for subject in dataset:
            self.independent_values.append(subject.get('gender'))
    
    def print_data(self):
        return f' Subject IDs: {self.subject_IDs} \nDependent Variable Values: {self.dependent_values} \nIndependent Variable Values: {self.independent_values}\n'

    def __str__(self):
        return f'ID: Identification number\nGender: Male = 0, Female = 1\nDependent Variable Name: {self.dependent_variable_name}\nDependent Variable Type: {self.dependent_variable_type}\nDependent Data Type: Continuous\nIndependent Variable Name: Gender\nIndependent Variable Type: Nominal\nIndependent Data Type: Discrete\n'

class Distribution: 
    def __init__(self, dependent_values: list): # Dataset will be a list of dependent variable values
        self.mean = mean(dependent_values)
        self.sum_of_squares = sum_of_squares(self.mean, dependent_values)
        self.variance = variance(self.sum_of_squares, dependent_values)
        self.standard_deviation = standard_deviation(self.variance)
    
    def __str__(self):
        return f'mean: {self.mean} \nsum of squares: {self.sum_of_squares} \nvariance: {self.variance} \nSD: {self.standard_deviation}\n'

    # def visualize():
    #     pass
        
class Independent_t_test:
    def __init__(self, dataset):
        self.sample_1 = []
        self.sample_2 = []
        for subject in dataset:
            if subject.get('gender') == 'male':
                self.sample_1.append(subject.get('dependent value'))
            elif subject.get('gender') == 'female':
                self.sample_2.append(subject.get('dependent value'))
        # print(self.sample_1, self.sample_2)

        self.sample_1_distribution = Distribution(self.sample_1)
        self.sample_1_mean = self.sample_1_distribution.mean
        self.sample_1_sum_of_squares = self.sample_1_distribution.sum_of_squares
        self.sample_1_variance = self.sample_1_distribution.variance
        self.sample_1_standard_deviation = self.sample_1_distribution.standard_deviation

        self.sample_2_distribution = Distribution(self.sample_2)
        self.sample_2_mean = self.sample_2_distribution.mean
        self.sample_2_sum_of_squares = self.sample_2_distribution.sum_of_squares
        self.sample_2_variance = self.sample_2_distribution.variance
        self.sample_2_standard_deviation = self.sample_2_distribution.standard_deviation

        self.degrees_of_freedom = len(self.sample_1) + len(self.sample_2) - 2
        self.common_variance = (self.sample_1_sum_of_squares + self.sample_2_sum_of_squares) / self.degrees_of_freedom
        self.t_value = (self.sample_1_mean - self.sample_2_mean)/(((self.common_variance/len(self.sample_1))+(self.common_variance/len(self.sample_2)))**(1/2))


    def __str__(self):
        return f'Sample 1 size: {len(self.sample_1)}\nSample 1 mean: {self.sample_1_mean}\nSample 1 SD: {self.sample_1_standard_deviation}\nSample 2 size: {len(self.sample_2)}\nSample 2 mean: {self.sample_2_mean}\nSample 2 SD: {self.sample_2_standard_deviation}\nt-value: {self.t_value}\nDegrees of Freedom: {self.degrees_of_freedom}'

class Single_sample_t_test:
    def __init__(self, dataset):
        self.sample = []
        for subject in dataset:
            self.sample.append(subject.get('dependent value'))
        self.sample_distribution = Distribution(self.sample)
        self.sample_mean = self.sample_distribution.mean
        self.sample_standard_deviation = self.sample_distribution.standard_deviation
        self.postulated_mean = float(input("Enter postulated mean: \n\t> "))

        self.degrees_of_freedom = len(self.sample) - 1
        self.t_value = ((self.sample_mean - self.postulated_mean)/self.sample_standard_deviation)*(len(self.sample)**(1/2))
    
    def __str__(self):
        return f'Sample size: {len(self.sample)}\n Sample mean: {self.sample_mean}\nSample SD: {self.sample_standard_deviation}\nPostulated mean: {self.postulated_mean}\nT-value: {self.t_value}\nDegrees of Freedom: {self.degrees_of_freedom}'

class Paired_sample_t_test:
    def __init__(self, dataset_1: list, dataset_2: list):
        self.sample_size = len(dataset_1)
        self.degrees_of_freedom = self.sample_size - 1
        self.differences = []
        for x in range(self.sample_size):
            self.differences.append(dataset_1[x].get('dependent value') - dataset_2[x].get('dependent value'))
        self.sum_differences = 0
        for difference in self.differences:
            self.sum_differences += difference
        self.sum_differences_squared = 0
        for difference in self.differences:
            self.sum_differences_squared += (difference ** 2)
        self.t_value = self.sum_differences / (((self.sample_size * (self.sum_differences_squared))-(self.sum_differences**2) / self.degrees_of_freedom)**(1/2))
    
    def __str__(self):
        return f'Sample size: {self.sample_size}\nDegrees of Freedom" {self.degrees_of_freedom}\nT-value: {self.t_value}'
    
#########################################################################################################

""" Testing """

test_data = Dataset(dataset)
independent_t_test = Independent_t_test(dataset)
print(independent_t_test)
print()
single_sample_t_test = Single_sample_t_test(dataset)
print(single_sample_t_test)
print()
paired_sample_t_test = Paired_sample_t_test(dataset, dataset_2)
print(paired_sample_t_test)