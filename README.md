# Blockchain
Transaction:

    Transaction.parse_hex() - парсинг hex-строки
    .txid - хеш транзакции
    .version - версия протокола
    .size - размер в байтах
    .locktime - время блокировки
    .inputs - список входов
    .outputs - список выходов

Input:

    .address - Bitcoin-адрес отправителя
    .value - сумма в сатоши
    .script_type - тип скрипта

Output:

    .address - Bitcoin-адрес получателя
    .value - сумма в сатоши
    .script_type - тип скрипта
