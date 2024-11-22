def solution(id_pw, db):
    

    for each in db :
        if id_pw == each : return "login"
    
        elif id_pw[0]==each[0] and id_pw[1] != each[1] : return "wrong pw"
    
    return "fail"
    
    