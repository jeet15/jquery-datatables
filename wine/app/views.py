from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, View, RedirectView
from django.template.loader import render_to_string
from django.middleware.csrf import get_token
#from braces.views import CsrfExemptMixin, JsonRequestResponseMixin

from models import Car
from utils import CarList, ManageCar, ManageUser 
import json

from libs.jsonresponse import JSONResponseMixin

class HomeView(TemplateView):

    template_name = 'app/home.html'

    def get_context_data(self,**kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['menu'] = 'home'
        return context

class APIView(View, JSONResponseMixin, CarList ):

    template_name = 'app/car.html'

    def get(self, request, *args, **kwargs):
        context = { 'cars': self.get_list() }
        data = {'html': render_to_string(self.template_name, context) }
        data['status'] = 1
        return self.render_to_response(data)

class JhtmlView(TemplateView, ManageCar):

    template_name = 'app/JHtml.html'

    def get_context_data(self,**kwargs):
        context = super(JhtmlView, self).get_context_data(**kwargs)
        context['menu'] = 'jhtml'
        return context


class AddUserView(View, JSONResponseMixin , ManageCar):
    template_name = 'app/add.html'

    def get(self, request, *args, **kwargs):
        data = {}
        form_car = self.car_form()
        context = {'action':'add','form' : form_car, 'csrf_token_value': get_token(self.request)}
        data['html'] = render_to_string(self.template_name, context)
        return self.render_to_response(data)

class SampleView(TemplateView):
    template_name = 'app/sample.html'

    def get_context_data(self, **kwargs):
        context = super(SampleView, self). get_context_data(**kwargs)
        context['menu'] = 'sample'
        return context
 
class ValidationView(TemplateView):
    template_name = 'app/jvalid.html'

    def get_context_data(self,**kwargs):
        context = super(ValidationView, self).get_context_data(**kwargs)
        context['menu'] = 'jhtml'
        return context


class UserView(View, JSONResponseMixin, ManageUser):
    template_name = 'app/user.html'

    def get(self, request, *args, **kwargs):
        data = {}
        user_form = self.get_form()
        context = {'action':'add','form' : user_form, 'csrf_token_value':get_token(self.request)}
        data['html'] = render_to_string(self.template_name, context)
        return self.render_to_response(data)

    def post(self, request, *args, **kwargs):
        data = {}
        dt = self.save_form(self.request)
        data['status'] = (0,1)[dt[0]]
        data['message'] = dt[1]
        return self.render_to_response(data)

class JqueryView(TemplateView):

    template_name = 'app/jquery.html'

    def get_context_data(self,**kwargs):
        context = super(JqueryView, self).get_context_data(**kwargs)
        context['menu'] = 'jquery'
        return context

class UserListView(View, JSONResponseMixin, ManageUser):
    template_name = 'app/alluser.html'

    def get(self, request, *args, **kwargs):
        user =  self.get_list()
        data = {}
        if user:
            data['status'] = 1
        else:
            data['status'] = 0
            data['message'] = "No User Exist Please add atleast one User."
        data['html'] = render_to_string(self.template_name, {'user':user})
        return self.render_to_response(data)

class EditView(View, JSONResponseMixin, ManageUser):

    template_name = 'app/add.html'

    def get(self, request, *args, **kwargs):
        data = {}
        user_id = self.request.GET.get('user_id')
        edit_form = self.edit_user(user_id)
        context = {'action':'edit', 'csrf_token_value': get_token(self.request)}
        data['status'] = edit_form['status']
        if data['status']:
            context['form'] = edit_form['form']
        else:
            data['message'] = edit_form['message']
        data['html'] = render_to_string(self.template_name, context)
        return self.render_to_response(data)

    def post(self, request, *args, **kwargs):
        data = self.update_user(self.request.POST)
        return self.render_to_response(data)

              
class DeleteView(View, JSONResponseMixin, ManageUser):
    '''
    @summary: Delete User
    '''
    def get(self, request, *args, **kwargs):
        user_id = self.request.GET.get('user_id')
        data = self.delete_user(user_id)
        return self.render_to_response(data)

