from django.views.generic.detail import DetailView
from webpage.models import UserFile
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate

from .models import PatientProfile, UserFile
from .forms import CreatePatientForm, CreateUserForm

members = [
    {
        "name": "Mireya Paredes",
        "image": "mireya-paredes.jpg",
        "bio": """La Dra. Mireya Paredes hizo su doctorado en Ciencias de la Computación en la Universidad
                        de Manchester en Reino Unido. Actualmente es profesora en la Universidad de las Américas
                        Puebla y pertenece al Sistema Nacional de Investigadores nivel Candidato. Sus líneas de
                        investigación son programación paralela, algoritmos de grafos y cómputo cuántico. Sus intereses son
                        proyectos multidisciplinarios de tecnología que lleguen a tener un impacto social en la sociedad
                        mexicana.""",
    },
    {
        "name": "José Correa",
        "image": "jose-correa.jpg",
        "bio": """Licenciatura en Medicina en la Escuela Superior de Medicina (ESM) del IPN en el 2002.
                        Maestría en Ciencias en Farmacología en la ESM del IPN en 2004. Doctorado en
                        Investigación en Medicina en la ESM del IPN, siendo premio como mejor tesis del IPN en
                        2006. Maestría en Bioinformática, modalidad “on line” en la Universidad Internacional de
                        Andalucia, España, 2013. Actualmente es Profesor-Investigador Titular C de la ESM del
                        IPN. Pertenece al Registro CONACYT de Evaluadores Acreditados. Es miembro del sistema
                        Nacional de Investigadores (SNI) desde 2007 como candidato, actualmente es nivel 3.
                        Tiene 3 patentes aceptadas, 2 patentes con examen de forma aceptado en el IMPI y 4 están
                        en evaluación. Ha realizado 3 diplomados. Realizó también una estancia como Profesor
                        Invitado en la Universidad de Evry Francia en el 2013. Tiene 182 artículos científicos
                        en revistas internacionales (JCR) y 6 no JCR, los cuales han generado más de 2002 citas
                        en google scholar con un Reseachgate 43.05. Ha publicado 11 capítulos de libros
                        internacionales de editoriales de prestigio. Varios trabajos en congresos nacionales e
                        internacionales. Ha supervisado 4 estancias posdoctorales y 60 tesis (12 de doctorado,
                        31 de Maestría y 25 de licenciatura y 4 de especialidad médica). Ha impartido más de 40
                        cursos de posgrado y de pregrado. Ha conseguido más de 10 proyectos con financiamiento
                        por CONACYT, ICyTDF, CYTED, 7 como responsable técnico, tanto nacionales como
                        internacionales. En el 2010 fue galardonado con el premio: Miguel Alemán en salud. Ha
                        sido asesor de alumnos que han recibido el premio como mejor tesis en el IPN. En el 2014
                        el recibió el premio a la investigación en el IPN. En el 2018 fue Presea Lázaro Cárdenas
                        en Modalidad de Profesor-Investigador, premio que entrega el Presidente de la República
                        Mexicana. En el 2019 obtuvo el 3er lugar de CANIFARMA, CATEGORÍA DE INVESTIGACIÓN
                        TECNOLÓGICA.""",
    },
    {
        "name": "Chema",
        "image": "chema.jpg",
        "bio": """Chema obtuvo su PhD en la Universidad de Barcelona estudiando el desarrollo embrionario
                        de las planarias (gusanos planos). Tras su doctorado, hizo una estancia postdoctoral en
                        Bergen, Noruega, bajo la dirección de Prof Andreas Hejnol en el Instituto Sars para la
                        Biología Molecular Marina, donde estudio una gran variedad de animales marinos
                        invertebrados. En particular, Chema se centro en el estudio de la evolución del sistema
                        digestivo y la gastrulacion en animals y en el origen del sistema nervioso. En 2018,
                        empezó una posición como investigador independiente en la Universidad de Londres Queen
                        Mary. En 2019 recibió la prestigiosa grant ERC Starting Grant para explorar la evolución
                        y control molecular del desarrollo espiral.""",
    },
]

# Create your views here.


class SiteView(CreateView):
    template_name = "webpage/index.html"
    model = UserFile
    fields = "__all__"
    success_url = "/BCDSaliva"

    

class IndexView(TemplateView):
    template_name = "webpage/index.html"
    
class BiomarkerComparisonView(TemplateView):
    template_name = "webpage/biomarker_comparison.html"
    
class MedicalInformationNoLoginView(TemplateView):
    template_name = "webpage/patients_nologin.html"
    
class MedicalInformationView(DetailView):
    model = PatientProfile
    template_name = "webpage/patients.html"
    
    def get_context_data(self, **kwargs):
        context = super(MedicalInformationView, self).get_context_data(**kwargs)
        page_user = get_object_or_404(PatientProfile, id=self.kwargs["pk"])
        context["page_user"] = page_user
        return context
    
class AboutUsView(TemplateView):
    template_name = "webpage/about_us.html"
    
    # Regresa contexto para renderizar en la pagina, en este caso el diccionario de miembros
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_members"] = members
        return context
    
# TODO: Make into a class-based view (if possible)
def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("webpage:home")
        
        messages.info(request, _("Username or password is incorrect"))
    
    context = {}
    return render(request, "webpage/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect("webpage:login")
    
# TODO: Make into a class-based view
def signupView(request):
    if request.method == "POST":
        user_form = CreateUserForm(request.POST)
        patient_form = CreatePatientForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            new_user = user_form.save()
            #https://stackoverflow.com/questions/41649976/django-exception-value-1048-column-user-id-cannot-be-null
            #new_patient = patient_form.save()
            new_patient = patient_form.save(commit=False)
            if new_patient.user_id is None:
                new_patient.user_id = new_user.id
            new_patient.save()
            username = user_form.cleaned_data.get("username")
            messages.success(request, _("Account for " + username + " created correctly"))
            return redirect("webpage:login")
        
    else:
        user_form = CreateUserForm()
        patient_form = CreatePatientForm()
    
    context = {"user_form":user_form, "patient_form":patient_form}
    
    return render(request, "webpage/signup.html", context)
    

class DonateView(TemplateView):
    template_name = "webpage/donate.html"
    

class PrivacyPolicyView(TemplateView):
    template_name = "webpage/privacy_policy.html"
    
class ShowProfilePageView(DetailView):
    model = PatientProfile
    template_name = "webpage/user_profile.html"
    
    def get_context_data(self, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        page_user = get_object_or_404(PatientProfile, id=self.kwargs["pk"])
        context["page_user"] = page_user
        return context
class EditProfilePageView(generic.UpdateView):
    model = PatientProfile
    template_name = "webpage/edit_profile_page.html"
    fields = ["name", "surname_1", "surname_2", "date_of_birth", "gender", \
              "level_of_education", "country", "state", "occupation", \
              "monthly_income", "phone_number" ]
    success_url = reverse_lazy("home")
    
    def get_context_data(self, **kwargs):
        context = super(EditProfilePageView, self).get_context_data(**kwargs)
        page_user = get_object_or_404(PatientProfile, id=self.kwargs["pk"])
        context["page_user"] = page_user
        return context
