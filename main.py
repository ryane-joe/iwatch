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
def get_basic_info(usrname_tar):
    profile = instaloader.Profile.from_username(loader.context, usrname_tar)
    comp_data = {'username:':profile.username,'user_id':profile.userid,'media_count':profile.mediacount,'follower_count' : profile.followers,'following_count':profile.followees,'bio':profile.biography,'external_url': profile.external_url}
    return comp_data
def download_posts(usrname_tar):
    profile = instaloader.Profile.from_username(loader.context, usrname_tar)
    profile.get_posts()
    

download_posts('ryanejoe_')