#pragma once
#include "Item.h"

/*
	clase usada para items que puedes agregar al invetario como la radio o una llave
*/
class ItemPickable:public Item
{
public:
	ItemPickable(string, string, vector<string>,string);
	string getDesc();
	string interactuar() override;
	void setInventario(bool);
	string getAccion();
	void test()override;
private:
	bool inventario;
	string accion;
};

ItemPickable::ItemPickable(string desc_, string nombre_, vector<string> palabras_, string d):Item(desc_,nombre_,palabras_) {
	accion = d;
	inventario = false;
}
string ItemPickable::getDesc() {
	return Item::getDesc();
}
string ItemPickable::getAccion() {
	return accion;
}
string ItemPickable::interactuar() {
	return accion;
}

void ItemPickable::setInventario(bool inventario) {
	this->inventario = inventario;
}

void ItemPickable::test() {
	Item::test();
	cout << "Accion: " + accion << endl;
	cout << "_______________________________________" << endl;
}

/*
txt:
pickable
#nombre una sola linea
#descropcion una sola linea
#lista de palabras
STOP
accion
*/
