
nombre1 = input("Indique su nombre, jugador 1: ")
nombre2 = input("Indique su nombre, jugador 2: ")
counter = input("Indique cuantos turnos desean jugar: ")
counter = int(counter)
turnos = 1

while counter >= turnos: 
 turnos += 1
 jugador1 = input(f"{nombre1}, ¿que elijes? ¿piedra, papel o tijeras? ")
 jugador2 = input(f"{nombre2}, ¿que elijes? ¿piedra, papel o tijeras? ")

 jugador1min = jugador1.lower()
 jugador2min = jugador2.lower()

 condicion1 = jugador1min == "piedra" and jugador2min == "tijeras"
 condicion2 = jugador1min == "papel" and jugador2min == "piedra"
 condicion3 = jugador1min == "tijeras" and jugador2min == "papel"
 
 if jugador1min == jugador2min:
    print (" Ha sido un empate.")
 elif condicion1 or condicion2 or condicion3:
    print('Ha ganado:',nombre1)
 else: 
    print('Ha ganado:',nombre2) 


