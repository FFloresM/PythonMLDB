from vehiculo import Vehiculo, Audiencia, Moto

auto1 = Vehiculo("azul", 4)
auto1.mostrar()

auto1.setColor("Negro")
auto1.setRuedas(6)

print(auto1.getColor(), auto1.getRuedas())

print("\n\n\n")

aud = Audiencia("P-01-2021", "preparatoria", "vulneración de derechos")
aud.asignarBloques(4)
aud.mostrar()

aud.plazo()
aud.mostrar()
print(aud.plazo_max)

print("\n\n\n")

moto = Moto("verde", 150)
#print("color =",moto.getColor())
print("cilindrada =", moto.cilindrada)
#print("numero de ruedas = ", moto.getRuedas())
moto.mostrar()