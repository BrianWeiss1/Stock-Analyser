import csv

def read_csv_to_dictionary(file_path):
    result_dict = {}
    
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Read the first row as header (topics)
        
        for row in reader:
            for topic, content in zip(header, row):
                if topic not in result_dict:
                    result_dict[topic] = []
                result_dict[topic].append(content)
    
    return result_dict

# Example usage:
csv_file_path = 'documents/nasdaq_screener_1691093113949.csv'
your_dict = read_csv_to_dictionary(csv_file_path)
print(your_dict['Symbol'])
