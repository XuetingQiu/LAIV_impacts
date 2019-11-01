#JumpExtractor.py: Extracts Markov jump counts from a full jump history log file.
#need to update source with discrete trait state, infile path and the counts in the log file. here it is 9001. 

def main():
    source = ['EAP','ECA','LAC','MENA','SAS','U','USA','V']

#    for clock in range(7):
    infile = open("H3N2-0405-GlobalTX-trait-USnoSea_geo_compjumpHistory-comb.log", "r")
    count = {}
    for line in infile:
        jumps = line.split("},{")
        for i in jumps:
            packet = i.split(",")
            if packet[2]+" "+packet[3] in count:
                count[packet[2]+" "+packet[3]] += 1/9001
            else:
                count[packet[2]+" "+ packet[3]] = 1/9001
        for x in source:
            for y in source:
                if x != y:
                    if x+" "+y not in count:
                        count[x+" "+y] = 0
    report = list(count.items())
    report.sort()
    for item in report:
        locations, average = item
        print(locations,average)
    infile.close()

main()