import src.StockReader as reader


def ChooseRandColor(barcode, size, northStock):
    if barcode in northStock['MY20'].stock.keys():
        stock = northStock['MY20'].stock
    elif barcode in northStock['MY21'].stock.keys():
        stock = northStock['MY21'].stock

    for size_color in stock[barcode].size_color_dict.keys():
        if size_color[0] == size:
            return size_color[1]

def main():
    stock2020path = r'C:\Users\Shahaf\Documents\North Kiteboarding Israel\North 2021\Games\Orderform North Kiteboarding 2020 Export Updated Prices.xlsx'
    stock2021path = r'C:\Users\Shahaf\Documents\North Kiteboarding Israel\North 2021\Games\Orderform North Kiteboarding 2021 Export.xlsx'
    header_row_2020 = 10
    header_row_2021 = 11
    my20 = reader.ReadStockFromExel(stock2020path, 'MY20', header_row_2020)
    my21 = reader.ReadStockFromExel(stock2021path, 'MY21', header_row_2021)
    northStock = {'MY20' : my20, 'MY21' : my21}
    total_sum_ex = 0
    total_sum_ran = 0
    stock_dict = {}
    f = open(r'C:\Users\Shahaf\Desktop\stock.txt', 'r')
    for i,line in enumerate(f):
        if i == 0:
            continue
        splitted_line = line.split('\t')
        item_details = splitted_line[0]
        splitted_item = item_details.split(',')
        barcode = splitted_item[-1].split(' ')[2].strip()
        if i > 42:
            size =  splitted_item[1].strip()
            color = ChooseRandColor(barcode, size, northStock)
        else:
            color = splitted_item[1].strip()
            size = splitted_item[2].strip()
        amount = int(splitted_line[7])
        stock_dict[(barcode, color, size)] = amount

    for item,amount in stock_dict.items():
        if item[0] in my20.stock.keys():
            if type(my20.stock[item[0]].size_color_dict[(item[2], item[1])].prices.retailPrice) == str:
                continue
            total_sum_ex += my20.stock[item[0]].size_color_dict[(item[2], item[1])].prices.exportPrice * amount
            total_sum_ran += my20.stock[item[0]].size_color_dict[(item[2], item[1])].prices.retailPrice * amount
        elif item[0] in my21.stock.keys():
            if type(my21.stock[item[0]].size_color_dict[(item[2], item[1])].prices.retailPrice) == str:
                continue
            total_sum_ex += my21.stock[item[0]].size_color_dict[(item[2], item[1])].prices.exportPrice * amount
            total_sum_ran += my21.stock[item[0]].size_color_dict[(item[2], item[1])].prices.retailPrice * amount
    print("Total stock value in NIS by Export price: %d" % (4.1*total_sum_ex*1.1))
    print("Total stock value in NIS by by retail - 30%%: %d" % ((1-0.3)*4.1*total_sum_ran/1.17))
    print("Total stock value in NIS by by retail - 40%%: %d" % ((1-0.4)*4.1*total_sum_ran/1.17))
    print("Total stock value in NIS by by retail - 45%%: %d" %  ((1-0.45)*4.1*total_sum_ran/1.17))
    print("Total stock value in NIS by by retail - 50%%: %d" % ((1-0.5)*4.1*total_sum_ran/1.17))

if __name__ == '__main__':
    main()