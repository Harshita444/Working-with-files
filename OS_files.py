#!/usr/bin/env python
# coding: utf-8

# # Interacting with the OS and filesystem

# In[1]:


import os


# In[2]:


os.getcwd()


# In[157]:


os.listdir('.')  


# In[3]:


help(os.listdir)


# In[4]:


os.listdir('/users')


# In[159]:


os.makedirs('./dummy',exist_ok=True)


# In[160]:


#Let us download some files into the `data` directory using the `urllib` module.


# In[161]:


url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
url2 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt'
url3 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt'


# In[162]:


import urllib.request


# In[166]:


urllib.request.urlretrieve(url1,'./dummy/loans1.txt')


# In[167]:


urllib.request.urlretrieve(url2,'./dummy/loans2.txt')


# In[168]:


urllib.request.urlretrieve(url3,'./dummy/loans3.txt')


# ## Reading from the file

# In[169]:


file3=open('/dummy/loans3.txt',mode='r')


# In[170]:


file1=open('/dummy/loans1.txt', mode='r')


# The `open` function also accepts a `mode` argument to specifies how we can interact with the file. The following options are supported:
# 
# ```
#     ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     'U'       universal newline mode (deprecated)
#     ========= ===============================================================
# ```
# 
# To view the contents of the file, we can use the `read` method of the file object.

# In[171]:


file1_contents=file1.read()


# In[172]:


print(file1_contents)


# In[173]:


file1.close()


# In[174]:


file1.read()  # since file is closed now


# ## Closing file autimatically using "with"

# In[175]:


with open('./dummy/loans2.txt') as file2:
    file2_contents=file2.read()
    print(file2_contents)


# Once the statements within the `with` block are executed, the `.close` method on `file2` is automatically invoked. Let's verify this by trying to read from the file object again.

# In[176]:


file2.read()


# ### Reading file line by line

# In[177]:


with open('./dummy/loans3.txt','r') as file3:
    file3_line=file3.readlines()


# In[51]:


file3_line


# In[ ]:





# ## Processing data from files
# 
# Before performing any operations on the data stored in a file, we need to convert the file's contents from one large string into Python data types. For the file `loans1.txt` containing information about loans in a CSV format, we can do the following:
# 
# * Read the file line by line
# * Parse the first line to get a list of the column names or headers
# * Split each remaining line and convert each value into a float
# * Create a dictionary for each loan using the headers as keys
# * Create a list of dictionaries to keep track of all the loans
# 
# Since we will perform the same operations for multiple files, it would be useful to define a function `read_csv`. We'll also define some helper functions to build up the functionality step by step. 
# 
# Let's start by defining a function `parse_header` that takes a line as input and returns a list of column headers.

# In[178]:


file3_line[0].strip()


# In[179]:


def parse_header(header_line):
    return header_line.strip().split('.')
    


# In[180]:


file3_line[0]


# In[181]:


headers=parse_header(file3_line[0])


# In[182]:


headers


# In[183]:


def parse_values(data_line):
    values=[]
    for item in data_line.strip().split(','):
        values.append(float(item))
    return values


# In[184]:


file3_line[1].strip().split(',')


# In[185]:


file3_line[1].strip()


# In[186]:


file3_line[2].strip().split(',')


# In[187]:


parse_values(file3_line[1])


# In[188]:


def parse_values(data_line):
    values=[]
    for item in data_line.strip().split(','):
        if item =='':
            values.append(0.0)
        else:
            values.append(float(item))
    return values


# In[189]:


file3_line[2]


# In[190]:


parse_values(file3_line[2])


# In[191]:


def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        if item == '':
            values.append(0.0)
        else:
            try:
                values.append(float(item))
            except ValueError:
                values.append(item)
    return values


# In[192]:


parse_values(file3_line[2])


# In[193]:


def create_item_dict(values, headers):
    result = {}
    for value, header in zip(values, headers):
        result[header] = value
    return result


# In[194]:


values1 = parse_values(file3_line[1])
create_item_dict(values1, headers)


# In[195]:


values1 = parse_values(file3_line[1])


# In[196]:


create_item_dict(values1, headers)


# In[197]:


def read_csv(path):
    result = []
    # Open the file in read mode
    with open(path, 'r') as f:
        # Get a list of lines
        lines = f.readlines()
        # Parse the header
        headers = parse_headers(lines[0])
        # Loop over the remaining lines
        for data_line in lines[1:]:
            # Parse the values
            values = parse_values(data_line)
            # Create a dictionary using values & headers
            item_dict = create_item_dict(values, headers)
            # Add the dictionary to the result
            result.append(item_dict)
    return result


# In[198]:


with open('./dummy/loans2.txt') as file2:
    print(file2.read())


# In[199]:


def parse_headers(header_line):
    return header_line.strip().split(',')

def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        if item == '':
            values.append(0.0)
        else:
            try:
                values.append(float(item))
            except ValueError:
                values.append(item)
    return values

def create_item_dict(values, headers):
    result = {}
    for value, header in zip(values, headers):
        result[header] = value
    return result

def read_csv(path):
    result = []
    # Open the file in read mode
    with open(path, 'r') as f:
        # Get a list of lines
        lines = f.readlines()
        # Parse the header
        headers = parse_headers(lines[0])
        # Loop over the remaining lines
        for data_line in lines[1:]:
            # Parse the values
            values = parse_values(data_line)
            # Create a dictionary using values & headers
            item_dict = create_item_dict(values, headers)
            # Add the dictionary to the result
            result.append(item_dict)
    return result


# In[200]:


import math

def loan_emi(amount, duration, rate, down_payment=0):
    """Calculates the equal montly installment (EMI) for a loan.
    
    Arguments:
        amount - Total amount to be spent (loan + down payment)
        duration - Duration of the loan (in months)
        rate - Rate of interest (monthly)
        down_payment (optional) - Optional intial payment (deducted from amount)
    """
    loan_amount = amount - down_payment
    try:
        emi = loan_amount * rate * ((1+rate)**duration) / (((1+rate)**duration)-1)
    except ZeroDivisionError:
        emi = loan_amount / duration
    emi = math.ceil(emi)
    return emi


# In[201]:


loans2=read_csv('./dummy/loans2.txt')


# In[202]:


loans2


# In[203]:


for loan in loans2:
    loan['emi'] = loan_emi(loan['amount'], 
                           loan['duration'], 
                           loan['rate']/12, # the CSV contains yearly rates
                           loan['down_payment'])


# In[204]:


loans2


# In[205]:


def compute_emis(loans):
    for loan in loans:
        loan['emi']=loan_emi(
        loan['amount'],
        loan['duration'],
        loan['rate']/12,
        loan['down_payment'])


# ## Writing to the file

# In[206]:


loans=read_csv('./dummy/loans2.txt')


# In[207]:


compute_emis(loans2)


# In[152]:


loans2


# In[208]:


with open('/dummy/loans2.txt','w') as f:
    for loan in loans2:
        f.write('{}.{},{},{},{}\n'.format(
        loan['amount'],
        loan['duration'],
        loan['rate'],
        loan['down_payment'],
        loan['emi']))


# In[209]:


def write_csv(items, path):
    # Open the file in write mode
    with open(path, 'w') as f:
        # Return if there's nothing to write
        if len(items) == 0:
            return
        
        # Write the headers in the first line
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')
        
        # Write one item per line
        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(','.join(values) + "\n")


# In[211]:


for i in range(1,4):
    loans = read_csv('./dummy/loans{}.txt'.format(i))
    compute_emis(loans)
    write_csv(loans, './dummy/emis{}.txt'.format(i))


# In[212]:


jovian.commit()


# In[ ]:




