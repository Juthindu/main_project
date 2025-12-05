from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

@receiver(post_migrate)
def create_super_admin(sender, **kwargs):
    # only run for your app
    if sender.label != "api":
        return

    print("SIGNAL RUNNING…")

    # get content type for user model
    ct = ContentType.objects.get_for_model(User)

    # try to fetch permissions — if not created yet, skip
    perms = {}
    perm_names = ["can_manage_users", "can_view_reports", "can_edit_courses"]

    for pname in perm_names:
        try:
            perms[pname] = Permission.objects.get(codename=pname, content_type=ct)
        except Permission.DoesNotExist:
            print(f"Permission {pname} not ready yet — skipping role setup.")
            return  # stop here; migration will run signal again later

    # create groups (roles)
    superadmin_group, _ = Group.objects.get_or_create(name="SuperAdmin")
    teacher_group, _ = Group.objects.get_or_create(name="Teacher")
    staff_group, _ = Group.objects.get_or_create(name="Staff")

    # assign permissions
    superadmin_group.permissions.set(perms.values())
    teacher_group.permissions.set([perms["can_view_reports"], perms["can_edit_courses"]])
    staff_group.permissions.set([perms["can_view_reports"]])

    # create default superadmin user
    if not User.objects.filter(username="superadmin").exists():
        user = User.objects.create_superuser(
            username="superadmin",
            password="SuperAdmin123",
            role="superadmin",
        )
        user.groups.add(superadmin_group)

    print("ROLE + SUPERADMIN SETUP COMPLETE")
