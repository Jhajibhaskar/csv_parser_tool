import argparse
import csv
import math

def load_file(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def count_rows(data):
    return len(data)

def calculate_mean(data, column):
    column_sum = sum(float(row[column]) for row in data)
    return column_sum / len(data)

def filter_rows(data, column, value):
    return [row for row in data if row[column] == value]

def sort_rows(data, column):
    return sorted(data, key=lambda row: row[column])

def calculate_standard_deviation(data, column):
    column_mean = calculate_mean(data, column)
    column_values = [float(row[column]) for row in data]
    squared_differences = [(value - column_mean)**2 for value in column_values]
    variance = sum(squared_differences) / len(data)
    return math.sqrt(variance)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSV Parser')
    parser.add_argument('file', help='CSV file to parse')
    args = parser.parse_args()

    data = load_file(args.file)

    while True:
        command = input('> ')

        if command.startswith('load'):
            parts = command.split(' ')
            filename = parts[1]
            data = load_file(filename)
            print(f'Loaded {len(data)} rows from {filename}')
        elif command == 'count':
            count = count_rows(data)
            print(f'{count} rows')
        elif command.startswith('mean'):
            parts = command.split(' ')
            column = parts[1]
            mean = calculate_mean(data, column)
            print(f'Mean of {column}: {mean}')
        elif command.startswith('filter'):
            parts = command.split(' ')
            column = parts[1]
            value = parts[2]
            filtered_data = filter_rows(data, column, value)
            print(f'{len(filtered_data)} rows where {column} is {value}')
        elif command.startswith('sort'):
            parts = command.split(' ')
            column = parts[1]
            sorted_data = sort_rows(data, column)
            print(f'Sorted by {column}')
            for row in sorted_data:
                print(row)
        elif command.startswith('stddev'):
            parts = command.split(' ')
            column = parts[1]
            stddev = calculate_standard_deviation(data, column)
            print(f'Standard deviation of {column}: {stddev}')
        elif command == 'exit':
            break
        else:
            print(f'Unknown command: {command}')
