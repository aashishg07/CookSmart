from django.urls import path
from .views import *


urlpatterns = [
    path('recipe/', RecipeListView.as_view(), name="recipe_list"),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name="recipe_detail"),
    path('meal-plan/', MealPlanListView.as_view(), name="meal-plan_list"),
    path('meal-plan/<int:pk>/', MealPlanDetailView.as_view(), name="meal-plan_detail"),
    path('shopping-list/', ShoppingListView.as_view(), name='shopping_list'),
    path('shopping-list/<int:pk>/', ShoppingDetailView.as_view(), name="shopping_detail"),
    path('interaction/', UserInteractionListView.as_view(), name='user_interaction_list'),
    path('interaction/<int:pk>/', UserInteractionDetailView.as_view(), name='user_interaction_detail'),
    path('diet-plan/', DietPlanListView.as_view(), name="diet-plan_list"),
    path('diet-plan/<int:pk>/', DietPlanDetailView.as_view(), name="diet-plan_detail"),
    path('notification/', NotificationListView.as_view(), name="notification_list"),
    path('notification/<int:pk>/', NotificationDetailView.as_view(), name="notification_detail")
]