from django.urls import path
from Programs.api.views import QuestionsAPI,AnswersAPI,TotalAnswersAPI,QuestionEditAPI,ListISQ_Questions
urlpatterns=[
    path('ISQ_Q',ListISQ_Questions.as_view(),name='user_questions'),
    path('ISQ/',QuestionsAPI.as_view(),name='quesions'),
path('ISQ_Edit/<int:pk>',QuestionEditAPI.as_view(),name='Q_update'),
path('ISQ_A/',AnswersAPI.as_view(),name='answers'),
path('I_ISQ/',TotalAnswersAPI.as_view(),name='total_answers'),

]