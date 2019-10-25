# import re
#
# ap_list = []
# new_list = []
# elem = ''
# with open('RuckusAPList.csv', 'r', encoding='utf-8') as file:
#     for line in file:
#         # my_search = re.match('("{1}[a-zA-Z0-9:_,]+"{1})', line)
#         data_list = re.split(r'""', line)
#         # mac = my_search.gr
#         # name = my_search.group(2)
#         # status = my_search.group(4)
#         data_list[0] = re.sub(r'"', '', data_list[0])
#         data_list[0] = re.sub(r',', '', data_list[0])
#         # elem = data_list[0] + " " + data_list[1] + ', ' + data_list[3] +',' + '\n'
#         elem = data_list[0] + '\n'
#         # print(mac, name, status)
#         # print(my_search)
#         new_list.append(elem)
# # print(new_list)
# with open('new_text_mac.csv', 'w', encoding='utf-8') as file_2:
#     for i in new_list:
#         file_2.write(i)

old_list = []
with open('smartzone.csv', 'r', encoding='utf-8') as old:
    for i in old:
        old_list.append(i)
with open('new_text_mac.csv', 'r', encoding='utf-8') as now:
    for n in now:
        if not n in old_list:
            print("Отсутствует точка: ", n)
