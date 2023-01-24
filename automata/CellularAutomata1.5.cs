using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using QuickGraph;
using TEdge = QuickGraph.UndirectedEdge<string>;
using TVertex = System.String;

namespace AutomataLibrary2D
{
    public class CellularAutomata1_5
    {
        //Inmunidad
        private List<TVertex> CellsInmune = null;                            // Contiene a las celulas inmune

        Random probabilityImmunoreaction = new Random();


        private SmallWorldNetwork _smallWorldNetwork = null;
        private Dictionary<TVertex, CellState> _dictStatesOriginal = null;  // Diccionario que contiene a todos los vertices del grafo y por cada uno se conoce el estado original que le fue asignado
        private Dictionary<TVertex, CellData> _dictStates = null;           // Diccionario que contiene a todos los vertices del grafo y por cada uno se conoce toda la informacion referente a este

        private Dictionary<int, List<TVertex>> _dictTumor = null;           // Contiene todos las celulas tumorales por ID
        private Dictionary<int, List<TVertex>> _dictMicro = null;

        private Dictionary<int, int> _dictRelativeTimesData = null;

        private Dictionary<int, int>[] _dictSuccessfulMicrometastasis = null;
        private Dictionary<int, int>[] _dictFailedMicrometastasis = null;

        private Dictionary<TVertex, int> _tumorFrontiers = null;
        private Dictionary<TVertex, int> _microFrontiers = null;

        private Dictionary<TVertex, bool> _synchronousCellsToUpdate = null;
        private Dictionary<TVertex, int>[] _dictAsyncMig = null;            // El array es solo de tamanno 2 
        private Dictionary<int, TVertex> _dictAsyncCS = null;
        private List<TVertex>[] _dictAsyncTum = null;

        private int _cellInBloodstreamIDGenerator = 0;
        private int _amountCellsInBloodStreamFromTumors = 0;
        private int _amountCellsInBloodStreamFromMigra = 0;
        private int _amountCellsGeneratedMigration = 0;

        private Dictionary<TVertex, int> _dictWanderedDistance = null;
        private Dictionary<int, int> _dictWanderedDistanceMeasurementsMetas = null;
        private Dictionary<int, int> _dictWanderedDistanceMeasurementsDeath = null;

        private Random _random = null;
        private ModelSettings _modelSettings = null;

        private OrganScheme _organ1Scheme = null; //organo primario
        private OrganScheme _organ2Scheme = null; //organo secundario

        private NutrientsSettings _nutrientsSettings = null;
        private ParametersSettings _parametersSettings = null;
        private int _generation = 0;
        private int _tumorIDGenerator = 0;
        private int[] _scaleMax = null;


        public List<KeyValuePair<TVertex, CellState>> DictOriginalStates //Propiedad que guarda las estados originales()
        {
            get
            {
                return _dictStatesOriginal.ToList();
            }
        }
        //Volver al final Propiedades
        public List<KeyValuePair<int, List<KeyValuePair<TVertex, int>>>> DictTumors
        {
            get
            {
                List<KeyValuePair<int, List<KeyValuePair<TVertex, int>>>> result = new List<KeyValuePair<int, List<KeyValuePair<TVertex, int>>>>();
                List<int> tumorIDs = _dictTumor.Keys.ToList();  // Dame los id de las listas de celulas tumorales
                for (int i = 0; i < tumorIDs.Count; i++)
                {
                    List<TVertex> tumorCells = _dictTumor[tumorIDs[i]]; // Dame la lista de c\'elula tumoral con id i
                    List<KeyValuePair<TVertex, int>> ls = new List<KeyValuePair<TVertex, int>>();
                    for (int j = 0; j < tumorCells.Count; j++)
                    {
                        TVertex cell = tumorCells[j];
                        int amount = _dictStates[cell].CantCells;  // cantidad de celulas
                        KeyValuePair<TVertex, int> pair = new KeyValuePair<TVertex, int>(cell, amount);
                        ls.Add(pair);
                    }
                    result.Add(new KeyValuePair<int, List<KeyValuePair<TVertex, int>>>(tumorIDs[i], ls));
                }
                return result;
            }
        }
        public List<KeyValuePair<int, List<KeyValuePair<TVertex, int>>>> DictMicro
        {
            get
            {
                List<KeyValuePair<int, List<KeyValuePair<TVertex, int>>>> result = new List<KeyValuePair<int, List<KeyValuePair<TVertex, int>>>>();
                List<int> microIDs = _dictMicro.Keys.ToList();
                for (int i = 0; i < microIDs.Count; i++)
                {
                    List<TVertex> microCells = _dictMicro[microIDs[i]];
                    List<KeyValuePair<TVertex, int>> ls = new List<KeyValuePair<TVertex, int>>();
                    for (int j = 0; j < microCells.Count; j++)
                    {
                        TVertex cell = microCells[j];
                        int amount = _dictStates[cell].CantCells;
                        KeyValuePair<TVertex, int> pair = new KeyValuePair<TVertex, int>(cell, amount);
                        ls.Add(pair);
                    }
                    result.Add(new KeyValuePair<int, List<KeyValuePair<TVertex, int>>>(microIDs[i], ls));
                }
                return result;
            }
        }
        public List<KeyValuePair<int, List<KeyValuePair<TVertex, int>>>> DictMigra
        {
            get
            {
                Dictionary<int, List<KeyValuePair<TVertex, int>>> migratoryDictionay = new Dictionary<int, List<KeyValuePair<TVertex, int>>>();
                List<TVertex> migratoryCells = _dictAsyncMig[0].Keys.ToList();//Me da las llaves del diccionario de la pos 0
                if (migratoryCells.Count != 0)
                {
                    for (int i = 0; i < migratoryCells.Count; i++)
                    {
                        int migratoryCellOriginalTumor = _dictStates[migratoryCells[i]].CurrentTumor;
                        int amount = _dictStates[migratoryCells[i]].CantCells;

                        KeyValuePair<TVertex, int> pair = new KeyValuePair<TVertex, int>(migratoryCells[i], amount);

                        if (migratoryDictionay.ContainsKey(migratoryCellOriginalTumor))
                            migratoryDictionay[migratoryCellOriginalTumor].Add(pair);
                        else
                        {
                            migratoryDictionay.Add(migratoryCellOriginalTumor, new List<KeyValuePair<TVertex, int>>());
                            migratoryDictionay[migratoryCellOriginalTumor].Add(pair);
                        }
                    }
                }
                else
                {
                    List<int> tumorsID = _dictTumor.Keys.ToList();
                    for (int i = 0; i < tumorsID.Count; i++)
                    {
                        migratoryDictionay.Add(tumorsID[i], new List<KeyValuePair<TVertex, int>>());
                    }
                }
                return migratoryDictionay.ToList();
            }
        }


        //Propiedades de las variables
        public int CellsInBloodstreamFromTumors { get { return _amountCellsInBloodStreamFromTumors; } }
        public int CellsInBloodstreamFromMigration { get { return _amountCellsInBloodStreamFromMigra; } }
        public int MigrationCellsGenerated { get { return _amountCellsGeneratedMigration; } }
        public List<KeyValuePair<int, int>> DictWanderedDistanceMeasurementsMetas { get { return _dictWanderedDistanceMeasurementsMetas.ToList(); } }
        public List<KeyValuePair<int, int>> DictWanderedDistanceMeasurementsDeath { get { return _dictWanderedDistanceMeasurementsDeath.ToList(); } }
        public List<KeyValuePair<int, int>>[] FailedMicrometastasis { get { return new[] { _dictFailedMicrometastasis[0].ToList(), _dictFailedMicrometastasis[1].ToList() }; } }
        public List<KeyValuePair<int, int>>[] SuccessfulMicrometastasis { get { return new[] { _dictSuccessfulMicrometastasis[0].ToList(), _dictSuccessfulMicrometastasis[1].ToList() }; } }

        //Por cada llave dame la cant de elementos que tiene el value <lleva, countcell>
        public Dictionary<int, int> DictExteriorCells(string type)
        {
            Dictionary<int, int> dict = new Dictionary<int, int>();
            //Por cada llave dame la cant de elementos que tiene el value <lleva, countcell>
            switch (type)
            {
                case "[Migra]":
                    List<KeyValuePair<int, List<KeyValuePair<TVertex, int>>>> migra = DictMigra;
                    for (int i = 0; i < migra.Count; i++)
                        dict.Add(migra[i].Key, migra[i].Value.Count); //Por cada llave dame la cant de elementos que tiene el value
                    break;
                case "[Tumors]":
                    List<KeyValuePair<TVertex, int>> tumors = _tumorFrontiers.ToList();
                    for (int i = 0; i < tumors.Count; i++)
                    {
                        int tumorID = tumors[i].Value;
                        if (!dict.ContainsKey(tumorID))
                            dict.Add(tumorID, 1);
                        else dict[tumorID]++;
                    }
                    break;
                case "[Micros]":
                    List<KeyValuePair<TVertex, int>> micro = _microFrontiers.ToList();
                    for (int i = 0; i < micro.Count; i++)
                    {
                        int microID = micro[i].Value;
                        if (!dict.ContainsKey(microID))
                            dict.Add(microID, 1);
                        else dict[microID]++;
                    }
                    break;
                default:
                    throw new Exception("Unexpected string parameter");
            }
            return dict;
        }


        //Constructor
        public CellularAutomata1_5(SmallWorldNetwork network, ModelSettings model, OrganScheme organ1, OrganScheme organ2,
           NutrientsSettings nutrients, ParametersSettings parameters)
        {
            _smallWorldNetwork = network;
            _generation = 0;
            _cellInBloodstreamIDGenerator = 0;
            _amountCellsInBloodStreamFromTumors = 0;
            _amountCellsInBloodStreamFromMigra = 0;
            _amountCellsGeneratedMigration = 0;
            _tumorIDGenerator = 0;
            _random = new Random();
            _modelSettings = model;
            _parametersSettings = parameters;
            _nutrientsSettings = nutrients;
            _organ1Scheme = organ1;
            _organ2Scheme = organ2;
            InitializeDictionaries(); // Modificado Inmunidad
            InitializeGrid();
            InitializeTumor();        // Modificado Inmunidad
            InmuneCells();            // Modificado Inmunidad
        }

        //Modificado
        //Inicializacion de las variables y estructuras
        private void InitializeDictionaries()
        {
            //Inmunidad
            CellsInmune = new List<TVertex>();


            _dictAsyncMig = new Dictionary<TVertex, int>[2];
            _dictAsyncMig[0] = new Dictionary<TVertex, int>();
            _dictAsyncMig[1] = new Dictionary<TVertex, int>();

            _dictAsyncTum = new List<TVertex>[2];
            _dictAsyncTum[0] = new List<TVertex>();
            _dictAsyncTum[1] = new List<TVertex>();

            _dictRelativeTimesData = new Dictionary<int, int>();
            _dictAsyncCS = new Dictionary<int, TVertex>();
            _dictStates = new Dictionary<TVertex, CellData>();
            _dictStatesOriginal = new Dictionary<TVertex, CellState>();
            _dictMicro = new Dictionary<int, List<TVertex>>();
            _dictTumor = new Dictionary<int, List<TVertex>>();

            _dictWanderedDistance = new Dictionary<string, int>();                // Distancia recorrida
            _dictWanderedDistanceMeasurementsMetas = new Dictionary<int, int>();
            _dictWanderedDistanceMeasurementsDeath = new Dictionary<int, int>();

            for (int i = 0; i <= _parametersSettings.mu_max; i++) //mu_max:Distancia máxima de migración
            {
                _dictWanderedDistanceMeasurementsMetas.Add(i, 0);
                _dictWanderedDistanceMeasurementsDeath.Add(i, 0);
            }

            _dictFailedMicrometastasis = new Dictionary<int, int>[2];
            _dictSuccessfulMicrometastasis = new Dictionary<int, int>[2];
            for (int i = 0; i < 2; i++)
            {
                _dictFailedMicrometastasis[i] = new Dictionary<int, int>();
                _dictFailedMicrometastasis[i].Add(-1, 0);
                _dictSuccessfulMicrometastasis[i] = new Dictionary<int, int>();
                _dictSuccessfulMicrometastasis[i].Add(-1, 0);
            }
            List<TVertex> vertices = _smallWorldNetwork.Vertices;
            //Agregar Inmunidad
            int verticesCount = vertices.Count;
            for (int i = 0; i < verticesCount; i++)
            {
                _dictStates.Add(vertices[i], new CellData(false, CellState.NULL, CellState.NULL, -1, -1, -1, -1));
                _dictStatesOriginal.Add(vertices[i], CellState.NULL);
            }

            _tumorFrontiers = new Dictionary<TVertex, int>();
            _microFrontiers = new Dictionary<TVertex, int>();

            _scaleMax = new int[_parametersSettings.SimScale];
            for (int i = 0; i < _parametersSettings.SimScale; i++)
            {
                _scaleMax[i] = i + 1;
            }
        }
        private void InitializeGrid()             // LLama a inicializar los tipos de sheme en dependecia del sheme de los organ sheme
        {
            switch (_organ1Scheme.SelectedScheme)
            {
                case SelectedScheme.Scheme1:
                    InitializeScheme1(0, 0, _smallWorldNetwork.NetworkDivision, _smallWorldNetwork.NetworkSizeY, 0);
                    break;
                case SelectedScheme.Scheme2:
                    InitializeScheme2(0, 0, _smallWorldNetwork.NetworkDivision, _smallWorldNetwork.NetworkSizeY, 0);
                    break;
                case SelectedScheme.Scheme3:
                    InitializeScheme3(0, 0, _smallWorldNetwork.NetworkDivision, _smallWorldNetwork.NetworkSizeY, 0);
                    break;
            }
            switch (_organ2Scheme.SelectedScheme)
            {
                case SelectedScheme.Scheme1:
                    InitializeScheme1(_smallWorldNetwork.NetworkDivision, 0, _smallWorldNetwork.NetworkSizeX, _smallWorldNetwork.NetworkSizeY, 1);
                    break;
                case SelectedScheme.Scheme2:
                    InitializeScheme2(_smallWorldNetwork.NetworkDivision, 0, _smallWorldNetwork.NetworkSizeX, _smallWorldNetwork.NetworkSizeY, 1);
                    break;
                case SelectedScheme.Scheme3:
                    InitializeScheme3(_smallWorldNetwork.NetworkDivision, 0, _smallWorldNetwork.NetworkSizeX, _smallWorldNetwork.NetworkSizeY, 1);
                    break;
            }
        }

        //Inicializa todos las celulas(vertices) que conformaran al organo en dependencia de si su estructura es del tipo scheme1
        private void InitializeScheme1(int x0, int y0, int xf, int yf, int organ)
        {
            OrganScheme1 current = null;
            if (organ == 0)
                current = (OrganScheme1)_organ1Scheme;
            else if (organ == 1)
                current = (OrganScheme1)_organ2Scheme;
            else throw new Exception("Invalid organ identifier.");

            CellState state = CellState.NULL;
            for (int i = y0; i < yf; i++)
            {
                if (0 <= i && i < current.Lumen)
                    state = CellState.Lumen;
                else if (current.Lumen <= i && i < current.Lumen + current.Epithelium)
                    state = CellState.Epith;
                else state = CellState.Strom;

                for (int j = x0; j < xf; j++)
                {
                    TVertex vertex = MF.BuildTVertexID(j, i);
                    _dictStates[vertex].CurrentState = state;
                    _dictStates[vertex].Organ = organ;
                    _dictStatesOriginal[vertex] = state;
                }
            }
        }

        //Inicializa todos las celulas(vertices) que conformaran al organo en dependencia de si su estructura es del tipo scheme2
        private void InitializeScheme2(int x0, int y0, int xf, int yf, int organ)
        {
            OrganScheme2 current = null;
            if (organ == 0)
                current = (OrganScheme2)_organ1Scheme;
            else if (organ == 1)
                current = (OrganScheme2)_organ2Scheme;
            else throw new Exception("Invalid organ identifier.");

            CellState state = CellState.Lumen;
            for (int i = 0; i < yf / 2 + 1; i++)
            {
                if (current.CentralDuct + i < current.CentralDuct + current.CentralDuctRadius)
                    state = CellState.Lumen;
                else if (current.CentralDuct + i >= current.CentralDuct + current.CentralDuctRadius &&
                    current.CentralDuct + i < current.CentralDuct + current.CentralDuctRadius + current.Epithelium)
                    state = CellState.Epith;
                else state = CellState.Strom;

                for (int j = x0; j < xf; j++)
                {
                    if (i == 249) //Revisa si es normal q esto este asi, es decir vacio
                    {

                    }
                    if (current.CentralDuct + i < xf)
                    {
                        TVertex vertex = MF.BuildTVertexID(j, current.CentralDuct + i);
                        _dictStates[vertex].CurrentState = state;
                        _dictStates[vertex].Organ = organ;
                        _dictStatesOriginal[vertex] = state;
                    }
                    if (current.CentralDuct - i >= 0)
                    {
                        TVertex vertex = MF.BuildTVertexID(j, current.CentralDuct - i);
                        _dictStates[vertex].CurrentState = state;
                        _dictStates[vertex].Organ = organ;
                        _dictStatesOriginal[vertex] = state;
                    }
                }
            }
        }

        //Inicializa todos las celulas(vertices) que conformaran al organo en dependencia de si su estructura es del tipo scheme3
        //las celulas solo se encuntran en el estroma
        private void InitializeScheme3(int x0, int y0, int xf, int yf, int organ)
        {
            CellState state = CellState.Strom;
            for (int i = y0; i < yf; i++)
            {
                for (int j = x0; j < xf; j++)
                {
                    TVertex vertex = MF.BuildTVertexID(j, i);
                    _dictStates[vertex].CurrentState = state;
                    _dictStates[vertex].Organ = organ;
                    _dictStatesOriginal[vertex] = state;
                }
            }
        }

        // Modificar
        private void InitializeTumor()
        {
            List<TVertex> tumorTemplate = MF.GetRegularNeighboursTemplate(_organ1Scheme.TumorRadius);
            List<TVertex> clusterTumorCells = new List<TVertex>();

            //Recorre todas los vecinos de TumorPos y los agrega a clusterTumorCells
            for (int i = 0; i < tumorTemplate.Count; i++)
            {
                int[] templatePos = MF.GetTVertexID(tumorTemplate[i]);   //direccion de los vecinos en el array
                TVertex tumorCell = MF.BuildTVertexID(templatePos[0] + _organ1Scheme.TumorPosX, templatePos[1] + _organ1Scheme.TumorPosY);
                clusterTumorCells.Add(tumorCell);
            }
            _dictTumor.Add(_tumorIDGenerator, new List<TVertex>());
            _dictRelativeTimesData.Add(_tumorIDGenerator, 0);

            for (int i = 0; i < clusterTumorCells.Count; i++)
            {
                // Actualiza la informacion sobre las celulas
                _dictStates[clusterTumorCells[i]].CurrentState = CellState.Tumor;
                _dictStates[clusterTumorCells[i]].CurrentTumor = _tumorIDGenerator;
                _dictStates[clusterTumorCells[i]].CantCells = GetRandomAmountCells(); //no entiendo 

                _dictTumor[_tumorIDGenerator].Add(clusterTumorCells[i]);
                List<TVertex> neigh = GetN(clusterTumorCells[i]);

                List<TVertex> dneigh = GetDN(clusterTumorCells[i], neigh);
                if (dneigh.Count > 0 && !_dictAsyncTum[0].Contains(clusterTumorCells[i]))
                    _dictAsyncTum[0].Add(clusterTumorCells[i]);
                _tumorFrontiers.Add(clusterTumorCells[i], _tumorIDGenerator);
            }
            FilterFrontierCells();
            _tumorIDGenerator++;
        }

        //Trabaja con el diccionaro de fronteras
        private void FilterFrontierCells()
        {
            List<TVertex> toremove = new List<TVertex>();
            List<TVertex> frontiersCells = _tumorFrontiers.Keys.ToList();
            for (int i = 0; i < frontiersCells.Count; i++)
            {
                List<TVertex> n = GetN(frontiersCells[i]);
                List<TVertex> nn = GetNN(frontiersCells[i], n);
                List<TVertex> nnfree = GetNNE(frontiersCells[i], nn, new List<CellState> { CellState.Lumen, CellState.Epith, CellState.Strom, CellState.Migra });
                if (nnfree.Count == 0)
                    toremove.Add(frontiersCells[i]);
            }
            for (int i = 0; i < toremove.Count; i++)
                _tumorFrontiers.Remove(toremove[i]); //Solo se quedan las celulsa que tengan vecinos tumorales o de micro
            for (int i = 0; i < toremove.Count; i++)
                _dictStates[toremove[i]].CantCells = _scaleMax[_scaleMax.Length - 1];

            toremove = new List<TVertex>();
            frontiersCells = _microFrontiers.Keys.ToList(); //fronteras de la micrometastasis
            for (int i = 0; i < frontiersCells.Count; i++)
            {
                List<TVertex> n = GetN(frontiersCells[i]);
                List<TVertex> nn = GetNN(frontiersCells[i], n);
                List<TVertex> nnfree = GetNNE(frontiersCells[i], nn, new List<CellState> { CellState.Lumen, CellState.Epith, CellState.Strom, CellState.Migra });
                if (nnfree.Count == 0)
                    toremove.Add(frontiersCells[i]);
            }
            for (int i = 0; i < toremove.Count; i++)
                _microFrontiers.Remove(toremove[i]);
            for (int i = 0; i < toremove.Count; i++)
                _dictStates[toremove[i]].CantCells = _scaleMax[_scaleMax.Length - 1];
        }

        //Obtiene todos los vertices vecinos de focalvertex
        private List<TVertex> GetN(TVertex focalVertex)
        {
            List<TVertex> neighbours = new List<TVertex>();
            List<TEdge> adjacentedges = _smallWorldNetwork.AdjacentEdges(focalVertex);  //Contiene las aristas adyacentes a focalVertex
            for (int i = 0; i < adjacentedges.Count; i++)
                neighbours.Add((adjacentedges[i].Target == focalVertex) ? adjacentedges[i].Source : adjacentedges[i].Target);
            if (CellsInmune.Contains(neighbours[neighbours.Count - 1])) neighbours.RemoveAt(neighbours.Count - 1);
            return neighbours;
        }

        //Te devuelve los vertice de la lista recibida que estan fuera del radio
        //Te devulve los vecinos lejanos
        private List<TVertex> GetDN(TVertex focalVertex, List<TVertex> neighbours)
        {
            List<TVertex> distantNeighbours = new List<TVertex>();

            for (int i = 0; i < neighbours.Count; i++)
                if (MF.EuclideanDistance(focalVertex, neighbours[i]) > _smallWorldNetwork.NeighbourhoodRadius)
                    distantNeighbours.Add(neighbours[i]);
            return distantNeighbours;
        }

        //Te devuelve los vertice de la lista recibida que pertecen a la vecindad de tamanno radio
        //Te devuelve los vecinos cercanos
        private List<TVertex> GetNN(TVertex focalVertex, List<TVertex> neighbours)
        {
            List<TVertex> nearNeighbours = new List<TVertex>();
            for (int i = 0; i < neighbours.Count; i++)
                if (MF.EuclideanDistance(focalVertex, neighbours[i]) <= _smallWorldNetwork.NeighbourhoodRadius)
                    nearNeighbours.Add(neighbours[i]);
            return nearNeighbours;
        }


        //Dado un vertice etorna los vertices cercanos a el que pertenecen a su mismo organo y que su estado actual pertenezca a la lista de estados celulares recibido
        private List<TVertex> GetNNE(TVertex focalVertex, List<TVertex> nearNeighbours, List<CellState> E)
        {
            int[] vertexpos = MF.GetTVertexID(focalVertex);
            int focalVertexOrgan = _dictStates[focalVertex].Organ;

            List<TVertex> filteredNeighbours = new List<TVertex>();

            for (int i = 0; i < nearNeighbours.Count; i++)
            {
                int neighbourOrgan = _dictStates[nearNeighbours[i]].Organ;
                if (focalVertexOrgan == neighbourOrgan && E.Contains(_dictStates[nearNeighbours[i]].CurrentState))
                    filteredNeighbours.Add(nearNeighbours[i]);
            }
            return filteredNeighbours;
        }

        //Dado un vertice y una lista de vecinos distantes devulve una lista con los vertices vecinos distante cuyo estado actual pertenece a la lista de estados celulares recibida
        private List<TVertex> GetDNE(TVertex focalVertex, List<TVertex> distantNeighbours, List<CellState> E)
        {
            int[] vertexpos = MF.GetTVertexID(focalVertex);
            List<TVertex> filteredNeighbours = new List<TVertex>();
            for (int i = 0; i < distantNeighbours.Count; i++)
                if (E.Contains(_dictStates[distantNeighbours[i]].CurrentState))
                    filteredNeighbours.Add(distantNeighbours[i]);
            return filteredNeighbours;
        }

        // Dado una lista de  vecinos se devuelve un diccionario de los vecinos que son celulas tumorales y el currentTumor de estos como llave los no tumorales tienen current -1
        private Dictionary<int, List<TVertex>> GetCompitingTumorsIDAndCells(List<TVertex> nearNeighbours)
        {
            Dictionary<int, List<TVertex>> tumorIDsAndCells = new Dictionary<int, List<TVertex>>();
            for (int i = 0; i < nearNeighbours.Count; i++)
            {
                if (!tumorIDsAndCells.ContainsKey(_dictStates[nearNeighbours[i]].CurrentTumor))
                {
                    if (_dictStates[nearNeighbours[i]].CurrentTumor != -1)//Si el estado actual es una celula tumoral
                        tumorIDsAndCells.Add(_dictStates[nearNeighbours[i]].CurrentTumor, new List<TVertex>() { nearNeighbours[i] });
                }
                else tumorIDsAndCells[_dictStates[nearNeighbours[i]].CurrentTumor].Add(nearNeighbours[i]);
            }
            return tumorIDsAndCells;
        }


        //Probabilidad de crecimiento tumoral en avascular
        //junto a la de abajo forman la funcion de transicion de crecimiento tumoral
        private double GetGrowthProbAvascular(double n)
        {
            double num = _modelSettings.P0a * _modelSettings.Ka * _modelSettings.ra * Math.Pow(Math.E, _modelSettings.ra * n * _modelSettings.deltata) * (_modelSettings.Ka - _modelSettings.P0a);
            double den = Math.Pow(((_modelSettings.P0a * Math.Pow(Math.E, _modelSettings.ra * n * _modelSettings.deltata)) - _modelSettings.P0a + _modelSettings.Ka), 2);
            double result = num / den;
            return result;
        }

        //Probabilidad de crecimiento tumoral en vascular
        private double GetGrowthProbVascular(double n)
        {
            double num = (_modelSettings.P0v * _modelSettings.Kv * _modelSettings.rv) * (Math.Pow(Math.E, _modelSettings.rv * n * _modelSettings.deltatv)) * (_modelSettings.Kv - _modelSettings.P0v);
            double den = Math.Pow(((_modelSettings.P0v * Math.Pow(Math.E, _modelSettings.rv * n * _modelSettings.deltatv)) - _modelSettings.P0v + _modelSettings.Kv), 2);
            double result = num / den;
            return result;
        }

        //probabilidad de aparici´on de c´elulas migratorias
        private double GetMigrantCellApparitionProb(int relativetime)
        {
            double estimatedPob = (_modelSettings.P0v * _modelSettings.Kv) / (_modelSettings.P0v + (_modelSettings.Kv - _modelSettings.P0v) * Math.Pow(Math.E, -1 * _modelSettings.rv * relativetime * _modelSettings.deltatv));
            double inner = estimatedPob / (_modelSettings.Kv + _parametersSettings.K_mig);
            double power = 1.0 / _parametersSettings.eta_mig;
            return Math.Pow(inner, power);
        }

        //Devuelve un numero random menor que la escala max de la red 
        private int GetRandomAmountCells()
        {
            int random = _random.Next(_scaleMax.Length);
            return _scaleMax[random];
        }

        // probabilidad de muerte celular migratoria (pag67)
        private double GetMigrantDeathProbability(int movements)
        {
            return Math.Pow(movements / (_parametersSettings.mu_max), 1.0 / (_parametersSettings.eta_mig_prima));
        }

        //Devuelve un vertice random pertenecinete a la lista recibida 
        private TVertex GetMetastasisDestiny(List<TVertex> distantFilteredNeighbours)
        {
            int random = _random.Next(distantFilteredNeighbours.Count);
            return distantFilteredNeighbours[random];
        }

        //Te da la lista de vecinos cercanos o inmediatos de migrantcell que pueden moverse
        private List<TVertex> GetAvailableDestinies(TVertex migrantCell, TVertex tumorCentroid, List<TVertex> nearNeighbours2)
        {
            List<TVertex> possibleMoves = new List<TVertex>();
            for (int i = 0; i < nearNeighbours2.Count; i++)
            {
                double distanceCellTumorCentroid = MF.EuclideanDistance(migrantCell, tumorCentroid);
                double distanceNeighbourCentroid = MF.EuclideanDistance(nearNeighbours2[i], tumorCentroid);
                if (distanceNeighbourCentroid > distanceCellTumorCentroid)  //si es menor no pueden moverse ya que estan dentro
                    possibleMoves.Add(nearNeighbours2[i]);
            }
            return possibleMoves;
        }

        //pag 56 Calcula el centroide del tumor con id
        private int[] GetTumorCentroid(int ID, bool tumor)
        {
            int[] centroid = new int[2];
            List<TVertex> cells = null;

            if (tumor) cells = _dictTumor[ID];
            else cells = _dictMicro[ID];

            int count = cells.Count;
            for (int i = 0; i < count; i++)
            {
                int[] pos = MF.GetTVertexID(cells[i]);
                centroid[0] += pos[0];
                centroid[1] += pos[1];
            }
            centroid[0] = (int)Math.Round(centroid[0] / (double)count);
            centroid[1] = (int)Math.Round(centroid[1] / (double)count);
            return centroid;
        }

        //Devuelve la region de nutriente que contiene al vertice cell
        private List<int[]> GetRegionNutrients(TVertex cell)
        {
            int[] cellpos = MF.GetTVertexID(cell);
            for (int i = 0; i < _nutrientsSettings.Regions.Count; i++)
            {
                int[] regionLimits = _nutrientsSettings.Regions[i];
                if ((regionLimits[0] <= cellpos[0] && cellpos[0] < regionLimits[1]) &&
                    (regionLimits[2] <= cellpos[1] && cellpos[1] < regionLimits[3]))
                    return _nutrientsSettings.Vectors[i];
            }
            throw new Exception("Vertex not contained in any region.");
        }

        //Obtiene el centroide de todos los id tumores
        private Dictionary<int, int[]> GetTumorCentroidsDictionaries(bool tumor)
        {
            Dictionary<int, int[]> result = new Dictionary<int, int[]>();
            Dictionary<int, List<TVertex>> collection = _dictTumor;
            if (tumor == false) collection = _dictMicro;
            List<KeyValuePair<int, List<TVertex>>> pairs = collection.ToList();
            for (int i = 0; i < pairs.Count; i++)
            {
                result.Add(pairs[i].Key, null);
                int[] centroid = GetTumorCentroid(pairs[i].Key, tumor);
                result[pairs[i].Key] = centroid;
            }
            return result;
        }

        //velocidad de expansi´on tumoral
        private double GetVelocity(double euclideanDistance)
        {
            if (euclideanDistance == Math.Sqrt(2))
                return 0.5;
            else return 1.5;
        }

        // similitud coseno alternativa (pag 55)
        private double GetSimAlt(double sim)
        {
            // i = 0.5, s = 1.5
            return (1 / 2) * sim + (1);
        }

        //Procedemiento de Actualizacion de todas las celulas
        public void UpdateProcedure()
        {
            Console.WriteLine("   cellularautomata library: updating migratory cells in bloodstream...");
            UpdateMigratoryCellsInBloodstream();

            Console.WriteLine("   cellularautomata library: updating migratory cells...");
            UpdateMigratoryCells();

            Console.WriteLine("   cellularautomata library: updating tumor migratory cells...");
            UpdateTumorMigratoryCells();

            Console.WriteLine("   cellularautomata library: checking micrometastasis survival...");
            CheckMicrometastasisSurvival(); //Revisar

            Console.WriteLine("   cellularautomata library: checking micrometastasis colonization...");
            CheckMicrometastasisColonization(); //Revisar

            //Revisar estos metodos nuevamente
            Console.WriteLine("   cellularautomata library: updating synchronous cells...");
            SetSynchronousUpdateList();
            UpdateSynchronousCellsOptimized();

            Console.WriteLine("   cellularautomata library: setting up next iteration...");
            SetupIteration();
        }

        //Cambia el estado actual de la celula a su estado futuro
        private void SetupIteration()
        {
            _generation++;
            List<TVertex> statesKeys = _dictStates.Keys.ToList();
            int keysCount = statesKeys.Count;
            for (int i = 0; i < keysCount; i++)
            {
                List<TVertex> neighbours = GetN(statesKeys[i]);
                _dictStates[statesKeys[i]].Updated = false;
                if (_dictStates[statesKeys[i]].FutureState == CellState.Tumor)
                {
                    // update future and current info
                    _dictStates[statesKeys[i]].CurrentState = CellState.Tumor;
                    _dictStates[statesKeys[i]].FutureState = CellState.NULL;
                    int tumorID = _dictStates[statesKeys[i]].FutureTumor;
                    _dictStates[statesKeys[i]].FutureTumor = -1;
                    _dictStates[statesKeys[i]].CurrentTumor = tumorID;
                    _dictStates[statesKeys[i]].CantCells = GetRandomAmountCells();
                    _dictTumor[tumorID].Add(statesKeys[i]);
                    // update tumor async set

                    List<TVertex> distantNeighbours = GetDN(statesKeys[i], neighbours);
                    if (distantNeighbours.Count > 0 && !_dictAsyncTum[0].Contains(statesKeys[i]))
                        _dictAsyncTum[0].Add(statesKeys[i]);
                    // update frontiers
                    _tumorFrontiers.Add(statesKeys[i], tumorID);

                }
                else if (_dictStates[statesKeys[i]].FutureState == CellState.Micro)
                {
                    _dictStates[statesKeys[i]].CurrentState = CellState.Micro;
                    _dictStates[statesKeys[i]].FutureState = CellState.NULL;
                    int microID = _dictStates[statesKeys[i]].FutureTumor;
                    _dictStates[statesKeys[i]].FutureTumor = -1;
                    _dictStates[statesKeys[i]].CurrentTumor = microID;
                    _dictStates[statesKeys[i]].CantCells = GetRandomAmountCells();
                    _dictMicro[microID].Add(statesKeys[i]);
                    // update frontiers
                    _microFrontiers.Add(statesKeys[i], microID);

                }
                else if (_dictStates[statesKeys[i]].FutureState == CellState.Migra)
                {
                    _dictStates[statesKeys[i]].CurrentState = CellState.Migra;
                    _dictStates[statesKeys[i]].FutureState = CellState.NULL;
                    var tumorID = _dictStates[statesKeys[i]].FutureTumor;
                    _dictStates[statesKeys[i]].FutureTumor = -1;
                    _dictStates[statesKeys[i]].CurrentTumor = tumorID;
                    _dictStates[statesKeys[i]].CantCells = GetRandomAmountCells();
                    _dictAsyncMig[0].Add(statesKeys[i], 0);

                }
            }

            FilterFrontierCells();
            List<TVertex> keys = _dictAsyncMig[1].Keys.ToList();
            int count = keys.Count;
            for (int i = 0; i < count; i++)
                _dictAsyncMig[0].Add(keys[i], _dictAsyncMig[1][keys[i]]);
            _dictAsyncMig[1].Clear();
            for (int i = 0; i < _dictAsyncTum[1].Count; i++)
                _dictAsyncTum[0].Add(_dictAsyncTum[1][i]);
            _dictAsyncTum[1].Clear();
        }

        //Modificado Inmune
        //Quita a los vertices que logran la colonizacion y pasan a ser estos partes del turmor y a pertenecer a las fronteras del tumor
        private void CheckMicrometastasisColonization()
        {
            List<int> micrometastasisToUpdate = new List<int>();
            List<int> micrometastasisIDs = _dictMicro.Keys.ToList();
            // int count = micrometastasisIDs.Count;

            _dictSuccessfulMicrometastasis[0].Add(_generation, _dictSuccessfulMicrometastasis[0][_generation - 1]);
            _dictSuccessfulMicrometastasis[1].Add(_generation, _dictSuccessfulMicrometastasis[1][_generation - 1]);

            for (int i = 0; i < micrometastasisIDs.Count; i++)
            {
                double prob = _random.NextDouble();
                int spawntime = _dictRelativeTimesData[micrometastasisIDs[i]]; //tiempo en que se convirtio en micrometastasis
                TVertex cell = _dictMicro[micrometastasisIDs[i]][0];
                int destinyOrgan = _dictStates[cell].Organ;

                // Probabilidad de supervivencia de una micrometástasis.
                double psi = (destinyOrgan == 0) ? _parametersSettings.psi_mic0 : _parametersSettings.psi_mic1;
                //Modificado
                List<TVertex> n = GetN(cell);
                //bool warm = Warm(cell, n, false);
                //if (!warm && _generation - spawntime >= _modelSettings.n_a && prob <= psi)
                if (_generation - spawntime >= _modelSettings.n_a && prob <= psi)
                {
                    // satisfactory colonization
                    _dictTumor.Add(micrometastasisIDs[i], new List<TVertex>());
                    List<TVertex> cellsInMicrometastasis = _dictMicro[micrometastasisIDs[i]];
                    for (int j = 0; j < cellsInMicrometastasis.Count; j++)
                    {
                        _dictStates[cellsInMicrometastasis[j]].CurrentState = CellState.Tumor;
                        _dictTumor[micrometastasisIDs[i]].Add(cellsInMicrometastasis[j]);
                        _tumorFrontiers.Add(cellsInMicrometastasis[j], micrometastasisIDs[i]);
                        _microFrontiers.Remove(cellsInMicrometastasis[j]);
                    }
                    micrometastasisToUpdate.Add(micrometastasisIDs[i]);
                    _dictSuccessfulMicrometastasis[destinyOrgan][_generation]++;
                }

            }
            for (int i = 0; i < micrometastasisToUpdate.Count; i++)
                _dictMicro.Remove(micrometastasisToUpdate[i]);

        }

        //Revisar si el metodo es igual al antiguo por si borre algo
        //Modificado Inmune
        private void SetSynchronousUpdateList()
        {
            _synchronousCellsToUpdate = new Dictionary<TVertex, bool>();
            List<TVertex> frontiersCells = _tumorFrontiers.Keys.ToList(); // Dame las celulas tumorales que estan en la frontera
            for (int j = 0; j < frontiersCells.Count; j++)
            {
                TVertex cell = frontiersCells[j];
                List<TVertex> neighbours = GetN(cell);                   //obtiene los vertices vecinos de cell
                List<TVertex> nearNeighbours = GetNN(cell, neighbours);  //Te devuelve los vecinos cercanos
                List<TVertex> normalNearNeighbours = GetNNE(cell, nearNeighbours, new List<CellState> { CellState.Epith, CellState.Lumen, CellState.Strom });

                if (normalNearNeighbours.Count > 0)
                {
                    for (int k = 0; k < normalNearNeighbours.Count; k++)
                    {
                        TVertex normalCellKey = normalNearNeighbours[k];
                        if (!_synchronousCellsToUpdate.ContainsKey(normalCellKey))
                            _synchronousCellsToUpdate.Add(normalCellKey, true);
                    }
                }
            }
            frontiersCells = _microFrontiers.Keys.ToList();

            for (int j = 0; j < frontiersCells.Count; j++)
            {
                TVertex cell = frontiersCells[j];
                List<TVertex> neighbours = GetN(cell);
                List<TVertex> nearNeighbours = GetNN(cell, neighbours);
                List<TVertex> normalNearNeighbours = GetNNE(cell, nearNeighbours, new List<CellState> { CellState.Epith, CellState.Lumen, CellState.Strom });
                if (normalNearNeighbours.Count > 0)
                {
                    for (int k = 0; k < normalNearNeighbours.Count; k++)
                    {
                        TVertex normalCellKey = normalNearNeighbours[k];
                        if (!_synchronousCellsToUpdate.ContainsKey(normalCellKey))
                            _synchronousCellsToUpdate.Add(normalCellKey, false);
                    }
                }
            }

        }

        //Modificado Inmune
        private void UpdateSynchronousCellsOptimized()
        {
            List<KeyValuePair<TVertex, bool>> cellsToUpdatePairs = _synchronousCellsToUpdate.ToList();
            Dictionary<int, int[]> tumorCentroidsDict = GetTumorCentroidsDictionaries(true);
            Dictionary<int, int[]> microCentroidsDict = GetTumorCentroidsDictionaries(false);
            int cellsCount = cellsToUpdatePairs.Count;
            _amountCellsGeneratedMigration = 0;
            for (int i = 0; i < cellsCount; i++)
            {
                KeyValuePair<TVertex, bool> pair = cellsToUpdatePairs[i];
                TVertex cellKey = pair.Key;
                bool cellValue = pair.Value;
                CellData data = _dictStates[cellKey];
                if (_dictStates[cellKey].Updated == true)
                    throw new Exception("Updated cell made it to the synchronous update list.");
                _dictStates[cellKey].Updated = true;
                List<TVertex> neighbours = GetN(cellKey);
                List<TVertex> nearNeighbours = GetNN(cellKey, neighbours);
                List<TVertex> nearNeighbours3 = GetNNE(cellKey, nearNeighbours, new List<CellState> { CellState.Tumor });


                if (nearNeighbours3.Count > 0)
                {
                    // tumor growth
                    Dictionary<int, List<TVertex>> tumorCompitingIDsAndCells = GetCompitingTumorsIDAndCells(nearNeighbours3);
                    List<int> tumorCompitingIDs = tumorCompitingIDsAndCells.Keys.ToList();
                    List<int[]> nutrientsVectorsRegion = GetRegionNutrients(cellKey);
                    List<double> individualTumoralCellApparitionProbs = new List<double>();
                    // all expanding tumors growth probabilities
                    for (int j = 0; j < tumorCompitingIDs.Count; j++)
                    {
                        // get beta
                        int[] tumorCentroid = tumorCentroidsDict[tumorCompitingIDs[j]];
                        int[] cellPos = MF.GetTVertexID(cellKey);
                        int[] expansionVector = MF.BuildVector(cellPos, tumorCentroid);
                        List<double> simValues = new List<double>();
                        if (nutrientsVectorsRegion.Count != 0)
                        {
                            for (int k = 0; k < nutrientsVectorsRegion.Count; k++)
                            {
                                double sim = MF.GetSim(expansionVector, nutrientsVectorsRegion[k]);
                                double simAlt = GetSimAlt(sim);
                                simValues.Add(simAlt);
                            }
                        }
                        else simValues.Add(1);
                        int maxSimIndex = MF.GetMaxValueIndex(simValues);
                        double beta = simValues[maxSimIndex];
                        // get velocity
                        List<TVertex> neighbouringCells = tumorCompitingIDsAndCells[tumorCompitingIDs[j]];
                        double velocity = GetVelocity(MF.EuclideanDistance(neighbouringCells[0], cellKey));
                        for (int k = 1; k < neighbouringCells.Count; k++)
                        {
                            double newVelocity = GetVelocity(MF.EuclideanDistance(neighbouringCells[k], cellKey));
                            if (newVelocity > velocity)
                            {
                                velocity = newVelocity;
                            }
                        }
                        // get full probability
                        int spawntime = _dictRelativeTimesData[tumorCompitingIDs[j]];
                        bool mode = true;
                        if (_generation - spawntime > _modelSettings.n_a)
                            mode = false;
                        if (mode)
                        {
                            CellState healthyCellState = _dictStates[cellKey].CurrentState;
                            if (healthyCellState == CellState.Strom)
                                individualTumoralCellApparitionProbs.Add(0);
                            else
                            {
                                double avascularProb = GetGrowthProbAvascular(_generation - spawntime);
                                double prob = avascularProb * beta * velocity;
                                individualTumoralCellApparitionProbs.Add(prob);
                            }
                        }
                        else
                        {
                            double vascularProb = GetGrowthProbVascular(_generation - (spawntime + _modelSettings.n_a));
                            double prob = vascularProb * beta * velocity;
                            individualTumoralCellApparitionProbs.Add(prob);
                        }
                    }
                    int maxProbIndexGrowth = MF.GetMaxValueIndex(individualTumoralCellApparitionProbs);
                    int expandingTumor = tumorCompitingIDs[maxProbIndexGrowth];
                    double rho3 = individualTumoralCellApparitionProbs[maxProbIndexGrowth];
                    if (_dictStates[cellKey].CurrentState == CellState.Strom)
                    {
                        // checking migrant cell apparition probability
                        List<double> migrantApparitionProbs = new List<double>();
                        for (int j = 0; j < tumorCompitingIDs.Count; j++)
                        {
                            List<TVertex> tumorCurrentCells = _dictTumor[tumorCompitingIDs[j]];
                            int spawntime = _dictRelativeTimesData[tumorCompitingIDs[j]];
                            bool mode = true;
                            if (_generation - spawntime > _modelSettings.n_a)
                                mode = false;
                            if (mode)
                                migrantApparitionProbs.Add(0);
                            else
                            {
                                double poblation = _modelSettings.Kv;
                                if (tumorCurrentCells.Count < poblation)
                                    poblation = tumorCurrentCells.Count;
                                double prob = GetMigrantCellApparitionProb(_generation - spawntime);
                                migrantApparitionProbs.Add(prob);
                            }
                        }
                        int maxProbIndexApparition = MF.GetMaxValueIndex(migrantApparitionProbs);
                        int tumorSpawningMigrantCell = tumorCompitingIDs[maxProbIndexApparition];
                        double rho4 = migrantApparitionProbs[maxProbIndexApparition];
                        double x3 = _random.NextDouble();
                        // deciding if the tumor grows or throw a new migrant cell
                        if (x3 <= rho3)
                        {
                            _dictStates[cellKey].FutureState = CellState.Tumor;
                            _dictStates[cellKey].FutureTumor = expandingTumor;
                        }
                        else
                        {
                            double x4 = _random.NextDouble();
                            if (x4 <= rho4)
                            {
                                _dictStates[cellKey].FutureState = CellState.Migra;
                                _dictStates[cellKey].FutureTumor = tumorSpawningMigrantCell;
                                _amountCellsGeneratedMigration++;
                                _dictWanderedDistance.Add(cellKey, 0);
                            }
                        }
                    }
                    else
                    {
                        // applying tumor growth rule, updating states
                        double Xtumor = _random.NextDouble();
                        if (Xtumor <= rho3)
                        {
                            _dictStates[cellKey].FutureState = CellState.Tumor;
                            _dictStates[cellKey].FutureTumor = expandingTumor;
                        }
                    }
                }
                else
                {
                    List<TVertex> nearNeighbours5 = GetNNE(cellKey, nearNeighbours, new List<CellState> { CellState.Micro });
                    if (nearNeighbours5.Count > 0)
                    {
                        // micrometastasis growth
                        Dictionary<int, List<TVertex>> microCompitingIDsAndCells = GetCompitingTumorsIDAndCells(nearNeighbours5);
                        List<int> microCompitingIDs = microCompitingIDsAndCells.Keys.ToList();
                        List<int[]> nutrientsVectorsRegion5 = GetRegionNutrients(cellKey);
                        List<double> individualMicroCellApparitionProbs = new List<double>();
                        for (int j = 0; j < microCompitingIDs.Count; j++)
                        {
                            // get beta
                            int[] microCentroid = microCentroidsDict[microCompitingIDs[j]];
                            int[] cellPos = MF.GetTVertexID(cellKey);
                            int[] expansionVector = MF.BuildVector(cellPos, microCentroid);
                            List<double> simValues = new List<double>();
                            if (nutrientsVectorsRegion5.Count != 0)
                            {
                                for (int k = 0; k < nutrientsVectorsRegion5.Count; k++)
                                {
                                    double sim = MF.GetSim(expansionVector, nutrientsVectorsRegion5[k]);
                                    double simAlt = GetSimAlt(sim);
                                    simValues.Add(simAlt);
                                }
                            }
                            else simValues.Add(1);
                            int maxSimIndex = MF.GetMaxValueIndex(simValues);
                            double beta = simValues[maxSimIndex];
                            //get velocity
                            List<TVertex> neighbouringCells = microCompitingIDsAndCells[microCompitingIDs[j]];
                            double velocity = GetVelocity(MF.EuclideanDistance(neighbouringCells[0], cellKey));
                            for (int k = 1; k < neighbouringCells.Count; k++)
                            {
                                double newVelocity = GetVelocity(MF.EuclideanDistance(neighbouringCells[k], cellKey));
                                if (newVelocity > velocity)
                                {
                                    velocity = newVelocity;
                                }
                            }
                            // get full probability
                            int relativetime = _dictRelativeTimesData[microCompitingIDs[j]];
                            bool mode = true;
                            if (_generation - relativetime > _modelSettings.n_a)
                                mode = false;
                            if (mode)
                            {
                                double avascularProb = GetGrowthProbAvascular(_generation - relativetime);
                                double prob = avascularProb * beta * velocity;
                                individualMicroCellApparitionProbs.Add(prob);
                            }
                            else individualMicroCellApparitionProbs.Add(0);
                        }
                        int maxProbIndexGrowth5 = MF.GetMaxValueIndex(individualMicroCellApparitionProbs);
                        int expandingMicro = microCompitingIDs[maxProbIndexGrowth5];
                        double rho5 = individualMicroCellApparitionProbs[maxProbIndexGrowth5];
                        double X = _random.NextDouble();
                        // applying rule, updating states
                        if (X <= rho5)
                        {
                            _dictStates[cellKey].FutureState = CellState.Micro;
                            _dictStates[cellKey].FutureTumor = expandingMicro;
                        }
                    }
                }

            }
        }

        //Me quede aqui
        //Elimina las celulas en micrometastasis que no lograron colonizar y las ponen en el estado original
        private void CheckMicrometastasisSurvival()
        {
            List<int> micrometastasisToRemove = new List<int>();
            List<int> micrometastasisIDs = _dictMicro.Keys.ToList(); //Lista de enteros que representa las id de las celulas en micrometastasis
            int count = micrometastasisIDs.Count;

            _dictFailedMicrometastasis[0].Add(_generation, _dictFailedMicrometastasis[0][_generation - 1]);//_dictFailedMicrometastasis[0]:Diccionario de micrometastasis fallida en el organ0
            _dictFailedMicrometastasis[1].Add(_generation, _dictFailedMicrometastasis[1][_generation - 1]);//_dictFailedMicrometastasis[1]:Diccionario de micrometastasis fallida en el organ2

            for (int i = 0; i < count; i++)
            {
                double prob = _random.NextDouble();//random entre 0 y 1
                int index = micrometastasisIDs[i];   // Dame el id de la llave i
                TVertex cell = _dictMicro[index][0]; // Dame el primer vertice en micrometastasis con id index
                int destinyOrgan = _dictStates[cell].Organ;
                // Probabilidad de colonización de una micrometástasis en destinyOrgan
                double xi = (destinyOrgan == 0) ? _parametersSettings.xi_mic0 : _parametersSettings.xi_mic1;
                //Si la probabilidad de muerte es mayor que el random , mueren las celulas en micrometastasis
                if (prob <= 1 - xi)
                {
                    // micrometastasis death
                    List<TVertex> cellsInMicrometastasis = _dictMicro[micrometastasisIDs[i]];
                    _dictRelativeTimesData.Remove(micrometastasisIDs[i]);
                    for (int j = 0; j < cellsInMicrometastasis.Count; j++)
                    {
                        _dictStates[cellsInMicrometastasis[j]].CurrentState = _dictStatesOriginal[cellsInMicrometastasis[j]];
                        _dictStates[cellsInMicrometastasis[j]].CurrentTumor = -1;
                        _microFrontiers.Remove(cellsInMicrometastasis[j]);
                    }
                    micrometastasisToRemove.Add(micrometastasisIDs[i]);
                    _dictFailedMicrometastasis[destinyOrgan][_generation]++;
                }
            }
            for (int i = 0; i < micrometastasisToRemove.Count; i++)
                _dictMicro.Remove(micrometastasisToRemove[i]); //Elimina las celulas en micrometastasis que no lograron colonizar

        }

        // Modificado Inmunidad
        private void UpdateTumorMigratoryCells()
        {
            int count = 0;
            int total = _dictAsyncTum[0].Count;
            while (_dictAsyncTum[0].Count != 0)
            {
                count++;
                int index = _random.Next(_dictAsyncTum[0].Count);
                TVertex cell = _dictAsyncTum[0][index];
                _dictAsyncTum[0].Remove(cell);
                _dictAsyncTum[1].Add(cell);
                int tumorID = _dictStates[cell].CurrentTumor;
                List<TVertex> tumorCells = _dictTumor[tumorID];
                double prob = 0.0;
                int spawntime = _dictRelativeTimesData[tumorID];
                bool mode = false;

                if (_generation - spawntime > _modelSettings.n_a)
                    mode = true;
                if (mode)
                    prob = GetMigrantCellApparitionProb(_generation - spawntime);
                double X = _random.NextDouble();
                List<TVertex> neighbours = GetN(cell);
                if (X <= prob)
                {
                    List<TVertex> distantNeighbours = GetDN(cell, neighbours);
                    List<TVertex> filteredDistantNeighbours = GetDNE(cell, distantNeighbours, new List<CellState> { CellState.Strom, CellState.Tumor, CellState.Micro });
                    if (filteredDistantNeighbours.Count > 0)
                    {
                        TVertex w = GetMetastasisDestiny(filteredDistantNeighbours);
                        int cantCellsInCell = GetRandomAmountCells();
                        for (int i = 0; i < cantCellsInCell; i++)
                        {
                            _dictAsyncCS.Add(_cellInBloodstreamIDGenerator, w);
                            _cellInBloodstreamIDGenerator++;
                            _amountCellsInBloodStreamFromTumors++;
                        }
                    }
                }
            }
        }

        //Modificado
        private void UpdateMigratoryCells()
        {
            int tentativeMovements = 0;// Cantidad de movimientos tentativos
            Dictionary<int, int[]> tumorCentroidsDict = GetTumorCentroidsDictionaries(true);
            while (tentativeMovements < _parametersSettings.mu_mig) //mu_mig: Cantidad de movimientos tentativos que la célula migratoria puede llevar a cabo en un  instante de tiempo
            {
                Console.WriteLine("   cellularautomata library: tentative movement " + tentativeMovements);
                int count = 0;
                tentativeMovements++;
                while (_dictAsyncMig[0].Count != 0)
                {
                    count++;
                    int index = _random.Next(_dictAsyncMig[0].Keys.Count);
                    TVertex cell = _dictAsyncMig[0].Keys.ToList()[index];      // vertice random del _dictAsyncMig
                    int movements = _dictAsyncMig[0][cell];                    // te devuelve el entero que representa() del vertice
                    _dictAsyncMig[0].Remove(cell);                             // quita el vertice del _dictAsyncMig[0]

                    int wanderedDistance = _dictWanderedDistance[cell];        // te devuelve el entero que representa() del vertice
                    _dictWanderedDistance.Remove(cell);                        // quita al vertice de wanderedDistance

                    int cantCellsInCell = _dictStates[cell].CantCells;
                    List<TVertex> neighbours = GetN(cell);                     // Obtiene todos los vertices vecinos de cell
                    List<TVertex> distantNeighbours = GetDN(cell, neighbours); // Te devulve los vecinos lejanos de cell en neighbours
                    //Devuelve una lista con los vertices vecinos distante cuyo estado actual es stroma, tumoral o micrometastasis 
                    List<TVertex> filteredDistantNeighbours = GetDNE(cell, distantNeighbours, new List<CellState> { CellState.Strom, CellState.Tumor, CellState.Micro });
                    if (filteredDistantNeighbours.Count > 0)
                    {
                        _dictStates[cell].CurrentState = CellState.Strom;
                        _dictStates[cell].CurrentTumor = -1;
                        //Devuelve un vertice random en filteredDistantNeighbours
                        TVertex w = GetMetastasisDestiny(filteredDistantNeighbours);

                        _dictWanderedDistanceMeasurementsMetas[wanderedDistance]++;
                        for (int i = 0; i < cantCellsInCell; i++)
                        {
                            _dictAsyncCS.Add(_cellInBloodstreamIDGenerator, w);
                            _cellInBloodstreamIDGenerator++;
                            _amountCellsInBloodStreamFromMigra++;
                        }
                    }
                    else  //Si no hay vecinos lejanos en estado de estroma , tumoral o micrometastasis
                    {
                        // cell choose to move
                        List<TVertex> nearNeighbours = GetNN(cell, neighbours); //Te devuelve vertice q son vecinos cercanos a cell   
                        // Dado un vertice etorna los vertices cercanos a el que pertenecen a su mismo organo y que su estado actual sea estroma
                        List<TVertex> nearNeighbours2 = GetNNE(cell, nearNeighbours, new List<CellState> { CellState.Strom });
                        int tumorID = _dictStates[cell].CurrentTumor;
                        if (nearNeighbours2.Count > 0)
                        {
                            // cell can move
                            _dictStates[cell].CurrentState = CellState.Strom;
                            _dictStates[cell].CurrentTumor = -1;
                            int[] tumorCentroid = tumorCentroidsDict[tumorID];//Array de tamanno dos que indica el controide de los vertices con tumorid
                            //Te da la lista de vecinos cercanos o inmediatos que pueden moverse
                            List<TVertex> availableDestinies = GetAvailableDestinies(cell, MF.BuildTVertexID(tumorCentroid), nearNeighbours2);
                            TVertex w = cell;
                            if (availableDestinies.Count != 0)
                            {
                                // possible destinies
                                int[] cellPos = MF.GetTVertexID(cell);
                                List<double> probs = new List<double>();//probabilidad cuando no hay vector nutriente al que moverse desde el destino disponible
                                for (int i = 0; i < availableDestinies.Count; i++)
                                {
                                    List<int[]> nutrientsVectorsRegion = GetRegionNutrients(availableDestinies[i]);
                                    int[] destinyPos = MF.GetTVertexID(availableDestinies[i]);
                                    int[] migrationVector = MF.BuildVector(destinyPos, cellPos);
                                    List<double> simValues = new List<double>();
                                    if (nutrientsVectorsRegion.Count != 0)
                                    {
                                        for (int j = 0; j < nutrientsVectorsRegion.Count; j++)
                                        {
                                            double sim = MF.GetSim(migrationVector, nutrientsVectorsRegion[j]);
                                            double simAlt = GetSimAlt(sim);
                                            simValues.Add(simAlt);
                                        }
                                    }
                                    else simValues.Add(1);
                                    int maxSimIndex = MF.GetMaxValueIndex(simValues);
                                    double beta = simValues[maxSimIndex];
                                    double prob = 1 / (double)availableDestinies.Count * beta;
                                    probs.Add(prob);
                                }
                                // choosing one possible destiny
                                double random = _random.NextDouble();
                                List<double> normalizedProbs = MF.GetNormalizedProbabilities(probs);
                                List<double> normalizedAddedProbs = MF.GetNormalizedAddedProbs(normalizedProbs);
                                int availableMovementIndex = 0;
                                for (int i = 1; i < normalizedAddedProbs.Count; i++)
                                {
                                    if (normalizedAddedProbs[i - 1] <= random && random < normalizedAddedProbs[i])
                                    {
                                        availableMovementIndex = i - 1;
                                        break;
                                    }
                                }
                                w = availableDestinies[availableMovementIndex];
                            }
                            // applying movement rule, updating states
                            double rho = GetMigrantDeathProbability(movements);
                            double X = _random.NextDouble();
                            if (X <= 1 - rho)
                            {
                                // cell survived 
                                _dictStates[w].CurrentState = CellState.Migra;
                                _dictStates[w].CantCells = cantCellsInCell;
                                _dictStates[w].CurrentTumor = tumorID;
                                _dictAsyncMig[1].Add(w, movements + 1);
                                _dictWanderedDistance.Add(w, wanderedDistance + 1);
                            }
                            else
                            {
                                _dictStates[cell].CurrentState = CellState.Strom;
                                _dictWanderedDistanceMeasurementsDeath[wanderedDistance]++;
                            }
                        }
                        else
                        {
                            // cell cannot move
                            double rho = GetMigrantDeathProbability(movements);
                            double X = _random.NextDouble();
                            if (X <= 1 - rho)
                            {
                                // cell survived 
                                _dictStates[cell].CurrentState = CellState.Migra;
                                _dictStates[cell].CantCells = cantCellsInCell;
                                _dictStates[cell].CurrentTumor = tumorID;
                                _dictAsyncMig[1].Add(cell, movements + 1);
                                _dictWanderedDistance.Add(cell, wanderedDistance);
                            }
                            else
                            {
                                _dictStates[cell].CurrentState = CellState.Strom;
                                _dictWanderedDistanceMeasurementsDeath[wanderedDistance]++;
                            }
                        }





                    }


                }

            }
        }


        //OJO Buscar mas inf sobre el dictAsyncCS
        //Quita a las celulas del dictAsyncCS y las pasa a estado de micrometastasis y las pone en microfrontera

        //Modificacion inmune
        private void UpdateMigratoryCellsInBloodstream() //celulas en el sistema circulatoria
        {
            int count = 0;
            int total = _dictAsyncCS.Count;
            while (_dictAsyncCS.Count != 0)
            {
                count++;
                int index = _random.Next(_dictAsyncCS.Keys.Count);
                int cellID = _dictAsyncCS.Keys.ToList()[index]; //Dame una lleva random
                TVertex destiny = _dictAsyncCS[cellID];
                _dictAsyncCS.Remove(cellID);
                int destinyOrgan = _dictStates[destiny].Organ;
                double random0 = _random.NextDouble();
                double random1 = _random.NextDouble();
                //Modificacion
                if (!CellsInmune.Contains(destiny) && random0 <= _parametersSettings.xi_sc && _dictStates[destiny].CurrentState == CellState.Strom)
                {
                    _dictStates[destiny].CurrentState = CellState.Micro;
                    _dictStates[destiny].CurrentTumor = _tumorIDGenerator;
                    _dictStates[destiny].CantCells = GetRandomAmountCells();

                    _dictMicro.Add(_tumorIDGenerator, new List<TVertex> { destiny });
                    _dictRelativeTimesData.Add(_tumorIDGenerator, _generation);
                    _microFrontiers.Add(destiny, _tumorIDGenerator);
                    _tumorIDGenerator++;
                }
            }
            _cellInBloodstreamIDGenerator = 0;
            _amountCellsInBloodStreamFromMigra = 0;
            _amountCellsInBloodStreamFromTumors = 0;
        }

        // Devuelve un numero random que determina la cant de celulas inmunes en el grafo
        private int CountInmuneCells()
        {
            int sup = _smallWorldNetwork.NetworkSizeX;
            int r = new Random().Next(10, sup);
            return r;
        }

        //Rellena la lista de las celulas inmunes
        private void InmuneCells()
        {
            List<TVertex> n = MF.GetRegularNeighboursTemplate(_organ1Scheme.TumorRadius);
            int count = CountInmuneCells();
            int x = 0;
            int y = 0;
            TVertex vertex = null;
            do
            {
                // Migra, Micro
                x = new Random().Next(0, _smallWorldNetwork.NetworkSizeX);
                y = new Random().Next(0, _smallWorldNetwork.NetworkSizeY);
                vertex = MF.BuildTVertexID(x, y);
                //si no es un vecino del centro del tumor, ni es el centro del tumor, ni ya existe, agregalo
                if (_dictStates[vertex].CurrentState != CellState.Tumor && _dictStates[vertex].CurrentState != CellState.Micro && _dictStates[vertex].CurrentState != CellState.Migra && !(x == _organ1Scheme.TumorPosX && y == _organ1Scheme.TumorPosY) && !CellsInmune.Contains(vertex) && !n.Contains(vertex)) CellsInmune.Add(vertex);
            }
            while (count > CellsInmune.Count);


        }

        //Todo lo Agregado Inmunidad
        private void DeleteVertex(TVertex cell)
        {
            List<int> Remove_idMicro = new List<int>();
            List<int> Remove_idTumor = new List<int>();
            List<int> id = new List<int>();
            foreach (var item in _dictTumor)
            {
                while (item.Value.Remove(cell)) id.Add(item.Key);
                if (item.Value.Count == 0) Remove_idTumor.Add(item.Key);
            }
            foreach (var item in _dictMicro)
            {
                while (item.Value.Remove(cell)) id.Add(item.Key);
                if (item.Value.Count == 0) Remove_idMicro.Add(item.Key);
            }
            foreach (var item in Remove_idMicro)
            {
                _dictMicro.Remove(item);
            }
            foreach (var item in Remove_idTumor)
            {
                _dictTumor.Remove(item);
            }
            _tumorFrontiers.Remove(cell);
            _microFrontiers.Remove(cell);
            _synchronousCellsToUpdate.Remove(cell);
            _dictAsyncMig[0].Remove(cell);
            _dictAsyncMig[1].Remove(cell);
            if (_dictAsyncCS.ContainsValue(cell))
                for (int i = 0; i < _dictAsyncCS.Count; i++)
                {
                    if (_dictAsyncCS.ElementAt(i).Value == cell)
                    {
                        _dictAsyncCS.Remove(_dictAsyncCS.ElementAt(i).Key);
                        i = 0;
                    }

                }
            for (int i = 0; i < _dictAsyncTum.Length; i++)
            {
                while (_dictAsyncTum[i].Remove(cell)) { }
            }
            if (_dictWanderedDistance.ContainsKey(cell))
            {
                int wand = -1;
                foreach (var item in _dictWanderedDistance)
                {
                    if (item.Key == cell) wand = item.Value;
                }
                _dictWanderedDistanceMeasurementsMetas[wand]--;
                _dictWanderedDistanceMeasurementsDeath[wand]--;
                _dictWanderedDistance.Remove(cell);
            }
            foreach (var item in id)
            {  //  pasa porque puede haber muchos vertices con la misma id y generacion
                if (!_dictMicro.ContainsKey(item) && !_dictTumor.ContainsKey(item)) _dictRelativeTimesData.Remove(item);
            }


            _dictStates[cell].CurrentState = _dictStatesOriginal[cell];
            _dictStates[cell].CurrentTumor = -1;

        }

        //Determina la probabilidad de intercambiar posicion con las celulas normales
        private int ProbabilityMov()
        {
            return 0;
        }
        //Determina la probabilidad de inmunoreaccion

        //Determina si la celula tumoral gana
        private bool TumorcellWins(int p)
        {
            if (p > 0.43) return true;
            return false;
        }
        private bool ImmunecellWins(double p)
        {
            if (p < 0.43) return true;
            return false;
        }
        //intermediate state
        private bool IntermediateState(double p) //Falta por implementar esto
        {
            if (p == 0.43) return true;
            return false;

        }

        //Agregado Inmunidad
        //Retorna falso si gana la celula tumoral
        private bool Warm(TVertex cellinmune, List<TVertex> neighbours, List<TVertex> normalneighbours)
        {
            foreach (var n in neighbours)
            {
                double p = probabilityImmunoreaction.NextDouble();

                if (IntermediateState(p))
                {
                    int t = neighbours.Count + normalneighbours.Count;
                    int n_porciento = (neighbours.Count * 100) / t;
                    if (n_porciento > 60)
                    {
                        p = p + 0.1; //Puede que tenga que arreglarse
                    }
                }
                if (ImmunecellWins(p))
                {
                    DeleteVertex(n);
                    return true;
                }
                CellsInmune.Remove(cellinmune);
            }
            return false;
        }

        //Verifica si el enfrentamiento es con una celula en migra, micro o tumor
        //private bool Verific(TVertex cell)
        //{
        //    foreach (var item in DictMigra)
        //        foreach (var item2 in item.Value)
        //        {
        //            bool migra = item2.Key == cell;
        //            if (migra) return true;
        //        }

        //    foreach (var item in _dictTumor)
        //    {
        //        bool tumor = item.Value.Contains(cell);
        //        if (tumor) return true;
        //    }

        //    foreach (var item in _dictMicro)
        //    {
        //        bool micro = item.Value.Contains(cell);
        //        if (micro) return true;
        //    }
        //    return false;
        //}

        public void InmuneWarm()
        {
            Console.WriteLine("   cellularautomata library: updating inmune cells ...");
            int count = CellsInmune.Count;
            for (int i = 0; i < count; i++)
            {
                TVertex item = CellsInmune[i];
                List<TVertex> n = GetN(item);
                List<TVertex> nn = GetNN(item, n);
                List<TVertex> nnw = GetNNE(item, nn, new List<CellState> { CellState.Micro, CellState.Migra, CellState.Tumor });
                //Para comprobar el estado medio
                List<TVertex> nnm = GetNNE(item, nn, new List<CellState> { CellState.Epith, CellState.Lumen, CellState.Strom });
                if (nn.Count > 0)
                {
                    Warm(item, nnw, nnm);
                    i--;
                    count--;
                }
            }
            
                
            
        }

    }


}
