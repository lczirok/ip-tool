import csv

filelocation= 'ipcsv.csv'

def initzialization(inputfile): 
    try:
        with open(inputfile, mode='r') as infile:
            reader = csv.reader(infile)
            return list(reader)
    except Exception as e:
        print("error while opening file", e)

def checking_duplicates():

    iplist = initzialization(inputfile=filelocation ) 
    iplist = [tuple(x) if isinstance(x, list) else x for x in iplist]
    dup = {x for x in iplist if iplist.count(x) > 1}
    return dup


myduplicates = checking_duplicates()
print (myduplicates)
