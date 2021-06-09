import sqlite3
import itertools

con = sqlite3.connect("myDB")
cursor = con.cursor()
cursor.execute("SELECT sec_key FROM ugroup")
query = cursor.fetchall()
list_of_keys = []
for k in query:
    list_of_keys.append(k[0])
print(list_of_keys )
program = True
while program:
    print('Введите \'exit\', чтобы выйти!')
    key = input('Введите ключ группы\n')
    if key == 'exit':
        program = False
        break
    if not key in list_of_keys:
        print('Группы с таким ключом не существует')
        continue
    cursor.execute(f'SELECT id FROM ugroup WHERE sec_key=\"{key}\"')
    id = cursor.fetchall()[0][0]
    cursor.execute(f'SELECT * FROM student WHERE id=\"{id}\"')
    group = cursor.fetchall()
    for stud in group:
        print(stud)
    id_of_student = 1
    student_input_mode = True
    while student_input_mode:
        try:
            id_of_student = int(input('Введите id студента'))
            if id_of_student-1<len(group):
                student_input_mode = False
            else:
                raise Exception('Нет такого чувака!')
        except:
            print('Вводите число')
    current_student = group[0]
    for st in group:
        if st[0]==id_of_student:
            current_student = st
    cursor.execute(f"SELECT vremya.time, vremya.kabinet, den.den"+
                                "  FROM vremya join den "+
                                "  on vremya.den_id = den.id"+
                                "  join rezhim_mid"+
                                "  on den.rezhim_id = rezhim_mid.id"+
                                f"  where rezhim_mid.id = {current_student[6]}"
    )
    raspisanie = cursor.fetchall()
    itertools.groupby(raspisanie, lambda x: x[2])
    print(raspisanie)


