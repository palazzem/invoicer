from rest_framework import viewsets, permissions

from .models import Partner


class CustomerViewSet(viewsets.ModelViewSet):
    model = Partner
    permission_classes = [permissions.IsAuthenticated]
