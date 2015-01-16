from django.core.urlresolvers import reverse
from models import Car, User

from forms import CarForm, UserForm


class CarList():
    def get_list(self):
        return Car.objects.all().order_by('name')


class ManageCar(object):
    def car_form(self):
        form = CarForm()
        return form



class ManageUser(object):
    def get_form(self):
        form = UserForm()
        return form
    
    def save_form(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            return [form.save(), 'User Added successfully.']
        else:
            return [False, ', '.join(form.errors.values()[0])]

    def get_list(self):
        return User.objects.all().order_by('-id')

    def edit_user (self, user_id):
        data = {}
        info = User.objects.filter(id = user_id)
        if info:
            info = info[0]
            form = UserForm({
                'user_id': info.id,
                'name':info.name,
                'email': info.email,
                })
            data['status'] = 1
            data['form'] = form
        else:
            data['status'] = 0
            data['message'] = 'User does not exist.'
        return data
        
    def delete_user (self, user_id):
        data = {}
        user = User.objects.filter(id = user_id)
        if user:
            user.delete()
            data['status'] = 1
            data['message'] = 'User has been deleted successfully'
        else:
            data['status'] = 0
            data['message'] = 'User does not exist. Please try again'
        return data

    def update_user (self, data):
        if data:
            form = UserForm(data)
            if form.is_valid():
                return form.update()
        return {'status': 0, 'error': form.errors, 'message': 'Form submitted with invalid data. Please try again.' }
        