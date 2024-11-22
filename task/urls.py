from django.urls import path
from .views import (
	home, 
	delete_task, 
	update_task, 
	toggle_task_status, 
	detail_task
)

urlpatterns = [
	path('', home, name='home'),
	path('detail_task/<pk>', detail_task, name='detail-task'),
	path('delete_task/<pk>', delete_task, name='delete-task'),
	path('update_task/<pk>', update_task, name='update-task'),
	path('toggle-task/<pk>', toggle_task_status, name='toggle-task-status')
]

