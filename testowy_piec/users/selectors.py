from testowy_piec.users.models import BaseUser

from .filters import BaseUserFilter


def user_get_login_data(*, user: BaseUser):
    return {
        'id': user.id,
        'email': user.email,
        'is_active': user.is_active,
        'is_admin': user.is_admin,
        'is_superuser': user.is_superuser,
    }


# TODO: Add queryset return type
def user_list(*, filters=None):
    filters = filters or {}

    qs = BaseUser.objects.all()

    return BaseUserFilter(filters, qs).qs
