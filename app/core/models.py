from django.db import models
from django.conf import settings

from app.core.validators import cpf_validator



class User(models.Model):
    name = models.CharField('nome', max_length=100)
    birthday = models.DateField('data de nascimento')
    cpf = models.CharField(
        'CPF', max_length=11, unique=True, validators=[cpf_validator])
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        unique_together = ['name', 'birthday']
        ordering = ['name']

    def __str__(self):
        return self.name


class Wallet(models.Model):
    BANK_CHOICES = settings.BANK_CHOICES

    amount = models.DecimalField('valor', max_digits=10, decimal_places=2)
    bank = models.CharField('banco', max_length=3, choices=BANK_CHOICES)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    user = models.ForeignKey(
        User, related_name='wallet', on_delete=models.CASCADE, verbose_name='usuário')

    class Meta:
        unique_together = ['user', 'bank']
        ordering = ['amount', 'bank']

    def __str__(self):
        return self.bank

    def get_absolute_bank_name(self, code):
        for _code, bank_name in self.BANK_CHOICES:
            if code == _code:
                return f'{_code} - {bank_name}'

        return 'N/A'
