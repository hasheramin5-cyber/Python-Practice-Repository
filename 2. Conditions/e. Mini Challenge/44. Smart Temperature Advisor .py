temperature = float(input("\nEnter temperature (°C): "))

if temperature < 10:
    print("Very Cold - Wear heavy clothes.")
elif temperature < 20:
    print("Cool - Wear a jacket.")
elif temperature < 30:
    print("Pleasant - Light clothing is fine.")
else:
    print("Hot - Stay hydrated and wear light clothes.")