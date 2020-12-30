"""
count columns in query
"""

fields = "object, kad_num, kad_kvartal, segment, code, code_vri, kad_num_near, " \
         "data, vid_doc, name, square, info, vid, vri, vio, source, nature, opis," \
         "date_post, category, kad_pre_price, date_price, date_egrn, date_approve," \
         " num_act, date_act_approve, doc_name, date_begin, date_claim, " \
         "  date_last_change, okato, kladr, oktmo, fias, index, area, city, " \
         "         community, street, element, another_address, note, restrictions, " \
         "            complex, reestr, num_act_gbu, upks, date_gbu, price"


for i,j in enumerate(fields.split(",")):
    print(f"{i} {j}")
    