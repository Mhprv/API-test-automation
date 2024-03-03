﻿# Автоматизация теста к API Яндекс Самокат
 
Шаги автотеста:
  Выполнить запрос на создание заказа.
  Сохранить номер трека заказа.
  Выполнить запрос на получения заказа по треку заказа.
  Проверить, что код ответа равен 200.
  
- Для запуска теста должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполняется командой pytest
- Cкриншот с запуском теста в PyCharm хранится в файле Screen_test_passed.png

# SQL Запросы

-Файл SQL.txt

1. Задание: Нужно проверить, отображается ли созданный заказ в базе данных. Для этого необходимо вывести список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).
  
2. Задание: Нужно вывести все трекеры заказов и их статусы. Статусы определяются по следующему правилу:
  Если поле finished == true, то вывести статус 2.
  Если поле canсelled == true, то вывести статус -1.
  Если поле inDelivery == true, то вывести статус 1.
  Для остальных случаев вывести 0. 

