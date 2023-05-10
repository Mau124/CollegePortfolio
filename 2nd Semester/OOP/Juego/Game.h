#pragma once

#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;

#include"Evento.h"
#include"Personaje.h"
#include"Habitacion.h"
#include"Item.h"
#include"ItemConsumible.h"
#include"ItemPickable.h"
#include"ItemStatic.h"
#include"Parser.h"
#include"ListaPalabras.h"

/*
	clase Game, se encarga de crear todo el juego y hacer el loop del mismo.
		- toda la informacion se obtiene de archivos de texto
		- la lista de eventos funciona como una cadena, primero se tiene que ejecutar el evento 1 antes que el 2
*/

class Game
{
public:
	Game();
	void play();

private:
	int nEvento;
	vector<Evento*>evento;
	int nAcciones;
	Personaje* personaje;
	Habitacion* habitacion[4];
	ListaPalabras palabras;
	Parser parser;

	void crearJuego();
	void crearEventos();
	void crearJugador();
	void crearHabitaciones();
	void crearListaPalabras();
	vector<Item*>crearItems(vector<string>);
	ItemStatic* crearItemStatic(string);
	ItemConsumible* crearItemConsumible(string);
	ItemPickable* crearItemPickable(string);
};

Game::Game() {
	nAcciones = 0;
	nEvento = 0;
	crearJuego();
}

void Game::crearJuego() {
	crearEventos();
	crearHabitaciones();
	crearListaPalabras();
	crearJugador();

	parser = Parser(personaje, palabras);
}

void Game::crearEventos() {
	int cont = 0;
	string linea;
	ifstream archivo;

	while (true) {
		archivo.open("evento" + to_string(cont) + ".txt");
		if (!archivo)break; // paramos de leer porque ya no hay mas eventos

		string desc = "";
		int n = -1;
		string hab;
		string nomItem;

		while (getline(archivo, linea)) {
			if (linea == "STOP") {
				getline(archivo, linea); // leemos el numero de acciones para ejecutarlo
				n = stoi(linea);
				getline(archivo, linea); // leemos la habitacion
				hab = linea;
				break;
			}
			desc += linea + "\n"; //leemos el evento
		}
		getline(archivo, nomItem); // leemos el item

		evento.push_back(new Evento(desc, n, hab, nomItem)); //creamos evento
		archivo.close();
		cont++;
	}
}

void Game::crearHabitaciones() {
	string habitacionTxt[4] = { "taller.txt","cocina.txt","sala.txt","recamara.txt" };
	string linea;
	ifstream archivo;

	for (int i = 0; i < 4; i++) {
		archivo.open(habitacionTxt[i]);

		string nombre;
		string descripcion = "";
		bool cerrada;
		string nombreLlave = "";
		vector<string> itemsTxt;

		getline(archivo, nombre); // leemos el nombre de la habitacion

		while (getline(archivo, linea)) { //leemos la descripocion de la habitacion
			if (linea == "STOP")break;
			descripcion += linea + "\n";
		}

		getline(archivo, linea); // leemos si esta cerrada o no la habitacion
		if (linea == "1") {
			cerrada = true;
			getline(archivo, nombreLlave); // nombre de la llave para abrir la habitacion
		}
		else {
			cerrada = false;
		}

		while (getline(archivo, linea)) { // leemos los items que hay en la habitacion
			itemsTxt.push_back(linea);
		}
		archivo.close();

		habitacion[i] = new Habitacion(nombre, descripcion, cerrada, nombreLlave);// crear habitacion
		habitacion[i]->setItems(crearItems(itemsTxt)); // creamos y añadimos los items
	}

	//Salidas
	habitacion[0]->setSalidas(habitacion[2], habitacion[1], NULL, NULL);
	habitacion[1]->setSalidas(habitacion[0], NULL, NULL, NULL);
	habitacion[2]->setSalidas(NULL, habitacion[0], NULL, habitacion[3]);
	habitacion[3]->setSalidas(NULL, NULL, habitacion[2], NULL);

}

vector<Item*> Game::crearItems(vector<string> itemsTxt) {
	vector<Item*> items;
	string linea;
	ifstream archivo;

	for (int i = 0; i < itemsTxt.size(); i++) {
		archivo.open("items/" + itemsTxt[i]);
		getline(archivo, linea);
		archivo.close();

		// checar de que tipo de item es
		if (linea == "static") {
			items.push_back(crearItemStatic("items/" + itemsTxt[i]));
		}
		else if (linea == "consumible") {
			items.push_back(crearItemConsumible("items/" + itemsTxt[i]));
		}
		else if (linea == "pickable") {
			items.push_back(crearItemPickable("items/" + itemsTxt[i]));
		}
		else {
			cout << "No se pudo identificar el item: " + itemsTxt[i] << endl;
		}
	}

	return items;
}

ItemStatic* Game::crearItemStatic(string itemTxt) {
	string linea;
	ifstream archivo;
	archivo.open(itemTxt);

	string desc, nombre;
	vector<string> palabras;

	getline(archivo, linea);
	getline(archivo, nombre);//nombre
	getline(archivo, desc);//descripcion

	while (getline(archivo, linea)) {
		if (linea == "STOP") break;
		palabras.push_back(linea);
	}

	//////////////////////////////////////////////

	string estados[2];
	getline(archivo, estados[0]);
	getline(archivo, estados[1]);

	archivo.close();
	return new ItemStatic(desc, nombre, palabras, estados);
}

ItemConsumible* Game::crearItemConsumible(string itemTxt) {
	string linea;
	ifstream archivo;
	archivo.open(itemTxt);

	string desc, nombre;
	vector<string> palabras;

	getline(archivo, linea);
	getline(archivo, nombre);
	getline(archivo, desc);

	while (getline(archivo, linea)) {
		if (linea == "STOP") break;
		palabras.push_back(linea);
	}

	//////////////////////////////////////////////

	int n;
	string accion;
	vector<string> palabras2;

	getline(archivo, linea);
	n = stoi(linea);
	getline(archivo, accion);

	archivo.close();
	return new ItemConsumible(desc, nombre, palabras, n, accion);
}

ItemPickable* Game::crearItemPickable(string itemTxt) {
	string linea;
	ifstream archivo;
	archivo.open(itemTxt);

	string desc, nombre;
	vector<string> palabras;

	getline(archivo, linea);
	getline(archivo, nombre);
	getline(archivo, desc);

	while (getline(archivo, linea)) {
		if (linea == "STOP") break;
		palabras.push_back(linea);
	}

	//////////////////////////////////////////////

	string accion;
	getline(archivo, accion);

	archivo.close();
	return new ItemPickable(desc, nombre, palabras, accion);
}

void Game::crearJugador() {
	string nom;
	cout << "Ingresa tu nombre: ";
	cin >> nom;
	cin.ignore();
	personaje = new Personaje(nom, habitacion[0]);
}

void Game::crearListaPalabras() {

	vector<string> instruccionesTxt{ "agregar.txt","comandos.txt","desc.txt","desplazamiento.txt", "lugar.txt", "soltar.txt" };
	vector<vector<string>> instrucciones(instruccionesTxt.size());
	string linea;
	ifstream archivo;

	for (int i = 0; i < instruccionesTxt.size(); i++) {
		archivo.open("instrucciones/" + instruccionesTxt[i]);
		while (getline(archivo, linea)) {
			instrucciones[i].push_back(linea);
		}
		archivo.close();
	}
	palabras.setLista(instrucciones);
	palabras.setTipos(vector<string>{"agregar", "comandos", "descripcion", "desplazamiento", "lugar", "soltar" });
	//palabras.test();
}

void Game::play() {
	string instruccion;

	//Inicio del juego, se imprime la habitacion y el primer evento de la historia
	cout << personaje->getHabitacion() << endl;
	bool success = evento[nEvento]->Ejecutar(nAcciones, personaje);
	if (success) {
		nAcciones = 0;
		nEvento++;
	}
	cout << endl << "Presiona una tecla para continuar...";
	getline(cin, instruccion);

	while (nEvento < evento.size()) { // ciclo de juego
		system("cls");
		cout << personaje->getHabitacion() << endl;
		cout << ">>>";
		getline(cin, instruccion);
		success = parser.procesaComando(instruccion); // prosesar comando
		
		if (success) { // se ejecuto el comando correctamente
			nAcciones++;
			++*personaje; // incrementamos el numero de movimientos
		}

		success = evento[nEvento]->Ejecutar(nAcciones, personaje); // Ejecutamos el evento

		if (success) {// evento se ejecuto correctamente
			nAcciones = 0;
			nEvento++;
		}
		cout << endl << "Presiona una tecla para continuar...";
		getline(cin, instruccion);
	}

	cout << endl << endl << "Fin" << endl;
	cout << endl << endl << endl << "\t ? " << endl;
}

