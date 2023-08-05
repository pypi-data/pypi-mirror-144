__all__ = ('BankCardPoint',)

from expressmoney.api import *


SERVICE = 'payments'


class BankCardCreateContract(Contract):
    M01 = "01"
    M02 = "02"
    M03 = "03"
    M04 = "04"
    M05 = "05"
    M06 = "06"
    M07 = "07"
    M08 = "08"
    M09 = "09"
    M10 = "10"
    M11 = "11"
    M12 = "12"

    MONTH_CHOICES = (
        (M01, '01'),
        (M02, '02'),
        (M03, '03'),
        (M04, '04'),
        (M05, '05'),
        (M06, '06'),
        (M07, '07'),
        (M08, '08'),
        (M09, '09'),
        (M10, '10'),
        (M11, '11'),
        (M12, '12'),
    )

    Y2020 = "2020"
    Y2021 = "2021"
    Y2022 = "2022"
    Y2023 = "2023"
    Y2024 = "2024"
    Y2025 = "2025"
    Y2026 = "2026"
    Y2027 = "2027"
    Y2028 = "2028"
    Y2029 = "2029"
    Y2030 = "2030"

    YEAR_CHOICES = (
        (Y2020, "2020"),
        (Y2021, "2021"),
        (Y2022, "2022"),
        (Y2023, "2023"),
        (Y2024, "2024"),
        (Y2025, "2025"),
        (Y2026, "2026"),
        (Y2027, "2027"),
        (Y2028, "2028"),
        (Y2029, "2029"),
        (Y2030, "2030"),
    )

    bin = serializers.CharField(max_length=6)
    number = serializers.CharField(max_length=4)
    expiry_month = serializers.ChoiceField(choices=MONTH_CHOICES)
    expiry_year = serializers.ChoiceField(choices=YEAR_CHOICES)
    ip = serializers.IPAddressField(allow_blank=True)
    cryptogram = serializers.CharField(max_length=1024, allow_blank=True)
    redirect_url = serializers.URLField(max_length=512, allow_blank=True)


class BankCardReadContract(BankCardCreateContract):
    PAYPAL = "PAYPAL"
    CLOUDPAYMENTS = "CLOUDPAYMENTS"
    GATEWAY_CHOICES = (
        (PAYPAL, "PayPal"),
        (CLOUDPAYMENTS, "CloudPayments")
    )
    pagination = PaginationContract()
    id = serializers.IntegerField(min_value=1)
    is_active = serializers.BooleanField(default=True)
    gateway = serializers.ChoiceField(choices=GATEWAY_CHOICES)


class BankCard3dsContract(Contract):
    md = serializers.CharField(max_length=512)
    pa_res = serializers.CharField(max_length=512)


class BankCardID(ID):
    _service = SERVICE
    _app = 'bank_cards'
    _view_set = 'bank_card'


class BankCard3dsID(ID):
    _service = SERVICE
    _app = 'bank_cards'
    _view_set = 'bank_card_3ds'


class BankCardPoint(ListPointMixin, CreatePointMixin, ContractPoint):
    _point_id = BankCardID()
    _create_contract = BankCardCreateContract
    _read_contract = BankCardReadContract


class BankCard3dsPoint(CreatePointMixin, ContractPoint):
    _point_id = BankCard3dsID()
    _create_contract = BankCard3dsContract
