using System;
using System.Collections.Generic;
using TEdge = QuickGraph.UndirectedEdge<string>;
using TVertex = System.String;
using TEdgeString = System.String;

namespace AutomataLibrary2D
{
    public static class MF
    {
        public static TVertex BuildTVertexID(int i, int j)                         // Construye un vector dada las coordenadas
        {
            return (i.ToString() + "," + j.ToString());
        }
        public static TVertex BuildTVertexID(int[] pos)                            // Construye un vector dado un array con las coordenadas
        {
            if (pos.Length != 2) throw new Exception("Array must have size 2."); ;
            return (pos[0].ToString() + "," + pos[1].ToString());
        }
        public static int[] GetTVertexID(TVertex v)                                // Dado un vector te devulve un array con las coordenadas
        {
            string[] strpos = v.Split(',');
            int[] intpos = new int[strpos.Length];
            for (int i = 0; i < strpos.Length; i++)
                intpos[i] = int.Parse(strpos[i]);
            return intpos;
        }
        public static int[] BuildVector(int[] origin, int[] dest)                   // Devuelve un array con las coordenadas del vector origen-destino 
        {
            return new int[2] { dest[0] - origin[0], dest[1] - origin[1]};          // Formula para obtener un vector dada las pos ininciales y finales de este
        }
        public static int ConvertCellStateToInt(CellState state)                    // Convierte a un estado en un valor numerico que lo representa
        {
            switch (state)
            {
                default: throw new Exception("Wrong state passed.");
                case CellState.Lumen: return 0;
                case CellState.Epith: return 1;
                case CellState.Strom: return 2;
                case CellState.Tumor: return 3;
                case CellState.Migra: return 4;
                case CellState.Micro: return 5;
            }
        }
        public static CellState ConvertIntToCellState(int state)                    // Convierte un valor numerico que representa  a un estado en el estado correspondiente 
        {
            switch (state)
            {
                default: return CellState.NULL;
                case 0: return CellState.Lumen;
                case 1: return CellState.Epith;
                case 2: return CellState.Strom;
                case 3: return CellState.Tumor;
                case 4: return CellState.Migra;
                case 5: return CellState.Micro;
            }
        }
        public static double GetSim(int[] expansionVector, int[] nutrientVector)    // Devuelve el coseno de similitud entre dos vectores  
        {
            if (expansionVector.Length != nutrientVector.Length)
                throw new Exception("Computing sim between vectors with different length.");
            var num = 0.0;
            var den0 = 0.0;
            var den1 = 0.0;
            for (int i = 0; i < expansionVector.Length; i++)
            {
                num += expansionVector[i] * nutrientVector[i];
                den0 += Math.Pow(expansionVector[i], 2);
                den1 += Math.Pow(nutrientVector[i], 2);
            }
            den0 = Math.Sqrt(den0);
            den1 = Math.Sqrt(den1);
            return num / (den0 * den1);
        }
        public static int GetMaxValueIndex(List<double> doubleList)                 // Devuelve el indice que contiene el mayor malor de una lista
        {
            int index = 0;
            var max_value = doubleList[0];
            for (int i = 1; i < doubleList.Count; i++)
            {
                if (max_value < doubleList[i])
                {
                    index = i;
                    max_value = doubleList[i];
                }
            }
            return index;
        }

        //(pag35)Dado un valor del radio de la vecindad (R) devuelve una lista con los vertices que representan una direccion que al ser sumados con la pos act te dara los vecinos inmediatos
        public static List<TVertex> GetRegularNeighboursTemplate(double R)  
        {
            var result = new List<TVertex>();
            var R_s = new List<int>();                                                
            for (int i = -1 * (int)Math.Ceiling(R); i <= (int)Math.Ceiling(R); i++)
                R_s.Add(i);
            for (int i = 0; i < R_s.Count; i++)
                for (int j = 0; j < R_s.Count; j++)
                {
                    var R_vertex = Math.Sqrt(Math.Pow(R_s[i], 2) + Math.Pow(R_s[j], 2));   
                    if (R_vertex <= R)
                        result.Add(BuildTVertexID(R_s[i], R_s[j]));                      
                }
            return result;
        }

        // Dado una lista con las direcciones que representa a mis vecinos se eliminan las direcciones que cumplen() y me quedo con el resto de las direcciones
        public static List<TVertex> FilterRegularNeighboursTemplate(List<TVertex> template)
        {
            List<TVertex> templateCopy = new List<TVertex>();
            templateCopy.AddRange(template);
            templateCopy.Remove(BuildTVertexID(0, 0));

            List<TVertex> result = new List<TVertex>();
            List<TVertex> pair = new List<TVertex>();
            while (templateCopy.Count != 0)
            {
                TVertex current = templateCopy[0];        //guarda la direccion en foma de vertive
                int[] currentPos = GetTVertexID(current); //guarda la direccion en forma de array
                templateCopy.RemoveAt(0);                 //elimina la direccion de donde estan todas(templatecopy)

                result.Add(current);                      //guarda en result el vertice con la direccion
                
                for (int i = 0; i < templateCopy.Count; i++)
                {
                    TVertex vertex = templateCopy[i];        //guarda la direccion en foma de vertive
                    int[] vertexPos = GetTVertexID(vertex);  //guarda la direccion en forma de array

                    var component = 0;           
                    for (int j = 0; j < currentPos.Length; j++)
                    {
                        if (currentPos[j] != 0)
                        {
                            component = j;
                            break;
                        }
                    }
                    
                    var lambda = vertexPos[component] / (double)currentPos[component]; // cojo x o y de las direccion del vecino y la divido con la direccion anterior
                    var condition = true;
                    for (int k = 0; k < 2; k++)
                        if (component != k)
                            condition &= lambda * currentPos[k] == vertexPos[k];
                    if (condition)
                    {
                        pair.Add(vertex);
                        templateCopy.Remove(vertex);  //Elimina el vertice
                        break;
                    }
                }
                templateCopy.Remove(pair[pair.Count - 1]);
            }
            return result;
        }

        //Devuelve una nueva posicion valida a partir de sumarle a un vertice una direccion 
        public static TVertex GetVertexUnCyclic(TVertex v, int dx, int dy, int sx, int sy) 
        {
            //sx el max valor de x y sy el maximo valor valido en y
            var pos = GetTVertexID(v);
            int xf = pos[0] + dx;
            int yf = pos[1] + dy;
            if (xf < 0 || xf >= sx || yf < 0 || yf >= sy) return null;   
            return BuildTVertexID(xf, yf);
        }

        //Devuelve una nueva posicion () a partir de sumarle a un vertice una direccion (Trabaja con aristas periódicas)
        public static TVertex GetVertexCyclic(TVertex v, int dx, int dy, int sx, int sy)
        {
            //sx el max valor de x y sy el maximo valor valido en y
            var pos = GetTVertexID(v);
            int xf = pos[0] + dx;
            int yf = pos[1] + dy;
            if (xf < 0) xf = sx + (pos[0] + dx);
            if (xf >= sx) xf = pos[0] - (dx + 1);
            if (yf < 0) yf = sy + (pos[1] + dy);
            if (yf >= sy) yf = pos[1] - (dy + 1);
            if (xf < 0 || yf < 0)
                throw new Exception("Vertex with negative component.");
            return BuildTVertexID(xf, yf);
        }

        public static string RemoveBlankSpaces(string input)    //Elimina espacios en blanco
        {
            var noBlankSpaces = input.Split(' ');
            string result = string.Empty;
            for (int i = 0; i < noBlankSpaces.Length; i++)
                result += noBlankSpaces[i];
            return result;
        }
        public static string[] GetVertexsFromEdge(TEdgeString key)  //Devuelve los vertices de la arista
        {
            TVertex[] vertexs = new TVertex[2];
            int index = 0;
            for (int i = 0; i < key.Length; i++)
            {
                if (key[i] == '<')
                {
                    i += 2;
                    index = 1;
                }
                else vertexs[index] += key[i];
            }
            return vertexs;
        }
        public static double EuclideanDistance(TVertex v, TVertex w)   //Devuelve dado dos vertices las distancia euclideana entre ellos
        {
            int[] vpos = GetTVertexID(v);
            int[] wpos = GetTVertexID(w);
            return Math.Sqrt(Math.Pow(vpos[0] - wpos[0], 2) + Math.Pow(vpos[1] - wpos[1], 2));
        }
        public static List<double> GetNormalizedProbabilities(List<double> unnormalizedProbs)  // Normaliza cada uno de los numeros recibidos en la lista
        {
            double sum = 0;                                         //Sumatoria de las probabilidades en la lista
            for (int i = 0; i < unnormalizedProbs.Count; i++)
                sum += unnormalizedProbs[i];                       

            List<double> normalizedProbs = new List<double>();
            for (int i = 0; i < unnormalizedProbs.Count; i++)
            {
                double normalizedProb = unnormalizedProbs[i] / sum;  //Normalización por elemento
                normalizedProbs.Add(normalizedProb);
            }
            return normalizedProbs;
        }

        //Devuelve una lista que en la pos i se encuentra la sumatoria de los elementos de la lista de entrada hasta la pos i
        public static List<double> GetNormalizedAddedProbs(List<double> normalizedProbs)    
        {
            List<double> added = new List<double> { 0 };
            double sum = 0;
            for (int i = 0; i < normalizedProbs.Count; i++)
            {
                sum += normalizedProbs[i];                 
                added.Add(sum);
            }
            added[added.Count - 1] += 1;
            return added;
        }
        
        public static string Reverse(string input)    //Devuelve el reverso de una cadena de string input
        {
            string reversed = input[input.Length - 1].ToString();
            for (int i = input.Length - 2; i >= 0; i--)
                reversed += input[i];
            return reversed;
        }

        public static bool IsEdgeContainedInList(TEdge edge, List<TEdge> list) //Verifica si una arista esta contenida en una lista de aristas
        {
            for (int i = 0; i < list.Count; i++)
            {
                bool compared = (edge.Source == list[i].Source && edge.Target == list[i].Target) ||
                    (edge.Source == list[i].Target && edge.Target == list[i].Source);
                if (compared) return true;
            }
            return false;
        }
    }
}