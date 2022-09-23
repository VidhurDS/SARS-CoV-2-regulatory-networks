
with open("cervical_normal.txt", 'r') as c:
    cervical_array = c.readlines()
c.close()

with open("heart_normal.txt", 'r') as h:
    heart_array = h.readlines()
h.close()

with open("liver_normal.txt", 'r') as lv:
    liver_array = lv.readlines()
lv.close()

with open("larynx_nomral.txt", 'r') as lx:
    larynx_array = lx.readlines()
lx.close()

with open("lung_normal.txt", 'r') as lu:
    lung_array = lu.readlines()
lu.close()

with open("ovary_normal.txt", 'r') as ov:
    ovary_array = ov.readlines()
ov.close()

with open("thymus_normal.txt", 'r') as ty:
    thymus_array = ty.readlines()
ty.close()


def mir_cleaner(m_str):
    t = m_str.strip()
    t = t.lower()
    out_mir = t.replace("-5p", "")
    out_mir = out_mir.replace("-3p", "")
    return out_mir


def mean_calculator(lst):
    temp = []
    for el in lst:
        if el != "NA":
            temp.append(el)
    lst2 = [float(i) for i in temp]
    avg = sum(lst2) / len(lst2)
    avg = round(avg, 2)
    return avg


cv_dict = {}
for line in cervical_array[1:]:
    line = line.strip()
    ele = line.split("\t")
    val = mean_calculator(ele[1:])
    mir = mir_cleaner(ele[0])
    if mir in cv_dict:
        cv_dict[mir] = max(cv_dict[mir], val)
    else:
        cv_dict[mir] = val


h_dict = {}         #
for line in heart_array[1:]:         #
    line = line.strip()
    ele = line.split("\t")
    val = mean_calculator(ele[1:])
    mir = mir_cleaner(ele[0])
    if mir in h_dict:         #
        h_dict[mir] = max(h_dict[mir], val)         ##
    else:
        h_dict[mir] = val         #


lx_dict = {}         #
for line in larynx_array[1:]:         #
    line = line.strip()
    ele = line.split("\t")
    val = mean_calculator(ele[1:])
    mir = mir_cleaner(ele[0])
    if mir in lx_dict:         #
        lx_dict[mir] = max(lx_dict[mir], val)         ##
    else:
        lx_dict[mir] = val         #

lv_dict = {}         #
for line in liver_array[1:]:         #
    line = line.strip()
    ele = line.split("\t")
    val = mean_calculator(ele[1:])
    mir = mir_cleaner(ele[0])
    if mir in lv_dict:         #
        lv_dict[mir] = max(lv_dict[mir], val)         ##
    else:
        lv_dict[mir] = val         #


ln_dict = {}         #
for line in lung_array[1:]:         #
    line = line.strip()
    ele = line.split("\t")
    val = mean_calculator(ele[1:])
    mir = mir_cleaner(ele[0])
    if mir in ln_dict:         #
        ln_dict[mir] = max(ln_dict[mir], val)         ##
    else:
        ln_dict[mir] = val         #

ov_dict = {}         #
for line in ovary_array[1:]:         #
    line = line.strip()
    ele = line.split("\t")
    val = mean_calculator(ele[1:])
    mir = mir_cleaner(ele[0])
    if mir in ov_dict:         #
        ov_dict[mir] = max(ov_dict[mir], val)         ##
    else:
        ov_dict[mir] = val         #


ty_dict = {}         #
for line in thymus_array[1:]:         #
    line = line.strip()
    ele = line.split("\t")
    val = mean_calculator(ele[1:])
    mir = mir_cleaner(ele[0])
    if mir in ty_dict:         #
        ty_dict[mir] = max(ty_dict[mir], val)         ##
    else:
        ty_dict[mir] = val         #

master_mir = list(cv_dict.keys()+h_dict.keys()+lx_dict.keys()+lv_dict.keys()+ln_dict.keys()+ov_dict.keys()+ty_dict.keys())
master_mir = list(set(master_mir))


# common checker
top_mirs_1 = ['hsa-miR-548k', 'hsa-miR-4659b', 'hsa-miR-376c', 'hsa-miR-376a', 'hsa-miR-4662b', 'hsa-miR-548as', 'hsa-miR-548aq', 'hsa-miR-548au', 'hsa-miR-548ar', 'hsa-miR-1282', 'hsa-miR-514a3', 'hsa-miR-514a', 'hsa-miR-920', 'hsa-miR-5006', 'hsa-miR-1976', 'hsa-miR-3972', 'hsa-miR-5195']
top_mirs = [x.lower() for x in top_mirs_1]

def common(a,b):
    temp = []
    for e in a:
        if e.lower() in b:
            temp.append(e.lower())
        else:
            print e.lower()
    return temp


d=common(top_mirs,master_mir)
print(len(d))

outfile = open("expression_merged.txt", "w")
outfile.write("miRNA\tCervical epithelium\tHeart\tLarynx\tLiver\tLung bronchiola\tOvary\tThymus\n")

outfile2 = open("top_mir_expression_merged.txt", "w")
outfile2.write("miRNA\tCervical epithelial cells\tHeart\tLarynx\tLiver\tLung bronchial epithelial cells\tOvary\tThymus\n")


for k in master_mir:
    if k not in cv_dict: cv_dict[k] = "NA"
    if k not in h_dict: h_dict[k] = "NA"
    if k not in lx_dict: lx_dict[k] = "NA"
    if k not in lv_dict: lv_dict[k] = "NA"
    if k not in ln_dict: ln_dict[k] = "NA"
    if k not in ov_dict: ov_dict[k] = "NA"
    if k not in ty_dict: ty_dict[k] = "NA"
    outfile.write(k + "\t" + str(cv_dict[k]) + "\t" + str(h_dict[k]) + "\t" + str(lx_dict[k]) + "\t" + str(lv_dict[k]) + "\t" + str(ln_dict[k]) + "\t" + str(ov_dict[k]) + "\t" + str(ty_dict[k]) + "\n")
    if k in top_mirs:
        outfile2.write(k + "\t" + str(cv_dict[k]) + "\t" + str(h_dict[k]) + "\t" + str(lx_dict[k]) + "\t" + str(
            lv_dict[k]) + "\t" + str(ln_dict[k]) + "\t" + str(ov_dict[k]) + "\t" + str(ty_dict[k]) + "\n")
