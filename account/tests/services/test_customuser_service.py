from rest_framework.test import APITransactionTestCase
from account.models import CustomUser
from account.services.customuser_service import create_single_user



class CustomUserServiceTest(APITransactionTestCase):

    def setUp(self) -> None:
        self.info = {
            "username":"testuser",
            "email":"testuser@testuser.com",
            "phone":"01056103812",
            "fullname":"테스터",
            "password":"testuser@"
        }
    
    
    def test_user_can_creat_single_user(self):

        # Given
        data = self.info

        # When
        user = create_single_user(**data)

        # Then
        self.assertIsNotNone(user)
        self.assertEqual(data["username"], user.username)
        self.assertEqual(1, CustomUser.objects.count())
        
