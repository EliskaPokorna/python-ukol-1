jmeno_a_prijmeni = str(input("Jaké je Vaše jméno a příjmení:"))

# Všechna písmena jsou velká
print(jmeno_a_prijmeni.upper())

# Všechna písmena jsou malá
print(jmeno_a_prijmeni.lower())

# první písmeno velké, další malá
print(jmeno_a_prijmeni.title())

# Iniciály
rozdeleni_slov = jmeno_a_prijmeni.split()
inicialy = ". ".join([rozdeleni_slov[0].upper() for rozdeleni_slov in rozdeleni_slov])
print(inicialy + ".")

# Křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, tj. první písmeno velké, další malá (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)
                                                                                                                                                                                                                                                                                              
jmeno, prijmeni = jmeno_a_prijmeni.split()

if len(jmeno) > 5:
    zkracene_jmeno = jmeno[0].upper() + ". "
else:
    zkracene_jmeno = jmeno.capitalize() + " "

print(f"Výsledné jméno je {zkracene_jmeno + prijmeni.capitalize()}")

