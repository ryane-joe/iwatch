import instaloader

def login(username, password):
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

# Usage
username = "ryanesalt"
password = "Jacob2755"

login(username, password)
loader = instaloader.Instaloader()
profile = instaloader.Profile.from_username(loader.context, 'ryanejoe_')
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers Count: ", profile.followers)
print("Following Count: ", profile.followees)
print("Bio: ", profile.biography)
print("External URL: ", profile.external_url)
