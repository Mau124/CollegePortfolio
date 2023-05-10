#pragma once

#include<iostream>
#include<vector>
#include "Habitacion.h"
#include "ItemPickable.h"
using namespace std;

/*
	Clase Personaje es la clase del juagdor:
		- contiene un inventario
		- se puede desplazar en el mapa

*/
class Personaje
{
public:
	Personaje(string,Habitacion*);
	Habitacion* getHabitacion();
	void setHabitacionActual(Habitacion*);
	void addItem(ItemPickable*);
	bool dropItem(ItemPickable*);
	vector<ItemPickable*> getInventario();
	ItemPickable* itemExist(string nombre);
	bool checkIfItemExists(string nombre);
	void desplazar(int);
	Personaje& operator++();
	
private:
	string nombre;
	Habitacion *habActual;
	int numeroMovimientos;
	vector<ItemPickable*> inventario;
};


Personaje::Personaje(string nombre_ , Habitacion* hab) {
	nombre = nombre_;
	habActual = hab;
	numeroMovimientos = 0;
}

Habitacion* Personaje::getHabitacion() {
	return habActual;
}

void Personaje::setHabitacionActual(Habitacion* hab) {
	habActual = hab;
	cout << habActual->getDescripcion() << endl;
}

void Personaje::addItem(ItemPickable* item) {

	if (habActual->quitarItem(item)) {
		inventario.push_back(item);
	}
	else {
		cout << "No existe ese objeto en la habitacion para ser agregado" << endl;
		return;
	}

	cout << endl<<"Este es tu Inventario: " << endl;
	for (int i = 0; i < inventario.size(); ++i) {
		cout << inventario[i]->getNombre() << endl;
	}
}

bool Personaje::dropItem(ItemPickable* item) {
	for (int i = 0; i < inventario.size(); ++i) {
		if (item == inventario[i]) {
			habActual->addItem(inventario[i]);
			inventario.erase(inventario.begin() + i);

			cout <<endl <<"Este es tu Inventario: " << endl;
			for (int i = 0; i < inventario.size(); ++i) {
				cout << inventario[i]->getNombre() << endl;
			}

			return true;
		}
	}
	return false;
}

vector<ItemPickable*> Personaje::getInventario() {
	return inventario;
}

ItemPickable* Personaje::itemExist(string nombre) {
	for (int i = 0; i < inventario.size(); ++i) {
		if (nombre == inventario[i]->getNombre())
			return inventario[i];
	}
	return NULL;
}

bool Personaje::checkIfItemExists(string nombre) {
	for (int i = 0; i < inventario.size(); ++i) {
		if (nombre == inventario[i]->getNombre())
			return true;
	}
	return false;
}

void Personaje::desplazar(int dir) {
	if (habActual->getSalida(dir) != NULL) {
		if (habActual->getSalida(dir)->isClosed()) {
			//abrir
			habActual->getSalida(dir)->setClosed(!checkIfItemExists(habActual->getSalida(dir)->getNombreLlave()));
		}
		if (!habActual->getSalida(dir)->isClosed()) {
			habActual = habActual->getSalida(dir);

			cout << "El personaje se movio" << endl << endl;
		}
		else {
			cout << "La habitacion esta cerrada... encuentra la llave" << endl;
		}
	}else
		cout << "No existe esa habitacion " << endl;
}

Personaje& Personaje::operator++() {
	numeroMovimientos++;
	return *this;
}