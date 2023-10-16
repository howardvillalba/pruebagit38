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


# In[30]:


lista = [1, 2, 3, 4, 5]

for numero in lista:
    if numero == 4:
        break
    print(numero)


# In[34]:


for i in range(2):
    print(i)


# In[35]:


10 % 3


# In[36]:


7%3


# In[37]:


lista_howard= [1,2,3,4,5]


# In[38]:


type(lista_howard)


# In[39]:


lista_howard2=[2,4,6,8,10]


# In[40]:


type(lista_howard2)


# In[41]:


howlist=lista_howard+lista_howard2


# In[42]:


howlist


# In[43]:


howlist[4]


# In[3]:


caracter=["Villalba"]


# In[4]:


caracter


# In[5]:


type(caracter)


# In[7]:


for num in range (9):
    print(num)


# In[12]:


for num in range (5,50,5):
    print(num)


# In[29]:


type(caracter)
caracter[-1]


# In[23]:


casa=[5]


# In[28]:


caracter[0]


# In[30]:


len(caracter)


# In[32]:


nombre="howard"


# In[33]:


len(nombre)


# In[37]:


nombre[-1]


# In[38]:


len(nombre)


# In[ ]:




