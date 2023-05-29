import instaloader
import csv
import os
import time
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
def check_for_changes(comp_data,newdata,poss):
    newdata = get_basic_info(loader, username)
    if newdata != comp_data:
        print("Changes detected:")
        for key in newdata:
            if newdata[key] != comp_data[key]:
                print(f"{key}: {comp_data[key]} -> {newdata[key]}")
                if poss == True and key == 'media_count':
                    download_posts_and_reels(usr)
def write_file(fil, co,new):
    header = ['username','userID','media_count','follower_count','following_count','bio','externalurl']
    if new == True:
        with open(fil,'w') as compE:
            for i in range(6):
                writer = csv.writer(compE)
                writer.writerow(header)
                writer.writerows(co)
    else:
        with open(fil,'a') as compE:
            for i in range(6):
                writer = csv.writer(compE)
                writer.writerow(header)
                writer.writerows(co)
def Latest_data_show(comp_data):
    print('LATEST DATA')
    print('username:',comp_data['username'])
    print('userID:',comp_data['user_id'])
    print('mediacount',comp_data['media_count'])
    print('follower count:',comp_data['follower_count'])
    print('following count:',comp_data['following_count'])
    print('bio:',comp_data['bio'])
    print('external link:',comp_data['external_url'])
def retrive_comp_data(filen):
    pass
while True:
    if os.path.isfile('comp__'):
        m = get_basic_info(usr)
        print('LATEST DATA:')
        Latest_data_show(m)
        comp_data = retrive_comp_data('comp__')
        if m != comp_data:
            check_for_changes(comp_data,m)
            print('updated comparison data')
            write_file('comp__',m,False)
            print('updated comp file')
        else:
            print('no changes detected')
    else:
        m = get_basic_info(usr)
        print('detected no comparision save file')
        Latest_data_show(m)
        write_file('comp__',m,True)
        print('written new comparsion data file')
    print('monitoring loop started')
    time.sleep(60)


    