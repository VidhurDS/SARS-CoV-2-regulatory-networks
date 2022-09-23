with open("filename.txt", 'r') as file:
    filenames = file.readlines()
file.close()

full_dict = {}
m_array = []
f_array = []
for fn in filenames:
    fn = fn.strip()
    with open(fn, 'r') as ci:
        in_arr = ci.readlines()
    ci.close()
    fn = fn.replace(".sf_normalized_count.txt", "")
    f_array.append(fn)
    for line in in_arr:
        line = line.strip()
        ele = line.split("\t")
        m_array.append(ele[0])
        k = fn + "|" + ele[0]
        full_dict[k] = ele[1]

top_17_mirs = ['hsa-miR-548k', 'hsa-miR-4659b', 'hsa-miR-376c', 'hsa-miR-376a1', 'hsa-miR-4662b', 'hsa-miR-548as', 'hsa-miR-548aq', 'hsa-miR-548au', 'hsa-miR-548ar', 'hsa-miR-1282', 'hsa-miR-514a3', 'hsa-miR-514a2', 'hsa-miR-920', 'hsa-miR-5006', 'hsa-miR-1976', 'hsa-miR-3972', 'hsa-miR-5195']

m_array = set(m_array)
f_array = set(f_array)

outfile = open("liver_normal_merged.txt", "w")
outfile.write("miRNA\t" + "\t".join(f_array) + "\n")

for e in m_array:
    ostr = e
    for n in f_array:
        sk = n + "|" + e
        if sk not in full_dict:
            full_dict[sk] = "NA"
        ostr = ostr + "\t" + full_dict[sk]
    outfile.write(ostr + "\n")
