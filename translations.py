# English to swahili translations parser


# takes a csv file returns a tuple of two dicts
def gen_map(trans_csv_file):
    # import csv
    translations_csv = [line for line in open(trans_csv_file)]

    #parse and create mapping
    swa_to_eng = {}
    eng_to_swa = {}
    for line in translations_csv:
        if ("#" in line) or("//" in line) or ("\n" == line):
            pass #skip
        else:
            english = line.split(',')[0].strip()
            swahili = line.split(',')[1].strip()
            swa_to_eng[swahili] = english
            eng_to_swa[english] = swahili
    
    return (swa_to_eng, eng_to_swa)


