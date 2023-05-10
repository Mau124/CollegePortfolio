#pragma once
#include<iostream>
#include<vector>
using namespace std;

/*

	clase base para los items del juego, cada item tiene sus propias palabras para interactuar
	como por ejecmplo la manzana tiene "comer" y la radio tiene "escuchar", pero estas
	llaman al metodo de iteractuar().

*/
class Item
{
public:
	Item(string, string, vector<string>);
	virtual string getDesc();
	virtual string interactuar();
	virtual void test();
	string getNombre();
	vector<string> getPalabras();
private:
	string desc;
	string nombre;
	vector<string> palabras;
};

Item::Item(string desc_, string nombre_, vector<string> palabras_) {
	desc = desc_;
	nombre = nombre_;
	palabras = palabras_;
}
string Item::getNombre() {
	return nombre;
}
string Item::getDesc() {
	return desc;
}
vector<string> Item::getPalabras() {
	return palabras;
}
string Item::interactuar() {
	return "";
}
void Item::test() {
	cout << "_______________________________________" << endl;
	cout << nombre << endl;
	cout << desc << endl;
	cout << "Palabras interactuar: " << endl;
	for (int i = 0; i < palabras.size(); i++) {
		cout << palabras[i] << endl;
	}
}