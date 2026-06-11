from usuario import Usuario

usuario = Usuario(
    "Ronald Verano",
    "ronald@gmail.com",
    "3001234567"
)

print("Datos iniciales:")
print(usuario.mostrar_datos())

usuario.set_nombre("Ronald Sosa")

print("\nDatos actualizados:")
print(usuario.mostrar_datos())
