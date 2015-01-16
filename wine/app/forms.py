from django import forms
from models import Car, User

class CarForm(forms.Form):
    name = forms.CharField(label='Name Of Car', widget = forms.TextInput())
    image = forms.ImageField(label = 'Upload Car Image')

    def save(self):
        data = self.cleaned_data
        car_data = Car(name = data['name'], image= data['image'])
        car_data.save()
        return True

class UserForm(forms.Form):
    user_id = forms.CharField(widget= forms.HiddenInput(), required= False)
    name = forms.CharField(label = 'Name' , widget= forms.TextInput())
    email = forms.CharField(label='Email', widget=forms.EmailInput())
    username = forms.CharField(label = 'username', widget= forms.TextInput())

    def clean(self):
        data = self.cleaned_data
        email = data.get('email')
        if User.objects.filter(email=email).count()>0:
            raise forms.ValidationError('email already exist!!')
        return data

    def save(self):
        data = self.cleaned_data
        user_data = User(name = data['name'], email = data['email'], username = data['username'])
        user_data.save()
        return True

    def update(self):
        data = self.cleaned_data
        user = User.objects.filter(id = data['user_id'])
        if user:
            user = user[0]
            user.name = data['name']
            user.email = data['email']
            user.save()
            return {'status': 1, 'message': 'User Updated successfully'}
        else:
            return {'status': 0, 'message': 'User does not exist.'}
