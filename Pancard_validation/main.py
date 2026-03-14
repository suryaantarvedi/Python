import pandas as pd
import re

df= pd.read_excel('PAN Number Validation Dataset.xlsx')
# print(df.head(10))
print("total  records:" ,len(df))
total_records = len(df)


# we care coverting the data frame into string because here data frame is a object

df["Pan_Numbers"] = df["Pan_Numbers"].astype('string').str.strip().str.upper()
# print(df.head(10))



#checking the missing values

# print('\n')
# print(df[df['Pan_Numbers']==""])   # python treates blank values differently
# print(df[df['Pan_Numbers'].isna()])  #  <NA> null values treated as pandas 


# changing the 2 values into na for clarity to the python

# df = df.replace({"Pan_Numbers":''},pd.NA) 
# print(df[df['Pan_Numbers']==''])
# print(df[df['Pan_Numbers'].isna()])


#dropping the na values

df = df.replace({"Pan_Numbers":''},pd.NA).dropna(subset="Pan_Numbers")
print("total records after  removing empty records:" ,len(df))



# # printing the unique values

print('Unique values = ', df["Pan_Numbers"].nunique())
# print("total no.of records:" ,len(df))



# # dropping the duplicate values:

df = df.drop_duplicates(subset="Pan_Numbers", keep='first')
print('Total records after duplicates = ',len(df))


#checking the pan

# def adjacent_repitition(pan): # AABCD, ABCDX
#     for i in range(len(pan)-1):
#         if pan[i] == pan[i+1]:
#             return True 
#     return False 


#List Comphernsion
def adjacent_repitition(pan):
    return any(pan[i] == pan[i+1] for i in range(len(pan)-1))

# print(adjacent_repitition('AABCD'))
# print(adjacent_repitition('FGHHH'))
# print(adjacent_repitition('ABCDX'))
# print(adjacent_repitition('MNJPQ'))


# checking the sequence of the data

# def is_sequencial(pan): #ABCDE , ACFGT
#     for i in range(len(pan)-1):
#         if ord(pan[i+1]) - ord(pan[i]) != 1:
#             return False 
#     return True


#list comphernshion
def is_sequencial(pan): 
    return all(ord(pan[i+1]) - ord(pan[i]) == 1 for i in range(len(pan)-1))


# print(is_sequencial('ABCDE'))
# print(is_sequencial('MNOPQ'))
# print(is_sequencial('ABCXY'))
# print(is_sequencial('XYZAB'))

#combining all the methods

def is_valid_pan(pan):
    if len(pan) != 10:
        return False 
    
    if not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', pan):
        return False 
    
    if adjacent_repitition(pan):
        return False 
    
    if is_sequencial(pan):
        return False
    
    return True

df["Status"] = df["Pan_Numbers"].apply(lambda x: "Valid" if is_valid_pan(x) else "Invalid")
print(df.head(10))


#finding the valid and invalid

valid_pan = (df["Status"]=='Valid').sum()
invalid_pan = (df["Status"]=='Invalid').sum()
missing_pan = total_records - (valid_pan+invalid_pan)


#printing the total data

print('Total records = ', total_records)
print('Valid = ', valid_pan)
print('Invalid = ', invalid_pan)
print('Missing = ', missing_pan)

# summary of the program

df_summary = pd.DataFrame({ "TOTAL PROCESSED RECORDS":[total_records]
                           ,"TOTAL VALID COUNT": [valid_pan]
                           ,"TOTAL INVALID COUNT": [invalid_pan]
                           ,"TOTAL MISSING PANS": [missing_pan]})
print(df_summary.head())


#adding the values to the excel sheet
with pd.ExcelWriter("PANCARD VALIDATION RESULT.xlsx") as writer:
    df.to_excel(writer, sheet_name="PANCARD Validations",index=False)
    df_summary.to_excel(writer, sheet_name="SUMMARY",index=False)