def sum_shopping(prices, shopping_cart):
    total = 0
    for key in shopping_cart:
        if key in prices:
            total += shopping_cart[key] * prices[key]
        else:
            print "{} is not in prices dictionary".format(key)
    return total


def main():
    prices = {'bananas': 10, 'apples': 8, 'bread': 7, 'cheese': 20, 'juice': 15}
    shopping_cart = {'bananas': 2, 'apples': 4, 'bread': 3, 'cheese': 1, 'juice': 5}
    print "Sum of shopping is: {}".format(sum_shopping(prices, shopping_cart))
    shopping_cart = {'bananas': 2, 'apples': 4, 'bread': 3, 'cheese': 1, 'juice': 5, 'tuna': 6}
    print "Sum of shopping is: {}".format(sum_shopping(prices, shopping_cart))


if __name__ == '__main__':
    main()
