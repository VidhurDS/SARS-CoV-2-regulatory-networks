with open("human_miRNA_targets_in_CoV2_all.txt", 'r') as mf:
    targets = mf.readlines()
mf.close()

all_outfile = open("all_hits_human_miRNA.txt", 'w')
energy_outfile = open("energy_hits_human_miRNA.txt.txt", 'w')
all_outfile.write("query_id	ref_id	score	energy	q_pos	r_pos	len	piden	piden_wobble\n")
energy_outfile.write("query_id	ref_id	total_score	total_energy	max_score	max_energy	Strand	Len1	Len2	Positions\n")

all_hits = []
energy_hits = []
positions = {}
for line in targets:
    line = line.strip()
    if line.startswith(">>"):
        energy_hits.append(line.strip(">>"))
        energy_outfile.write(line.strip(">>")+"\n")
    elif line.startswith(">"):
        all_hits.append(line.strip(">"))
        all_outfile.write(line.strip(">")+"\n")

freq = {}
for hit in all_hits:
    hit = hit.strip()
    e = hit.split("\t")
    m = e[0].split("|")[2]

    if m in freq:
        freq[m] += 1
    else:
        freq[m] = 1

    if m in positions:
        positions[m].append(e[5])
    else:
        positions[m] = []
        positions[m].append(e[5])


out2 = open("miRNA_frequency.txt", "w")
out2.write("miRNA\tFrequency\n")
for k in freq:
    out2.write(k+"\t"+str(freq[k])+"\n")

number_of_columns = max(freq.values())

# writing input for plot
cutoff = 10 # atleast 5 binding locations per mirna
genome_size = float(29930)
start = 0
stop = 0
out3 = open("miRNA_frequency_plot_input.txt", "w")
# out3.write("miRNA\tdistribution_across_genome\n")

o4 = open("miRNA_frequency_plot_input_4.txt", "w")
o4.write("miRNA\tgenome\n")


min_dict = {}
odict = {}
for em in positions:
    ostr = ''
    if freq[em] >= cutoff:
        # ostr = em + "\t"
        mid_pt_array = []
        for coordinates in positions[em]:
            ec = coordinates.split(" ")
            stop = max(float(ec[0]), float(ec[1]))
            start = min(float(ec[0]), float(ec[1]))
            norm_mid_point = (start + stop)/2
            mid_pt_array.append(float(norm_mid_point/genome_size))
            # o4.write(em + "\t" + (str(float(norm_mid_point/genome_size))) + "\n")
            for i in range(int(start), int(stop)+1):
                o4.write(em + "\t" + str(float(i/genome_size)) + "\n")
        # min_dict[em] = min(mid_pt_array)
        # out3.write(ostr + ("\t").join(mid_pt_array))
        na_count = number_of_columns - len(mid_pt_array)
        nstr = "\tNA" * na_count
        # mid_pt_array_sorted = list(mid_pt_array.sort())
        mid_pt_array.sort()
        mid_pt_array_2 = [str(i) for i in mid_pt_array]
        odict[em] = (("\t").join(mid_pt_array_2) + nstr)
        # out3.write(nstr + "\n")

# sorted_d = list(sorted(min_dict.items(), key=lambda x: x[1]))
# e = []
# for each in sorted_d:
#     e.append(each[0])
#     # e = e + "\"" + each[0] + "\", "
#     out3.write(each[0] + "\t" + odict[each[0]] + "\n")
#     for n in odict[each[0]].split("\t"):
#         if n != "NA":
#             o4.write(each[0] + "\t" + n + "\n")

print e