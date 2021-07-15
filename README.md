# converter
Программа для преобразования файлов .py в .exe
!!! Не работает без предустановки python в систему !!!

Начните работу с запуска cnv.exe.
Использует библиотеку tkinter для формирования графического интерфейса, содержит консоль для просмотра процесса формирования exe файла в режиме реального времени.
Включает в себя проверку введенных пользователем данных на каждом шаге, что исключает возможность появления ошибки, потому что программа тестировалась на протяжении нескольких лет.

Программа позволяет:
1) Добавлять иконки в формате .ico к создаваемой программе;
2) Преобразовывать программы, использующие картинки (для таких библиотек, как tkinter или pygame), включая их в готовую сборку - таким образом картинки добавляются к exe файлу, не требующему каких-либо дополнительных файлов для корректной работы;
3) Скрывать консоль для программ, использующих библиотеки, которым при запуске она не нужна, так как работа проходит в отдельном окне (например, для tkinter);
4) Автоматически добавлять к программам, использующим консоль, строку input(), заставляющую программу не завершать свою работу сразу после выполнения и позволяющую таким образом пользователю просмотреть результат выполнения программы.
