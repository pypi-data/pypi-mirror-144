import pandas as pd


"""
    File name: web.py
    Author: Jacob Gerlach
    Description: Assortment of basic web request operations.
    Notes:
        * = Function has associated unit test.
"""

def read_spreadsheet(file, return_ext=False):  # *
    """Reads spreadsheet from werkzeug FileStorage object according to file mimetype.

    :param file: Werkzeug FileStorage input
    :type file: werkzeug FileStorage
    :param return_ext: If True the extension is returned with df as a tuple, defaults to False
    :type return_ext: bool, optional
    :return: pandas DataFrame if return_ext is False, else (pandas DataFrame, file extension)
    :rtype: pandas DataFrame or (pandas DataFrame, str)
    """

    # Get file MIME
    file_mime = file.content_type

    # Read CSV
    if file_mime == 'text/csv':
        file_ext = 'csv'

        # Read in data
        input_data = pd.read_csv(file)
        
    # Read TSV
    elif file_mime == 'text/tab-separated-values':
        file_ext = 'tsv'

        # Read in data
        input_data = pd.read_csv(file, sep='\t')
        
    # Read Excel
    elif (file_mime == 'application/vnd.ms-excel' or
        file_mime == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):
        file_ext = 'xlsx'

        # Read in data
        input_data = pd.read_excel(file)

    # Unsupported filetype
    else:
        raise(f'"{file_mime}" is not a supported filetype.')


    return (input_data, file_ext) if return_ext else input_data
