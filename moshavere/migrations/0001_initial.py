# Generated by Django 4.0.2 on 2022-04-22 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Daneshkadeh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('daneshgah_code', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('meli_code', models.IntegerField(unique=True)),
                ('is_authorized', models.BooleanField(default=False)),
                ('job', models.CharField(choices=[('مشاور', 'مشاور'), ('ناظر', 'ناظر')], default='مشاور', max_length=8, null=True)),
                ('saghfe_mojaz_hafte', models.IntegerField(default=0)),
                ('hours_weekly_authorized', models.IntegerField(default=0)),
                ('type_hamkari_ba_daneshgah', models.CharField(choices=[('مدعو', 'مدعو'), ('رسمی', 'رسمی'), ('پروژه ای', 'پروژه ای'), ('قراردادی', 'قراردادی')], default='پروژه ای', max_length=100)),
                ('akharin_maghta_tahsili', models.CharField(max_length=100)),
                ('akharin_reshte_tahsili', models.CharField(max_length=150)),
                ('sazman_parvane_behzisti', models.CharField(choices=[('سازمان نظام روانشناسی', 'سازمان نظام روانشناسی'), ('پروانه اشتغال تخصصی', 'پروانه اشتغال تخصصی'), ('بهزیستی', 'بهزیستی'), ('ندارد', 'ندارد')], default='ندارد', max_length=150)),
                ('tarikh_shoro_faliyat', models.DateTimeField(auto_now_add=True)),
                ('roozhaye_hozor', models.CharField(blank=True, max_length=250, null=True)),
                ('pedar_name', models.CharField(blank=True, max_length=250, null=True)),
                ('birthday', models.DateField()),
                ('shaba_number', models.CharField(blank=True, max_length=250, null=True)),
                ('hesab_number', models.IntegerField(default=0)),
                ('molahezat', models.TextField(blank=True, max_length=9000, null=True)),
                ('city', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='moshavere.city')),
                ('daneshkadeh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moshavere.daneshkadeh')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MarakezMoshavere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('karbari_markaz_moshavere', models.CharField(blank=True, max_length=80, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='moshavere.city')),
                ('daneshgah_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moshavere.daneshkadeh')),
            ],
        ),
        migrations.CreateModel(
            name='Consulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('mashroot_len', models.IntegerField(default=0)),
                ('moadel', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('arzyabi', models.CharField(choices=[('عادی', 'عادی'), ('وسواس', 'وسواس'), ('مضطرب', 'مضطرب')], default='عادی', max_length=20)),
                ('erja_moshavere_tahsili', models.BooleanField(default=False)),
                ('erja_moshavere_shoghli', models.BooleanField(default=False)),
                ('erja_moshavere_balini', models.BooleanField(default=False)),
                ('nobat', models.DateField(default=django.utils.timezone.now)),
                ('hozor', models.BooleanField(default=False)),
                ('model_term_ghabl', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('moshkel_asli', models.TextField(blank=True, max_length=9000)),
                ('neshanehaye_raftari', models.TextField(blank=True, max_length=9000)),
                ('ahdaf_modakhele', models.TextField(blank=True, max_length=9000)),
                ('farayande_modakhele', models.TextField(blank=True, max_length=9000)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=200, null=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='moshavere.profileemployee')),
            ],
        ),
        migrations.CreateModel(
            name='AgentMarkaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('meli_code', models.IntegerField(blank=True, unique=True)),
                ('is_authorized', models.BooleanField(default=False)),
                ('markaz_moshavere', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='moshavere.marakezmoshavere')),
            ],
        ),
    ]
