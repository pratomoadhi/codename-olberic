from rest_framework import routers
from .views import UserViewSet, CourseViewSet, EnrollmentViewSet

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls
