#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        #Calculator is made by ASAP-ARO, 
    #The program is the property of the creator and has been made available for commercial purposes, please do not share it, as the author does not consent to it.
    #All rights reserved.
    
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def kalkulator_zysku():
    while True:
        try:
    # Poprawiona obsługa przecinków w liczbie
            suma = float(input("Amount you have: ").replace(',', '.'))
            if suma <= 0:
                print("The amount must be greater than zero.")
                continue

            x = float(input("Cryptocurrency entry price: ").replace(',', '.'))
            if x <= 0:
                print("The entry price must be greater than zero.")
                continue

            y = float(input("Cryptocurrency starting price: ").replace(',', '.'))
            if y <= 0:
                print("The starting price must be greater than zero.")
                continue

            oplata_gieldowa_input = input("Enter the exchange fee in % (if 0, enter 0): ").replace(',', '.')
            oplata_gieldowa = 0

    # Obsługa wartości opłaty giełdowej jako procent lub kwota stała
            if '%' in oplata_gieldowa_input:
                oplata_gieldowa = float(oplata_gieldowa_input.strip('%'))
            elif oplata_gieldowa_input != '0':
                oplata_gieldowa = float(oplata_gieldowa_input) / (suma * x / 100)       # Przeliczenie na procent

    # Obliczenie procentowego wzrostu/spadku
            procent = ((y - x) / x) * 100

    # Obliczenie nowej sumy bez uwzględnienia opłaty giełdowej
            nowa_suma = suma * (y / x)

    # Obliczenie i odjęcie opłaty giełdowej
            oplata_wartosc = nowa_suma * oplata_gieldowa / 100
            nowa_suma -= oplata_wartosc

    # Zaokrąglenie wyników
            procent = round(procent, 2)
            nowa_suma = round(nowa_suma, 2)
            oplata_wartosc = round(oplata_wartosc, 2)

    # Obliczenie ilości kryptowaluty
            ilosc_krypto = suma / x 

    # Wyświetlenie wyników
            print(f" ")
            print(f">>> Amount of cryptocurrency purchased: {ilosc_krypto} units")
            print(f">>> Exchange Fee: {oplata_wartosc} $ ({oplata_gieldowa}%)")
            print(f">>> Percentage increase/decrease: {procent}%")
            print(f">>> Total profit/loss: {nowa_suma} $")
            print(f" ")

    # Zapytanie o ponowne uruchomienie kalkulacji
            ponownie = input("Do you want to count again? (yes/no/exit): ").lower()
            if ponownie == 'no' or ponownie == 'exit':
                print("Goodbye!")
                break

        except ValueError as e:
            print("An invalid value was entered. Try again. Error details:", e)

if __name__ == "__main__":
    kalkulator_zysku()


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        #Calculator is made by ASAP-ARO, 
    #The program is the property of the creator and has been made available for commercial purposes, please do not share it, as the author does not consent to it.
    #All rights reserved.
    
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!