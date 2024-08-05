from django.urls import path,include
from .views import taskdelete,Updatetask ,apply ,homepage,index,user_login,user_logout,user_signup,adminpage,admindetail
urlpatterns = [
    path('test/<int:id>/', homepage, name='test'),
    path('', index, name='home'),    
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    # path('adminpage/', adminpage, name='adminpage'),
    # path('adminpage/apply/', apply, name='apply'),    
    # path('adminpage/modul/<int:id>/', admindetail, name='admindetail'),
    # path('taskdelete/<int:id>/', taskdelete, name='taskdelete'),
    # path('updatetask/<int:pk>/', Updatetask.as_view(), name='updatetask'),
]
