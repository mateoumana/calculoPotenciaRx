import math
def main():
	print("Este programa calcula la potencia total recibida en un receptor.");
	print("Para ello ingrese la potencia de transmición Tx, indique", end=" ");
	print("(1 Watts, 0 en dBm):");
	option_ptx = int(input());
    
	while(option_ptx != 0 and option_ptx != 1):
		print("\n==============================================================");
		print("Entrada invalida, garantice que la opción sea de las ofrecidas.");
		print("\t\t  Intentelo de nuevo.");
		print("==============================================================\n");
		option_ptx = int(input(("(1 Watts, 0 en dBm): ")));

	if(option_ptx == 0):
		ptx = int(input("\nIngrese la potencia total transmitida en dBm: "));
	else: 
		ptx = int(input("\nIngrese la potencia total transmitida en Watts: "));
		ptx = 10*math.log((ptx*10**3),10); #10log(P(mW)/1mW)
    
	print("\n>>>Ahora, cuántos componentes de amplificación utilizó?");
	num_amps = int(input("Cantidad de amplificadores: "));
	while(num_amps < 0):
		print("\n==============================================================");
		print("Entrada invalida, garantice que la cantidad se mayor a cero.")
		print("\t\t  Intentelo de nuevo.");
		print("==============================================================");
		num_amps = int(input("Cantidad de amplificadores: "));

	print("\nIngrese la respectiva amplificación en dB de cada amplificador.");
	gains = []
	for n in range (0,num_amps):
		print("\t-Ganancia ", n+1, ": ", end="");
		gains.append(int(input()));

	print("\n>>>Ahora, cuántos componentes de atenuación utilizó?");
	num_ate = int(input("Cantidad de atenuadores: "));
	while(num_ate < 0):
		print("\n==============================================================");
		print("Entrada invalida, garantice que la cantidad se mayor a cero.")
		print("\t\t  Intentelo de nuevo.");
		print("==============================================================\n");
		num_ate = int(input("Cantidad de atenuadores: "));

	print("\nIngrese la respectiva atenuación en dB de cada atenuador. (Ingrese el valor absoluto de este)");
	alpha = []
	for n in range (0,num_ate):
		print("\t-Atenuación ", n+1, ": ", end="");
		alpha.append(int(input()));

	perdidas = 0;
	for n in range (0, num_ate):
		perdidas = perdidas + alpha[n];

	ganancias = 0;
	for n in range (0, num_amps):
		ganancias = ganancias + gains[n];

	Prx = ptx + ganancias - perdidas;

	print("\n\n===========================================================");
	print("\t\t\t RESULTADOS");
	print("===========================================================");
	print("La potencia total recibida en dBm es: ", Prx);
	Prx = (10**(Prx/10))/1000
	print("La potencia total recibida en Watts es: ", Prx);

main()
