with open("", 'r') as file:
    data = file.readlines()
file.close()

all_rbps= {}
for line in data[1:]:
    line = line.strip()
    if not line.startswith("#") and len(line) > 1:
        ele = line.split("\t")
        if ele[1] in all_rbps:
            all_rbps[ele[1]] += 1
        else:
            all_rbps[ele[1]] = 1

outfile = open("RBP_frequency.txt", 'w')

# sorted_all_rbps = dict(sorted(all_rbps.items(), key = lambda kv:(float(kv[1]), kv[0])))
# sorted_all_rbps = dict(sorted(all_rbps.items(), key=lambda x: float(x[1]), reverse=True))
outfile.write("RBP\tFrequency\n")
for key in all_rbps:
    outfile.write(key + "\t" + str(all_rbps[key]) + "\n")

