from rest_framework import serializers
from movies.models import Movie , MovieOrder
from movies.models import RationgChoice

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length= 127)
    duration = serializers.CharField(max_length=10,allow_null=True,default=None)
    rating = serializers.ChoiceField(
        allow_null=True,
        choices=RationgChoice.choices, 
        default=RationgChoice.G
        )
    synopsis = serializers.CharField(allow_null=True, default=None)

    added_by = serializers.SerializerMethodField()
    
    
    def get_added_by(self, obj):
        added_by = obj.user.email
        return added_by
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8,decimal_places=2)    
    buyed_by = serializers.SerializerMethodField()

    def get_title(self,obj):
        title = obj.movie.title
        return title

    def get_buyed_by(self,obj):
        buyed_by = obj.order.email
        return buyed_by    

    
    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)