import instaloader
def login(usrname_attk,passwd_attk):
    try:
        instaloader.Instaloader().login(usrname_attk,passwd_attk)
    except:
        tfa_code_attk = input('enter 2fa code:')
        instaloader.Instaloader.two_factor_login(tfa_code_attk)