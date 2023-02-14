from django.contrib import admin
from django.urls import path
from schoolapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    # path('home/',views.home,name='home'),
    # path('about/',views.about,name='about'),
    path('principal_quotes/',views.principal_quotes,name='principal_quotes'),
    path('profile/',views.profile,name='profile'),
    path('acc_users/',views.acc_users,name='acc_users'),
    path('attendance_view/',views.attendance_view,name='attendance_view'),
    path('attendance_taken/',views.attendance_taken,name='attendance_taken'),
    path('class_timetable/',views.class_timetable,name='class_timetable'),
    path('student_list/',views.student_list,name='student_list'),
    path('teacher_list/',views.teacher_list,name='teacher_list'),
    path('staff_list/',views.staff_list,name='staff_list'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('contact/',views.contact,name='contact'),
    path('courses/',views.course,name='courses'),
    path('staff_reg/',views.staff_reg,name='staff_reg'),
    path('student_reg/',views.student_reg,name='student_reg'),
    path('teacher_reg/',views.teacher_reg,name='teacher_reg'),
    path('datatable_adminpage/',views.datatable_adminpage,name='datatable_adminpage'),
    path('admin_page/',views.admin_page,name='admin_page'),
    path('base_details/',views.admin_base_details,name='base_details'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_signup/',views.admin_signup,name='admin_signup'),
    path('office_page/',views.office_page,name='office_page'),
    path('office_login/',views.office_login,name='office_login'),
    path('tution_fee/',views.tution_fee,name='tution_fee'),
    path('fees_system/',views.fees_system,name='fees_system'),
    path('office_signup/',views.office_signup,name='office_signup'),
    path('library/',views.library,name='library')

]