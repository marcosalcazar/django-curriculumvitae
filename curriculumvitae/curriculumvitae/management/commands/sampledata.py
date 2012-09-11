# -*- coding: utf-8 *-*
import datetime
from django.core.management.base import NoArgsCommand

from curriculumvitae.models import Person, ExperienceGroup, ExperienceItem, \
    LineItem, Style


class Command(NoArgsCommand):
    help = "Fill the database with sample data (English and Spanish only)"

    def handle_noargs(self, **options):

        cvs = Style.objects.get(pk=1)

        print "Creating a person:"
        p = Person.objects.create(
            first_name='Jhon',
            last_name='Doe',
            short_description_en='A very good person',
            short_description_es='Una buena persona',
            address='97 Evergreen Av.',
            email='jhon.doe@youremail.com',
            phone='0321-123456321',
            mugshot='mugshots/sampleimage.jpg',
            curriculum_vitae_style=cvs
        )

        print "Creating education history"
        exp_edu = ExperienceGroup.objects.create(
            person=p,
            name_en=u'Education',
            name_es=u'Educación',
            order=1
        )
        ExperienceItem.objects.create(
            experience_type=exp_edu,
            title_en='High School',
            title_es='Colegio Secundario',
            subtitle_en='Tecnical Orientation',
            subtitle_es=u'Orientación Técnica',
            url='http://www.somefancyhighschoolwebpage.com',
            location=u'Tunuyán, Mendoza, Argentina',
            description_en='I got a very high degree at high school',
            description_es='Obtuve notas finales altas en la secundaria',
            start_date=datetime.date(year=1998, month=03, day=01),
            completion_date=datetime.date(year=2002, month=11, day=30)
        )
        ExperienceItem.objects.create(
            experience_type=exp_edu,
            title_en='University',
            title_es='Universidad',
            subtitle_en='Information Systems Engineering',
            subtitle_es=u'Ingeniería en Sistemas de Información',
            url='http://www.somefancyhighschoolwebpage.com',
            location=u'Tunuyán, Mendoza, Argentina',
            description_en="""Information systems engineers apply knowledge of
engineering and scientific principles, computer technologies, and human
cognition to design, implement and manage information systems.
The information systems engineer may be called upon to design and develop
databases, develop a system architecture, establish system standards,
integrate an information system with varied data sources and networks, and
generally to plan, integrate, design, test or operate information systems.
Differences among Degree Options that focus on information science knowledge
domains. """,
            description_es=u"""Participa en la toma de decisiones de una
organización y asesora respecto de las posibilidades de desarrollo en lo
referente a Sistemas de Información. Planifica y evalúa estudios y proyectos de
diseños de Sistemas de Información, modificación o reemplazo de los sistemas
existentes. También entiende en cuanto a los Sistemas de Computación (Hard)
asociados a dichos proyectos. Evalúa y selecciona los sistemas de programación
para su utilización en Sistemas de Información. Determina el perfil de los
recursos humanos que se requieren en los distintos sistemas de información.
Elabora métodos y normas de seguridad para preservar la privacidad de la
información procesada o generada, además evalúa su aplicación. Desarrolla
modelos de simulación de Procesos y Sistemas Expertos. Realiza auditoría de
Sistemas de Información y medios de procesamientos de datos. """,
            start_date=datetime.date(year=2003, month=3, day=1),
            completion_date=None
        )

        print "Creating job experience"
        exp_job = ExperienceGroup.objects.create(
            person=p,
            name_en=u'Labor Experience',
            name_es=u'Experiencia Laboral',
            order=2
        )
        ExperienceItem.objects.create(
            experience_type=exp_job,
            title_en='A Huge Company',
            title_es=u'Una Compañía Muy Grande',
            subtitle_en='Python Software Developer',
            subtitle_es=u'Desarrollador de Software Python',
            url='http://www.companywebgenericwebpage.com',
            location=u'Mendoza, Argentina',
            description_en="""I perform development tasks, but not only that.
I also participate in all the software development process, including
analysis, design, development. Also I create unit tests for the apps.""",
            description_es=u"""Realizo tareas de desarrollo de softare, pero no
sólo eso. Además participo en todo el proceso de desarrollo de software,
incluyendo análisis, diseño y desarrollo. También desarrollo test unitarios
de prueba para las aplicaciones.""",
            start_date=datetime.date(year=2008, month=8, day=1),
            completion_date=None
        )

        print "Creating skills"
        exp_skills = ExperienceGroup.objects.create(
            person=p,
            name_en=u'Skills / Knowledge',
            name_es=u'Habilidades / Conocimientos',
            order=3
        )
        exp_skills_1 = ExperienceItem.objects.create(
            experience_type=exp_skills,
            title_en="Programming Languages",
            title_es=u"Lenguajes de Programación"
        )
        LineItem.objects.create(
            experience=exp_skills_1,
            url="http://www.python.com",
            details_en="Python, Django, WebWare, virtualenv, and lots more"
        )
        exp_skills_2 = ExperienceItem.objects.create(
            experience_type=exp_skills,
            title_en="Programming IDEs",
            title_es=u"Entornos de Programación"
        )
        LineItem.objects.create(
            experience=exp_skills_2,
            url="http://www.ninja-ide.org",
            details_en="Ninja IDE"
        )
        LineItem.objects.create(
            experience=exp_skills_2,
            url="https://github.com/fisadev/fisa-vim-config",
            details_en="VIM using fisa-vim-config"
        )

        print "End fill"
