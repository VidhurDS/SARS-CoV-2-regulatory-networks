with open("mir_binding_freq.txt", 'r') as file:
    mir_freq = file.readlines()
file.close()

mirs = []
for line in mir_freq[1:]:
    line = line.strip()
    ele = line.split("\t")
    mirs.append(ele[0])

with open("human.srna.cpm.txt", 'r') as file2:
    exp_data = file2.readlines()
file2.close()

fantom_header = exp_data[0].strip().split("\t")

# feed key values of tissue ids here
with open("human.srna.samples_v2.tsv", 'r') as file3:
    cell_code = file3.readlines()
file3.close()

code_dict = {}
for line in cell_code[1:]:
    line = line.strip()
    ele = line.split("\t")
    code_dict[ele[0]] = ele[4]

# create output file
outfile = open("heatmap_top_mir_expression_v2.txt", "w")

# convert the fantom header array into the new header and print to output file
outh = []
for e in fantom_header[1:]:
    if e in code_dict:
        outh.append(code_dict[e])
    else:
        outh.append("NA")

# creating tissue name - index dictionary
index_dict = {}
i = 1
for o in outh:
    if o in index_dict:
        index_dict[o].append(i)
    else:
        index_dict[o] = []
        index_dict[o].append(i)
    i += 1

unique_tissues = list(index_dict.keys())
print len(unique_tissues)
str_outh = "\t".join(unique_tissues)
outfile.write("miRNA\t" + str_outh + "\n")

for line in exp_data[1:]:
    line = line.strip()
    ele = line.split("\t")
    mir = ele[0]
    if mir in mirs:
        outfile.write(mir)
        for tissue in unique_tissues:
            indices = index_dict[tissue]
            sum_val = float(0)
            avg = float(0)
            for i in indices:
                sum_val += float(ele[i])
            avg = float(sum_val)/float(len(indices))
            outfile.write("\t" + str(avg))
        outfile.write("\n")
