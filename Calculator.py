#!/usr/bin/env python
# coding: utf-8

# In[28]:


numero1=float(input("Ingrese Primer Numero\n"))
numero2=float(input("Ingrese Segundo Numero\n"))
operacion=float(input("Para Suma marque 1, para resta marque 2, para multiplicacion marque 3, para division marque 4\n"))
if operacion == 1:
    resultado = numero1 + numero2
    print(f"El resultado de sumar {numero1} mas {numero2} es igual a {resultado}")
elif operacion == 2:
    resultado = numero1 - numero2
    print(f"El resultado de restar {numero1} menos {numero2} es igual a {resultado}")
elif operacion == 3:
    resultado = numero1 * numero2
    print(f"El resultado de multiplicar {numero1} por {numero2} es igual a {resultado}")
elif operacion == 4 and numero2 == 0:
    print("Operacion no se puede realizar, ya que el resultado de la division entre 0 no esta definido")
elif operacion > 4:
    print("Operacion no se puede realizar")
elif operacion == 4:
    resultado = numero1 / numero2
    print(f"El resultado de dividir {numero1} entre {numero2} es igual a {resultado}")
print("\n\n\n\nGracias por usar la calculadora")
print("Prueba Git")
print("Prueba Git2")