
class Persona:
    def __init__(self):
        self.codigo = []
        self.nombre = []
        self.apellido = []
        self.carnet = []
        self.celular = []
        self.estado = []

class Docente(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.materia = []
        self.carrera=[]
class Colegio(Docente):
    def __init__(self):
        Docente.__init__(self)
    def menuR(self):

        opcion = """
        ***** SISTEMA DE RECURSOS HUMANOS*****
             ( COLEGIO NACIONAL LA GUARDIA )  

        1.-REGISTRAR DOCENTES
        2.-MOSTRAR LISTADO DE DOCCENTES HABILITADOS
        3.-INABILITAR REGISTRO DE DOCENTE
        4.-HABILITAR REGISTRO DE DOCENTE
        5.-MOSTRAR LOS DOCENTES NO HABILITADOS
        6.-SALIR

        """
        print(opcion)
        print('***********************************************************************')
        seleccion = int(input('DIGITE UNA OPCION:\n'))
        if (seleccion == 1):
            print(self.resgDoc())
            print(self.menuR())
        elif (seleccion == 2):
            print(self.mostrarReg())
            print(self.pregunta())
        elif (seleccion == 3):
            print(self.cambiarHabilitar())
            print(self.pregunta())
        elif (seleccion == 4):
            print(self.habilitarDoc())
            print(self.pregunta())
        elif (seleccion == 5):
            print(self.mostrarInab())
            print(self.pregunta())
        elif (seleccion == 6):
            print(self.salir())
        else:

            print("** Digite una opción del Menú **")
            self.menuR()
    def resgDoc(self):
        codigo=int(input('Ingrese codido:\n '))
        nombre = input('Ingrese nombre:\n')
        apellido = input('Ingrese apellido:\n')
        carnet = int(input('Ingrese carnet:\n '))
        celular = int(input('Ingrese numero celular\n'))
        materia = input('Ingrese materia:\n')
        carrera= input('Ingrese carrera \n')

        # codigo=self.codAutomatico()
        print(self.guardarDoc(codigo,nombre.upper(), apellido.upper(), carnet, celular, materia.upper(), carrera.upper()))

        agregarmas = input('DESEA AGREGAR OTRO DOCENTE: y/n \n')
        if (agregarmas == 'y' or agregarmas == 'Y'):
            self.resgDoc()
        return 'SE REGISTRO CORRECTAMENTE EL DOCENTE'
    def guardarDoc(self, cd, nb, ap, cr, tl, mt, crr):
        self.codigo.append(cd)
        self.nombre.append(nb)
        self.apellido.append(ap)
        self.carnet.append(cr)
        self.celular.append(tl)
        self.materia.append(mt)
        self.carrera.append(crr)
        self.estado.append(1)

        return "SE REGISTRO CON EXITO EL DOCENTE : {} {} **".format(nb,ap)
    def mostrarReg(self):
        print('***DOCENTES HABILITADOS**')
        if (self.nombre):
            for i in range(len(self.nombre)):
                if (self.estado[i] == 1):
                    self.descripcionMenu(i)
        else:
            return 'ESTA VACIO EL REGISTRO'
    def descripcionMenu(self, hb):
        # if (self.habilitado[hb] ==1):
        print('*******************************************************')
        print('**  *****REGISTRO DEL DOCENTE {} {} '.format(self.nombre[hb],self.apellido[hb]))
        print('CODIGO = {}'.format(self.codigo[hb]))
        print('CARNET = {}'.format(self.carnet[hb]))
        print('TELEFONO/CELULAR = ***{}***'.format(self.celular[hb]))
        print('MATERIA= {} '.format(self.materia[hb]))
        print('CARRERA = {}  '.format(self.carrera[hb]))
        print('ESTADO = {}'.format(self.estado[hb]))
        pass
    def pregunta(self):
        preg = input('DESEA VOLVER AL MENU PRINCIPAL:y/n \n')
        if (preg == 'y' or preg == 'Y'):
            self.menuR()
        elif (preg == 'n' or preg == 'N'):
            print(self.salir())
        else:
            print("** Digite una opción del Menú **")
            self.menuR()
    def activo(self):
        self.mostrarReg()
        codServ = int(input('INGRESE NUMERO DEL CARNET DEL DOCENTE PARA INABILITAR :\n '))
        posicion = self.carnet.index(codServ)
        return posicion
    def cambiarHabilitar(self):
        posicion = self.activo()
        return self.inabilitarDoc(posicion)
    def inabilitarDoc(self, posicion):
        self.estado[posicion] = 0
        self.descripcionMenu(posicion)
        return '** EL DOCENTE {} {} QUEDO INABILITADO **'.format(self.nombre[posicion],self.apellido[posicion])
    def habilitarDoc(self):
        self.mostrarInab()
        codServ = int(input('INGRESE NUEMRO DE CARNET PARA HABILITAR AL DOCENTE :\n '))
        posicion = self.carnet.index(codServ)
        self.estado[posicion] = 1
        return ' ***EL DOCENTE {} SE HABILITO CORRECTAMENTE***'.format(self.nombre[posicion])
    def mostrarInab(self):
        print('*****DOCENTES NO HABILITADOS******')
        if (self.codigo):
            for i in range(len(self.codigo)):
                if (self.estado[i] == 0):
                    self.descripcionMenu(i)
    def salir(self):
        return '*****GRACIAS POR UTILIZAR EL SISTEMA*****'

colegio = Colegio()
colegio.guardarDoc(1,'ANTONIO', 'MELGAR', 11223652, 69354210, 'MATEMATICAS', 'ADMINISTRACION DE EMPRESAS')
colegio.guardarDoc(2,'JUAN', 'MERCADO', 6323652, 69054210, 'CONTABILIDAD GENERAL I', 'INGENIERA COMERCIAL')
colegio.guardarDoc(3,'MARCO','MERCADO', 11023652, 77254210,  'MICROECONOMIA', 'ADMINISTRACION DE EMPRESAS')
colegio.guardarDoc(4,'MARIO','PEREZ', 11123652, 69054278, 'MACROECONOMIA', 'INGENIERA COMERCIAL')
colegio.menuR()
