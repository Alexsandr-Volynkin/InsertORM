# InsertORM

-> Запуск из командной строки: python -m InsertORM

-> Задание: 

-> "Нужно разработать простенький ORM. Функция только одна - делать вставку записей в таблицу. Структура таблицы должна задаваться словарем Python. В структуре определяем название поля, тип, значение по умолчанию. Данные - массив словарей

Должен быть метод insert(table_structure, table_data). В методе достаточно сформировать INSERT-конструкцию для вставки.
Например:

TABLE_STRUCTURE = {
     "TableName": ....,
     "Fields": {
          "Field1": структура, описывающая поле,
          "Field2": .....
     }
}

insert(TABLE_STRUCTURE, [{"Field1": 1, "Field2": 2}])"
