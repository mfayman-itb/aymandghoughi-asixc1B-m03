#region constants & variables
LOGIN = 'retigga'
PASS = '010'
ME = ("""\
          _.-*'""'*-._
       .-"            "-.
     ,"                  ",
   .'      _.-.--.-._      ',
  /     .-'.-"    "-.'-.     \
 /     /  /"'-.  .-'"\  \     \
:     :  :     ;:     ;  ;     ;
;     :  ; *   !! *   :  ;     :
;      ; :   .'  '.   ; :      :
:       \ \-'      '-/ /       ;
 \       '.'-_    _-'.'       /
  \        '*-"-+"-*'        /
   '.          /|          .'
     *,       / |        ,*
     / '-_            _-'  \
    /     "*-.____.-*"      \
   /            |            \
  :    :        |        ;    ;
  |.--.;        |        :.--.|
  (   ()        |        ()   )
   '--^_        |        _^--'
      | "'*--.._I_..--*'" |
      | __..._  | _..._   |
     .'"      `"'"     ''"'.
""")
SECRET_USR = 'usuari1'
SECRET_PASSW = 'asdasd'
#endregion

#region functions
def setLogin():
    log = input('login: ')
    passw = input('password: ')
    trys = int(input('try: '))
    return log, passw, trys
def verification(login, passw):
    count = 0
    while True:
        if count != trys:
            if login == LOGIN and passw == PASS and count > trys:
                print('¡Benvingut al Sistema!')
                print(ME)
            elif login != LOGIN or passw != PASS or count == trys:
                print('Error: user name or paswword not correct')
                count += 1
        else:
            print('Error: not more trys')
def easter_egg():
    if login == SECRET_USR and passw == SECRET_PASSW and count != trys:
        return True
    else:
        return False
#endregion

#region main
setLogin()
verification()
easter_egg()
#endregion