import csv
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="finding duplicates")
    parser.add_argument("--check-collision",required=True, help= "<filelocation>")
    return parser.parse_args()

def initialization(inputfile): 
    try:
        with open(inputfile, mode='r') as infile:
            reader = csv.reader(infile)
            return list(reader)
    except Exception as e:
        print("error while opening file", e)

def checking_duplicates():

    iplist = initialization(inputfile=filelocation ) 
    iplist = [tuple(x) if isinstance(x, list) else x for x in iplist]
    dup = {x for x in iplist if iplist.count(x) > 1}
    return dup

def write_output(output):
    try:
        with open("output.csv", mode='w') as outfile:
          for ip in output:
              outfile.write (f"{ip}\n")
              
    except Exception as e:
        print("error while opening/writing the file", e)

if __name__ == "__main__":
    args = parse_args()
    filelocation= args.check_collision  
    myduplicates = checking_duplicates()

    if myduplicates :
        write_output(myduplicates)
    else:
        print("no collision found")
        