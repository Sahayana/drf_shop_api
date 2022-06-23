from rest_framework.test import APITransactionTestCase, APIClient
from account.models import CustomUser
from account.services.customuser_service import create_single_user




class CustomUserViewTest(APITransactionTestCase):

    def setUp(self) -> None:
        self.info = {
            "username":"testuser2",
            "email":"testuser2@testuser.com",
            "phone":"01056103812",
            "fullname":"테스터",
            "password":"testuser2@"
        }
        
        self.client = APIClient()


    def test_user_can_create_single_user(self):
        
        # Given
        info = self.info

        # When
        res = self.client.post(
            path="/api/accounts",
            data=info
        )

        # Then
        self.assertEqual(201, res.status_code)
        self.assertEqual(
            info["username"],
            CustomUser.objects.first().username            
            )
        self.assertEqual(1, CustomUser.objects.count())
    

    def test_user_never_create_user_with_invalid_info(self):

        # Given
        info = self.info

        # Case 1: invalid email
        invalid_email = "testuser#test.com"
        info["email"] = invalid_email

        # When
        res = self.client.post(
            path="/api/accounts",
            data=info
        )

        # Then
        self.assertEqual(400, res.status_code)       
        self.assertEqual(0, CustomUser.objects.count())
        self.assertIn("email", res.data)    # EmailField에서 이미 검사하기 때문에 error가 아닌 email로 detail 표현


        # Case 2: invalid password
        info["email"] = "testuser@test.com"
        invalid_password = "password4"
        info["password"] = invalid_password

        # When
        res = self.client.post(
            path="/api/accounts",
            data=info
        )

        # Then
        self.assertEqual(400, res.status_code)       
        self.assertEqual(0, CustomUser.objects.count())
        self.assertIn("error", res.data)

        # Case 3: invalid phone
        info["password"] = "password4@"
        invalid_phone = "0105984578a"
        info["phone"] = invalid_phone

        # When
        res = self.client.post(
            path="/api/accounts",
            data=info
        )

        # Then
        self.assertEqual(400, res.status_code)       
        self.assertEqual(0, CustomUser.objects.count())
        self.assertIn("error", res.data)
    

    def test_valid_user_can_obtain_token(self):

        # Given
        info = self.info
        user = create_single_user(**info)        
        data = {
            "username": user.username,
            "password": "testuser2@"
        }

        # When
        res = self.client.post(
            path="/api/accounts/token",
            data=data
        )

        # Then
        self.assertEqual(200, res.status_code)
        self.assertIsNotNone(res.data["access"])

    
    def test_unvalid_user_never_obtain_token(self):

        # Given
        info = self.info
        user = create_single_user(**info)        
        data = {
            "username": user.username,
            "password": "unvaliduser@2"
        }

        # When
        res = self.client.post(
            path="/api/accounts/token",
            data=data
        )

        # Then
        self.assertEqual(401, res.status_code)  # Unauthorized
        