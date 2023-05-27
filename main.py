import instaloader

username = input('enter username:')
password = input('enter password:')
try:
    loader = instaloader.Instaloader()
    loader.login(username, password)
    print("Login successful!")
except instaloader.exceptions.TwoFactorAuthRequiredException:
    tfa_code = input("Enter 2FA code: ")
    loader.two_factor_login(tfa_code)
    print("2FA login successful!")
except instaloader.exceptions.BadCredentialsException:
    print("Invalid username or password.")
#Since im lazy and dont wanna work w dictionaries, and since its gonna be simply 7 elems of data i work w.
'''
0:username
1:userID
2:Mediacount
3: followers
4: followees
5.Bio
6:external url
'''
def get_basic_info(usrname_tar):
    profile = instaloader.Profile.from_username(loader.context, usrname_tar)
    comp_data = {'username:':profile.username,'user_id':profile.userid,'media_count':profile.mediacount,'follower_count' : profile.followers,'following_count':profile.followees,'bio':profile.biography,'external_url': profile.external_url}
    return comp_data
print(get_basic_info('usrname'))