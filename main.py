from pyscript import document

def add_member(e):
    first_name = document.getElementById("input1").value.strip().title()
    last_name = document.getElementById("input2").value.strip().title()
    full_name = first_name + " " + last_name #combine fname and lname to create full name

    Grade7 = {"Li Hansen", "Samuel Lee", "Maria Cruz"}
    Grade8 = {"Tian Gotsap", "Earl Jung", "Jack Ere", "Yosef Kim"}
    Grade9 = {"Akira Masato", "Kim Il-Park"}
    Grade10 = {"Krum Despina", "Sofia Martinez", "John Sakazuki", "Nakamura Hiroshi"}

    student_list = Grade7|Grade8|Grade9|Grade10|{full_name} # combines list of all students in the club
    document.getElementById("result").textContent = f"Total members: {len(student_list)}"

    student_list = "<br>".join(sorted(student_list)) # lists and sorts the names of the students in the club by alphabetical order

    document.getElementById("result").innerHTML += f"<br>{student_list}" #add the sorted list of students to the result div


   
