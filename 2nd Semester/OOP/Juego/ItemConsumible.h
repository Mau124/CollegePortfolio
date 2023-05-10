#pragma once
#include "Item.h"
#include "ItemPickable.h"

/*
	clase usada para items que puedes agregar al inventario, pero puedes consumir por lo que tienen un uso limitado
*/
class ItemConsumible: public ItemPickable
{
public:
	ItemConsumible(string, string, vector<string>,int,string);
	string interactuar();
	int getCantidad();
	void setCantidad(int);
	void test()override;
private:
	int cantidad;
};

ItemConsumible::ItemConsumible(string desc_, string nombre_, vector<string> palabras_, int n, string accion_) :ItemPickable(desc_, nombre_, palabras_, accion_) {
	cantidad = n;
	ItemPickable::setInventario(false);
}

string ItemConsumible::interactuar() {
	if (cantidad == 0)
		return "Ya no puedes consumir este item, te lo has acabado";

	cantidad--;
	return ItemPickable::getAccion();
}

int ItemConsumible::getCantidad() {
	return cantidad;
}

void ItemConsumible::setCantidad(int n) {
	cantidad = n;
}

void ItemConsumible::test() {
	Item::test();
	cout << "Cantidad: " << cantidad << endl;
	cout << "Accion: " + ItemPickable::getAccion() << endl;
	cout << "_______________________________________" << endl;
}

/*
txt:
consumible
#nombre una sola linea
#descropcion una sola linea
#lista de palabras
STOP
cantidad
accion
*/