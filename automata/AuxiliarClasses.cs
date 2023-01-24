using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using TVertex = System.String;

namespace AutomataLibrary2D
{
    public enum CellState { NULL, Lumen, Epith, Strom, Tumor, Migra, Micro } //Lugar donde se encuentra la celula
    public enum SelectedOrgan { Primary, Secondary }
    public enum SelectedScheme { Scheme1, Scheme2, Scheme3 }
    public enum SelectedZoom { Normal, Increased }
    public enum HeavisideMode { Population, Generation }
    public enum NeighboursAmountInfluence { No, Yes }
    public enum ExecutionMode { Normal, Optimized }
    public enum PaintMode { Rectangle, Ellipse }

    public class CellData
    {
        public bool Updated { get; set; }            // Te dice si la celula ha sido actualizada
        public CellState CurrentState { get; set; }  // Estado actual de la celula
        public CellState FutureState { get; set; }   // Posible proximo estado de la celula
        public int CurrentTumor { get; set; }        // id del turmor al que pertenece
        public int FutureTumor { get; set; }
        public int Organ { get; set; }               // id que representa al organo que pertenece
        public int CantCells { get; set; }         

        public CellData(bool upd, CellState current, CellState future, int currentt, int futuret, int organ, int cantCells)
        {
            Updated = upd;
            CurrentState = current;
            FutureState = future;
            CurrentTumor = currentt;
            FutureTumor = futuret;
            Organ = organ;
            CantCells = cantCells;
        }
    }

    public class NetworkPropertiesData
    {
        public double AveragePathLength { get; set; }      // longitud promedio del camino de la red Lg
        public double ClusteringCoefficient { get; set; }  // Coeficiente de agrupamiento Cg

        public NetworkPropertiesData()                     // Inicializa con 0
        {
            AveragePathLength = 0;
            ClusteringCoefficient = 0;
        }
    }

    public class ModelSettings                        // Parámetros del modelo
    {
        public double ra { get; private set; }       // Ritmo de crecimiento en etapa avascular
        public double rv { get; private set; }       // Ritmo de crecimiento en etapa vascular
        public double Ka { get; private set; }       // Capacidad de carga avascular o 
        public double Kv { get; private set; }       // Capacidad de carga vascular
        public double P0a { get; private set; }      // Población inicial avascular
        public double P0v { get; private set; }      // Población inicial vascular
        public double deltata { get; private set; }  // Tiempo que trascurre en el modelo entre los instantes de tiempo n y n+1 en etapa avascular
        public double deltatv { get; private set; }  // Tiempo que trascurre en el modelo entre los instantes de tiempo n y n+1 en etapa vascular
        public double n_a { get; set; }              // Período de tiempo que dura la etapa avascular

        public ModelSettings(double ka, double kv, double p0a, double p0v, double rain, double rvin, 
            double delta, double deltav, double n_a_in)
        {
            ra = rain;
            rv = rvin;
            Ka = ka;
            Kv = kv;
            P0a = p0a;
            P0v = p0v;
            deltata = delta;
            deltatv = deltav;
            n_a = n_a_in;
        }
    }

    public class NetworkSettings                                    // Configuracione de la red de mundo pequeño
    {
        public int NetworkSizeX { get; private set; }                 // sx: cantidad de x que conforman vertices
        public int NetworkSizeY { get; private set; }                 // sy: cantidad de y que conforman vertices 

        public int NetworkDivision { get; set; }                      // so :  indica la división del grafo entre una localizaci´on y la otra.
        public double ReconnectionProbability { get; private set; }  //  p : probabilidad de reconexion de aristas de forma aleatoria
        public double NeighbourhoodRadius { get; private set; }      //  R : valor del radio de la vecindad inmediata
        public bool IsNetworkTest { get; private set; }              
        public bool HasPeriodicEdges { get; private set; }           // Te indica si la configuracion contiene aristas periódicas o no

        public NetworkSettings(int sizex, int sizey, int div, double p, double r, bool test, bool periodic)
        {
            NetworkSizeX = sizex;  
            NetworkSizeY = sizey; 
            
            NetworkDivision = div;  
            ReconnectionProbability = p; 
            NeighbourhoodRadius = r;
            IsNetworkTest = test;
            HasPeriodicEdges = periodic;
        }
    }

    public abstract class OrganScheme                               // Estructura de un órgano en que pude estar el tumor
    {
        public SelectedScheme SelectedScheme { get; set; }          // Estructura específica del órgano
        public int TumorPosX { get; set; }
        public int TumorPosY { get; set; }
        public double TumorRadius { get; set; }
    }

    public class OrganScheme1 : OrganScheme                         // Estructura específica del órgano
    {
        public int Lumen { get; set; }        // Scheme 1
        public int Epithelium { get; set; }   // Scheme 1
        public int Stroma { get; set; }       // Scheme 1

        public OrganScheme1(int lumen, int epith, int stroma, int tumorx, int tumory, double tumorradius)
        {
            SelectedScheme = SelectedScheme.Scheme1;
            Lumen = lumen;
            Epithelium = epith;
            Stroma = stroma;
            TumorPosX = tumorx;
            TumorPosY = tumory;
            TumorRadius = tumorradius;
        }
    }

    public class OrganScheme2 : OrganScheme                                    // Estructura específica del órgano
    {
        public int Epithelium { get; private set; }  // Scheme 2
        public int CentralDuct { get; set; }         // Scheme 2
        public int CentralDuctRadius { get; set; }   // Scheme 2

        public OrganScheme2(int epith, int centralDuct, int centralDuctRadius, int tumorx, int tumory, double tumorradius)
        {
            SelectedScheme = SelectedScheme.Scheme2;
            Epithelium = epith;
            CentralDuct = centralDuct;
            CentralDuctRadius = centralDuctRadius;
            TumorPosX = tumorx;
            TumorPosY = tumory;
            TumorRadius = tumorradius;
        }
    }

    public class OrganScheme3 : OrganScheme
    {
        public OrganScheme3()
        {
            SelectedScheme = SelectedScheme.Scheme3;
        }      
    }

    public class NutrientsSettings
    {
        public List<int[]> Regions { get; private set; }

        public List<List<int[]>> Vectors { get; private set; }

        public NutrientsSettings(List<int[]> regions, List<List<int[]>> vectors)
        {
            Regions = regions;
            Vectors = vectors;
        }
    }

    public class ParametersSettings //: Parámetros utilizados en el procedimiento de actualización y en el ajuste de las reglas del autómata celular. pag86 Tesis

    {
        public double mu_mig { get; private set; }       // Cantidad de movimientos tentativos que la célula migratoria puede llevar a cabo en un  instante de tiempo
        public double eta_mig { get; private set; }      // Parámetro de ajuste de la probabilidad de transición relacionada con la aparición de células migratorias
        public double eta_mig_prima { get; private set; }// Parámetro de ajuste de la probabilidad de transición relacionada con la muerte de células migratorias durante su desplazamiento
        public double mu_max { get; private set; }       // Distancia máxima de migración.
        public double xi_sc { get; private set; }        // Probabilidad de supervivencia de una célula migratoria durante el transporte en el sistema circulatorio
        public double xi_mic0 { get; private set; }      // Probabilidad de colonización de una micrometástasis
        public double psi_mic0 { get; private set; }     // Probabilidad de supervivencia de una micrometástasis.
        public double xi_mic1 { get; private set; }      // Probabilidad de colonización de una micrometástasis
        public double psi_mic1 { get; private set; }     // Probabilidad de supervivencia de una micrometástasis.
        public double K_mig { get; private set; }        // Parámetro de ajuste de la probabilidad de transición relacionada con la aparición de células migratorias.
        public int SimScale { get; set; }                // Escala de simulación

        public ParametersSettings(double mu_mig_in, double eta_mig_in,
            double eta_mig_prima_in, double mu_max_in, double xi_sc_in, 
            double xi_mic_in0, double psi_mic_in0, double xi_mic_in1, 
            double psi_mic_in1, double K_mig_in, int simScale)
        {
            mu_mig = mu_mig_in;
            eta_mig = eta_mig_in;
            eta_mig_prima = eta_mig_prima_in;
            mu_max = mu_max_in;
            xi_sc = xi_sc_in;
            xi_mic0 = xi_mic_in0;
            psi_mic0 = psi_mic_in0;
            xi_mic1 = xi_mic_in1;
            psi_mic1 = psi_mic_in1;
            K_mig = K_mig_in;
            SimScale = simScale;
        }
    }
}