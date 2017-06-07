import xlrd
def open_excel(file= 'appData.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print (str(e))

def get_colnum(by_index=0):
    data=open_excel()
    table=data.sheet_by_index(by_index)
    return table.ncols

def get_table(by_index=0):
	data = open_excel()
	return data.sheet_by_index(by_index)

def get_colvalue(by_index):
	table=get_table()
	colval_hasnull=table.col_values(by_index)
	colval = filter(lambda x: x !="", colval_hasnull)
	return list(colval)


def main():
 #  tables = excel_table_byindex()
 #  for row in tables:
 #      print (row)
    colvalue=get_colvalue(0)
    print (len(colvalue))
    print(get_colnum())
##   for val in colvalue:
#	    print(val)

if __name__=="__main__":
    main()