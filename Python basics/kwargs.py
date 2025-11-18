def profile(**kwargs):
    print("User Profile")
    for k,v in kwargs.items():
        print(f"{k}={v}")

profile(name="vaithi",age=21,job="DATA SCIENTIST")