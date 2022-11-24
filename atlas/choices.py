from djchoices import ChoiceItem, DjangoChoices


class PaymentStatusChoices(DjangoChoices):
    PAYENT_PENDING = ChoiceItem("PENDING")
    PAYMENT_COMPLETED = ChoiceItem("COMPLETED")

class PaymentCurrencyStatusChoices(DjangoChoices):
    CURRENCY_USD = ChoiceItem("USD")
    CURRENCY_RUPEE = ChoiceItem("RUPEE")
    CURRENCY_EURO = ChoiceItem("EURO")
    CURRENCY_POUND = ChoiceItem("POUND")
    