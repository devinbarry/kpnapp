import csv
import io
import requests


class CSVImporter(object):

    def __init__(self, file_path):
        self.file_path = file_path

        with open(self.file_path) as f:
            buffer = self._process_newlines(f)

        self._process_csv_lines(buffer)

    def _process_newlines(self, input_file):
        """
        Custom implementation of 'universal newline mode'.

        Process new lines in files to prevent the universal newline mode error.

        :param input_file:
        :return: memory buffer containing the file data
        """
        # Implement 'universal newline mode'
        all_lines = input_file.read().splitlines()
        universal_newline = '\n'.join(all_lines)
        input_file.close()

        # Convert lines to a StringIO
        return io.StringIO(universal_newline)

    def _process_csv_lines(self, input_file):
        """
        Process all lines in the CSV file.

        :param input_file:
        :return: None
        """
        reader = csv.reader(input_file, dialect='excel')
        next(reader)  # header row. We ignore this

        keys = ['first_name', 'last_name', 'street', 'zip', 'city', 'image']
        for line in reader:

            # Fix empty image URL
            if not line[5]:
                line[5] = 'http://nothing.com'

            data = dict(zip(keys, line))
            print(data)

            # POST data to the REST API
            r = requests.post('http://127.0.0.1:8000/api/contacts/', data=data)
            print(r)
            print(r.text)

        input_file.close()


c = CSVImporter('/Users/devinbarry/Desktop/KPN/contact_application_data - Sheet1.csv')
