from django.contrib.auth import get_user_model
from factory import Faker, PostGenerationMethodCall
from factory.django import DjangoModelFactory


UserModel = get_user_model()


class UserFactory(DjangoModelFactory):

    email = Faker("email")
    password = PostGenerationMethodCall('set_password', 'test')
    is_active = True
    is_superuser = True

    class Meta:
        model = UserModel
