from django.core.validators import RegexValidator, MinValueValidator


def validate_ttl(value):
    """Validates that the ttl value is greater than or equal to a certain value."""
    validator = MinValueValidator(300)
    validator(value)


def validate_mac_address(address):
    """Validates that the mac address is on a valid form."""
    adr_regex = "[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$"
    validator = RegexValidator(adr_regex)
    validator(address)
