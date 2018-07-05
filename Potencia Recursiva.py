def potenciaRecursiva(numero, exponente):
  if (exponente == 0 ):
    return 1;

  else:
    return numero*potenciaRecursiva(numero,exponente-1);

numero = int(input("\ningrese un numero: "))
exponente = int(input("\ningrese un exponente"))
print("la pontencia entre los dos numeros es "+ str(potenciaRecursiva(numero, exponente)) );
