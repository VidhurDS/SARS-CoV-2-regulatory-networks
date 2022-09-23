with open("ensmbl_GRCH38_miRNAs_2.txt", 'r') as mf:
    mir_fa = mf.readlines()
mf.close()

# file clean up
id_seq = {}
s = ''
mids= []
for line in mir_fa:
    line = line.strip()
    if line.startswith(">"):
        k = line
        mids.append(k)
        s = ''
    else:
        s = line.strip()
        if k in id_seq:
            id_seq[k] += s
        else:
            id_seq[k] = s


# splitting into 10 files

count = 1
# initiate first file
set_num = 1
fn = "ensmbl_GRCH38_miRNAs_" + str(set_num) + ".fa"
outfile = open(fn, 'w')
scf = open("script_file.txt", 'w')
scf.write("cd /data2/Vidhur/miranda/miRanda-3.3a\n")
scf.write("nohup miranda /data2/Vidhur/miranda/split_input/" + fn + " /data2/Vidhur/miranda/SARS-Cov2_Wuhan-Hu-1_complete_genome.fa -strict -out /data2/Vidhur/miranda/split_output/human_miRNA_targets_in_CoV2"+ str(set_num) +".txt &\n\n")

for fid in mids:
    if count == 100:
        outfile.close()
        count = 1
        set_num += 1
        fn = "ensmbl_GRCH38_miRNAs_" + str(set_num) + ".fa"
        outfile = open(fn, 'w')
        scf.write("cd /data2/Vidhur/miranda/miRanda-3.3a\n")
        scf.write("nohup miranda /data2/Vidhur/miranda/split_input/" + fn + " /data2/Vidhur/miranda/SARS-Cov2_Wuhan-Hu-1_complete_genome.fa -strict -out /data2/Vidhur/miranda/split_output/human_miRNA_targets_in_CoV2"+ str(set_num) +".txt &\n\n")

    outfile.write(fid + "\n")
    outfile.write(id_seq[fid] + "\n")
    count += 1
