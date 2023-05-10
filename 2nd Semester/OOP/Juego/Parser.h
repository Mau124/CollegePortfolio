#pragma once
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include "Personaje.h"
#include "ListaPalabras.h"
#include "Habitacion.h"
using namespace std;

// Necesito tambien a todas las habitaciones

// Mensajes del Parser
const char* msg1 = "No comprendo la instruccion. Verifique que las palabras hayan sido escritas corretamente y que el orden de ellas sea el adecuado";
const char* msg2 = "No comprendo la instruccion. Verifique que la instruccion tecleada sea un comando";
const char* msg3 = "Ese objeto no puede ser llevado en tu inventario.";
const char* msg4 = "Solo puedes eliminar objetos que esten en tu inventario";


/*
	Clase parser que se encarga de prosesar  y ejecutar los comandos ingresados por el usuario
	para esto utiliza la clase ListaPalabras para obtener los comandos.
*/
class Parser
{
public:
	Parser();
	Parser(Personaje*, ListaPalabras&);
	bool procesaComando(string);
	void imprimirMapa();
	bool ejecutaComando();
private:
	Personaje* personaje;
	ListaPalabras palabras;
	string palabra1, palabra2;
	string tipo1, tipo2;
	Item* item;

	void getPalabras(string);
	bool exist(string, vector<string>);
	void getSemanticValue();
	string toLower(string);
	void test(vector<string>);
};

Parser::Parser() {}

Parser::Parser(Personaje* personaje, ListaPalabras& palabras) {
	this->personaje = personaje;
	this->palabras = palabras;

	palabra1 = "";
	palabra2 = "";
	tipo1 = "";
	tipo2 = "";

	item = NULL;
}

bool Parser::procesaComando(string instruccion) {
	// 1. Descomponemos el string con las instrucciones
	try {
		getPalabras(instruccion);
	}
	catch (invalid_argument e) {
		cout << e.what() << endl;
		return false;
	}
	getSemanticValue();

	// Si la instruccion es de una palabra
	if (palabra2 == "") {
		if (tipo1 == "comandos") {
			return ejecutaComando();
		}else
			cout << msg2 << endl;
		return false;
	}

	// Si la instruccion es de dos palabras
	if (tipo1 == "agregar" && tipo2 == "objeto") {
		if (ItemPickable* pickable = dynamic_cast<ItemPickable*>(item)) {
			personaje->addItem(pickable);
		}
		else {
			cout << msg3 << endl;
		}
		return true;
	}

	if (tipo1 == "soltar" && tipo2 == "objeto") {
		if (ItemPickable* pickable = dynamic_cast<ItemPickable*>(item)) {
			if (personaje->dropItem(pickable)) {
				cout << "Se ha eliminado el item de tu inventario" << endl;
			}
		}
		else {
			cout << msg4 << endl;
		}
		return true;
	}

	if (tipo1 == "interactuar" && tipo2 == "objeto") {
		if (ItemPickable* pickable = dynamic_cast<ItemPickable*>(item)) {
			if (personaje->itemExist(item->getNombre())) {
				cout << item->interactuar() << endl;
			}
			else {
				cout << "El objeto necesita estar en tu inventario para interactuar" << endl;
			}
		}
		else {
			cout << item->interactuar() << endl;
		}
		return true;
	}

	if (tipo1 == "descripcion" && tipo2 == "objeto") {
		cout << item->getDesc() << endl;
		return true;
	}

	if (tipo1 == "desplazamiento" && tipo2 == "lugar") {
		int dir = 0;
		if (palabra2 == "norte") dir = 0;
		if (palabra2 == "este") dir = 1;
		if (palabra2 == "sur") dir = 2;
		if (palabra2 == "oeste") dir = 3;
		personaje->desplazar(dir);
		return true;
	}

	if (tipo1 == "descripcion" && palabra2 == "mapa") {
		imprimirMapa();
		return false;
	}

	cout << msg1 << endl;
	return false;
}

void Parser::getPalabras(string str) {

	if (str == "" || str.size() == 0) {
		throw invalid_argument(msg1);
	}
	palabra1 = "";
	palabra2 = "";
	string instruccion = toLower(str);
	istringstream ss(instruccion);
	ss >> palabra1;
	ss >> palabra2;
	ss.ignore();
}

bool Parser::exist(string palabra, vector<string> listaPalabras) {
	for (string str : listaPalabras) {
		if (toLower(str) == toLower(palabra))
			return true;
	}
	return false;
}

void Parser::getSemanticValue() {
	tipo1 = "";
	tipo2 = "";
	// Busca en todos los comandos del juego
	for (int i = 0; i < palabras.getLista().size(); ++i) {
		if (exist(palabra1, palabras.getLista()[i]))
			tipo1 = palabras.getTipos()[i];
		if (exist(palabra2, palabras.getLista()[i]))
			tipo2 = palabras.getTipos()[i];
	}

	// Busca en los objetos que hay en la habitacion
	for (int i = 0; i < personaje->getHabitacion()->getItems().size(); ++i) {
		if (palabra1 == toLower(personaje->getHabitacion()->getItems()[i]->getNombre())) {
			tipo1 = "";
			tipo2 = "";
			return;
		}

		if (exist(palabra2, personaje->getHabitacion()->getItems()[i]->getPalabras())) {
			tipo1 = "";
			tipo2 = "";
			return;
		}

		if (palabra2 == toLower(personaje->getHabitacion()->getItems()[i]->getNombre())) {
			item = personaje->getHabitacion()->getItems()[i];
			tipo2 = "objeto";
		}

		if (exist(palabra1, personaje->getHabitacion()->getItems()[i]->getPalabras())) {
		
			if (palabra2 == toLower(personaje->getHabitacion()->getItems()[i]->getNombre())) {
				item = personaje->getHabitacion()->getItems()[i];
				tipo1 = "interactuar";
				tipo2 = "objeto";
				return;
			}
		}
	}

	// Busca en el inventario del personaje y en las palabras de interactuar de cada Item
	for (int i = 0; i < personaje->getInventario().size(); ++i) {
		if (palabra1 == toLower(personaje->getInventario()[i]->getNombre())) {
			tipo1 = "";
			tipo2 = "";
			return;
		}

		if (exist(palabra2, personaje->getInventario()[i]->getPalabras())) {
			tipo1 = "";
			tipo2 = "";
			return;
		}

		if (palabra2 == toLower(personaje->getInventario()[i]->getNombre())) {
			item = personaje->getInventario()[i];
			tipo2 = "objeto";
		}

		if (exist(palabra1, personaje->getInventario()[i]->getPalabras())) {
			if (palabra2 == toLower(personaje->getInventario()[i]->getNombre())) {
				item = personaje->getInventario()[i];
				tipo2 = "objeto";
				tipo1 = "interactuar";
				return;
			}
		}
	}
}

string Parser::toLower(string str) {
	string res;
	for (char c : str) {
		res += tolower(c);
	}
	return res;
}

void Parser::test(vector<string> str) {
	cout << "IMPRIMIENDO LISTA" << endl;
	for (string s : str) {
		cout << s << endl;
	}
}

void Parser::imprimirMapa() {
	ifstream archivo;
	archivo.open("mapa.txt");
	string linea;
	string mapa = "";

	while (getline(archivo, linea)) {
		mapa += linea + "\n";
	}
	archivo.close();
	cout << mapa << endl;
}

bool Parser::ejecutaComando() {
	if (palabra1 == "buscar") {
		cout << "Buscando..." << endl;
		return true;
	}
	if (palabra1 == "help" || palabra1 =="ayuda") {
		string msgAyuda = "No sabes que hacer, pero no te preocupes, recuerda....\n ->Cada comando es de 2 palabras\n ->Primero va el verbo y despues el objeto :D\n ->Existen comandos especiales como ayuda o salir que son solo de una palabra";
		cout << msgAyuda << endl;
		return false;
	}
	if (palabra1 == "salir" || palabra1=="exit") {
		cout << endl << endl << endl << "Adios :D" << endl << endl;
		exit(0);
	}
	return false;
}