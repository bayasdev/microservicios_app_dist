from rest_framework.routers import DefaultRouter
from api.views import PersonaViewSet,TipoPersonaViewSet

router = DefaultRouter()

router.register('api/persona', PersonaViewSet)
router.register('api/tipopersona', TipoPersonaViewSet)
# Otras rutas

urlpatterns = []

urlpatterns += router.urls
