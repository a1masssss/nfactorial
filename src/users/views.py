from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from users.forms import UserAuthenticationForm, UserRegisterForm
from django.views.generic import FormView  
from django.contrib.auth import authenticate, login

class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Your Fortnite account was created successfully"

class CustomLoginView(FormView):
    template_name = 'login.html'
    form_class = UserAuthenticationForm
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, password = password)
        
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid email or password.')
            return self.form_invalid(form)
