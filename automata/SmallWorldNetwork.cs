﻿using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using QuickGraph;
using TEdge = QuickGraph.UndirectedEdge<string>;
using TVertex = System.String;
using TEdgeString = System.String;

namespace AutomataLibrary2D
{
    public class SmallWorldNetwork
    {
        private UndirectedGraph<TVertex, TEdge> _g = null;                                                     // Grafo 
        private Random _random = null;
        private NetworkSettings _networkSettings = null;                                                       // Configuracione de la red de mundo pequeño
        private NetworkPropertiesData _networkProperties = null;                            
        private int _reconnectedEdgesAmount = 0;                                                               // Cantidad de aristas reconectadas

        public List<TVertex> Vertices { get { return _g.Vertices.ToList(); } }                                 // Vértices del grafo
        public List<TEdge> Edges { get { return _g.Edges.ToList(); } }                                         // Aristas del grafo
        public double AveragePathLength { get { return _networkProperties.AveragePathLength; } }               // Longitud promedio del camino de la red Lg
        public double ClusteringCoefficient { get { return _networkProperties.ClusteringCoefficient; } }       // Coeficiente de agrupamiento Cg
        public int NetworkSizeX { get { return _networkSettings.NetworkSizeX; } }                              // sx: cantidad de x que conforman vertices
        public int NetworkSizeY { get { return _networkSettings.NetworkSizeY; } }                              // sy: cantidad de y que conforman vertices
        public int NetworkDivision { get { return _networkSettings.NetworkDivision; } }                        // so :  indica la división del grafo entre una localizaci´on y la otra.
        public double NeighbourhoodRadius { get { return _networkSettings.NeighbourhoodRadius; } }             // R : valor del radio de la vecindad inmediata

        public SmallWorldNetwork(NetworkSettings network)
        {
            //Inicialización de las variables grafo , datos y configuración de la red
            _g = new UndirectedGraph<TVertex, TEdge>();
            _random = new Random();
            _networkProperties = new NetworkPropertiesData();
            _networkSettings = network;

            // Agrega los vertices al grafo 
            int timeStart = Environment.TickCount;
            Console.WriteLine("   smallworldnetwork library: adding vertices...");
            FillVertices();                                                                                             
            int elapsedMiliseconds = Environment.TickCount - timeStart;
            string formattedTime = Notification.TimeStamp(elapsedMiliseconds);
            Console.WriteLine("   smallworldnetwork library: finished adding vertices" + formattedTime);
            Console.WriteLine("   smallworldnetwork library: added " + _g.VertexCount + " vertices");

            // Agrega las aristas al grafo 
            timeStart = Environment.TickCount;
            Console.WriteLine("   smallworldnetwork library: adding regular edges...");
            FillRegularEdges();
            elapsedMiliseconds = Environment.TickCount - timeStart;
            formattedTime = Notification.TimeStamp(elapsedMiliseconds);
            Console.WriteLine("   smallworldnetwork library: finished adding regular edges" + formattedTime);
            Console.WriteLine("   smallworldnetwork library: added " + _g.EdgeCount + " regular edges");
            
            
            if (_networkSettings.ReconnectionProbability != 0)          // Si hay probabilidad de reconexión, reconecta las vertices
            {
                timeStart = Environment.TickCount;
                Console.WriteLine("   smallworldnetwork library: rewiring edges...");
                RewireEdges(_networkSettings.ReconnectionProbability);
                elapsedMiliseconds = Environment.TickCount - timeStart;
                formattedTime = Notification.TimeStamp(elapsedMiliseconds);
                Console.WriteLine("   smallworldnetwork library: finished rewiring edges" + formattedTime);
                Console.WriteLine("   smallworldnetwork library: added " + _reconnectedEdgesAmount + " rewired edges");
            }
            if (_networkSettings.IsNetworkTest == true)
            {
                timeStart = Environment.TickCount;
                Console.WriteLine("   smallworldnetwork library: determining network properties...");
                _networkProperties.AveragePathLength = GetAveragePathLength();
                _networkProperties.ClusteringCoefficient = GetClusteringCoefficient();
                elapsedMiliseconds = Environment.TickCount - timeStart;
                formattedTime = Notification.TimeStamp(elapsedMiliseconds);
                Console.WriteLine("   smallworldnetwork library: finished determining the properties" + formattedTime);
            }
        }
        public SmallWorldNetwork(NetworkSettings network, string networkpath)
        {
            _g = new UndirectedGraph<TVertex, TEdge>();
            _random = new Random();
            _networkProperties = new NetworkPropertiesData();
            _networkSettings = network;

            int timeStart = Environment.TickCount;
            Console.WriteLine("   smallworldnetwork library: loading vertices...");
            LoadVertices(networkpath);
            int elapsedMiliseconds = Environment.TickCount - timeStart;
            string formattedTime = Notification.TimeStamp(elapsedMiliseconds);
            Console.WriteLine("   smallworldnetwork library: finished loading vertices" + formattedTime);
            Console.WriteLine("   smallworldnetwork library: added " + _g.VertexCount + " vertices");

            timeStart = Environment.TickCount;
            Console.WriteLine("   smallworldnetwork library: loading edges...");
            LoadEdges(networkpath);
            elapsedMiliseconds = Environment.TickCount - timeStart;
            formattedTime = Notification.TimeStamp(elapsedMiliseconds);
            Console.WriteLine("   smallworldnetwork library: finished loading edges" + formattedTime);
            Console.WriteLine("   smallworldnetwork library: added " + _g.EdgeCount + " edges");

            if (_networkSettings.IsNetworkTest == true)
            {
                timeStart = Environment.TickCount;
                Console.WriteLine("   smallworldnetwork library: determining network properties...");
                _networkProperties.AveragePathLength = GetAveragePathLength();
                _networkProperties.ClusteringCoefficient = GetClusteringCoefficient();
                elapsedMiliseconds = Environment.TickCount - timeStart;
                formattedTime = Notification.TimeStamp(elapsedMiliseconds);
                Console.WriteLine("   smallworldnetwork library: finished determining the properties" + formattedTime);
            }
        }

        //Restablecer las variables
        public void Dispose()
        {
            _networkSettings = null;
            _networkProperties = null;
            _random = null;
            _g.Clear();
        }

        //Carga los vertices desde un archivo o .text
        private void LoadVertices(string networkpath)
        {
            string[] textbody = File.ReadAllLines(networkpath);
            int textbodyLength = textbody.Length;
            bool mark = false;
            bool written = false;
            for (int i = 0; i < textbodyLength; i++)
            {
                Notification.CompletionNotification(i, textbody.Length, ref written, "      ");
                if (mark && textbody[i] != string.Empty && textbody[i] != "[Edges]")
                    _g.AddVertex(textbody[i]);
                if (textbody[i] == "[Vertexs]")
                    mark = true;
                if (textbody[i] == "[Edges]")
                    break;
            }
            Notification.FinalCompletionNotification("      ");
        }

        //Carga las aristas desde un archivo o .text
        private void LoadEdges(string networkpath)
        {
            string[] textbody = File.ReadAllLines(networkpath);
            int textbodyLength = textbody.Length;
            bool mark = false;
            bool written = false;
            for (int i = 0; i < textbodyLength; i++)
            {
                Notification.CompletionNotification(i, textbody.Length, ref written, "      ");
                if (mark && textbody[i] != string.Empty && textbody[i] != "[EOF]")
                {
                    var vertexs = MF.GetVertexsFromEdge(textbody[i]);
                    _g.AddEdge(new TEdge(vertexs[0], vertexs[1]));
                }
                if (textbody[i] == "[Edges]")
                    mark = true;
                if (textbody[i] == "[EOF]")
                    break;
            }
            Notification.FinalCompletionNotification("      ");
        }

        
        private void FillVertices()                //Agrega los vertices al grafo
        {
            bool written = false;
            int inf = 0;
            int sup = _networkSettings.NetworkSizeX * _networkSettings.NetworkSizeY; //cant maxima de nodos del grafo y cant de elementos o casillas de la matriz
            for (int i = 0; i < _networkSettings.NetworkSizeX; i++)
                for (int j = 0; j < _networkSettings.NetworkSizeY; j++)
                {
                    Notification.CompletionNotification(inf, sup, ref written, "      ");
                    inf++;
                    _g.AddVertex(MF.BuildTVertexID(i, j));    //Los vértices del grafo contienen una posicion referente en la matriz
                }
            Notification.FinalCompletionNotification("      ");
        }
        private void FillRegularEdges()                //Agrega las aristas al grafo 
        {
            List<TVertex> template = MF.GetRegularNeighboursTemplate(_networkSettings.NeighbourhoodRadius);
            List<TVertex> filtered = MF.FilterRegularNeighboursTemplate(template);      // direccion de vecinos inmediatos
            List<TVertex> vg = _g.Vertices.ToList();                                    // vértices en el grafo
            int vgCount = vg.Count;
            int filteredCount = filtered.Count;                                         // cantidad de direcciones de vecinos inmediatos
            
            bool written = false;
            for (int i = 0; i < vgCount; i++)                                           // itera por los vértices
            {
                Notification.CompletionNotification(i, vg.Count, ref written, "      ");
                TVertex vertex = vg[i];                                                 // vértice i

                for (int j = 0; j < filteredCount; j++)                                 // itera por las direcciones
                {
                    TVertex dir = filtered[j];                                          // dirección j
                    int[] dir_pos = MF.GetTVertexID(dir);                               // vértice de la dirección j 

                    TVertex wertex = string.Empty;
                    
                    if (_networkSettings.HasPeriodicEdges)                              // Si la matriz contiene aristas periódicas
                        wertex = MF.GetVertexCyclic(vertex, dir_pos[0], dir_pos[1], _networkSettings.NetworkSizeX, _networkSettings.NetworkSizeY);
                    
                    else wertex = MF.GetVertexUnCyclic(vertex, dir_pos[0], dir_pos[1], _networkSettings.NetworkSizeX, _networkSettings.NetworkSizeY);
                    
                    if (wertex != null)
                    {
                        TEdge edge = new TEdge(vertex, wertex);
                        _g.AddEdge(edge);                                              // Agrega la arista al grafo 
                    }
                }
            }
            Notification.FinalCompletionNotification("      ");
        }

        //Establece nuevas conexiones entre los vertices del grafo y elimina algunas conexiones si se cumple la condicion de un random menor que p
        //Ver foto enviada en el grupo la explicacion es larga para un mejor entendimiento
        private void RewireEdges(double p)                                              //  p : probabilidad de reconexion de aristas de forma aleatoria
        {
            Dictionary<TEdgeString, TVertex> reconnectionsDict = new Dictionary<TEdgeString, TVertex>();
            List<TVertex> vg = _g.Vertices.ToList();                                          // Dame los vertices del grafo
            int vgCount = vg.Count;                                                           // Dame la catn de vertices que hay
            bool written = false;

            for (int i = 0; i < vgCount; i++)                                                 // Itera por los vertices
            {
                Notification.CompletionNotification(i, vg.Count, ref written, "      ");
                TVertex vertex = vg[i];                                                       // Dame el vertice i
                List<TEdge> edges = _g.AdjacentEdges(vertex).ToList();                        // Dame todas las aristas adyacentes al vertex
                int edgesCount = edges.Count;                                                 // Dame la cant de aristas adyacentes
                
                for (int j = 0; j < edgesCount; j++)                                          // Itera por las aristas adyacentes
                {
                    TEdge edge = edges[j];                                                    // Dame la arista j
                    if (edge.Source == vertex)                                                // Si el vertice origen de j es al que le estoy recorriendo sus aristas adyacentes
                    {
                        TVertex oldtarget = edge.Target;                                      // Vertice destino de la arista o adyacente de i
                        
                        int[] vpos = MF.GetTVertexID(vertex);                                 
                        TVertex newtarget;
                        TEdge newedge;
                        int x = 0, y = 0;
                        List<TVertex> regularNeighbours = new List<TVertex>();
                        
                        //Agrega todos los vertices adyacentes al vertice i
                        for (int k = 0; k < edgesCount; k++)
                        {
                            if (edges[k].Source == vertex) regularNeighbours.Add(edges[k].Target);
                            else if (edges[k].Target == vertex) regularNeighbours.Add(edges[k].Source);  //Agrega todos los vertices adyacentes al vertice i
                            else throw new Exception("Error in neighbourhood.");
                        }

                        double random = _random.NextDouble();
                        //Crea un nuevo vertor y una nueva arista adyacente al vertice i, que no este relacionado a el de ninguna forma y los conecta, siempre y cuando se cumpla la condicion
                        if (random < p)                                 
                        {
                            do    //Crea un nuevo vertor random y una nueva arista adyacente al vertice i, que no este relacionado a el de ninguna forma y los conecta
                            {
                                x = _random.Next(_networkSettings.NetworkSizeX);
                                y = _random.Next(_networkSettings.NetworkSizeY);
                                newtarget = MF.BuildTVertexID(x, y);          
                                newedge = new TEdge(vertex, newtarget);
                            }
                            while ((vpos[0] == x && vpos[1] == y) || (regularNeighbours.Contains(newtarget)) ||
                                   (reconnectionsDict.ContainsKey(newedge.ToString())));
                            
                            reconnectionsDict.Add(newedge.ToString(), oldtarget);
                        }
                    }
                }
            }
            
            List<TEdgeString> reconnections = reconnectionsDict.Keys.ToList();               // Dame todas las reconexiones o aristasadyacentes random o lejanas
            int recCounts = reconnections.Count;

            for (int i = 0; i < recCounts; i++)
            {
                TEdgeString key = reconnections[i];                            // Dame la arista i de reconexion
                TVertex[] origin_newtarget_pair = MF.GetVertexsFromEdge(key);  // Dame los vertices de la arista i
                TVertex origin = origin_newtarget_pair[0];                     // Vertice origen de la arista i
                TVertex newtarget = origin_newtarget_pair[1];                  // Vertice destino de la arista i
                TVertex oldtarget = reconnectionsDict[key];                    // Dame el vertice destino del vertice origen de la arista i
                
                //Elimina
                TEdge to_remove_edge;
                bool obtained = _g.TryGetEdge(origin, oldtarget, out to_remove_edge);
                if (obtained) _g.RemoveEdge(to_remove_edge);
                else throw new Exception("Edge to be removed not found, internal problems.");
                
                //Agrega las aristas de reconexion al grafo
                TEdge to_add_edge = new TEdge(origin, newtarget);
                bool added = _g.AddEdge(to_add_edge);
                if (!added) throw new Exception("Edge to be add not added, internal problems.");
            }
            _reconnectedEdgesAmount = reconnections.Count;
            Notification.FinalCompletionNotification("      ");
        }

        //Devuelve el promedio de las ditancias
        //Analiza un nodo y luego sus veecinos
        //las distancias son calculadas de modo tal que los vecinos son 1+ la distancia del vertice
        private double GetAveragePathLength()
        {
            double average = 0.0;
            List<TVertex> vg = _g.Vertices.ToList();                      // Dame todos los vertices
            int vgCount = vg.Count;
            for (int i = 0; i < vgCount; i++)
            {
                TVertex vertex = vg[i];                                   // Dame el vertice i
                Dictionary<TVertex, int> pathLengths = new Dictionary<TVertex, int>();
                for (int j = 0; j < vgCount; j++)                         //Recorre todos los vertices y pone -1 en el path
                {
                    TVertex v = vg[j];                                   // Dame un vertice j y ponle distancia -1(Inicializa la distancia)
                    pathLengths.Add(v, -1);
                }
                pathLengths[vertex] = 0;                                 // Pone 0 en el path del vertice analizado
                
                Queue<TVertex> queue = new Queue<TVertex>();             // Cola de vertices
                queue.Enqueue(vertex);                                   // Agrega vertice i al final de la cola
                while (queue.Count != 0)
                {
                    TVertex currentNode = queue.Dequeue();               // Elimina el primer elemento de la cola
                    List<TEdge> adjacentEdges = _g.AdjacentEdges(currentNode).ToList(); // Dame las aristas adyacentes del eliminado
                    List<TVertex> neighbours = new List<TVertex>();
                    for (int j = 0; j < adjacentEdges.Count; j++)                      
                    {
                        TEdge edge = adjacentEdges[j];
                        neighbours.Add((edge.Source == currentNode) ? edge.Target : edge.Source);  //Agrega todos los vertices adyacentes del eliminado
                    }
                    for (int j = 0; j < neighbours.Count; j++)
                    {
                        TVertex neighbour = neighbours[j];
                        if (pathLengths[neighbour] == -1)
                        {
                            queue.Enqueue(neighbour);    //mete al vecino en la cola
                            pathLengths[neighbour] = pathLengths[currentNode] + 1; //ponle al vecino de path el del vertice +1
                        }
                    }
                }
                
                double average0 = 0.0;
                List<TVertex> pathLengthsLs = pathLengths.Keys.ToList();
                int path_lengths_lsCount = pathLengthsLs.Count;
                for (int j = 0; j < path_lengths_lsCount; j++)
                {
                    TVertex v = pathLengthsLs[j];
                    average0 += pathLengths[v];
                }
                average0 /= vg.Count;
                average += average0;
            }
            double result = Math.Round(average / vg.Count, 4);
            return result;
        }

        //Devuelve el Coeficiente de agrupamiento
        private double GetClusteringCoefficient()
        {
            double clusteringCoefficient = 0.0;
            List<TVertex> vg = _g.Vertices.ToList();
            int vgCount = vg.Count;
            // iterate over all vertices v \in V_G
            for (int i = 0; i < vgCount; i++)
            {
                TVertex v = vg[i];
                List<TEdge> neighbourhoodEdges = new List<TEdge>();
                List<TVertex> neighboursV = new List<TVertex>();
                List<TEdge> adjacentEdgesV = _g.AdjacentEdges(v).ToList();
                // iterate over the adjacent edges of v, fill the neighbours list of v
                for (int j = 0; j < adjacentEdgesV.Count; j++)
                {
                    TEdge edge = adjacentEdgesV[j];
                    neighboursV.Add((edge.Source == v) ? edge.Target : edge.Source);
                }
                // iterate over all the neighbours of v
                for (int j = 0; j < neighboursV.Count; j++)
                {
                    TVertex w = neighboursV[j];
                    List<TVertex> neighboursW = new List<TVertex>();
                    List<TEdge> adjacentEdgesW = _g.AdjacentEdges(w).ToList();
                    // iterate over the adjacent edges of w, fill the neighbours list of w
                    for (int k = 0; k < adjacentEdgesW.Count; k++)
                    {
                        TEdge edge = adjacentEdgesW[k];
                        neighboursW.Add((edge.Source == w) ? edge.Target : edge.Source);
                    }
                    // iterate over all the neighbours of w
                    for (int k = 0; k < neighboursW.Count; k++)
                    {
                        TVertex x = neighboursW[k];
                        TEdge newedge = new TEdge(w, x);
                        // if the w's neighbour x is neighbours with v AND
                        // the newedge has not been added yet AND
                        // the newedge is not an edge between v and w
                        bool cond1 = neighboursV.Contains(x);
                        bool cond2 = !MF.IsEdgeContainedInList(newedge, neighbourhoodEdges);
                        bool cond3 = !MF.IsEdgeContainedInList(newedge, adjacentEdgesV);
                        if (cond1 && cond2 && cond3)
                            neighbourhoodEdges.Add(newedge);
                    }
                }
                double possibleNumEdges = 0.0;
                possibleNumEdges = (neighboursV.Count * (neighboursV.Count - 1)) / (double)2;
                if (possibleNumEdges > 0)
                    clusteringCoefficient += neighbourhoodEdges.Count / possibleNumEdges;
            }
            double result = Math.Round(clusteringCoefficient / vg.Count, 4);
            return result;
        }

        public List<TEdge> AdjacentEdges(TVertex vertex)   // Dado un vertice devulve todas las aristas adyacentes a el
        {
            return _g.AdjacentEdges(vertex).ToList();
        }
    }
}