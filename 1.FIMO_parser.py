with open("Fimo_calc.txt", 'r') as file:
    fimo_out = file.readlines()
file.close()

freq = {}
positions = {}
genome_size = float(29903)


def mid_point_extractor(s,p):
    s = float(s)
    p = float(p)
    mp = float((s + p)/2)
    pos = (float(mp/genome_size))
    return pos


outfile = open("mir_binding_out_v2.txt", 'w')
outfile.write("miRNA	genome\n")
for line in fimo_out[1:]:
    line = line.strip()
    ele = line.split("\t")
    mir = ele[0]
    p_val = float(ele[8])
    if p_val <= 0.05:
        # frequency counting
        if mir in freq:
            freq[mir] += 1
        else:
            freq[mir] = 1

        # appending positions
        if mir in positions:
            positions[mir].append(str(ele[4]) + "," + str(ele[5]))
        else:
            positions[mir] = []
            positions[mir].append(str(ele[4]) + "," + str(ele[5]))

outfile2 = open("mir_binding_freq.txt", 'w')
outfile2.write("miRNA	Frequency\tminimun_value\n")
min_val = {}
for mir in freq:
    if freq[mir] >= 15:
        for p in positions[mir]:
            e = p.split(",")
            val = mid_point_extractor(e[0], e[1])
            outfile.write(mir + "\t" + str(val) + "\n")
            if mir in min_val:
                min_val[mir].append(val)
            else:
                min_val[mir] = []
                min_val[mir].append(val)
        outfile2.write(mir + "\t" + str(freq[mir]) + "\t" + str(min(min_val[mir]))  + "\n")
