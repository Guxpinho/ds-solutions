# Variables to store sum of ages for each gender
soma_h = 0
soma_m = 0

# Counters for number of men and women
sexo_homem= 0 
sexo_mulher = 0

# Variables for average calculations
media_h = 0
media_m = 0
media_geral = 0

# Loop to collect data for 10 people
for i in range(10):
    # Ask the user's gender
    sexo = input("você é homem(h) ou mulher(m)").lower()
    
    if sexo == 'h':
        sexo_homem += 1  # Count men
        homem = int(input("qual é sua idade: "))
        soma_h += homem  # Add to total age for men
        
    elif sexo == "m":
        sexo_mulher +=1  # Count women
        mulher = int(input("qual é sua idade: "))
        soma_m += mulher  # Add to total age for women

# Calculate average ages for men, women, and overall
media_h = soma_h/sexo_homem
media_m = soma_m/sexo_mulher
media_geral = (soma_h + soma_m)/(sexo_mulher + sexo_homem)

# Display results
print(f"essa é a média masculina{media_h}")
print(f"essa é a média feminina {media_m}")
print(f"essa é a media geral {media_geral}")
