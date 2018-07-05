def numeroPrimoRecursivo(numero, c):
  if(numero % c == 0 and numero > 2):
    return False;
  
  elif(c > numero / 2):
   return True;

  else:
    return numeroPrimoRecursivo( numero, c+1 );

numero = int(input("\ningrese un numero: "))
if(numeroPrimoRecursivo(numero, 2) ):
   print ("el numero es primo")
else:
  print ("el numero no es primo")  