# -*- coding: utf-8 -*-
import sqlite3
import sys


class InsertORM:
    def insertToTable(self, table_data, TABLE_STRUCTURE):
        nameTable = ''
        queryCreate = ''
        fields = {}
        fields = TABLE_STRUCTURE['Fields']
        keys = list(fields.keys())
        values = list(fields.values())

        for ind in range(len(fields)):
            queryCreate += str(keys[ind]) + ' ' + str(values[ind]) + ', '

        queryCreate = queryCreate[:-2]
        nameTable = str(TABLE_STRUCTURE['TableName'])

        try:
            connect = sqlite3.connect('./Table.db')
            cursr = connect.cursor()
            cursr.execute('CREATE TABLE IF NOT EXISTS ' +
                          nameTable + "(" + queryCreate + ")")
            for table in table_data:
                cursr.execute("INSERT OR IGNORE INTO " +
                              nameTable + " VALUES(?, ?, ?, ?)", (
                                table["id"],
                                table["Color"],
                                table["Type"],
                                table["Year"]))
            connect.commit()

        except sqlite3.Error as e:
            if connect:
                connect.rollback()

            print("Error %s:" % e.args[0])
            sys.exit(1)

        finally:
            if connect:
                cursr.close()
                connect.close()
