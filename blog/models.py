# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Posts_Duplicate(models.Model):
    title = models.CharField(max_length=191)
    body = models.TextField()
    cover_image = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        # managed = False
        db_table = '_posts'


class Recipes_Duplicate(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=191)
    description = models.TextField()
    special_instructions = models.TextField()
    cover_image = models.CharField(max_length=100, blank=True, null=True)
    bb_cocoa = models.CharField(max_length=191)
    bb_shea = models.CharField(max_length=191)
    bb_mango = models.CharField(max_length=191)
    bf_coconut = models.CharField(max_length=191)
    bf_palm = models.CharField(max_length=191)
    bf_lanolin = models.CharField(max_length=191)
    bo_olive = models.CharField(max_length=191)
    bo_advocado = models.CharField(max_length=191)
    bo_caster = models.CharField(max_length=191)
    eo_hemp_seed = models.CharField(max_length=191)
    eo_tea_tree = models.CharField(max_length=191)
    eo_honey = models.CharField(max_length=191)
    fo_lavendar = models.CharField(max_length=191)
    fo_lemongrass = models.CharField(max_length=191)
    fo_eucalyptus = models.CharField(max_length=191)
    cl_gold = models.CharField(max_length=191)
    cl_cappuccino = models.CharField(max_length=191)
    cl_lavendar = models.CharField(max_length=191)
    ex_oatmeal = models.CharField(max_length=191)
    ex_flaxseed = models.CharField(max_length=191)
    ex_seaweed = models.CharField(max_length=191)
    pr_grapeseed_extract = models.CharField(max_length=191)
    pr_carrot_root_oil = models.CharField(max_length=191)
    pr_tocopherols = models.CharField(max_length=191)
    sodium_hydroxide = models.CharField(max_length=191)
    potassium_hydroxide = models.CharField(max_length=191)
    sodium_lactate = models.CharField(max_length=191)
    distilled_water = models.CharField(max_length=191)
    buttermilk = models.CharField(max_length=191)
    coconut_milk = models.CharField(max_length=191)
    temp_min = models.CharField(max_length=191)
    temp_max = models.CharField(max_length=191)
    discount = models.CharField(max_length=191)
    image_id = models.CharField(max_length=191)
    user_id = models.IntegerField()

    class Meta:
        # managed = False
        db_table = '_recipes'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=191)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'failed_jobs'


class Images(models.Model):
    id = models.BigAutoField(primary_key=True)
    filename = models.CharField(max_length=191)
    url = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'images'


class Migrations(models.Model):
    migration = models.CharField(max_length=191)
    batch = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'migrations'


class MolecularWeightFattyAcids(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    formula = models.CharField(max_length=100, blank=True, null=True)
    molecular_weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'molecular_weight_fatty_acids'


class OilsFattyAcids(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    arachidic = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    caproic = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    capric = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    capryli = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    erucic = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lauric = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    linoleic = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    linolenic = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    monoetherioic = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    myristic = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    oleic = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    palmitic = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    palmitoleic = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ricinoleic = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stearic = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    other = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'oils_fatty_acids'


class OilsSap(models.Model):
    name = models.CharField(max_length=100)
    sap = models.DecimalField(max_digits=5, decimal_places=2)
    naoh_per_100g = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    h2o_per_100g = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'oils_sap'


class PasswordResets(models.Model):
    email = models.CharField(max_length=191)
    token = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'password_resets'


class Posts(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=191)
    body = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    cover_image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'posts'


class Recipes(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    bb_cocoa = models.CharField(max_length=100, blank=True, null=True)
    bb_shea = models.CharField(max_length=100, blank=True, null=True)
    bb_mango = models.CharField(max_length=100, blank=True, null=True)
    bf_coconut = models.CharField(max_length=100, blank=True, null=True)
    bf_palm = models.CharField(max_length=100, blank=True, null=True)
    bf_lanolin = models.CharField(max_length=100, blank=True, null=True)
    bo_olive = models.CharField(max_length=100, blank=True, null=True)
    bo_advocado = models.CharField(max_length=100, blank=True, null=True)
    bo_caster = models.CharField(max_length=100, blank=True, null=True)
    eo_hemp_seed = models.CharField(max_length=100, blank=True, null=True)
    eo_tea_tree = models.CharField(max_length=100, blank=True, null=True)
    eo_honey = models.CharField(max_length=100, blank=True, null=True)
    fo_lavendar = models.CharField(max_length=100, blank=True, null=True)
    fo_lemongrass = models.CharField(max_length=100, blank=True, null=True)
    fo_eucalyptus = models.CharField(max_length=100, blank=True, null=True)
    cl_gold = models.CharField(max_length=100, blank=True, null=True)
    cl_cappuccino = models.CharField(max_length=100, blank=True, null=True)
    cl_lavendar = models.CharField(max_length=100, blank=True, null=True)
    ex_oatmeal = models.CharField(max_length=100, blank=True, null=True)
    ex_flaxseed = models.CharField(max_length=100, blank=True, null=True)
    ex_seaweed = models.CharField(max_length=100, blank=True, null=True)
    pr_grapeseed_extract = models.CharField(max_length=100, blank=True, null=True)
    pr_carrot_root_oil = models.CharField(max_length=100, blank=True, null=True)
    pr_tocopherols = models.CharField(max_length=100, blank=True, null=True)
    sodium_hydroxide = models.CharField(max_length=100, blank=True, null=True)
    potassium_hydroxide = models.CharField(max_length=100, blank=True, null=True)
    sodium_lactate = models.CharField(max_length=100, blank=True, null=True)
    distilled_water = models.CharField(max_length=100, blank=True, null=True)
    buttermilk = models.CharField(max_length=100, blank=True, null=True)
    coconut_milk = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    special_instructions = models.TextField(blank=True, null=True)
    temp_min = models.CharField(max_length=100, blank=True, null=True)
    temp_max = models.CharField(max_length=100, blank=True, null=True)
    discount = models.CharField(max_length=100, blank=True, null=True)
    image_id = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    cover_image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'recipes'


class SoapProperties(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    hard_bar = models.IntegerField(blank=True, null=True)
    cleansing = models.IntegerField(blank=True, null=True)
    fluffy_lather = models.IntegerField(blank=True, null=True)
    conditioning = models.IntegerField(blank=True, null=True)
    stable_lather = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'soap_properties'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    email = models.CharField(unique=True, max_length=191)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=191)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'users'


class WaxSap(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    sap = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'wax_sap'

