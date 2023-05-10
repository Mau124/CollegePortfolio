#pragma once
#include <vector>
#include <map>
#include <iostream>
using namespace std;

/*
	Clase que contiene la lista de todas las palabras globales del juego
	Estas palabras son las listas de:
		[0] addItem -> agregar objetos
		[1] dropItem -> soltar los objetos
		[2] desc -> descripcion de los items
		[3] command -> comandos de la aplicacion
		[4] desplazamiento -> palabras para desplazar al usuario
		[5] lugar -> palabras de lugar
*/

class ListaPalabras
{
public:
	ListaPalabras();
	ListaPalabras(vector<vector<string>>&, vector<string>);
	vector<vector<string>> getLista();
	void setLista(vector<vector<string>>&);
	vector<string> getTipos();
	void setTipos(vector<string>);
	void test();
private:
	vector<vector<string>> lista;
	vector<string> tipos;
};

ListaPalabras::ListaPalabras() { }

ListaPalabras::ListaPalabras(vector<vector<string>>& lista, vector<string> tipos) {
	this->lista = lista;
	this->tipos = tipos;
}

vector<vector<string>> ListaPalabras::getLista() { return lista; }

void ListaPalabras::setLista(vector<vector<string>>& lista) {
	this->lista = lista;
}

vector<string> ListaPalabras::getTipos() { return tipos; }

void ListaPalabras::setTipos(vector<string> tipos) {
	this->tipos = tipos;
}

void ListaPalabras::test() {
	cout << "Palabras" << endl;
	for (int i = 0; i < lista.size(); ++i) {
		for (int j = 0; j < lista[i].size(); ++j) {
			cout << "Palabra: " << lista[i][j] << endl;
		}
 	}
	cout << endl;
}