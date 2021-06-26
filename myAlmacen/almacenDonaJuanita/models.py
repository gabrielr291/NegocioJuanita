from django.db import models

# Create your models here.

from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Boleta(models.Model):
    idboleta = models.BigIntegerField(primary_key=True)
    fechaboleta = models.DateField()
    idpago = models.BigIntegerField(blank=True, null=True)
    idcliente = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'boleta'


class Cliente(models.Model):
    idcliente = models.BigIntegerField(primary_key=True)
    rutcliente = models.CharField(max_length=20)
    nombrecliente = models.CharField(max_length=50)
    telefonocliente = models.BigIntegerField()
    correocliente = models.CharField(max_length=50)
    estadocliente = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cliente'


class Detalleboleta(models.Model):
    idboleta = models.BigIntegerField()
    idproducto = models.BigIntegerField()
    cantidadproducto = models.BigIntegerField()
    totalventa = models.BigIntegerField()
    valorproducto = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'detalleboleta'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estadopedido(models.Model):
    idestado = models.BigIntegerField(primary_key=True)
    descestado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estadopedido'


class Familiaproducto(models.Model):
    idfamilia = models.BigIntegerField(primary_key=True)
    descfamilia = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'familiaproducto'


class Pedido(models.Model):
    idpedido = models.BigIntegerField(primary_key=True)
    fechapedido = models.DateField()
    idestado = models.BigIntegerField()
    idproducto = models.BigIntegerField()
    idproveedor = models.BigIntegerField()
    fechallgegada = models.DateField()
    idusuario = models.BigIntegerField()
    totalproducto = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pedido'


class Producto(models.Model):
    idproducto = models.CharField(primary_key=True, max_length=20)
    nombreproducto = models.CharField(max_length=50, blank=True, null=True)
    descproducto = models.CharField(max_length=150, blank=True, null=True)
    fechavencimiento = models.DateField(blank=True, null=True)
    preciocompra = models.BigIntegerField()
    precioventa = models.BigIntegerField()
    stockproducto = models.BigIntegerField()
    stockcriticoproducto = models.BigIntegerField()
    idfamilia = models.BigIntegerField()
    idtipo = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'producto'
        unique_together = (('idproducto', 'idfamilia', 'idtipo'),)


class Proveedor(models.Model):
    idproveedor = models.BigIntegerField(primary_key=True)
    telefonoproveedor = models.BigIntegerField()
    correoproveedor = models.CharField(max_length=50, blank=True, null=True)
    idrubro = models.BigIntegerField()
    nombreproveedor = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Rubroproveedor(models.Model):
    idrubro = models.BigIntegerField(primary_key=True)
    descrubro = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rubroproveedor'


class Tipopago(models.Model):
    idpago = models.BigIntegerField(primary_key=True)
    descpago = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipopago'


class Tipoproducto(models.Model):
    idtipo = models.BigIntegerField(primary_key=True)
    desctipo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipoproducto'


class Usuario(models.Model):
    idusuario = models.BigIntegerField(primary_key=True)
    tipousuario = models.CharField(max_length=50)
    nombreusuario = models.CharField(max_length=20)
    contrasenausuario = models.CharField(max_length=50)
    telefonousuario = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'
