from account.models import CustomUser

def create_single_user(username:str, password:str, email:str, fullname: str, phone: str):
    return CustomUser.objects.create_user(
        username=username,
        password=password,
        email=email,
        fullname=fullname,
        phone=phone
    )
