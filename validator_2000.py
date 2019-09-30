list_options = """01 - Coletor | 02 - CAN: """
option = str(input(list_options)).upper()

if option == 'CAN' or '2' or '02':
    print('Aplicar macro: Solicitar - Kit CAN completo')

if option == 'Coletor' or '1' or '02':
    print('')