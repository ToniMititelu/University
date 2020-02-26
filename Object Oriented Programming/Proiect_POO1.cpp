#include <iostream>
#include <fstream>
#include <vector>
#include <queue>

using namespace std;

class Graph
{
	int N, M;

	vector< vector<int> > adj, componente;

public:
    void muchie(int node1, int node2);
    friend istream & operator >> (istream &in,  Graph &c);
	friend ostream & operator << (ostream &out, const Graph &c);
	void utilDFS(int i, bool visited[]);
    void DFS();
    void utilBFS(int nod, bool visited[]);
    void BFS();
    void markVisited(int i, bool visited[], int nrComp);
	int numaraComponente();
	void compConexe();
	void verifConex();
	void matriceDrumuri();
	friend Graph operator+ (Graph g1, Graph g2);
};

void Graph::matriceDrumuri()
{
    vector< vector<int> > matrix = vector< vector<int> >(N, vector<int>(N, 0));

    for(int i = 0; i < N; ++i)
        for(auto j : adj[i])
        {
            matrix[i][j] = matrix[j][i] = 1;
        }

    for(int k = 0 ; k < N ; ++k)
        for(int i = 0 ; i < N ; ++i)
            for(int j = 0 ; j < N ; ++j)
                if(matrix[i][j] == 0)
                    matrix[i][j] = matrix[i][k] * matrix[k][j];

    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
            cout << matrix[i][j] << " ";
        cout << endl;
    }
}

void Graph::utilBFS(int nod, bool visited[])
{
    queue<int> C;

    visited[nod] = true;
    C.push(nod);

    while(!C.empty())
    {
        int curr_nod = C.front();
        C.pop();
        cout << curr_nod << " ";

        for(auto k : adj[curr_nod])
            if(visited[k] == false)
            {
                C.push(k);
                visited[k] = true;
            }
    }
}

void Graph::BFS()
{
    bool *visited = new bool[N];
	for(int i = 0; i < N; ++i)
		visited[i] = false;

    for(int i = 0; i < N; ++i)
        if(visited[i] == false)
            utilBFS(i, visited);
    cout << "\n";
}

void Graph::muchie(int node1, int node2)
{
	adj[node1].push_back(node2);
	adj[node2].push_back(node1);
}

void Graph::markVisited(int i, bool visited[], int nrComp)
{
	visited[i] = true;
    componente[nrComp].push_back(i);

	for(auto k : adj[i])
		if(visited[k] == false)
			markVisited(k, visited, nrComp);
}

int Graph::numaraComponente()
{
    bool *visited = new bool[N];
	for(int i = 0; i < N; ++i)
		visited[i] = false;

    componente = vector< vector<int> >(N);
    int nrComp = 0;

	for (int i = 0; i < N; ++i)
	{
		if (visited[i] == false)
		{
			markVisited(i, visited, nrComp);
			nrComp++;
		}
	}

	return nrComp;
}

void Graph::utilDFS(int i, bool visited[])
{
    visited[i] = true;
    cout << i << " ";

	for(auto k : adj[i])
		if(visited[k] == false)
			utilDFS(k, visited);
}

void Graph::DFS()
{
    bool *visited = new bool[N];
	for(int i = 0; i < N; ++i)
		visited[i] = false;

	for (int i = 0; i < N; ++i)
	{
		if (visited[i] == false)
		{
			utilDFS(i, visited);
		}
	}
    cout << "\n";
}

void Graph::compConexe()
{
    int nrComp = numaraComponente();
	for(int i = 0; i < nrComp; ++i)
    {
        cout << "Componenta " << i+1 << " : ";
        for(auto j : componente[i])
            cout << j << " ";
        cout << endl;
    }
}

void Graph::verifConex()
{
    int nrComp = numaraComponente();
	if(nrComp > 1)
        cout << "Nu este conex\n";
    else
        cout << "Este conex\n";
}

istream & operator >> (istream &in,  Graph &g)
{
    int node1, node2, i = 0;

    in >> g.N >> g.M;

    g.adj = vector< vector<int> >(g.N);

    while(i < g.M)
    {
        in >> node1;
        in >> node2;
        g.muchie(node1, node2);
        ++i;
    }
    return in;
}

ostream & operator << (ostream &out, const Graph &g)
{
    for(int i = 0; i < g.N; ++i)
    {
        out << i << " : ";
        for(auto k : g.adj[i])
            out << k << " ";
        out << endl;
    }
    return out;
}

Graph operator+ (Graph g1, Graph g2)
{
    for(int i = 0; i < g1.N; i++)
    {
        for(auto j : g2.adj[i]){
            bool ok = true;
            for(auto k : g1.adj[i])
                if(j == k)
                    ok = false;
            if(ok == true) g1.adj[i].push_back(j);
        }
    }
    return g1;
}

void meniu()
{
    cout << "1. Afiseaza graf\n";
    cout << "2. Parcurgere in latime\n";
    cout << "3. Parcurgere in adancime\n";
    cout << "4. Matricea drumurilor\n";
    cout << "5. Determina componentele conexe\n";
    cout << "6. Este graful conex?\n";
    cout << "7. Reuniunea a doua grafuri\n";
    cout << "0. Exit\n";
}

int main()
{
    ifstream fin("date.in");
	Graph g;
    fin >> g;

	int operatie = -1;
	while(operatie != 0)
    {
        meniu();
        cin >> operatie;
        switch(operatie)
        {
            case 1 : cout << g; break;
            case 2 : g.BFS(); break;
            case 3 : g.DFS(); break;
            case 4 : g.matriceDrumuri(); break;
            case 5 : g.compConexe(); break;
            case 6 : g.verifConex(); break;
            case 7 :
                {
                    Graph gPrim, gNou;
                    fin >> gPrim;
                    gNou = g + gPrim;
                    cout << gNou;
                    break;
                }
            case 0 : operatie = 0; break;
            default : cout << "Operatie invalida\n"; break;
        }
    }

	return 0;
}
