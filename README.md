issue with login check name-only checking first one- adding duplicates to file-?why
adding name to spreadsheet- was expecting list[]
formatting the time correctly for comparison
separateing delete function from check date function as was repeating with each iteration
Adding 1 to index as not 0 indexed
Not recognising interger for input??
adding row in data rather than data in data resolved name spreadsheet issue. 

Date issues tried:
        # both = set(dates_list).intersection(old_data)
        # date_index =[dates_list.index(i) for i in both] 
        # needs +2 added for title and not 0 index, only returning 1 value!!


        # date_index = []
        # for i in old_data:
        #     if i in dates_list:
        #         for j in dates_list:
        #             if i == j:
        #                 if dates_list.index(i) not in date_index:
        #                     date_index.append(dates_list.index(i)+2)


https://stackoverflow.com/questions/51171314/find-indexes-of-common-items-in-two-python-lists
https://stackoverflow.com/questions/60825828/how-to-delete-column-by-user-input-in-excel-in-python-using-openpyxl
