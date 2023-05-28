import instaloader
usr = input('enter target username:')
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
    compa_data = {'username':profile.username,'user_id':profile.userid,'media_count':profile.mediacount,'follower_count' : profile.followers,'following_count':profile.followees,'bio':profile.biography,'external_url': profile.external_url}
    return compa_data
import instaloader

def download_posts_and_reels(username):
    profile = instaloader.Profile.from_username(loader.context, username)
    posts = profile.get_posts()
    for index, post in enumerate(posts,1):
        loader.download_post(post, target=f"{profile.username}_{index}")

while True:
    if "comp_data" not in globals():
        comp_data = get_basic_info(usr)
        print('recived original data')
        print('username:',comp_data['username'])
        print('userdata:',comp_data['user_id'])
        print('mediacount',comp_data['media_count'])
        print('follower count:',comp_data['follower_count'])
        print('following count:',comp_data['following_count'])
        print('bio:',comp_data['bio'])
        print('external link:',comp_data['external_url'])
    elif "comp_data" in globals():
        print('not implemented')
        break
