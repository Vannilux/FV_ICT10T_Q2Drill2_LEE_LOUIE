from pyscript import document

list1 = ["Edrian Correa","Cheree Mendoza","Alexa Cunanan","Carlos Borromeo","Jericho Magsalin","Eran Diaz","Louie Lee"]

def member_check(e):
    first_name = document.getElementById("input1").value.strip().title()
    last_name = document.getElementById("input2").value.strip().title()
    full_name = first_name + " " + last_name

    message = {
        True: "congratulations! You have been accepted into the SOCSCI Club!",
        False: "sorry, you have not been accepted into the SOCSCI Club."
    }[full_name in list1]

    document.getElementById("result").innerText = full_name + ", " + message