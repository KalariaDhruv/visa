from rest_framework import serializers
from .models import File, Tour, Work

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = File
    fields = ('degree', 'transcript', 'acceptance_letter','passport',
     'university_fee_reciept', 'embassy_fee_reciept','insurance', 'bank_statement',
     'image', 'name','e_mail', 'dath_of_birth','sponser','phone','passport_number','address',
      'timestamp')

class FileSerializerWork(serializers.ModelSerializer):
  class Meta():
    model = Tour
    fields = ('legal_status', 'economic_activity', 'deed_for_company','passport',
     'embassy_fee_reciept','insurance', 'bank_statement',
     'image', 'name','e_mail', 'dath_of_birth','sponser','phone','passport_number','address',
      'timestamp')

class FileSerializerTour(serializers.ModelSerializer):
  class Meta():
    model = Tour
    fields = ('cover_letter', 'proof_of_accomodation', 'flight_reservation','passport',
    'embassy_fee_reciept','insurance', 'bank_statement',
     'image', 'name','e_mail', 'dath_of_birth','sponser','phone','passport_number','address',
      'timestamp')