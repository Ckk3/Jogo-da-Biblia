# Generated by Django 3.1.14 on 2022-05-15 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('biblia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'tema',
            },
        ),
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblia.livro')),
                ('versiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblia.versiculo', verbose_name='Versículo')),
            ],
            options={
                'db_table': 'referencia',
            },
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('enunciado', models.TextField()),
                ('tipo_resposta', models.CharField(choices=[('MES', 'Múltipla Escolha'), ('RCO', 'Referência Completa'), ('RLC', 'Referência Livro-Capítulo'), ('RES', 'Resposta Simples')], max_length=3, verbose_name='Tipo de Resposta')),
                ('status', models.BooleanField(default=True, verbose_name='Pergunta Status')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('revisado_em', models.DateTimeField(auto_now_add=True)),
                ('publicado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criado_por', to=settings.AUTH_USER_MODEL)),
                ('outras_referencias', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outras_referencias', to='perguntas.referencia')),
                ('publicado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publicado_por', to=settings.AUTH_USER_MODEL)),
                ('refencia_resposta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='perguntas.referencia')),
                ('revisado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revisado_por', to=settings.AUTH_USER_MODEL)),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perguntas.tema')),
            ],
            options={
                'verbose_name': 'Pergunta',
                'db_table': 'pergunta',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=126)),
                ('phone', models.CharField(max_length=11)),
                ('is_whatsapp', models.BooleanField(default=True, verbose_name='É Whatsapp?')),
                ('mensagem', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perguntas.pergunta')),
            ],
            options={
                'db_table': 'comentario',
            },
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('texto', models.TextField()),
                ('alternativas_corretas', models.BooleanField(default=False)),
                ('alternativas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alternativas', to='perguntas.pergunta')),
            ],
            options={
                'db_table': 'alternativa',
            },
        ),
    ]