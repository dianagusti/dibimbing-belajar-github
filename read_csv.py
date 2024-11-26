import csv

def read_csv(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"File {file_path} not found.")

if __name__ == "__main__":
    read_csv('username.csv')
