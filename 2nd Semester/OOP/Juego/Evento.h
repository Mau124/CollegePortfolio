#pragma once
#include"Personaje.h"
class Evento
{
public:
	Evento(string, int, string, string);
	bool Ejecutar(int, Personaje*);
	void test(); // Metodo para ver que le evento este bien 
	string toLower(string str);
private:
	string descripcion;
	int nAcciones;
	string habitacion;
	string nombreItem;
};

Evento::Evento(string desc, int n, string hab, string nom) {
	descripcion = desc;
	nAcciones = n;
	habitacion = hab;
	nombreItem = nom;
}

bool Evento::Ejecutar(int n, Personaje* personaje) {
	if (n >= nAcciones && toLower(personaje->getHabitacion()->getNombre()) == toLower(habitacion)) { // checamos numero de acciones realizadas y la habitacion actual
		if (nombreItem == "none" || (nombreItem != "none" && personaje->checkIfItemExists(nombreItem))) { // cehcamos que el jugador tenga el item correspondiednte para poder seguir
			cout << endl<<descripcion << endl; // ejecutamos el evento
			return true;
		}
	}
	return false;
}

void Evento::test() {
	cout << descripcion << endl;
	cout << "N = " + to_string(nAcciones) << endl;
	cout << "habitacion: " + habitacion << endl << endl;
}

string Evento::toLower(string str) {
	string res;
	for (char c : str) {
		res += tolower(c);
	}
	return res;
}

/*
txt:
#Descripcion del evento
Descripcion
STOP #Señal que indica que ya se termino la descripcion del evento
#Condiciones para que el evento se lanze
nAcciones
habitacion en la que tiene que estar ubicado el jugador
*/