from bitcoinlib.transactions import Transaction

def parse_bitcoin(filename):

    with open(filename, 'r') as file:
        transactions = file.readlines()
    
    for i, tx_hex in enumerate(transactions, 1):
        tx_hex = tx_hex.strip()
        if not tx_hex:
            continue
            
        print(f"Транзакция {i}")
        
        try:
            tx = Transaction.parse_hex(tx_hex)
            
            print(f"Хэш: {tx.txid}")
            print(f"Версия: {tx.version}")
            print(f"Блокировка: {tx.locktime}")
            print(f"Размер: {tx.size} байт")
            
            print(f"\nВходы ({len(tx.inputs)}):")
            for j, inp in enumerate(tx.inputs):
                print(f"{j+1}. Адрес: {inp.address or 'Coinbase'}")
                if inp.value:
                    print(f"Сумма: {inp.value:,} сатоши")
                print(f"Тип: {inp.script_type}")
            
            total_output = sum(out.value for out in tx.outputs)
            print(f"\nВыходы ({len(tx.outputs)}):")
            for k, out in enumerate(tx.outputs):
                print(f"{k+1}. Адрес: {out.address}")
                print(f"Сумма: {out.value:,} сатоши ({out.value/100000000:.8f} BTC)")
                print(f"Тип: {out.script_type}")
            
            print(f"\nИтого: {total_output:,} сатоши ({total_output/100000000:.8f} BTC)")

            print("\n")
            
        except Exception as e:
            print(f"Ошибка: {e}")
            print("\n")
            continue

if __name__ == "__main__":
    parse_bitcoin("txs_raw.txt")