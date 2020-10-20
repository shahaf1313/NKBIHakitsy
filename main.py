from src.NorthStock import *

def main():
    north_stock = NorthStock()
    stock2020path = r'C:\Users\Shahaf\Documents\North Kiteboarding Israel\North 2021\Games\Orderform North Kiteboarding 2020 Export Updated Prices.xlsx'
    stock2021path = r'C:\Users\Shahaf\Documents\North Kiteboarding Israel\North 2021\Games\Orderform North Kiteboarding 2021 Export.xlsx'
    header_row_2020 = 10
    header_row_2021 = 11
    north_stock.ReadStockFromExel(stock2020path, 'MY20', header_row_2020)
    north_stock.ReadStockFromExel(stock2021path, 'MY21', header_row_2021)

    total_sum_ex = 0
    total_sum_ran = 0
    f = open(r'C:\Users\Shahaf\Desktop\stock.txt', 'r')
    for i,line in enumerate(f):
        if i == 0:
            continue
        splatted_line = line.split('\t')
        barcode = splatted_line[1].strip()
        amount = int(splatted_line[7].strip())
        total_sum_ex += north_stock.stock[barcode].prices.export_price * amount
        total_sum_ran += 0 if type(north_stock.stock[barcode].prices.retail_price) == str else north_stock.stock[barcode].prices.retail_price * amount


    print("Total stock value in NIS by Export price: %d" % (4.1*total_sum_ex*1.1))
    print("Total stock value in NIS by by retail - 30%%: %d" % ((1-0.3)*4.1*total_sum_ran/1.17))
    print("Total stock value in NIS by by retail - 40%%: %d" % ((1-0.4)*4.1*total_sum_ran/1.17))
    print("Total stock value in NIS by by retail - 45%%: %d" %  ((1-0.45)*4.1*total_sum_ran/1.17))
    print("Total stock value in NIS by by retail - 50%%: %d" % ((1-0.5)*4.1*total_sum_ran/1.17))

if __name__ == '__main__':
    main()