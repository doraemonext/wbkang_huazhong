# -*- coding: utf-8 -*-

from math import ceil


def convert_sale_to_bonus(sale):
    """
    将销售达成率转为奖金达成系数
    :param sale: 销售达成率
    :return: 奖金大成系数
    """
    if sale < 0.8:
        return 0
    elif sale < 0.85:
        return 0.8
    elif sale < 0.9:
        return 0.85
    elif sale < 0.95:
        return 0.9
    elif sale < 1.0:
        return 1.0
    elif sale < 1.05:
        return 1.2
    elif sale < 1.1:
        return 1.4
    elif sale < 1.15:
        return 1.6
    elif sale < 1.2:
        return 1.8
    elif sale < 1.25:
        return 2.0
    elif sale < 1.3:
        return 2.2
    else:
        return 2.2 + int((sale - 1.25) * 100 / 5) * 0.2
