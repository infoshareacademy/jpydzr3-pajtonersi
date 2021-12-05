from users.user_services import UserServices


def test_print_menu_admin(doctor1, capsys):
    us = UserServices(doctor1)
    us.print_menu()
    assert '1. Dodaj pacjenta\n2. Zaplanuj wizyte\n3. Zaplanuj badanie\n4. Zarządzanie dostępnością lekarzy\n5. Wybierz pakiet medyczny\n6. Wyjście z programu\n1. Dodaj pacjenta\n2. Zaplanuj wizyte\n3. Zaplanuj badanie\n4. Zarządzanie dostępnością lekarzy\n5. Wybierz pakiet medyczny\n6. Wyjście z programu\n' == capsys.readouterr().out
