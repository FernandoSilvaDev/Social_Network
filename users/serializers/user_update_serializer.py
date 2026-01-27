from rest_framework import serializers

from users.models import User


class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, min_length=8)

    class Meta:
        model = User
        fields = [
            "full_name",
            "username",
            "password",
            "bio",
            "avatar",
            "user_bg",
            "website",
            "location",
        ]

    def to_internal_value(self, data):
        for field in ["avatar", "user_bg", "website"]:
            if data.get(field) == "":
                data[field] = None
        return super().to_internal_value(data)

    def validate_username(self, value):
        if User.objects.exclude(pk=self.instance.pk).filter(username=value).exists():
            raise serializers.ValidationError("Esse username já está em uso.")
        return value

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance