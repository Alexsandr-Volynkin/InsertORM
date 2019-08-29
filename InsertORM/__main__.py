# -*- coding: utf-8 -*-

from .insertORM import InsertORM


def main():

    TABLE_STRUCTURE = {'TableName': 'Clock', 'Fields': {
                                            'id': 'INTEGER PRIMARY KEY',
                                            'Color': 'TEXT', 'Type': 'TEXT',
                                            'Year': 'INTEGER'}}
    table_data = [
            {'id': 1, 'Color': 'Red', 'Type': 'Electronic', 'Year': 2018},
            {'id': 2, 'Color': 'Black', 'Type': 'Electronic', 'Year': 2017},
            {'id': 3, 'Color': 'Blue', 'Type': 'Electronic', 'Year': 2019},
            {'id': 4, 'Color': 'Yellow', 'Type': 'Electronic', 'Year': 2019}
            ]

    obj = InsertORM()
    obj.insertToTable(table_data, TABLE_STRUCTURE)

if __name__ == '__main__':
    main()
