Списковые включения #116

Скорее всего вы заметили кое‑что общее в двух предыдущих задачах. Мы брали один список и создавали на его основе другой из элементов, удовлетворяющих 
определенному условию. Вообще, создание одного списка из другого с фильтрацией и/или изменением элементов — довольно частая история в программировании.

В Python есть удобная конструкция, с помощью которой эту операцию можно сделать проще и красивее. Называется эта конструкция списковым включением 
(англ. list comprehension) и в общем виде выглядит так

[выражение for элемент in коллекция if условие]

Можно сказать, что это упрощенный однострочный цикл for, создающий список из элементов коллекции, которые удовлетворяют условию. С помощью выражения 
эти элементы могут быть обработаны. Например, создать список из четных чисел на основе списка всех чисел, можно так

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [i for i in numbers if i % 2 == 0]
print(even_numbers)

В качестве выражения мы используем просто i, то есть оставляем исходный элемент без изменений. Если, например, нам нужно преобразовать целые числа 
в строки (мало ли?), можно использовать знакомую вам функцию str

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [str(i) for i in numbers if i % 2 == 0]
print(even_numbers)

Выражение и условие для обработки элемента могут быть любыми, но не стоит сильно усердствовать с их сложностью. Ведь чем сложнее выражение или условие, 
тем сложнее будет читать вашу программу. А это уже будет не совсем в стиле Python.

Да, если нужно просто обработать элементы списка не отфильтровывая, условие можно опустить

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [str(i) for i in numbers]
print(even_numbers)
