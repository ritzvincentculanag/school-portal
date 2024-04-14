from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from staffs.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'is_staff',
            'utype',
            'subjects'
        )


class CustomUserUpdateForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'is_staff',
            'utype',
            'subjects'
        )
