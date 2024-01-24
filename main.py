import pytest
import os

def test_verify_txt_file():
    filename = 'output.txt' 
    print('Verifying file exists...')
    try:
        assert os.path.exists(filename)
        print('File exists.')
    except AssertionError:
        print("File does not exist")

    with open(filename, 'r') as file:
        data = file.read()
        print('Verifying file content...')
        try:
            assert 'Hello!' in data
            print('Expected string found in file.')
        except AssertionError:
            print("Expected string not found in file")  

if __name__ == '__main__':
    test_verify_txt_file()