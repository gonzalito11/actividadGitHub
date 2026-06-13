
nomAlum = input("Igrese el nombre del alumno: ")
curso = input("Ingrese curso al cual el alumno debe matricularse: ")
rut = input("Ingrese rut apoderado: ")
matricula = int(25000)
mensualidad = int(30000)
resultadoAnual = int(mensualidad*10)+matricula

print(f"-----Detalle Anualidad Colegio-----")
print(f"NOMBRE ALUMNO: {nomAlum}")
print(f"RUT APODERADO: {rut}")
print(f"CURSO MATRICULADO: {curso}")
print(f"VALOR MATRÍCULA: {matricula}")
print(f"VALOR MENSUALIDAD: {mensualidad}")
print(f"VALOR TOTAL A PAGAR: {resultadoAnual}")

#ValorNetoDeUnProducto
producto = input ("Ingrese el nombre del producto: ")
valorProducto = int(input("Ingrese el valor del producto: "))
valorNeto = float(0.81)
valorSinIva = float(valorProducto * valorNeto)
print(f"-----Detalle producto----")
print(f"NOMBRE PRODUCTO: {producto}")
print(f"VALOR PRODUCTO: {valorProducto}")
print(f"VALOR PRODUCTO SIN IVA: {valorSinIva}")