#!/usr/bin/python
# -*- coding:UTF-8 -*-

from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

promos = []


# 装饰器。添加所有折扣活动的函数
def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)

    def total(self):
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


@promotion
def fidelity(order):  # 第一个具体策略
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):  # 第二个具体策略
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


@promotion
def large_order(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_itmes = {item.product for item in order.cart}
    if len(distinct_itmes) >= 10:
        return order.total() * .07
    return 0


def best_promo(order):
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)


if __name__ == '__main__':
    joe = Customer('John Doe', 10)
    ann = Customer('Ann Smith', 1200)
    # 有三个商品的购物车
    cart = [LineItem('banana', 4, .6),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]
    banana_cart = [LineItem('banana', 30, .6),
                   LineItem('apple', 10, 1.5)]
    long_order = [LineItem(str(item_code), 1, 1.0)
                  for item_code in range(10)]
    print(Order(joe, banana_cart, best_promo))
    print(Order(ann, long_order, best_promo))
