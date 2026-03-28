# async def verify_password(plain_password, hashed_password):
#     return plain_password == hashed_password

# async def authenticate_user(username: str, password: str):
#    user = await User.get(username = username)

#    if user and verify_password(password, user.password):
#        return user

# async def token_generator(username: str, password: str):
    # user = await authenticate_user(username, password)