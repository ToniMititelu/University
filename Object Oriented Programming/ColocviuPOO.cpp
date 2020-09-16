// This was a 90 min exam and this is what i managed to achieve in that time 

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

class Statie
{
protected:
    string strada;
    int numar, sector, nrMijTransport;
    vector<int> mijTransport;
    bool punctImportant;
    string numePunct;
    int linieDirecta;
    int ID;
    string tip;
public:
    Statie() { }
    Statie(string s, int nr, int sec, vector<int> mij, bool PI, string np)
    {
        this->strada = s;
        this->numar = nr;
        this->sector = sec;
        for(auto i : mij) {
            mijTransport.push_back(i);
        }
        this->nrMijTransport = mijTransport.size();
        this->punctImportant = PI;
        this->numePunct = np;
        this->tip = "NU";
    }
    virtual ~Statie()
    {

    }
    virtual void cit(istream& in)
    {
        cout << "Strada: "; in >> strada;
        cout << "Numar: "; in >> numar;
        cout << "Sector: "; in >> sector;
        cout << "Linie directa cu: "; in >> linieDirecta;
        cout << "Nr mij transport: "; in >> nrMijTransport;
        for(int i=0; i<nrMijTransport; i++)
        {
            int x;
            in >> x;
            mijTransport.push_back(x);
        }
    }
    virtual void afis(ostream& out)
    {
        out << "Strada: " << strada << endl;
        out << "Numar: " << numar << endl;
        out << "Sector: " << sector << endl;
        if(punctImportant == true)
            out << "Punct important" << numePunct << endl;
        out << "Nr mij transport prin statie: " << nrMijTransport << endl;
        out << "Mij de transport care trec prin statie: ";
        for(auto i : mijTransport)
            out << i << " ";
        out << endl;
    }
    friend istream & operator >> (istream& in, Statie &S)
    {
        S.cit(in);
        return in;
    }
    friend ostream & operator << (ostream& out, Statie &S)
    {
        S.afis(out);
        return out;
    }
    void setLiniDirecta(int n)
    {
        linieDirecta = n;
    }
    void setID(int n)
    {
        ID = n;
    }
    int getNR()
    {
        return numar;
    }
    int getID()
    {
        return ID;
    }
    string getAdr()
    {
        return strada;
    }
    string getTip()
    {
        return tip;
    }
    int getLinieDir()
    {
        return linieDirecta;
    }
    vector<int> getVect()
    {
        return mijTransport;
    }
};

class StatieUrbana : virtual public Statie
{
 protected:
    bool punctAprovizionare;
 public:
    StatieUrbana() { this->tip = "SU"; }
    StatieUrbana(string s, int nr, int sec, vector<int> mij, bool ok, bool PI, string np) : Statie(s, nr, sec, mij, PI, np)
    {
        this->punctAprovizionare = ok;
        this->tip = "SU";
    }
    ~StatieUrbana()
    {

    }
    void cit(istream& in)
    {
        cout << "Strada: "; in >> strada;
        cout << "Numar: "; in >> numar;
        cout << "Sector: "; in >> sector;

        cout << "Linie directa cu: "; in >> linieDirecta;
        int x;
        cout << "Punct important (1-da, 0-nu): "; in >> x;
        if(x)
            punctImportant = true;
        else
            punctImportant = false;
        if(punctImportant){
            cout << "Nume pct imp: "; in >> numePunct;
        }
        else
            numePunct = "*";
        cout << "Punct aprovizionare (1-da, 0-nu): "; in >> x;
        if(x)
            punctAprovizionare = true;
        else
            punctAprovizionare = false;
        cout << "Nr mij transport: "; in >> nrMijTransport;
        for(int i=0; i<nrMijTransport; i++)
        {
            int x;
            in >> x;
            mijTransport.push_back(x);
        }
    }
    void afis(ostream& out)
    {
        out << "Statie urbana\n";
        out << "Strada: " << strada << endl;
        out << "Numar: " << numar << endl;
        out << "Sector: " << sector << endl;

        cout << "Linie directa cu: "; in >> linieDirecta;
        if(punctImportant == true)
            out << "Punct important" << numePunct << endl;
        out << "Punct aprovizionare: " << punctAprovizionare << endl;
        out << "Nr mij transport prin statie: " << nrMijTransport << endl;
        out << "Mij de transport care trec prin statie: ";
        for(auto i : mijTransport)
            out << i << " ";
        out << endl;
    }
    friend istream & operator >> (istream& in, StatieUrbana &S)
    {
        S.cit(in);
        return in;
    }
    friend ostream & operator << (ostream& out, StatieUrbana &S)
    {
        S.afis(out);
        return out;
    }
};

class StatieExterna : virtual public Statie
{
public:
    StatieExterna() { this->tip = "SE"; }
    StatieExterna(string s, int nr, int sec, vector<int> mij, bool PI, string np) : Statie(s, nr, sec, mij, PI, np)
    {
        this->tip = "SE";
    }
    ~StatieExterna()
    {

    }
    void cit(istream& in)
    {
        cout << "Strada: "; in >> strada;
        cout << "Numar: "; in >> numar;
        cout << "Sector: "; in >> sector;
        int x;
        cout << "Punct important (1-da, 0-nu): "; in >> x;
        if(x)
            punctImportant = true;
        else
            punctImportant = false;
        if(punctImportant) {
            cout << "Nume pct imp: "; in >> numePunct;
        }
        else
            numePunct = "*";
        cout << "Linie directa cu: "; in >> linieDirecta;
        cout << "Nr mij transport: "; in >> nrMijTransport;
        for(int i=0; i<nrMijTransport; i++)
        {
            int x;
            in >> x;
            mijTransport.push_back(x);
        }
    }
    void afis(ostream& out)
    {
        out << "Statie externa\n";
        out << "Strada: " << strada << endl;
        out << "Numar: " << numar << endl;
        out << "Sector: " << sector << endl;
        if(punctImportant == true)
            out << "Punct important" << numePunct << endl;
        out << "Nr mij transport prin statie: " << nrMijTransport << endl;
        out << "Mij de transport care trec prin statie: ";
        for(auto i : mijTransport)
            out << i << " ";
        out << endl;
    }
    friend istream & operator >> (istream& in, StatieExterna &S)
    {
        S.cit(in);
        return in;
    }
    friend ostream & operator << (ostream& out, StatieExterna &S)
    {
        S.afis(out);
        return out;
    }
};

int calculDiscount(Statie *s1, Statie *s2)
{
    if(s1->getTip() == s2->getTip() && s1->getTip() == "SU") {
        if(s1->getLinieDir() != s2->getID())
            return 15;
    }
    if(s1->getTip() == s2->getTip() && s1->getTip() == "SE") {
        if(s1->getLinieDir() == s2->getID())
            return 20;
        else
            return 25;
    }
     if(s1->getTip() != s2->getTip()) {
        if(s1->getLinieDir() == s2->getID())
            return 30;
        else
            return 40;
    }
}

template <class T> class STB
{
    int ID;
    vector<T*> statii;
public:
    STB() { ID=0; }
    operator += (Statie *S)
    {
        statii.push_back(S);
        ID++;
        S->setID(ID);
    }
    void afsiStatiipPrinCareTreceMij()
    {
        int id;
        cout << "Numarul mijlocului de transport: "; cin >> id;
        for(auto statie : statii)
            for(auto i : statie->getVect())
                if(id == i)
                    cout << (*statie) << endl;
    }
    void afisDetaliiStatie()
    {
        cout << "Alegeti dupa ce vreti sa cautati: \n";
        cout << "1. Numar\n2. Adresa\n3. Cod\n";
        int op;
        cin >> op;
        if(op == 1)
        {
            int nr;
            cin >> nr;
            for(auto statie : statii)
                if(statie->getNR() == nr)
                {
                    cout << (*statie) << "\n";
                    break;
                }
        }
        else
            if(op==2)
            {
                string adresa;
                cin >> adresa;
                for(auto statie : statii)
                if(statie->getAdr() == adresa)
                {
                    cout << (*statie) << "\n";
                    break;
                }
            }
            else
                if(op==3)
                {
                    int cod;
                    cin >> cod;
                    for(auto statie : statii)
                        if(statie->getID() == cod)
                        {
                            cout << (*statie) << "\n";
                            break;
                        }
                }
    }
    void calculDiscount(string nume1, string nume2)
    {

    }
};

void meniu()
{
    cout << "1. Adaugare statie\n2. Afisare detalii statie\n3. Afisare statii prin care trece un bus\n4. Estimare pret\n0. Exit\n";
}

int main()
{
    /*vector<int> v(3, 1);
    Statie s("Str", 3, 1, v);
    cout << s;
    Statie s1;
    cin >> s1;
    cout << s1;
    Statie *s = new StatieExterna();
    cin >> (*s);
    cout << (*s);*/
    STB<Statie> buc;
    int nr_statii;
    cin >> nr_statii;
    for(int i=0; i<nr_statii; i++)
    {
        Statie *s = new Statie();
        cin >> (*s);
        buc += s;
    }

    int operatie = -1;
    while(operatie != 0)
    {
        meniu();
        cin >> operatie;
        if(operatie==1)
        {
            int x;
            cout << "1 SE, 2 SU";
            cin >> x;
            if(x == 1)
            {
                Statie *s = new StatieExterna();
                cin >> (*s);
                buc += s;
            }
            else
            {
                Statie *s = new StatieUrbana();
                cin >> (*s);
                buc += s;
            }
        }
        if(operatie==2)
        {
            buc.afisDetaliiStatie();
        }
        if(operatie==3)
        {
            buc.afsiStatiipPrinCareTreceMij();
        }
        if(operatie==4)
        {

        }

    }
    return 0;
}
