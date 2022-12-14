from dataclasses import fields
from django import forms
from users import models as user_models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = user_models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except user_models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))



# class SignUpForm(forms.ModelForm):
#     class Meta:
#         model = user_models.User
#         fields = ["first_name", "last_name", "email"]

#     password = forms.CharField(widget=forms.PasswordInput)
#     password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

#     def clean_password1(self):
#         password = self.cleaned_data.get("password")
#         password1 = self.cleaned_data.get("password1")

#         if password != password1:
#             raise forms.ValidationError("Password confirmation does not match")
#         else:
#             return password
    
#     def save(self, *args, **kwargs):
#         user = super().save(commit=False)
#         email = self.cleaned_data.get("email")
#         password = self.cleaned_data.get("password")
#         user.username = email
#         user.set_password(password)
#         user.save()


class SignUpForm(forms.Form):

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            user_models.User.objects.get(email=email)
            raise forms.ValidationError("User already exists with that email")
        except user_models.User.DoesNotExist:
            return email
    
    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password
    

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        print(self.cleaned_data)
        user = user_models.User.objects.create_user(email, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
