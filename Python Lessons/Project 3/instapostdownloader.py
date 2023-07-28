import instaloader
ig = instaloader.instaloader()
dp = input("Enter Insta Username : ")
ig.download_profile(dp, profile_pic_only = True)