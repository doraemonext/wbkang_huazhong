# -*- coding: utf-8 -*-


def get_actual_value(sheet, merged_cells, row, col):
    for cell in merged_cells:
        if cell[0] <= row < cell[1] and cell[2] <= col < cell[3]:
            return sheet.cell_value(cell[0], cell[2])
    return sheet.cell_value(row, col)