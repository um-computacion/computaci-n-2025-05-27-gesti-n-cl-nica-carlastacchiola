from models.paciente import Paciente
from models.medico import Medico
from models.especialidad import Especialidad
from models.clinica import Clinica
from models.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException,
    DiaInvalidoException
)
from datetime import datetime


def input_no_vacio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("⚠️ Error: Este campo no puede estar vacío. Intentelo de nuevo.")

clinica = Clinica()

def menu():
    print("\n--- Sistema de Gestión Clínica ---")
    print("1. Agregar paciente")
    print("2. Agregar médico")
    print("3. Agendar turno")
    print("4. Agregrar especialidad")
    print("5. Emitir receta")
    print("6. Ver historia clínica")
    print("7. Ver todos los turnos")
    print("8. Ver todos los pacientes")
    print("9. Ver todos los médicos")
    print("0. Salir")

def agregar_paciente():
    print("--- Agregar paciente ---")
    
    try:
        nombre = input_no_vacio("Nombre: ")
        apellido = input_no_vacio("Apellido: ")
        dni = input_no_vacio("DNI: ")

        while True:
            fecha_nacimiento = input("Fecha de nacimiento (dd/mm/yyyy): ")
            try:
                datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
                break
            except ValueError as e:
                print("⚠️ Error: La fecha de nacimiento debe tener el formato dd/mm/yyyy. Intente nuevamente.")

                

        paciente = Paciente(nombre, apellido, dni, fecha_nacimiento)
        clinica.agregar_paciente(paciente)
        print("✅ Paciente agregado correctamente.")

    except ValueError as e:
        print("⚠️ Error:", e)
      

def agregar_medico():
    print("--- Agregar médico ---")
    try:
        nombre = input_no_vacio("Nombre del médico: ")
        apellido = input_no_vacio("Apellido del médico: ")
        matricula = input_no_vacio("Matrícula: ")
        especialidad = input_no_vacio("Especialidad: ")
        dias = input_no_vacio("Días de atención (separados por coma, ej: lunes,miércoles): ").split(",")
        esp = Especialidad(especialidad, [d.strip() for d in dias])
        medico = Medico(nombre, apellido, matricula, [esp])
        clinica.agregar_medico(medico)
        print("✅ Médico agregado correctamente.")
    except ValueError as e:
        print("⚠️ Error:", e)

def agendar_turno():
    print("--- Agendar turno ---")
    
    dni = input_no_vacio("DNI del paciente: ")
    matricula = input_no_vacio("Matrícula del médico: ")
    especialidad = input_no_vacio("Especialidad: ")

    while True:
        try:

            fecha_str = input_no_vacio("Fecha y hora del turno (formato: YYYY-MM-DD HH:MM): ")
            fecha_hora = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
            clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
            print("✅ Turno agendado correctamente.")
            break
        except (MedicoNoDisponibleException, DiaInvalidoException) as e:
            print("⚠️", e)
            print("Intente con otra fecha y hora")
        except (PacienteNoEncontradoException, MedicoNoEncontradoException, TurnoOcupadoException) as e:
            print("⚠️", e)
            break
        except ValueError as e:
            print("⚠️ Formato de fecha inválido. Debe ser YYYY-MM-DD HH:MM.")


def agregar_especialidad():
    print("--- Agregar especialidad a un médico ---")
    try:
        matricula = input_no_vacio("Matrícula del médico: ")
        medico = clinica.obtener_medico_por_matricula(matricula)

        nombre_especialidad = input_no_vacio("Nombre de la nueva especialidad: ")
        dias_raw = input_no_vacio("Días de atención (separados por coma, ej: lunes,miércoles): ")
        dias = [d.strip() for d in dias_raw.split(",") if d.strip()]
        especialidad = Especialidad(nombre_especialidad, dias)

        medico.agregar_especialidad(especialidad)
        print("✅ Especialidad agregada correctamente.")

    except MedicoNoEncontradoException as e:
        print("⚠️", e)
    except ValueError as e:
        print("⚠️ Error:", e)


def emitir_receta():
    print("--- Emitir receta ---")
    try:
        dni = input_no_vacio("DNI del paciente: ")
        matricula = input_no_vacio("Matrícula del médico: ")
        medicamentos = input_no_vacio("Medicamentos (separados por coma): ").split(",")
        clinica.emitir_receta(dni, matricula, [m.strip() for m in medicamentos])
        print("✅ Receta emitida correctamente.")
    except (PacienteNoEncontradoException, MedicoNoEncontradoException, RecetaInvalidaException) as e:
        print("⚠️", e)

def ver_historia_clinica():
    print("--- Ver historia clínica ---")
    try:
        dni = input_no_vacio("DNI del paciente: ")
        historia = clinica.obtener_historia_clinica_por_dni(dni)
        if historia:
            print(historia)
        else:
            raise PacienteNoEncontradoException(dni)
    except PacienteNoEncontradoException as e:
        print("⚠️", e)

def ver_todos_los_turnos():
    print("--- Todos los turnos ---")
    turnos = clinica.obtener_turnos()
    if turnos:
        for turno in turnos:
            print(turno)
    else:
        print("No hay turnos registrados.")

def ver_todos_los_pacientes():
    print("--- Todos los pacientes ---")
    pacientes = clinica.obtener_pacientes()
    if pacientes:
        for paciente in pacientes:
            print(paciente)
    else:
        print("No hay pacientes registrados.")

def ver_todos_los_medicos():
    print("--- Todos los médicos ---")
    medicos = clinica.obtener_medicos()
    if medicos:
        for medico in medicos:
            print(medico)
    else:
        print("📭 No hay médicos registrados.")



def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_paciente()
        elif opcion == "2":
            agregar_medico()
        elif opcion == "3":
            agendar_turno()
        elif opcion == "4":
            agregar_especialidad()
        elif opcion == "5":
            emitir_receta()
        elif opcion == "6":
            ver_historia_clinica()
        elif opcion == "7":
            ver_todos_los_turnos()
        elif opcion == "8":
            ver_todos_los_pacientes()
        elif opcion == "9":
            ver_todos_los_medicos()
        elif opcion == "0":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción inválida. Intente nuevamente.")



if __name__ == "__main__":
    main()
