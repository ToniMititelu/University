// Proiect_POO2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <string>
#include <vector>

class Angajat
{
private:
	std::string nume;
	float salariu;

public:
	Angajat();
	Angajat(std::string nume, float salariu);
	Angajat(const Angajat& angajat);
	virtual ~Angajat();
	virtual void display();
	float getSalariu();
	void setSalariu(float salariu);
	std::string getName();
	Angajat operator= (Angajat const& a);
	friend std::istream & operator >> (std::istream &in, Angajat &a);
	friend std::ostream & operator << (std::ostream &out, Angajat &a);
};

class Administrator : public Angajat
{
private:
	int sectie;

public:
	Administrator();
	Administrator(std::string nume, float salariu, int sectie);
	Administrator(const Administrator& administrator);
	~Administrator();
	Administrator operator=(Administrator const & a);
	friend std::istream & operator >> (std::istream &in, Administrator &a);
	void display();
};

int main()
{
	/*
	Angajat angajat1, angajat3;
	std::cin >> angajat1;
	std::cout << angajat1 << std::endl;
	Angajat angajat2(angajat1);
	angajat2.display();
	angajat3 = angajat2;
	angajat3.display();
	Administrator administrator1("Administrator1", 55.2f, 1);
	administrator1.display();
	Administrator administrator2(administrator1);
	administrator2.display();
	Angajat *a = new Administrator("Administrator1", 55.2f, 1);
	a->display();
	Angajat *b(a);
	b->display();
	Angajat *c = new Administrator();
	c = b;
	c->display();*/
	Angajat *angajat1 = new Angajat();
	std::cin >> (*angajat1);
	Angajat *angajat2 = new Angajat(*angajat1);
	Angajat *angajat3 = new Angajat();
	*angajat3 = *angajat2;
	Angajat *administrator1 = new Administrator("Administrator", 25, 3);
	Angajat *administrator2 = new Administrator();
	*administrator2 = *administrator1;

	std::vector<Angajat*> array;
	
	array.push_back(angajat2);
	array.push_back(angajat3);
	array.push_back(administrator1);
	array.push_back(administrator2);
	array.push_back(angajat1);


	for (auto i : array)
	{
		i->display();
	}

	delete(angajat1);
	delete(angajat2);
	delete(angajat3);
	delete(administrator1);
	delete(administrator2);
	return 0;
}

std::istream & operator >> (std::istream &in, Angajat &a)
{
	std::getline(in, a.nume);
	in >> a.salariu;
	return in;
}

std::ostream & operator << (std::ostream &out, Angajat &a)
{
	out << "Nume: " << a.nume <<std::endl;
	out << "Salariu: " << a.salariu << std::endl;
	return out;
}

std::istream & operator>>(std::istream & in, Administrator & a)
{
	in >> (Angajat&)a;
	in >> a.sectie;
	return in;
}

Angajat::Angajat() { nume = ""; salariu = 0; }

Angajat::Angajat(std::string nume, float salariu) : nume(nume), salariu(salariu) { }

Angajat::Angajat(const Angajat & angajat) : nume(angajat.nume), salariu(angajat.salariu) { }

Angajat::~Angajat() { }

void Angajat::display()
{
	std::cout << "Nume: " << nume << std::endl << "Salariu: " << salariu << std::endl;
}

float Angajat::getSalariu() { return salariu; }

void Angajat::setSalariu(float salariu) { this->salariu = salariu; }

std::string Angajat::getName() { return nume; }

Angajat Angajat::operator=(Angajat const & a)
{
	nume = a.nume;
	salariu = a.salariu;
	return *this;
}

Administrator::Administrator() : Angajat() { sectie = 0; }

Administrator::Administrator(std::string nume, float salariu, int sectie) : Angajat(nume, salariu), sectie(sectie) { }

Administrator::Administrator(const Administrator & administrator) : Angajat(administrator), sectie(administrator.sectie) { }

Administrator::~Administrator() { }

Administrator Administrator::operator=(Administrator const & a)
{
	Angajat::operator=(a);
	sectie = a.sectie;
	return *this;
}

void Administrator::display()
{
	Angajat::display();
	std::cout << "Salariu: " << sectie << std::endl << std::endl;
}

