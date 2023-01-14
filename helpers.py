import csv ;

#config is the object that contains file locations and data for manipulations
class config :
    def __init__(self, builderFile = "./BUILDER.csv",framesFile = "./FRAMES.csv",outputFile = "./OUTPUT.csv"):
        self.builderFile = builderFile
        self.framesFile = framesFile
        self.outputFile = outputFile
    Aframes = []
    Abuilders = []
    fields = []

def dataINIT(config):
    builderCSV = config.builderFile
    framesCSV = config.framesFile  
    

    with open(framesCSV, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        config.fields = next(csvreader)
        for row in csvreader:
            config.Aframes.append(row)
    
    with open(builderCSV, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        Bfields = next(csvreader)
        for row in csvreader:
            config.Abuilders.append(row)

    return 

def syncronize(config):
    Aframes = config.Aframes
    Abuilders = config.Abuilders
    for i in Abuilders:
        for r in Aframes:
            if r[8] == i[8]:
                if r[11] != i[11]:
                    print("*Triggered* PC SKU: ",i[8]," Changed: ",i[11]," to: ",r[11])
                    i[11] = r[11]    
                if r[12] != i[12]:
                    print("*Triggered* SLC SKU: ",i[8]," Changed: ",i[12]," to: ",r[12])
                    i[12] = r[12]
                if r[13] != i[13]:
                    print("*Triggered* WH SKU: ",i[8]," Changed: ",i[13]," to: ",r[13])
                    i[13] = r[13]

def output(config):
    outputCSV = config.outputFile
    with open(outputCSV,mode='w') as csvFile:
        writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(config.fields)
        for i in config.Abuilders:
            writer.writerow(i)


def create_output (filepath1,filepath2):
    C = config(builderFile=filepath1,framesFile=filepath2)
    dataINIT(C)
    print("\nTEST_LOGS:\n")
    syncronize(C)
    output(C)
    print("\n\n\n")