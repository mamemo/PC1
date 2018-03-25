from tec.ic.ia.pc1.g07 import generar_muestra_pais, generar_muestra_provincia, set_semilla

#Para ejecutar estas pruebas, deben encontrarse los csv Juntas.csv, VotosxPartidoxJunta.csv, e Indicadores_x_Canton.csv en en mismo directorio.

# Metodo que testea la funcion test_generar_muestra_pais.
# Setea la semilla de RNG en 10 para obtener un resultado
# seguro. Pide que genere una muestra a generar_muestra_pais
# y compara con el resultado esperado.
# Se pide solo 1 muestra porque todos los resultados generados
# seran los mismos.
# Parametros: None
# Requisitos: Setear la semilla del RNG.
# Salidas: Un lista con un elemento lista dentro.

def test_generar_muestra_pais_len1():
    set_semilla(10)
    muestra_generada = generar_muestra_pais(1)
    assert muestra_generada == [['SAN JOSE',
                                 'CENTRAL',
                                 'SAN SEBASTIAN',
                                 '101011008 SAN SEBASTIAN',
                                 '360',
                                 '600',
                                 '429',
                                 '288054',
                                 '44.619998931884766',
                                 '6455.7150805792835',
                                 '100',
                                 'urbana',
                                 '89.90526294970431',
                                 'hombre',
                                 '45.7136353289324',
                                 '40 a 44',
                                 '81903',
                                 '3.49998168565254',
                                 '63.39450325384907',
                                 'vivienda en buen estado',
                                 '6.781192386115283',
                                 'vivienda no hacinada',
                                 'secundaria completa',
                                 '98.75840265820393',
                                 '98.47701215186378',
                                 'alfabeta',
                                 '9.876764995308566',
                                 '10.332647081354363',
                                 '31.12624547523977',
                                 '9.52696981486167',
                                 '43.291743411730835',
                                 '56.708256588269165',
                                 '71.21249737410005',
                                 '44.168248988689285',
                                 'dentro de fuerza',
                                 'sector terciario',
                                 '13.706924577373089',
                                 '16.266741652607404',
                                 'no nacido en extranjero',
                                 '12.348379123358626',
                                 'sin discapacidad',
                                 '14.207752713033045',
                                 'asegurado',
                                 'indirecto',
                                 '39.64385125972442',
                                 '6.866659',
                                 'jefatura masculina',
                                 'telefono celular',
                                 'telefono residencial',
                                 'no computadora',
                                 'no internet',
                                 'electricidad',
                                 'servicio sanitario',
                                 'agua',
                                 'RESTAURACION NACIONAL']]


# Metodo que testea la funcion test_generar_muestra_pais.
# Pide que genere una muestra de 10000 elementos a
# generar_muestra_pais y verifica que la longitud de la
# lista resultante sea 10000.
# Parametros: None
# Requisitos: None
# Salidas: Un lista con 10000 elementos.

def test_generar_muestra_pais_len10000():
    muestra_generada = generar_muestra_pais(10000)
    assert len(muestra_generada) == 10000


# Metodo que testea la funcion test_generar_muestra_pais.
# Pide que genere una muestra de 100 elementos a
# generar_muestra_pais y verifica que la longitud de la
# cada elemento de la lista resultante sea 55.
# Parametros: None
# Requisitos: None
# Salidas: Un lista con 100 elementos, cada elemento con 55 elementos.

def test_generar_muestra_pais_len100_55elem():
    muestra_generada = generar_muestra_pais(100)
    assert len(muestra_generada[0]) == 55


# Metodo que testea la funcion test_generar_muestra_pais.
# Pide que genere una muestra de "10" (tipo string) elementos a
# generar_muestra_pais y verifica que la funcion maneje el error
# del parametro (que debe ser un entero) y retorne None.
# Parametros: None
# Requisitos: None
# Salidas: None

def test_generar_muestra_pais_len10_error():
    muestra_generada = generar_muestra_pais("10")
    assert muestra_generada is None


# Metodo que testea la funcion test_generar_muestra_provincia.
# Setea la semilla de RNG en 755 para obtener un resultado
# seguro. Pide que genere una muestra a generar_muestra_provincia
# de la provincia "HEREDIA" y compara con el resultado esperado.
# Se pide solo 1 muestra porque todos los resultados generados
# seran los mismos.
# Parametros: None
# Requisitos: Setear la semilla del RNG.
# Salidas: Un lista con un elemento lista dentro.

def test_generar_muestra_provincia_heredia_len1():
    set_semilla(755)
    muestra_generada = generar_muestra_provincia(1, "HEREDIA")
    assert muestra_generada == [['HEREDIA',
                                 'SARAPIQUI',
                                 'LAS HORQUETAS',
                                 '410003009 LAS HORQUETAS',
                                 '4678',
                                 '500',
                                 '300',
                                 '57147',
                                 '2140.5400390625',
                                 '26.69746837579776',
                                 '18.05694087178704',
                                 'no urbana',
                                 '103.44250622997508',
                                 'hombre',
                                 '55.620608899297416',
                                 '55 a 59',
                                 '15768',
                                 '3.6026763064434295',
                                 '44.67275494672755',
                                 'vivienda en mal estado',
                                 '9.145104008117706',
                                 'vivienda no hacinada',
                                 'secundaria completa',
                                 '94.38626347253164',
                                 '91.90770114117608',
                                 'alfabeta',
                                 '5.8938491351467235',
                                 '6.434638014837547',
                                 '33.66173098597042',
                                 '5.235771190698323',
                                 '49.52214363576425',
                                 '50.47785636423575',
                                 '73.82929757854663',
                                 '26.49159771827953',
                                 'fuera de fuerza',
                                 'otros',
                                 '18.135038203648918',
                                 '17.757712565838883',
                                 'no nacido en extranjero',
                                 '10.472990708173532',
                                 'sin discapacidad',
                                 '19.297600923932837',
                                 'asegurado',
                                 'indirecto',
                                 '23.96336180220322',
                                 '5.910705',
                                 'jefatura masculina',
                                 'telefono celular',
                                 'telefono residencial',
                                 'no computadora',
                                 'no internet',
                                 'electricidad',
                                 'no servicio sanitario',
                                 'agua',
                                 'RESTAURACION NACIONAL']]


# Metodo que testea la funcion test_generar_muestra_provincia.
# Pide que genere una muestra de 1000 elementos a
# generar_muestra_provincia de la provincia "LIMON" y verifica
# que la longitud de la lista resultante sea 1000.
# Parametros: None
# Requisitos: None
# Salidas: Un lista con 1000 elementos.

def test_generar_muestra_provincia_limon_len1000():
    muestra_generada = generar_muestra_provincia(1000, "LIMON")
    assert len(muestra_generada) == 1000


# Metodo que testea la funcion test_generar_muestra_provincia.
# Pide que genere una muestra de 100 elementos a
# generar_muestra_provincia de la provincia "PUNTARENAS" Y
# verifica que la longitud de la cada elemento de la lista resultante sea 55.
# Parametros: None
# Requisitos: None
# Salidas: Un lista con 100 elementos, cada elemento con 55 elementos.

def test_generar_muestra_provincia_puntarenas_len100_55elem():
    muestra_generada = generar_muestra_provincia(100, "PUNTARENAS")
    assert len(muestra_generada[0]) == 55


# Metodo que testea la funcion test_generar_muestra_provincia.
# Pide que genere una muestra de 50 elementos a
# generar_muestra_provincia de  la provincia "guanacaste"
# en minuscula y verifica que la funcion maneje el error
# de los parametros (deben ser entero y string en mayuscula)
# y retorne None.
# Parametros: None
# Requisitos: None
# Salidas: None

def test_generar_muestra_provincia_guanacaste_len50_error():
    muestra_generada = generar_muestra_provincia(50, "guanacaste")
    assert muestra_generada is None


# Metodo que testea la funcion test_generar_muestra_provincia.
# Pide que genere una muestra de "50" (string) elementos a
# generar_muestra_provincia de  la provincia "CARTAGO"
# en minuscula y verifica que la funcion maneje el error
# de los parametros (deben ser entero y string en mayuscula)
# y retorne None.
# Parametros: None
# Requisitos: None
# Salidas: None

def test_generar_muestra_provincia_cartago_len50_error():
    muestra_generada = generar_muestra_provincia("50", "CARTAGO")
    assert muestra_generada is None


# Metodo que testea la funcion test_generar_muestra_provincia.
# Pide que genere una muestra de 20 elementos a
# generar_muestra_provincia de  la provincia "INEXISTENTE"
# y verifica que la funcion maneje el error
# de los parametros (deben ser entero y string en mayuscula
# de provincia existente).
# y retorne None.
# Parametros: None
# Requisitos: None
# Salidas: None

def test_generar_muestra_provincia_inexistente_len20_error():
    muestra_generada = generar_muestra_provincia("50", "INEXISTENTE")
    assert muestra_generada is None
