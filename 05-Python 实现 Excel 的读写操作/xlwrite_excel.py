import xlwt

wb = xlwt.Workbook()  # 新建一个 workbook 对象

sheet = wb.add_sheet('第一个sheet')

head_data = ['姓名', '地址', '手机号', '城市']
for head in head_data:
    sheet.write(0, head_data.index(head), head)
    # sheet.write(行, 列, 写入数据)

"""
另外两种写入方法：
for index, head in enumerate(head_data):
    # print(head)
    sheet.write(0, index, head)
    # sheet.write(行, 列, 插入的数据)

i = 0
for head in head_data:
    sheet.write(0, i, head)
    i += 1
"""
