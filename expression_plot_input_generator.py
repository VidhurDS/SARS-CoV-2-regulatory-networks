with open("final_GSE11879_series_matrix_quantile.txt", 'r') as file:
    data = file.readlines()
file.close()

top_mirs = ['MIR548K', 'MIR4659B', 'MIR376C', 'MIR376A1', 'MIR4662B', 'MIR548AS', 'MIR548AQ', 'MIR548AU', 'MIR548AR', 'MIR1282', 'MIR514A3', 'MIR514A2', 'MIR920', 'MIR5006', 'MIR1976', 'MIR3972', 'MIR5195']
top_mirs_2 = []

for t in top_mirs:
    t = t.replace("MIR", "")
    t = t.lower()
    t = "hsa-miR-" + t
    top_mirs_2.append(t)

tissue_index = {}
i = 0
for tis in (data[0].strip()).split("\t"):
    tis = tis.split(".")[0]
    tis = tis.replace(" Total RNA", "")
    tis = tis.replace("Human", "")
    tissue_index[i] = tis
    i += 1

for line in data[1:]:
    line = line.strip()
    ele = line.split("\t")
    mir = ele[0].replace("-5p", "")
    mir = mir.replace("-3p", "")
    if mir in top_mirs_2:
        print mir
        # if ele[1] in all_rbps:
        #     all_rbps[ele[1]] += 1
        # else:
        #     all_rbps[ele[1]] = 1

outfile = open("RBP_frequency.txt", 'w')


#
# # sorted_all_rbps = dict(sorted(all_rbps.items(), key = lambda kv:(float(kv[1]), kv[0])))
# # sorted_all_rbps = dict(sorted(all_rbps.items(), key=lambda x: float(x[1]), reverse=True))
# outfile.write("RBP\tFrequency\n")
# for key in all_rbps:
#     outfile.write(key + "\t" + str(all_rbps[key]) + "\n")
#
