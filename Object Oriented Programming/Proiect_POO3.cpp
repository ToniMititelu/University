#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

struct date
{
    int zi, luna, an;
};

class Examen
{
    string name;
    date d;
    int nota_scris;
public:
    Examen() { }
    Examen(string name, date d, int nota_scris) : name(name), d(d), nota_scris(nota_scris) { }
    Examen(const Examen& e);
    ~Examen() { }
    virtual void display();
    Examen operator= (const Examen& e);
    string getName() { return name; }
    date getData() { return d; }
    int getNotaScris() { return nota_scris; }
    void setNotaScris(int n) { nota_scris = n; }
    friend istream & operator >> (istream &in, Examen &e);
    friend ostream & operator << (ostream &out, const Examen &e);
};

void Examen::display()
{
    cout << "Denumire examen: " << name << "\n";
    cout << "Data: " << d.zi << "/" << d.luna << "/" << d.an << "\n";
    cout << "Nota scris: " << nota_scris << "\n";
}

istream & operator >> (istream &in, Examen &e)
{
    getline(in, e.name);
    in >> e.d.zi >> e.d.luna >> e.d.an;
    in >> e.nota_scris;
    return in;
}

ostream & operator << (ostream &out, const Examen &e)
{
    out << "Denumire examen: " << e.name << "\n";
    out << "Data: " << e.d.zi << "/" << e.d.luna << "/" << e.d.an << "\n";
    out << "Nota scris: " << e.nota_scris << "\n";
    return out;
}

Examen::Examen(const Examen& e)
{
    this->name = e.name;
    this->d = e.d;
    this->nota_scris = e.nota_scris;
}

Examen Examen::operator=(const Examen& e)
{
    this->name = e.name;
    this->d = e.d;
    this->nota_scris = e.nota_scris;
    return *this;
}

class Partial : public Examen
{
    int nota_oral;
public:
    Partial() { }
    Partial(string name, date d, int nota_scris, int nota_oral) : Examen(name, d, nota_scris), nota_oral(nota_oral) { }
    Partial(const Partial& p) : Examen(p), nota_oral(p.nota_oral) { }
    ~Partial() { }
    Partial operator= (const Partial& p);
    void display();
    int getNotaOral() { return nota_oral; }
    friend istream & operator >> (istream &in, Partial &p);
    friend ostream & operator << (ostream &out, const Partial &p);
};

Partial Partial::operator=(const Partial& p)
{
    Examen::operator=(p);
    this->nota_oral = p.nota_oral;
    return *this;
}

istream & operator >> (istream &in, Partial &p)
{
    in >> (Examen&)p;
    in >> p.nota_oral;
    return in;
}

ostream & operator << (ostream &out, const Partial &p)
{
    out << (Examen&)p;
    out << "Nota oral: " << p.nota_oral << "\n";
    return out;
}

void Partial::display()
{
    cout << "Examen partial\n";
    Examen::display();
    cout << "Nota oral: " << this->nota_oral << "\n";
}

class Final : public Examen
{
    int puncte_bonus;
    int nota_partial;
public:
    Final() { }
    Final(string name, date d, int nota_scris, int puncte_bonus) : Examen(name, d, nota_scris), puncte_bonus(puncte_bonus) { }
    Final(const Final& f) : Examen(f), puncte_bonus(f.puncte_bonus) { }
    ~Final() { }
    void display();
    Final operator= (const Final& f);
    int getPuncteBonus() { return puncte_bonus; }
    void notaScrisNoua() { setNotaScris(getNotaScris()+getPuncteBonus()); }
    void setNotaPartial(int nota) { nota_partial = nota; }
    friend istream & operator >> (istream &in, Final &f);
    friend ostream & operator << (ostream &out, const Final &f);
};

void Final::display()
{
    cout << "Examen final\n";
    Examen::display();
    cout << "Puncte bonus: " << this->puncte_bonus << "\n";
    cout << "Nota dupa aplicarea punctelor bonus: " << getNotaScris()+getPuncteBonus() << "\n";
}

istream & operator >> (istream &in, Final &f)
{
    in >> (Examen&)f;
    in >> f.puncte_bonus;
    return in;
}

ostream & operator << (ostream &out, const Final &f)
{
    out << (Examen&)f;
    out << "Puncte bonus: " << f.puncte_bonus << "\n";
    return out;
}

Final Final::operator=(const Final& f)
{
    Examen::operator=(f);
    this->puncte_bonus = f.puncte_bonus;
    return *this;
}

template<class T> class CatalogIndividual
{
    const int nr_examene = 5;
    vector<T*> examene;
    static int index;
    int id;

public:
    operator += (T* e)
    {
        bool ok = true;
        try {
            if(index > nr_examene)
                throw 1;
        }
        catch(int x) {
            if(x==1) {
                cout << "\nNumar maxim de examene atins!\n";
                ok = false;
            }
        }
        if(ok)
        {
            examene.push_back(e);
            index++;
        }
    }

    void afisare()
    {
        for(auto examen : examene)
        {
            examen->display();
            cout << "\n";
        }
    }

    void setID(int id) { this->id = id; }
};

template <class T> int CatalogIndividual <T> :: index = 1;

template <>class CatalogIndividual<unsigned>
{
    float medie;
    int nr;
public:
    CatalogIndividual()
    {
        medie = 0;
        nr = 0;
    }
    void calcM(Examen *f)
    {
        medie += (f->getNotaScris());
        nr++;
    }
    void displayM() const
    {
        cout << "Media examenelor finale: " << medie/nr << "\n";
    }
};

int main()
{
    /*Examen e, f;
    cin >> e;
    cout << e;
    f = e;
    Examen g(e);
    cout << f << g;*/
    ifstream fin("date.in");

    Examen *e = new Examen;
    fin >> (*e);
    CatalogIndividual <Examen> catalog;
    CatalogIndividual <unsigned> finals;
    catalog += e;
    date d; d.an = 2019; d.luna = 10; d.zi = 3;
    Examen *f1 = new Final("Mate", d, 6, 2);
    catalog += f1;
    Examen *f2 = new Final("Asc", d, 5, 1);
    catalog += f2;
    d.an = 2019; d.luna = 12; d.zi = 12;
    Examen *p = new Partial("PP", d, 5, 7);
    catalog += p;
    Examen *f3 = new Final("LM", d, 6, 3);
    catalog += f3;
    catalog.afisare();
    /*vector<CatalogIndividual<Examen>> catFac;
    catFac.push_back(catalog);
    catFac[0].setID(5);
    //catFac[0].afisare();
    */
    Final *fprim1 = dynamic_cast<Final*>(f1);
    Final *fprim2 = static_cast<Final*>(f2);
    Final *fprim3 = dynamic_cast<Final*>(f3);
    fprim1->notaScrisNoua();
    fprim2->notaScrisNoua();
    fprim3->notaScrisNoua();
    finals.calcM(fprim1);
    finals.calcM(fprim2);
    finals.calcM(fprim3);
    finals.displayM();

    fin.close();

    Examen *j = new Partial();

    cin >> (*j);
    catalog += j;

    return 0;
}
