def kalkulator():
    while True:
        print("\nProsty Kalkulator")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Wyjście")
        
        wybor = input("Wybierz operację (1-5): ")
        
        if wybor == '5':
            print("Zamykanie kalkulatora...")
            break
        
        if wybor not in ['1', '2', '3', '4']:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            continue
        
        try:
            liczba1 = float(input("Podaj pierwszą liczbę: "))
            liczba2 = float(input("Podaj drugą liczbę: "))
        except ValueError:
            print("Błąd: Wprowadzono niepoprawną liczbę.")
            continue
        
        if wybor == '1':
            print(f"Wynik: {liczba1 + liczba2}")
        elif wybor == '2':
            print(f"Wynik: {liczba1 - liczba2}")
        elif wybor == '3':
            print(f"Wynik: {liczba1 * liczba2}")
        elif wybor == '4':
            if liczba2 == 0:
                print("Błąd: Dzielenie przez zero!")
            else:
                print(f"Wynik: {liczba1 / liczba2}")

if __name__ == "__main__":
    kalkulator()
