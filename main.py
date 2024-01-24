import pytest
import os
import logging

logging.basicConfig(level=logging.DEBUG)

def test_verify_txt_file():
    filename = 'output.txt' 
    logging.debug('Verifying file exists...')
    try:
        assert os.path.exists(filename)
        logging.debug('File exists.')
    except AssertionError:
        logging.debug("File does not exist")

    with open(filename, 'r') as file:
        data = file.read()
        logging.debug('Verifying file content...')
        try:
            assert 'Hello!' in data
            logging.debug('Expected string found in file.')
        except AssertionError:
            logging.debug("Expected string not found in file")  

if __name__ == '__main__':
    test_verify_txt_file()