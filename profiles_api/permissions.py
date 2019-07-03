from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allows users to update their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to update their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
            
        return request.user.id == obj.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to only update their own status"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id